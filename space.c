#include <stdio.h>
#include <stdlib.h>

void constant_space(int n) {
    int a = 10;
    int b = 20;
    int c = a + b;
}

void linear_space(int n) {
    int *arr = (int *)malloc(n * sizeof(int));
    if (!arr) return;

    for (int i = 0; i < n; i++) {
        arr[i] = i;
    }

    free(arr);
}

void quadratic_space(int n) {
    int *matrix = (int *)malloc(n * sizeof(int *));
    if (!matrix) return;

    for (int i = 0; i < n; i++) {
        matrix[i] = (int *)malloc(n * sizeof(int));
        if (!matrix[i]) return;
    }

    matrix[0] = 1;

    for (int i = 0; i < n; i++) {
        free(matrix[i]);
    }
    free(matrix);
}

int main() {
    int n;
    printf("Enter the number of samples\n");
    scanf("%d",&n);
    int sizes[n];
    for(int i=0;i<n;i++){
        printf("Enter sample %d :",i+1);
        scanf("%d",&sizes[i]);
    }
    int len = sizeof(sizes) / sizeof(sizes[0]);

    for (int i = 0; i < len; i++) {
        int n = sizes[i];
        printf("\nInput size n = %d\n", n);

        constant_space(n);
        printf("O(1)   Space: %d bytes\n",3*sizeof(int));

        linear_space(n);
        printf("O(n)   Space: %lu bytes\n", n * sizeof(int));

        quadratic_space(n);
        printf("O(n^2) Space: %lu bytes\n",
               (unsigned long)n * n * sizeof(int));
    }

    return 0;
}