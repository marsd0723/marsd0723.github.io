// #include <stdio.h>
// #include <time.h>

// int main() {
//     clock_t start = clock();

//     long long sum = 0;
//     for (long long i = 0; i < 1000000000; i++) {
//         sum += i;
//     }

//     clock_t end = clock();

//     printf("Sum: %lld\n", sum);
//     printf("Time: %f seconds\n", (double)(end - start) / CLOCKS_PER_SEC);

//     return 0;
// }

#include <stdio.h>
#include <time.h>

int main() {
    const int SIZE = 16;
    int arr[SIZE] = {0};
    long long sum = 0;

    clock_t start = clock();

    for (long long i = 0; i < 1000000000LL; i++) {
        sum += i;

        // Update array in a way compiler can't optimize out easily
        arr[i % SIZE] = (arr[i % SIZE] + (int)(sum & 0xFF)) % 100;
    }

    clock_t end = clock();

    // Print results to prevent optimization
    printf("Sum: %lld\n", sum);

    int arr_sum = 0;
    for (int i = 0; i < SIZE; i++) {
        arr_sum += arr[i];
    }
    printf("Array checksum: %d\n", arr_sum);

    printf("Time: %f seconds\n", (double)(end - start) / CLOCKS_PER_SEC);

    return 0;
}

