#include "binary_trees.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * swap_values - Swap the values of two nodes.
 * @a: Pointer to the first node.
 * @b: Pointer to the second node.
 */
void swap_values(binary_tree_t *a, binary_tree_t *b)
{
	int temp = a->n;
	a->n = b->n;
	b->n = temp;
}

/**
 * insert_node - Insert the node in the next available position.
 * @root: Pointer to the root of the heap.
 * @new: Node to insert.
 *
 * Return: The parent of the newly inserted node.
 */
heap_t *insert_node(heap_t *root, heap_t *new)
{
	binary_tree_t *queue[1024];
	int front = 0;
	int rear = 0;
	binary_tree_t *current;

	if (!root)
	return (NULL);
	
	queue[rear++] = root;

	while (front < rear)
	{
		current = queue[front++];

		if (!current->left || !current->right)
		{
			if (!current->left)
			{
				current->left = new;
				new->parent = current;
				return (current);
			}
            else
			{
				current->right = new;
				new->parent = current;
				return (current);
			}
		}
		
		if (current->left)
		queue[rear++] = current->left;
		
		if (current->right)
		queue[rear++] = current->right;
    }

    return (NULL);
}

/**
 * heap_insert - Inserts a value into a Max Binary Heap.
 * @root: Double pointer to the root node of the heap.
 * @value: Value to insert.
 *
 * Return: Pointer to the newly inserted node, or NULL on failure.
 */
heap_t *heap_insert(heap_t **root, int value)
{
    heap_t *new = binary_tree_node(NULL, value);
    heap_t *parent;

    if (!root || !new)
        return (NULL);

    if (!*root)
    {
        *root = new;
        return (new);
    }

    parent = insert_node(*root, new);
    if (!parent)
    {
        free(new);
        return (NULL);
    }

    while (new->parent && new->n > new->parent->n)
    {
        swap_values(new, new->parent);
        new = new->parent;
    }

    return (new);
}
