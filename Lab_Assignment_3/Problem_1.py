# Recursive function to reverse a stack
def reverse_stack(stack):
    if not stack:
        return
    top = stack.pop()
    reverse_stack(stack)
    insert_at_bottom(stack, top)

# Function to insert an element at the bottom of the stack


def insert_at_bottom(stack, element):
    if not stack:
        stack.append(element)
        return
    top = stack.pop()
    insert_at_bottom(stack, element)
    stack.append(top)


# Example usage
stack = [1, 2, 3, 4, 5]
print("Original stack:", stack)
reverse_stack(stack)
print("Reversed stack:", stack)


# T(n) = T(n-1) + O(n)
# = T(n-2) + O(n-1) + O(n)
# = T(n-3) + O(n-2) + O(n-1) + O(n)
# = ...
# = T(0) + O(1) + O(2) + ... + O(n-1) + O(n)
# The sum of the first n natural numbers can be expressed as n(n+1)/2. Therefore, the time complexity of the reverse_stack function can be simplified to O(n^2).
