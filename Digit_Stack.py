def golf(commands):
    sum = 0
    stack = []
    for command in commands:
        if (command.split(" ")[0] == "POP"):
            try:
                sum = int(stack[-1]) + sum
            except Exception:
                sum = 0 + sum
            if len(stack) != 0:
                stack.pop(-1)
        elif (command.split(" ")[0] == "PUSH"):
            stack += command.split(" ")[1]
        else:
            try:
                sum = int(stack[-1]) + sum
            except Exception:
                sum = 0 + sum
    return sum


golf(("POP", "POP")) == 0
# if __name__ == '__main__':
#    # These "asserts" using only for self-checking and not necessary for auto-testing
#    assert golf(("PUSH 3", "POP", "POP", "PUSH 4", "PEEK", "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK")) == 8, "Example"
#    assert golf(("POP", "POP")) == 0, "PopPop"
#    assert golf(("PUSH 9", "PUSH 9", "POP")) == 9, "Push 9"
#    assert golf(()) == 0, "Empty"
#    print("All done? Earn rewards by using the 'Check' button!")



#"PUSH X" -- add X in the stack, where X is a digit.
#"POP" -- look and remove the top position. If the stack is empty, then it returns 0 (zero) and does nothing.
#"PEEK" -- look at the top position. If the stack is empty, then it returns 0 (zero). The stack can only contain digits.
#You should process all commands and sum all digits which were taken from the stack ("PEEK" or "POP"). The initial value of the sum is 0 (zero).

#Let's look at an example, here’s the sequence of commands:

#["PUSH 3", "POP", "POP", "PUSH 4", "PEEK", "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"]

#| Command | Stack | Sum 
#|---------|-------|-----
#| PUSH 3  | 3     | 0
#| POP     |       | 0+3
#| POP     |       | 3+0
#| PUSH 4  | 4     | 3
#| PEEK    | 4     | 3+4
#| PUSH 9  | 4,9   | 7
#| PUSH 0  | 4,9,0 | 7
#| PEEK    | 4,9,0 | 7+0
#| POP     | 4,9   | 7+0
#| PUSH 1  | 4,9,1 | 7
#| PEEK    | 4,9,1 | 7+1=8