def selection_sort(seq: list[int]) -> None:
    n = len(seq)
    for i in range(n - 1):
        smallest = i
        for j in range(i + 1, n):
            if seq[j] < seq[smallest]:
                smallest = j
        seq[i], seq[smallest] = seq[smallest], seq[i]
        

my_list = [2, 4, 7, 1, 5, 2, 0, 4, 3]
print('Original list:', my_list)
selection_sort(my_list)
print('Sorted list  :', my_list)