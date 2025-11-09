from binarytree import build

values = [10, 5, 15, 12, 3]
root = build(values)

print(root)


print(f"Список всіх елементів: {root.values}")
print(f"Найменший елемент: {min(root.values)}")
print(f"Найбільший елемент: {max(root.values)}")
print(f"Кількість: {len(root.values)}")
print(f"Чи є введений Вами елемент?: {12 in root.values}")
print(f"введений Вами елемент?: {7 in root.values}")
