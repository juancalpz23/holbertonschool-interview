#include <stdio.h>
#include "sandpiles.h"

/**
 * sandpiles_sum - Computes the sum of two sandpiles
 * @grid1: The first 3x3 sandpile grid
 * @grid2: The second 3x3 sandpile grid
 *
 * This function adds grid2 to grid1 and topples unstable cells
 * in grid1 until it becomes stable.
 */
void sandpiles_sum(int grid1[3][3], int grid2[3][3])
{
    int i, j;

    /* Sum the grids */
    for (i = 0; i < 3; i++)
    {
        for (j = 0; j < 3; j++)
        {
            grid1[i][j] += grid2[i][j];
        }
    }

    /* Check stability and apply toppling if necessary */
    while (!is_stable(grid1))
    {
        /* Print '=' and the grid if unstable */
        printf("=\n");
        print_grid(grid1);
        toppling(grid1);
    }
}

/**
 * is_stable - Checks if a sandpile is stable
 * @grid: The 3x3 sandpile grid
 *
 * Return: 1 if the grid is stable, 0 otherwise.
 */
int is_stable(int grid[3][3])
{
    int i, j;

    for (i = 0; i < 3; i++)
    {
        for (j = 0; j < 3; j++)
        {
            if (grid[i][j] > 3)
            {
                return (0); /* Not stable */
            }
        }
    }
    return (1); /* Stable */
}

/**
 * toppling - Topples the unstable cells in a sandpile
 * @grid: The 3x3 sandpile grid
 *
 * This function distributes the grains from unstable cells (more than
 * 3 grains) to the neighboring cells.
 */
void toppling(int grid[3][3])
{
    int temp[3][3] = {0};
    int i, j;

    /* Topple the unstable cells */
    for (i = 0; i < 3; i++)
    {
        for (j = 0; j < 3; j++)
        {
            if (grid[i][j] > 3)
            {
                temp[i][j] -= 4;
                if (i > 0)
                    temp[i - 1][j] += 1; /* Up */
                if (i < 2)
                    temp[i + 1][j] += 1; /* Down */
                if (j > 0)
                    temp[i][j - 1] += 1; /* Left */
                if (j < 2)
                    temp[i][j + 1] += 1; /* Right */
            }
        }
    }

    /* Apply the toppling changes to the grid */
    for (i = 0; i < 3; i++)
    {
        for (j = 0; j < 3; j++)
        {
            grid[i][j] += temp[i][j];
        }
    }
}

/**
 * print_grid - Prints a 3x3 grid
 * @grid: The 3x3 sandpile grid
 *
 * This function prints the grid in a formatted manner.
 */
void print_grid(int grid[3][3])
{
    int i, j;

    for (i = 0; i < 3; i++)
    {
        for (j = 0; j < 3; j++)
        {
            if (j)
                printf(" ");
            printf("%d", grid[i][j]);
        }
        printf("\n");
    }
}
