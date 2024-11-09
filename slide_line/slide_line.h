#ifndef SLIDE_LINE_H
#define SLIDE_LINE_H

#include <stddef.h>  /* For size_t */

/* Define macros for directions */
#define SLIDE_LEFT  0
#define SLIDE_RIGHT 1

/**
 * slide_line - Slides and merges the integers in an array.
 *
 * @line: Pointer to an array of integers.
 * @size: The number of elements in the array.
 * @direction: The direction to slide (SLIDE_LEFT or SLIDE_RIGHT).
 *
 * Return: 1 on success, 0 on failure.
 */
int slide_line(int *line, size_t size, int direction);

#endif /* SLIDE_LINE_H */
