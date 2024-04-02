def count_neg_nonneg(nums: list[int]) -> tuple[int, int]:
    #  Initialize counters
    neg_count, nonneg_count = 0, 0
    for num in nums:
        if num < 0:
            neg_count += 1
        else:
            nonneg_count += 1
    return neg_count, nonneg_count

if __name__ == '__main__':
    print(count_neg_nonneg([9, -13, 88, 2, 0, -5, -10, 1]))