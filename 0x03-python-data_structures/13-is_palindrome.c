#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to the head of the list
 *
 * Return: 1 if the list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *prev = NULL;
	listint_t *second_half, *mid_node = NULL;
	int is_palindrome = 1;

	if (*head == NULL || (*head)->next == NULL)
		return 1;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;

		listint_t *next = slow->next;
		slow->next = prev;
		prev = slow;
		slow = next;
	}

	if (fast != NULL)
	{
		mid_node = slow;
		slow = slow->next;
	}

	second_half = slow;
	while (prev != NULL && second_half != NULL)
	{
		if (prev->n != second_half->n)
		{
			is_palindrome = 0;
			break;
		}
		prev = prev->next;
		second_half = second_half->next;
	}

	listint_t *restore = NULL;
	while (slow != NULL)
	{
		listint_t *next = slow->next;
		slow->next = restore;
		restore = slow;
		slow = next;
	}

	if (mid_node != NULL)
		mid_node->next = restore;

	return is_palindrome;
}
