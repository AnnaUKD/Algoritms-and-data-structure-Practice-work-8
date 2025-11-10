from binarytree import Node

def add(node, value):
    if node is None:
        return Node(value)
    if value < node.value:
        node.left = add(node.left, value)
    if value > node.value:
        node.right = add(node.right, value)
    return node


def find(node, value):
    if node is None:    
        return Node(value)
    if value == node.value:
        return True


def min_value(node):
    if node is None:    
        return None
    while node.left:
        node = node.left
    return node.value


def max_value(node):
    if node is None:    
        return None
    while node.right:
        node = node.right
    return node.value


def list_elements(node):
    if node is None:
        return []
    return list_elements(node.left) + [node.value] + list_elements(node.right)


def count(node):
    if node is None:
        return 0
    return 1 + count(node.left) + count(node.right)


def delete(node, value):
    if node is None:
        return None
    if value < node.value:
        node.left = delete(node.left, value)
    if value > node.value:
        node.right = delete(node.right, value)
    else:
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        temp = node.right
        while temp.left:
            temp = temp.left
        node.value = temp.value
        node.right = delete(node.right, temp.value)
    return node


def print_tree(node):
    if node:
        print(node)
    else:
        print('Дерево порожнє')

root = None
for v in [10, 5, 15, 67, 9]:
    root = add(root, v)



print_tree(root)
print('Перелік елементів: ', list_elements(root))
print('Найменше значення дерева: ', min_value(root))
print('Найбільше значення дерева: ', max_value(root))
print('Кількість елементів дерева: ', count(root))
print('Чи є введений Вами елемент у дереві?: ', find(root, 89))
print('Чи є введений Вами елемент у дереві?: ', find(root, 10))

root = delete(root, 5)

print_tree(root)
print(list_elements(root))

