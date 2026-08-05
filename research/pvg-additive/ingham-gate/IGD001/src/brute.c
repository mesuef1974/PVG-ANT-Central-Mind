/* Independent brute-force check: d(n) by direct divisor counting, D_1(x) for small x. */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
int main(int argc, char **argv) {
    uint64_t X = (argc > 1) ? strtoull(argv[1], 0, 10) : 100000;
    uint32_t *d = calloc(X + 2, sizeof(uint32_t));
    for (uint64_t i = 1; i <= X + 1; i++)
        for (uint64_t j = i; j <= X + 1; j += i) d[j]++;
    uint64_t s = 0;
    for (uint64_t n = 1; n <= X; n++) {
        s += (uint64_t)d[n] * d[n + 1];
        if (n == 10 || n == 1000 || n == 100000 || n == X)
            printf("%llu %llu\n", (unsigned long long)n, (unsigned long long)s);
    }
    return 0;
}
