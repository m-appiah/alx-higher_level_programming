#include "lists.h"
#include <stddef.h>

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Pointer to the head of a list
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *ptr;
	int array[3000] = {0};
	int len = 0, r_idx = 2999;

	if (head == NULL)
		return (1);

	ptr = *head;

	if (ptr == NULL || ptr->next == NULL)
		return (1);

	while (ptr != NULL)
	{
		array[r_idx] = ptr->n;
		len++;
		r_idx--;
		ptr = ptr->next;
	}
	ptr = *head;
	r_idx++;

	while (ptr != NULL)
	{
		if (ptr->n != array[r_idx])
			return (0);
		r_idx++;
		ptr = ptr->next;
	}

	return (1);
}

