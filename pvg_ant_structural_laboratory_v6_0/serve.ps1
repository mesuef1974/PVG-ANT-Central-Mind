$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $root
Write-Host 'PVG–ANT Structural Laboratory v6.0: http://localhost:8000'
python -m http.server 8000
