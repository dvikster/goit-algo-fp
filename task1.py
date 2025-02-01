# Клас вузла однозв’язного списку.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Функція додавання вузла на початок списку.
# Повертає нову голову списку.
def push(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node

# Функція друку списку.
def print_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

# Завдання 1: Реверсування однозв’язного списку.
# Змінює напрямок посилань між вузлами та повертає нову голову перевернутого списку.
def reverse_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next  # зберігаємо наступний вузол
        current.next = prev       # змінюємо напрямок посилання
        prev = current            # рухаємо prev вперед
        current = next_node       # рухаємо current вперед
    return prev

# Допоміжна функція для розділення списку на дві половини.
# Використовує метод повзунків: slow і fast.
# Повертає кортеж (ліва_половина, права_половина).
def split_list(head):
    if head is None or head.next is None:
        return head, None

    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    mid = slow.next
    slow.next = None  # розділяємо список
    return head, mid

# Функція злиття двох відсортованих списків.
# Повертає голову об’єднаного відсортованого списку.
def merge_sorted_lists(a, b):
    if a is None:
        return b
    if b is None:
        return a

    if a.data <= b.data:
        result = a
        result.next = merge_sorted_lists(a.next, b)
    else:
        result = b
        result.next = merge_sorted_lists(a, b.next)
    return result

# Завдання 2: Сортування злиттям для однозв’язного списку.
# Рекурсивно сортує список і повертає його голову.
def merge_sort(head):
    if head is None or head.next is None:
        return head

    # Розділяємо список на дві половини
    left, right = split_list(head)

    # Рекурсивно сортуємо кожну половину
    left = merge_sort(left)
    right = merge_sort(right)

    # Зливаємо відсортовані половини
    return merge_sorted_lists(left, right)

# Завдання 3: Об'єднання двох відсортованих списків в один відсортований список.
# Використовує функцію merge_sorted_lists.
def merge_two_sorted_lists(list1, list2):
    return merge_sorted_lists(list1, list2)

# Демонстрація роботи завдань
if __name__ == '__main__':
    # ============================================================
    # Завдання 1: Реверсування однозв’язного списку
    # ============================================================
    print("=== Завдання 1: Реверсування однозв’язного списку ===")
    list_head = None
    # Створюємо список: 1 -> 2 -> 3 -> 4 -> None
    # (використовується push, тому дані додаються на початок)
    for value in [4, 3, 2, 1]:
        list_head = push(list_head, value)
    
    print("Початковий список:")
    print_list(list_head)
    
    reversed_head = reverse_list(list_head)
    print("Список після реверсування:")
    print_list(reversed_head)
    
    # ============================================================
    # Завдання 2: Сортування злиттям однозв’язного списку
    # ============================================================
    print("\n=== Завдання 2: Сортування злиттям ===")
    unsorted_head = None
    # Створюємо список з елементами у випадковому порядку: 2 -> 3 -> 20 -> 5 -> 10 -> 15 -> None
    for value in [15, 10, 5, 20, 3, 2]:
        unsorted_head = push(unsorted_head, value)
    
    print("Початковий несортований список:")
    print_list(unsorted_head)
    
    sorted_head = merge_sort(unsorted_head)
    print("Список після сортування злиттям:")
    print_list(sorted_head)
    
    # ============================================================
    # Завдання 3: Об'єднання двох відсортованих однозв’язних списків
    # ============================================================
    print("\n=== Завдання 3: Об'єднання двох відсортованих списків ===")
    
    # Створюємо перший список: 1 -> 3 -> 5 -> None (початковий)
    sorted_list1 = None
    for value in [5, 3, 1]:
        sorted_list1 = push(sorted_list1, value)
    print("Початковий перший список (до сортування):")
    print_list(sorted_list1)
    
    sorted_list1 = merge_sort(sorted_list1)
    print("Відсортований перший список:")
    print_list(sorted_list1)
    
    # Створюємо другий список: 2 -> 4 -> 6 -> None (початковий)
    sorted_list2 = None
    for value in [6, 4, 2]:
        sorted_list2 = push(sorted_list2, value)
    print("Початковий другий список (до сортування):")
    print_list(sorted_list2)
    
    sorted_list2 = merge_sort(sorted_list2)
    print("Відсортований другий список:")
    print_list(sorted_list2)
    
    merged_list = merge_two_sorted_lists(sorted_list1, sorted_list2)
    print("Об'єднаний відсортований список:")
    print_list(merged_list)
