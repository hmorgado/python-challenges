# personal script

_nums = [1, 3, 6, 8, 5, 4, 9, 9, 0]
nums = set()
nums = _nums

target = 8

visited_indexes = []
target_found = False
for i in range(len(nums)):
    current_item = nums[i]
    delta_target_item = target - current_item
    if delta_target_item in nums:
        index_one = nums.index(delta_target_item)
        index_two = nums.index(current_item)

        hash_1 = f"{index_one}-{index_two}"
        hash_2 = f"{index_two}-{index_one}"

        target_found = True
        both_index_are_the_same = index_one == index_two
        condition = (hash_1 not in visited_indexes or hash_2 not in visited_indexes) and not both_index_are_the_same
        if condition:
            print(f"index {index_one}, element {nums[index_one]}")
            print(f"index {index_two}, element {nums[index_two]}")
            print(f"sum {nums[index_one] + nums[index_two]}")

            visited_indexes.append(hash_1)
            visited_indexes.append(hash_2)
            print('---')

if not target_found:
    print(f"target {target} not found")