# Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

numbers = 35231

def digitize(n):
    result = []
    n_str = str(n)
    for i in reversed(n_str):
        result.append(int(i))
    return result

print(digitize(numbers))