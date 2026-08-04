/* D_1(x) = sum_{n<=x} d(n) d(n+1)  via segmented factorisation sieve.
 * Diagnostic for the Ingham gate (h=1 K-estimation). No claim is made here.
 * Build: gcc -O3 -march=native -fopenmp d1.c -o d1
 * Usage: d1 <Xmax_exponent> [segment_size]      e.g.  d1 8
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <omp.h>

#define SEG 1000000ULL           /* segment length; all checkpoints are multiples */

static uint32_t *primes; static uint32_t nprimes;

static void build_primes(uint64_t limit) {
    char *c = calloc(limit + 1, 1);
    primes = malloc(sizeof(uint32_t) * 6000000);
    nprimes = 0;
    for (uint64_t i = 2; i <= limit; i++) {
        if (!c[i]) { primes[nprimes++] = (uint32_t)i;
            for (uint64_t j = i * i; j <= limit; j += i) c[j] = 1; }
    }
    free(c);
}

/* fill dd[0..len-1] with d(n) for n = lo .. lo+len-1 */
static void divisor_segment(uint64_t lo, uint64_t len,
                            uint64_t *rem, uint32_t *dd) {
    uint64_t hi = lo + len - 1;
    for (uint64_t i = 0; i < len; i++) { rem[i] = lo + i; dd[i] = 1; }
    for (uint32_t k = 0; k < nprimes; k++) {
        uint64_t p = primes[k];
        if (p * p > hi) break;
        uint64_t start = (lo + p - 1) / p * p;
        for (uint64_t n = start; n <= hi; n += p) {
            uint64_t i = n - lo;
            uint32_t e = 0;
            while (rem[i] % p == 0) { rem[i] /= p; e++; }
            dd[i] *= (e + 1);
        }
    }
    for (uint64_t i = 0; i < len; i++) if (rem[i] > 1) dd[i] *= 2;
}

int main(int argc, char **argv) {
    int expmax = (argc > 1) ? atoi(argv[1]) : 8;
    uint64_t X = 1; for (int i = 0; i < expmax; i++) X *= 10ULL;

    build_primes(200000);        /* covers sqrt(1e10 + 1) = 1e5 */

    uint64_t nseg = X / SEG;
    uint64_t *segsum = calloc(nseg, sizeof(uint64_t));
    double t0 = omp_get_wtime();

    #pragma omp parallel
    {
        uint64_t *rem = malloc(sizeof(uint64_t) * (SEG + 1));
        uint32_t *dd  = malloc(sizeof(uint32_t) * (SEG + 1));
        #pragma omp for schedule(dynamic, 1)
        for (long long s = 0; s < (long long)nseg; s++) {
            uint64_t lo = (uint64_t)s * SEG + 1;      /* segment covers n = lo .. lo+SEG-1 */
            divisor_segment(lo, SEG + 1, rem, dd);    /* one extra for n+1 */
            uint64_t acc = 0;
            for (uint64_t i = 0; i < SEG; i++)
                acc += (uint64_t)dd[i] * (uint64_t)dd[i + 1];
            segsum[s] = acc;
        }
        free(rem); free(dd);
    }

    uint64_t run = 0;
    printf("# x  D_1(x)\n");
    for (uint64_t s = 0; s < nseg; s++) {
        run += segsum[s];
        uint64_t x = (s + 1) * SEG;
        uint64_t p = SEG;
        while (p <= X) { if (x == p) printf("%llu %llu\n", (unsigned long long)x, (unsigned long long)run); p *= 10; }
    }
    fprintf(stderr, "elapsed %.2f s, threads %d\n", omp_get_wtime() - t0, omp_get_max_threads());
    return 0;
}
