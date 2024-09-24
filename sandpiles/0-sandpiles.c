#include <stdio.h>
#include "sandpiles.h"

int is_stable(int grid[3][3]);
void toppling(int grid[3][3]);
static void print_grid(int grid[3][3]);

void sandpiles_sum(int grid1[3][3], int grid2[3][3]) {
    int i, j;

    // Sum the grids
    for (i = 0; i < 3; i++) {
        for (j = 0; j < 3; j++) {
            grid1[i][j] += grid2[i][j];
        }
    }

    // Print "=" before starting any toppling rounds
    printf("=\n");

    // Check stability and apply toppling if necessary
    while (!is_stable(grid1)) {
        print_grid(grid1);
        printf("=\n"); // Print '=' after each grid output
        toppling(grid1);
    }

    // Print the final stable grid, followed by an "=" sign
    print_grid(grid1);
}

int is_stable(int grid[3][3]) {
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (grid[i][j] > 3) {
                return 0; // Not stable
            }
        }
    }
    return 1; // Stable
}

void toppling(int grid[3][3]) {
    int temp[3][3] = {0};
    int i, j;

    // Topple the unstable cells
    for (i = 0; i < 3; i++) {
        for (j = 0; j < 3; j++) {
            if (grid[i][j] > 3) {
                temp[i][j] -= 4;
                if (i > 0) temp[i - 1][j] += 1; // Up
                if (i < 2) temp[i + 1][j] += 1; // Down
                if (j > 0) temp[i][j - 1] += 1; // Left
                if (j < 2) temp[i][j + 1] += 1; // Right
            }
        }
    }

    // Apply the toppling changes to the grid
    for (i = 0; i < 3; i++) {
        for (j = 0; j < 3; j++) {
            grid[i][j] += temp[i][j];
        }
    }
}

static void print_grid(int grid[3][3]) {
    int i, j;

    for (i = 0; i < 3; i++) {
        for (j = 0; j < 3; j++) {
            if (j)
                printf(" ");
            printf("%d", grid[i][j]);
        }
        printf("\n");
    }
}
