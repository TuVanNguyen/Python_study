def removeDuplicates(s: str) -> str:
    string_stack = []

    for i in range(len(4)):
        for letter in s:
            string_stack.append(letter)
            if len(string_stack) >= 1 and string_stack[-1] == letter :
                string_stack.pop()
            elif string_stack[0] == letter:
                print(letter)
            elif string_stack[-1] == 'a':
                print(letter)
            else:
                string_stack.append(letter)
    return "".join(string_stack) # From Leetcode Problem from datetime import date

