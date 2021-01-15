# Exam 2
# Problem 1:
    # inorder: L H D M I B E A N J F C G Q O R K P
    # post-order: L H M I D E B N J F Q R O P K G C A

# Problem 2:
    #recurrence formula and inital conditions: a(n) = 2a(n-1) + 3a(n-2)
                                             # a(0) = 1 and a(1) = 0

    # closed form: a(n) = 3/4(-1)^n + 1/4(3)^n

# Problem 3:
    # Tail Recursion:

def tail_a(n, a4 = 2, a5 = 0):
    if n == 4:
        return a4
    elif n == 5:
        return a5
    else:
        a6 = 4 * a5 + 7 * a4
        return tail_a(n-1, a5, a6)

    # Memoization:

def mem_a(n, D = {}):
    if n in D:
        return D[n]
    else:
        if n == 4:
            result = 2
        elif n == 5:
            result = 0
        else:
            result = 4 * mem_a(n-1) + 7 * mem_a(n-2)
    D[n] = result
    return result

# Problem 4:

class Chain(object):
    def __init__(self, value = None):
        self.value = value
        self.right = None
    
    def insert_link(self, new_value):
        if self.right == None:
            self.right = Chain(new_value)
        else:
            self.right.insert_link(new_value)

    def generate_chain(self, L):
        self.value = L[0]
        for element in L[1:]:
            self.insert_link(element)
    
    def print_chain(self):
        print(self.value)
        if self.right != None:
            self.right.print_chain()

def main():
    C = Chain()
    C.generate_chain([1, 2, 3])
    C.print_chain()

main()

# Problem 5:
sqlite3
.open weather.db
create table rain (date text, inch_amount float);
create table temperature (date text, degrees_fahrenheit float);

select max(inch_amount) from rain;
select * from temperature where degrees_fahrenheit > 40.5;
