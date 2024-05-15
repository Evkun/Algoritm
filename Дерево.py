class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def search(root, key, path=[]):
    if root is None:
        return None, path
    path.append(root.val)
    if root.val == key:
        return root, path
    if root.val < key:
        return search(root.right, key, path)
    else:
        return search(root.left, key, path)

def print_tree(root, level=0, prefix="Root: "):
    if root is not None:
        print_tree(root.right, level + 1, "R---- ")
        print(" " * (level * 6) + prefix + str(root.val))
        print_tree(root.left, level + 1, "L---- ")

# Функция для создания дерева из массива
def construct_tree(arr):
    r = None
    for key in arr:
        r = insert(r, key)
    return r

# Пример использования
arr = [20, 8, 22, 4, 12, 10, 14]
root = construct_tree(arr)
key_to_find = 10
root = construct_tree(arr)
print_tree(root)
# Поиск вершины и пути к ней
node, path = search(root, key_to_find)
if node is not None:
    print(f"Вершина с ключом {key_to_find} найдена.")
    print("Путь к вершине:", " -> ".join(str(v) for v in path))
else:
    print(f"Вершина с ключом {key_to_find} не найдена.")
