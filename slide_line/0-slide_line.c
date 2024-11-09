#include "slide_line.h"

/**
 * shift_left - Shifts non-zero values to the left in the array.
 * @line: Array of integers.
 * @size: Size of the array.
 */
void shift_left(int *line, size_t size)
{
	size_t i, j = 0;

	for (i = 0; i < size; i++)
	{
		if (line[i] != 0)
		{
			if (j < i)
			{
				line[j] = line[i];
				line[i] = 0;
			}
			j++;
		}
	}
}

/**
 * shift_right - Shifts non-zero values to the right in the array.
 * @line: Array of integers.
 * @size: Size of the array.
 */
void shift_right(int *line, size_t size)
{
	int i, j = size - 1;

	for (i = size - 1; i >= 0; i--)
	{
		if (line[i] != 0)
		{
			if (j > i)
			{
				line[j] = line[i];
				line[i] = 0;
			}
			j--;
		}
	}
}

/**
 * slide_line - Slides and merges an array based on direction.
 *
 * @line: Array of integers.
 * @size: Size of the array.
 * @direction: Direction to slide (SLIDE_LEFT or SLIDE_RIGHT).
 *
 * Return: 1 on success, 0 on failure.
 */
int slide_line(int *line, size_t size, int direction)
{
	size_t i;

	if (!line || (direction != SLIDE_LEFT && direction != SLIDE_RIGHT))
		return (0);

	if (direction == SLIDE_LEFT)
	{
		shift_left(line, size);
		for (i = 0; i < size - 1; i++)
		{
			if (line[i] == line[i + 1] && line[i] != 0)
			{
				line[i] *= 2;
				line[i + 1] = 0;
			}
		}
		shift_left(line, size);
	}
	else
	{
		shift_right(line, size);
		for (i = size - 1; i > 0; i--)
		{
			if (line[i] == line[i - 1] && line[i] != 0)
			{
				line[i] *= 2;
				line[i - 1] = 0;
			}
		}
		shift_right(line, size);
	}

return (1);
}
