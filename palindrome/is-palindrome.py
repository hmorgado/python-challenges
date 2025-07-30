# check if is palindrome
#

def is_palindrome(_w: str) -> bool:
    word = _w.strip()
    size = len(word)
    if size == 1:
        print(f"{word} IS palindrome")
        return True

    if size == 0:
        print("Empty string...")
        return False

    reversed_word = word[::-1]
    for i in range(0, size - 1):
        if word[i] != reversed_word[i]:
            print(f"{word} IS NOT palindrome")
            return False
    print(f"{word} IS palindrome")
    return True

if __name__ == "__main__":
    is_palindrome("heitor")
    is_palindrome("racecar")
    is_palindrome("test")
    is_palindrome("abba")
    is_palindrome("   ")
    is_palindrome("a")

# def is_palindrome(w):
#     word = w.strip()
#     size = len(word)
#     if size == 1:
#         print(f"{w} IS palindrome")
#         return True
#
#     word_reverse = w[::-1].strip()
#     for i in range(0, size - 1):
#         if word[i] != word_reverse[i]:
#             print(f"{word} IS NOT palindrome")
#             return False
#         print(f"{word} IS palindrome")
#         return True
#
# if __name__ == "__main__":
#     for w in ["racecar", "level", "heitor", "deified", "rotor", "moto", "abba", "a"]:
#         is_palindrome(w)
