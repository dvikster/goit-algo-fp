# Програма для вибору страв з максимальними калоріями в межах заданого бюджету
# з використанням жадібного алгоритму та алгоритму динамічного програмування.

# Функція, що реалізує жадібний алгоритм
def greedy_algorithm(items, budget):
    # Сортуємо страви за співвідношенням калорії до вартості у спадному порядку
    sorted_items = sorted(items.items(),
                          key=lambda x: x[1]['calories'] / x[1]['cost'],
                          reverse=True)
    chosen = []       # Список вибраних страв
    total_cost = 0    # Загальна вартість вибраних страв
    total_calories = 0  # Сумарна калорійність вибраних страв

    # Ітеруємо по відсортованому списку страв
    for name, info in sorted_items:
        # Якщо додавання страви не перевищує бюджет, додаємо її до списку
        if total_cost + info['cost'] <= budget:
            chosen.append(name)
            total_cost += info['cost']
            total_calories += info['calories']
    
    # Повертаємо список вибраних страв, загальну вартість та сумарну калорійність
    return chosen, total_cost, total_calories

# Функція, що використовує динамічне програмування 
def dynamic_programming(items, budget):
    item_names = list(items.keys())
    n = len(item_names)
    
    # Створюємо таблицю dp розміром (n+1) x (budget+1), заповнену нулями
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    
    # Заповнюємо таблицю dp: dp[i][w] - максимальна калорійність, що може бути досягнута
    # використовуючи перші i страв при бюджеті w
    for i in range(1, n + 1):
        name = item_names[i - 1]
        cost = items[name]['cost']
        calories = items[name]['calories']
        for w in range(budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)
            else:
                dp[i][w] = dp[i - 1][w]
    
    # Відновлюємо оптимальний набір страв, використовуючи заповнену таблицю dp
    chosen = []
    w = budget
    for i in range(n, 0, -1):
        # Якщо значення dp змінилося, це означає, що страва була вибрана
        if dp[i][w] != dp[i - 1][w]:
            chosen.append(item_names[i - 1])
            w -= items[item_names[i - 1]]['cost']
    
    chosen.reverse()  # Повертаємо порядок страв у початковому порядку
    # Повертаємо список вибраних страв та максимальну сумарну калорійність
    return chosen, dp[n][budget]

# Словник з інформацією про страви: назва -> вартість та калорійність
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100  # Заданий бюджет

# Виконуємо функцію жадібного алгоритму та виводимо результати
greedy_result = greedy_algorithm(items, budget)
print("Жадібний алгоритм:")
print("Вибрані страви:", greedy_result[0])
print("Загальна вартість:", greedy_result[1])
print("Сумарна калорійність:", greedy_result[2])

# Виконуємо функцію динамічного програмування та виводимо результати
dp_result = dynamic_programming(items, budget)
print("\nДинамічне програмування:")
print("Вибрані страви:", dp_result[0])
print("Максимальна сумарна калорійність:", dp_result[1])
