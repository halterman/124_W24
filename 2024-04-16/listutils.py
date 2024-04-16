def selection_sort(seq: list[int]) -> None:
    """ Rearranges the element of a list of integers so that
        the elements appear in non-decreasing order. """
    n = len(seq)
    for i in range(n - 1):
        smallest = i
        for j in range(i + 1, n):
            if seq[j] < seq[smallest]:
                smallest = j
        if smallest != i:
            seq[i], seq[smallest] = seq[smallest], seq[i]
        

def is_ascending_1(seq: list[int]) -> bool:
    n = len(seq)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if seq[i] > seq[j]:
                return False
    return True


def is_ascending_2(seq: list[int]) -> bool:
    n = len(seq)
    for i in range(1, n):
        if seq[i - 1] > seq[i]:
            return False
    return True