import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Параметри симуляції
num_simulations = 1_000_000  # Велика кількість кидків

# Симуляція кидків двох кубиків
dice1 = np.random.randint(1, 7, num_simulations)
dice2 = np.random.randint(1, 7, num_simulations)
sums = dice1 + dice2

# Підрахунок частоти появи кожної суми
sum_counts = pd.Series(sums).value_counts().sort_index()

# Обчислення ймовірностей
probabilities = (sum_counts / num_simulations) * 100

# Таблиця аналітичних ймовірностей
analytical_probs = {
    2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89,
    7: 16.67, 8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78
}

# Створення таблиці з результатами
results_df = pd.DataFrame({
    "Сума": sum_counts.index,
    "Ймовірність (Монте-Карло), %": probabilities.values,
    "Ймовірність (Аналітична), %": [analytical_probs[k] for k in sum_counts.index],
})

# Додавання стовпця "Різниця (%)"
results_df["Різниця (%)"] = results_df["Ймовірність (Монте-Карло), %"] - results_df["Ймовірність (Аналітична), %"]

# Вивід таблиці
print(results_df)

# Візуалізація
plt.figure(figsize=(10, 6))
plt.bar(results_df["Сума"] - 0.2, results_df["Ймовірність (Монте-Карло), %"], width=0.4, label="Монте-Карло", alpha=0.7)
plt.bar(results_df["Сума"] + 0.2, results_df["Ймовірність (Аналітична), %"], width=0.4, label="Аналітичні", alpha=0.7)
plt.xlabel("Сума чисел на кубиках")
plt.ylabel("Ймовірність (%)")
plt.title("Порівняння ймовірностей методом Монте-Карло та аналітичних розрахунків")
plt.xticks(results_df["Сума"])
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()
