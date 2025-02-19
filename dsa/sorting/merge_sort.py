from dsa.models.node import Node


def find_middle(head: Node) -> Node:
    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def merge(head1: Node, head2: Node) -> Node:
    head = Node()
    tail = head

    while head1 and head2:
        if head1.value < head2.value:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next
        tail = tail.next
    tail.next = head1 or head2
    return head.next


def merge_sort(head: Node | None) -> Node:
    if not head or not head.next:
        return head
    middle = find_middle(head)
    after_middle = middle.next
    middle.next = None

    left = merge_sort(head)
    right = merge_sort(after_middle)
    return merge(left, right)


def build_linked_list(arr: list[int]) -> Node:
    head = Node(value=arr[0])
    tail = head
    for v in arr[1:]:
        tail.next = Node(value=v)
        tail = tail.next
    return head


def print_linked_list(head: Node) -> None:
    values = []
    while head:
        values.append(head.value)
        head = head.next
    print(values)


if __name__ == "__main__":
    linked_list = build_linked_list([2, 4, 1, 7, 3, 9])

    sorted_list = merge_sort(linked_list)
    print_linked_list(sorted_list)
