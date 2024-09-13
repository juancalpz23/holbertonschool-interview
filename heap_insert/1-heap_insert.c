#include "binary_trees.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * swap_values - Swap the values of two nodes
 * @a: Pointer to the first node
 * @b: Pointer to the second node
 */
void swap_values(binary_tree_t *a, binary_tree_t *b)
{
    int temp = a->n;
    a->n = b->n;
    b->n = temp;
}

/**
 * heapify_up - Restore the Max Heap property by swapping up
 * @node: The node to start heapifying up from
 */
void heapify_up(binary_tree_t *node)
{
    if (!node || !node->parent)
        return;

    if (node->n > node->parent->n)
    {
        swap_values(node, node->parent);
        heapify_up(node->parent);
    }
}

/**
 * insert_node - Insert a node into the Max Binary Heap
 * @root: Double pointer to the root node of the heap
 * @value: Value to store in the node to be inserted
 *
 * Return: Pointer to the newly inserted node, or NULL on failure
 */
heap_t *insert_node(heap_t **root, int value)
{
    if (!root)
        return NULL;

    binary_tree_t *new_node = NULL;
    binary_tree_t *current = NULL;
    binary_tree_t *parent = NULL;
    binary_tree_t *queue[1024];
    int front = 0, rear = 0;

    if (*root == NULL)
    {
        new_node = binary_tree_node(NULL, value);
        if (!new_node)
            return NULL;
        *root = new_node;
        return new_node;
    }

    queue[rear++] = *root;

    while (front < rear)
    {
        current = queue[front++];
        if (!current->left || !current->right)
        {
            parent = current;
            break;
        }
        if (current->left)
            queue[rear++] = current->left;
        if (current->right)
            queue[rear++] = current->right;
    }

    new_node = binary_tree_node(parent, value);
    if (!new_node)
        return NULL;

    if (!parent->left)
        parent->left = new_node;
    else
        parent->right = new_node;

    heapify_up(new_node);
    return new_node;
}

/**
 * heap_insert - Insert a value into a Max Binary Heap
 * @root: Double pointer to the root node of the heap
 * @value: Value to store in the node to be inserted
 *
 * Return: Pointer to the newly inserted node, or NULL on failure
 */
heap_t *heap_insert(heap_t **root, int value)
{
    return insert_node(root, value);
}
