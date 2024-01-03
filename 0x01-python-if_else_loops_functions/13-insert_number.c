#include "lists.h"

/**
 * insert_node - adds a new node to a sorted listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be assigned to new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *prev = *head, *current = *head;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);

	if (number < (*head)->n)
	{
		new_node->n = number;
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	while (current && current->n < number)
	{
		prev = current;
		current = current->next;
	}
	new_node->n = number;
	new_node->next = current;
	prev->next = new_node;
	return (new_node);
}
