class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Singly:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def merge_sort(self, head):
        if head is None or head.next is None:
            return head

        middle = self.get_middle(head)
        next_to_middle = middle.next
        middle.next = None

        left = self.merge_sort(head)
        right = self.merge_sort(next_to_middle)

        sorted_list = self.merge(left, right)
        return sorted_list

    def get_middle(self, head):
        if head is None:
            return head

        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, left, right):
        result = None

        if left is None:
            return right
        if right is None:
            return left

        if left.data <= right.data:
            result = left
            result.next = self.merge(left.next, right)
        else:
            result = right
            result.next = self.merge(left, right.next)

        return result

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

# Пример использования
sll = Singly()
sll.append(3)
sll.append(1)
sll.append(4)
sll.append(2)
sll.append(5)

print("Исходный список:")
sll.print_list()

sll.head = sll.merge_sort(sll.head)

print("Отсортированный список:")
sll.print_list()
