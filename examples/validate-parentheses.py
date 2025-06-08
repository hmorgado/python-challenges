# AI script

def is_valid_parentheses(s: str) -> bool:
    stack = []
    mapping = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in s:
        if char in mapping.values():
            # add char to stack if it matches any of the values ( { [
            stack.append(char)
            print(f"stack: {stack}")
            print('---')
        elif char in mapping:
            if stack and stack[-1] == mapping[char]:
                print(f"stack[-1]: {stack[-1]}")
                print(f"mapping[char]: {mapping[char]}")
                stack.pop()
            else:
                # return false if stack is empty AND last item in the list
                # does not match mapping[char] (for ex mapping[']'])
                return False
        else:
            return False

    return not stack

# Example usage
# print(is_valid_parentheses("()[]{}")) # Output: True
# print(is_valid_parentheses("(]"))     # Output: False
print(is_valid_parentheses("()()"))     # Output: True
# print(is_valid_parentheses("[]"))     # Output: True
