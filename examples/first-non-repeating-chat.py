# Challenge: Find the First Non-Repeating Character
# Problem: Given a string, find the first non-repeating character and return its index. If it doesn't exist, return -1.

def find_first_non_repeating_char(string: str) -> int:
    count_dict = {}
    for char in string:
        count_dict[char] = string.count(char)

    print(count_dict)

    first_non_rep_index = -1
    for k, v in count_dict.items():
        if count_dict[k] == 1:
            first_non_rep_index = string.index(k)
            break

    return first_non_rep_index

print(find_first_non_repeating_char('cellphone'))
print(find_first_non_repeating_char('heitor'))
print(find_first_non_repeating_char('saskatoon'))
print(find_first_non_repeating_char('aabb'))
print(find_first_non_repeating_char('leetcode'))
print(find_first_non_repeating_char('loveleetcode'))