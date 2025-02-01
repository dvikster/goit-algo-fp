import matplotlib.pyplot as plt
import numpy as np

def draw_tree(ax, x, y, length, angle, level):
    if level == 0:
        return

    # Обчислюємо нові кінцеві координати гілки
    x_new = x + length * np.cos(angle)
    y_new = y + length * np.sin(angle)

    # Малюємо гілку
    ax.plot([x, x_new], [y, y_new], color='brown', linewidth=1)

    # Зменшуємо довжину гілки
    new_length = length * 0.75

    # Викликаємо рекурсію для двох нових гілок 
    draw_tree(ax, x_new, y_new, new_length, angle + np.pi / 4, level - 1)  
    draw_tree(ax, x_new, y_new, new_length, angle - np.pi / 4, level - 1)

def main():
    level = int(input("Введіть рівень рекурсії (рекомендовано 7-10): "))

    fig, ax = plt.subplots(figsize=(12, 8))  
    ax.set_aspect('equal')
    ax.axis('off')

    # Запускаємо рекурсію від основи дерева
    draw_tree(ax, 0, -200, 120, np.pi / 2, level)

    plt.show()

if __name__ == "__main__":
    main()
