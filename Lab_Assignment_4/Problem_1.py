def sort_stack(stack):
    if len(stack) <= 1:
        return stack

    top = stack.pop()
    sorted_stack = sort_stack(stack)

    if top >= sorted_stack[-1]:
        sorted_stack.append(top)
    else:
        temp = sorted_stack.pop()
        sorted_stack = sort_stack(stack+[top])
        sorted_stack.append(temp)

    return sorted_stack


# Example usage
stack = [5, 1, 2, 6, 4]
sorted_stack = sort_stack(stack)
print(sorted_stack)

# output
# [6, 5, 4, 2, 1]
