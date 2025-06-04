_nums = [1, 3, 6, 8, 5, 4, 9, 9]
nums = set()
nums = _nums

target = 11

for i in range(len(nums)):
    current_item = nums[i]
    delta_target_item = target - current_item
    if delta_target_item in nums:
        index_one = nums.index(delta_target_item)
        index_two = nums.index(current_item)
        print(f"index {index_one}, element {nums[index_one]}")
        print(f"index {index_two}, element {nums[index_two]}")
        print(f"sum {nums[index_one] + nums[index_two]}")
        print('---')