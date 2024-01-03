#include "lists.h"

/**
 * check_cycle - checks if there's a cycle in linkedlist
 * @head: pointer to list to be checked
 * Return: 1 if cycle and 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *tortoise = list, *hare = list;

	while (hare && hare->next)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;

		if (tortoise == hare) {
			return (1);
		}
	}

	return (0);
}
