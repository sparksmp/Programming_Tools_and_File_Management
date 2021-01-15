
'''
S = "spring semester is almost over"
print(S[16:])
print(S[:15])
print(S[16:18])
print(S[::-1])

# Problem 4:
D = {'W' : (10, 20, 30), 'X' : {'a' : 1, 'b' : ['F', 'G'], 'c' : 'H'}, 'Y' : ['I', 'J', 'K'], 'Z' : 'summer'}
print(D['Z'][5])
print(D['X']['b'][1])
print(D['W'][2])
print(D['Y'][1])

# Problem 5:
a. closed form: a(n) = 1/9(-5)^n - 1/9(4)^n
b. 0, 2, 

#Probmel 6:
a. 

def a(n, a0 = 0, a1 = 2):
    if n == 0:
        return a0
    elif n == 1:
        return a1
    else:
        return a(n-1, a1, 14 * a0 - 5 * a1)

b. 

def mem_a(n, D ={}):
    if n in D:
        return D[n]
    else:
        if n == 0:
            result = 0
        elif n == 1:
            result = 1
        else:
            result = -5 * mem_a(n-1) + 14 * mem_a(n-2)
    D[n] = result
    return result

# Problem 7:
[7, 3, 8, 2, 4, 5, 4, 3, 9, 1, 0, 2, 6]
[7, 3, 8, 2, 4, 5] [4, 3, 9, 1, 0, 2, 6]
[7, 3, 8] [2, 4, 5] [4, 3, 9] [1, 0, 2, 6]
[7] [3, 8] [2] [4, 5] [4] [3, 9] [1, 0] [2, 6]
[7] [3] [8] [2] [4] [5] [4] [3] [9] [1] [0] [2] [6]
'''
# Problem 8:
def quick_sort(data):
    if len(data) <= 1:
        return data
    else:
        Smaller = []
        Greater = []
        pivot = data[0]
        for value in data[1:]:
            if len(value) < len(pivot):
                Smaller.append(value)
            else:
                Greater.append(value)
        return quick_sort(Greater) + [pivot] + quick_sort(Smaller)


print(quick_sort(['abc', 'a', 'aabb', 'acb', 'ab', 'abcab']))