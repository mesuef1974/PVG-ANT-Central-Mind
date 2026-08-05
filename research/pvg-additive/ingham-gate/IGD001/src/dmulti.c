/* D_h(x) = sum_{n<=x} d(n) d(n+h) for h in {1,2,6,12,30}, single pass. */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <omp.h>

#define SEG 1000000ULL
#define NH 5
static const uint64_t H[NH] = {1, 2, 6, 12, 30};
#define HMAX 30

static uint32_t *primes; static uint32_t nprimes;

static void build_primes(uint64_t limit) {
    char *c = calloc(limit + 1, 1);
    primes = malloc(sizeof(uint32_t) * 6000000); nprimes = 0;
    for (uint64_t i = 2; i <= limit; i++)
        if (!c[i]) { primes[nprimes++] = (uint32_t)i;
            for (uint64_t j = i * i; j <= limit; j += i) c[j] = 1; }
    free(c);
}

static void divisor_segment(uint64_t lo, uint64_t len, uint64_t *rem, uint32_t *dd) {
    uint64_t hi = lo + len - 1;
    for (uint64_t i = 0; i < len; i++) { rem[i] = lo + i; dd[i] = 1; }
    for (uint32_t k = 0; k < nprimes; k++) {
        uint64_t p = primes[k];
        if (p * p > hi) break;
        for (uint64_t n = (lo + p - 1) / p * p; n <= hi; n += p) {
            uint64_t i = n - lo; uint32_t e = 0;
            while (rem[i] % p == 0) { rem[i] /= p; e++; }
            dd[i] *= (e + 1);
        }
    }
    for (uint64_t i = 0; i < len; i++) if (rem[i] > 1) dd[i] *= 2;
}

int main(int argc, char **argv) {
    int expmax = (argc > 1) ? atoi(argv[1]) : 10;
    uint64_t X = 1; for (int i = 0; i < expmax; i++) X *= 10ULL;
    build_primes(200000);
    uint64_t nseg = X / SEG;
    uint64_t *segsum = calloc(nseg * NH, sizeof(uint64_t));
    double t0 = omp_get_wtime();

    #pragma omp parallel
    {
        uint64_t *rem = malloc(sizeof(uint64_t) * (SEG + HMAX + 1));
        uint32_t *dd  = malloc(sizeof(uint32_t) * (SEG + HMAX + 1));
        #pragma omp for schedule(dynamic, 1)
        for (long long s = 0; s < (long long)nseg; s++) {
            uint64_t lo = (uint64_t)s * SEG + 1;
            divisor_segment(lo, SEG + HMAX, rem, dd);
            for (int t = 0; t < NH; t++) {
                uint64_t h = H[t], acc = 0;
                for (uint64_t i = 0; i < SEG; i++)
                    acc += (uint64_t)dd[i] * (uint64_t)dd[i + h];
                segsum[(uint64_t)s * NH + t] = acc;
            }
        }
        free(rem); free(dd);
    }

    uint64_t run[NH] = {0};
    printf("# x");
    for (int t = 0; t < NH; t++) printf(" D_%llu", (unsigned long long)H[t]);
    printf("\n");
    for (uint64_t s = 0; s < nseg; s++) {
        for (int t = 0; t < NH; t++) run[t] += segsum[s * NH + t];
        uint64_t x = (s + 1) * SEG, p = SEG;
        while (p <= X) { if (x == p) { printf("%llu", (unsigned long long)x);
                for (int t = 0; t < NH; t++) printf(" %llu", (unsigned long long)run[t]);
                printf("\n"); } p *= 10; }
    }
    fprintf(stderr, "elapsed %.2f s\n", omp_get_wtime() - t0);
    return 0;
}
