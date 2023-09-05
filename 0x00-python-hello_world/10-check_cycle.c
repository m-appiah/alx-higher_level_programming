#include "lists.h"

/**
 * check_cycle - function to check if a singly linked list has a cycle in it.
 * @list: pointer to the head of the list
 * Return: 1 if there is a cycle, 0 if there is no cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *walk = list;
	listint_t *run = list;

	while (walk != NULL && run != NULL && run->next != NULL)
	{
		walk = walk->next;
		run = run->next->next;

		if (walk == run)
			return (1);
	}

	return (0);
}
