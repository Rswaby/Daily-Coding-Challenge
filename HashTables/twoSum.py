def two_sum(lst, target):
    seen = {}

    for num in lst:
        if target - num in seen:
            return True
        seen[num] = True
    return False