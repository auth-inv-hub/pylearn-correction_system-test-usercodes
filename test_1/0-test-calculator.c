#include <stdio.h>
#include <stdlib.h>

int add(int a, int b);

int main() {
    int a = 5;
    int b = 10;
    int expected_sum = 15;

    int c = add(a, b);

    if (c != expected_sum) {
        fprintf(stderr, "Test failed: %d + %d = %d, expected %d\n", a, b, c, expected_sum);
        return EXIT_FAILURE;
    }

    printf("Test passed: %d + %d = %d\n", a, b, c);
    return EXIT_SUCCESS;
}