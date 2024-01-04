def recursive_sum(arr):
    """
    Рекурсивно подсчитывает сумму элементов массива.
    """
    if len(arr) == 1:
        return arr[0]

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    sum_left = recursive_sum(left_half)
    sum_right = recursive_sum(right_half)

    return sum_left + sum_right


# Пример использования
if __name__ == "__main__":
    array_example = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = recursive_sum(array_example)
    print(f"Сумма элементов массива: {result}")
