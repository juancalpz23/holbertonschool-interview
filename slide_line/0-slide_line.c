#include "slide_line.h"

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
	int i, j;

	if (!line || (direction != SLIDE_LEFT && direction != SLIDE_RIGHT))
		return (0); /* Return failure if invalid input or direction */

	if (direction == SLIDE_LEFT)
	{
		for (i = 0; i < (int)size; i++)
			if (line[i] == 0)
				for (j = i + 1; j < (int)size && line[j] == 0; j++)
					;
		for (i = 0; i < (int)size - 1; i++)
			if (line[i] == line[i + 1] && line[i] != 0)
			{
				line[i] *= 2;
				line[i + 1] = 0;
				i++;
			}
	}
	else
	{
		for (i = (int)size - 1; i >= 0; i--)
			if (line[i] == 0)
				for (j = i - 1; j >= 0 && line[j] == 0; j--)
					;
		for (i = (int)size - 1; i > 0; i--)
			if (line[i] == line[i - 1] && line[i] != 0)
			{
				line[i] *= 2;
				line[i - 1] = 0;
				i--;
			}
	}
	return (1);
}
