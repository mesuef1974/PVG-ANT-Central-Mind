[CmdletBinding()]
param(
    [ValidateSet("Audit", "SafeSync", "PrepareBranch")]
    [string]$Mode = "Audit",

    [string]$ExpectedRepository = "mesuef1974/PVG-ANT-Central-Mind",

    [switch]$AsJson
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

function Invoke-Git {
    param(
        [Parameter(Mandatory = $true)]
        [string[]]$Arguments,
        [switch]$AllowFailure
    )

    $output = & git @Arguments 2>&1
    $exitCode = $LASTEXITCODE
    if (-not $AllowFailure -and $exitCode -ne 0) {
        $rendered = ($output | Out-String).Trim()
        throw "git $($Arguments -join ' ') failed with exit code $exitCode. $rendered"
    }

    return [pscustomobject]@{
        ExitCode = $exitCode
        Output   = @($output)
        Text     = (($output | Out-String).Trim())
    }
}

function Get-RepositorySlug {
    param([Parameter(Mandatory = $true)][string]$RemoteUrl)

    $trimmed = $RemoteUrl.Trim().Replace("\", "/")
    if ($trimmed -match "github\.com[:/](?<slug>[^/]+/[^/]+?)(?:\.git)?/?$") {
        return $Matches["slug"].TrimEnd("/").ToLowerInvariant()
    }

    throw "Cannot determine a GitHub owner/repository slug from origin URL: $RemoteUrl"
}

function Write-Result {
    param([Parameter(Mandatory = $true)][hashtable]$Result)

    if ($AsJson) {
        $Result | ConvertTo-Json -Depth 5
        return
    }

    foreach ($key in @(
        "mode",
        "repository",
        "root",
        "branch",
        "head",
        "origin_main",
        "ahead",
        "behind",
        "dirty",
        "action",
        "status"
    )) {
        Write-Host ("{0,-14}: {1}" -f $key, $Result[$key])
    }
}

$inside = Invoke-Git -Arguments @("rev-parse", "--is-inside-work-tree")
if ($inside.Text -ne "true") {
    throw "The current directory is not inside a Git worktree."
}

$root = (Invoke-Git -Arguments @("rev-parse", "--show-toplevel")).Text
Set-Location -LiteralPath $root

$originUrl = (Invoke-Git -Arguments @("remote", "get-url", "origin")).Text
$actualRepository = Get-RepositorySlug -RemoteUrl $originUrl
$expected = $ExpectedRepository.Trim().TrimEnd("/").ToLowerInvariant()
if ($actualRepository -ne $expected) {
    throw "Repository identity mismatch. Expected '$expected' but origin resolves to '$actualRepository'."
}

Invoke-Git -Arguments @("fetch", "--prune", "origin", "main") | Out-Null

$branchResult = Invoke-Git -Arguments @("branch", "--show-current")
$branch = $branchResult.Text
if ([string]::IsNullOrWhiteSpace($branch)) {
    $branch = "DETACHED"
}

$head = (Invoke-Git -Arguments @("rev-parse", "HEAD")).Text
$originMain = (Invoke-Git -Arguments @("rev-parse", "origin/main")).Text
$statusText = (Invoke-Git -Arguments @("status", "--porcelain=v1")).Text
$dirty = -not [string]::IsNullOrWhiteSpace($statusText)

$countText = (Invoke-Git -Arguments @("rev-list", "--left-right", "--count", "HEAD...origin/main")).Text
$countParts = -split $countText
if ($countParts.Count -lt 2) {
    throw "Unexpected ahead/behind output: '$countText'"
}
$ahead = [int]$countParts[0]
$behind = [int]$countParts[1]

$action = "fetch-only"
$state = "ok"

switch ($Mode) {
    "PrepareBranch" {
        if ($dirty) {
            throw "PrepareBranch refused: the worktree is dirty."
        }
        if ($head -ne $originMain) {
            throw "PrepareBranch refused: HEAD must equal fetched origin/main. ahead=$ahead behind=$behind"
        }
        $action = "branch-base-verified"
    }

    "SafeSync" {
        if ($branch -eq "main") {
            if ($dirty) {
                $state = "attention_required"
                $action = "dirty-main-fetch-only"
            }
            elseif ($ahead -gt 0) {
                $state = "attention_required"
                $action = "local-main-ahead-fetch-only"
            }
            else {
                Invoke-Git -Arguments @("merge", "--ff-only", "origin/main") | Out-Null
                $head = (Invoke-Git -Arguments @("rev-parse", "HEAD")).Text
                $countText = (Invoke-Git -Arguments @("rev-list", "--left-right", "--count", "HEAD...origin/main")).Text
                $countParts = -split $countText
                $ahead = [int]$countParts[0]
                $behind = [int]$countParts[1]
                $action = "main-fast-forwarded-or-current"
            }
        }
        else {
            $action = "feature-branch-fetch-only"
            if ($behind -gt 0) {
                $state = "attention_required"
            }
        }
    }

    "Audit" {
        if ($dirty -or $ahead -gt 0 -or $behind -gt 0) {
            $state = "attention_required"
        }
    }
}

$result = @{
    mode        = $Mode
    repository  = $actualRepository
    root        = $root
    branch      = $branch
    head        = $head
    origin_main = $originMain
    ahead       = $ahead
    behind      = $behind
    dirty       = $dirty
    action      = $action
    status      = $state
}

Write-Result -Result $result

if ($Mode -eq "PrepareBranch" -and $state -ne "ok") {
    exit 2
}

exit 0
