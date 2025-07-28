# sum all integers

def is_palindrome(w):
    word = w.strip()
    size = len(word)
    if size == 1:
        print(f"{w} IS palindrome")
        return True

    word_reverse = w[::-1].strip()
    for i in range(0, size - 1):
        if word[i] != word_reverse[i]:
            print(f"{word} IS NOT palindrome")
            return False
        print(f"{word} IS palindrome")
        return True

if __name__ == "__main__":
    for w in ["racecar", "level", "heitor", "deified", "rotor", "moto", "abba", "a"]:
        is_palindrome(w)
