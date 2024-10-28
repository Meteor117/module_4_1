from math import inf

def divide(first, second):

    if second != 0:
        result = first / second
        return result
    else:
        result = float('inf')
    return inf

if __name__ == '__main__':
    result3 = divide(49, 7)
    result4 = divide(15, 0)

    print(result3)
    print(result4)






# positive_infinity = float('inf')
# print(positive_infinity)
#
# negative_infinity = float('-inf')
# print(negative_infinity)