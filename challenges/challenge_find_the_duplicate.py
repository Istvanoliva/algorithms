from collections import Counter


def find_duplicate(nums):
    if nums:
        for item in nums:
            if type(item) != int or item < 1:
                return False
        list_nums = Counter(nums).most_common(1)[0]
        if list_nums[1] > 1:
            return list_nums[0]
    return False
