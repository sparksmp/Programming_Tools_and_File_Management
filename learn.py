'''
age = input("How old are you? ")
height = input("How tall are you? ")
weight = input("How much do you weigh? ")

print(f"So, you're {age} old, {height} tall, and {weight} heavy.")

from sys import argv
script, user_name = argv
prompt = '>'

print(f"Hi {user_name}, I'm the {script} script.")
print("Id like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where fo you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"Alright, so you said {likes} about liking me. \n And you live in {lives}. Not sure where that is. \nAnd you have a {computer} computer. Nice")

from sys import argv
script, filename = argv

txt = open(filename)
print(f"Here's your file {filename}")
print(txt.read())

print("Type the filename again: ")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
txt.close()
txt_again.close()

from sys import argv
script, filename = argv
print("We're going to erase {filename}")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")
print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()
print("Now I am going to ask you fro three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to a file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally we close it.")
target.close()

from sys import argv
from os.path import exists
script, from_file, to_file = argv
print(f"Copying from {from_file} to {to_file}.")
in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")
print(f"Does the output file exists? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")
out_file.close()
in_file.close()

def chesse_crackers(cheese, crackers):
    print(f"You have {cheese} cheeses!")
    print(f"You have {crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanked.\n")

print("We can just give the function numbers directly:")
chesse_crackers(20, 30)

print("OR, we can use variables from our script:")
amount_cheese = 10
amount_crackers = 50

chesse_crackers(amount_cheese, amount_crackers)

print("We can even do math inside too:")
chesse_crackers(10 + 20, 5 + 6) #30, 11

print("And we can combine the two, variables and math:")
chesse_crackers(amount_cheese + 100, amount_crackers + 1000) # 110, 1050

from sys import argv
script, input_file = argv
def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())
current_file = open(input_file)

print("first let's print the whole file:\n")
print_all(current_file)
print("Now let's rewind, kind of like a tape.")
rewind(current_file)
print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)

def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print("MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

def exponatiate(a, b):
    print(f"EXPONENTIATING {a} ^ {b}")
    return a ** b
print("Let's do some math!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)
whatever = exponatiate(2, 3)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}, Child: {whatever}")

print("Here is a puzzle.")
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")

import sys
script, input_encoding, error = sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline()
    if line:
        print(line, encoding, errors)
        return main(language_file, encoding, errors)
def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<=====>", cooked_string)
languages = open("languages.txt", encoding = "utf-8")
main(languages, input_encoding, error)

print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n new lines and \t tabs.')
poem = "\tThe lovely world with logic so firmly plantedcannot discern \n the needs of love nor comprehend passion from intuition and requires an explination \n\t\twhere there is none"

print("---------------------")
print(poem)
print("---------------------")

five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

print("With a starting point of {}".format(start_point))
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates/ ")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)

print("We'd have {} beans, {} jars, and {} crates".format(*formula))

def break_words(stuff):
    words= stuff.split(' ')
    return words

def sort_words(words):
    return sorted(words)
    
def print_first_word(words):
    word = words.pop(0)
    print(word)

def print_last_word(words):
    word = word.pop(-1)
    print(word)

def sort_sentence(sentence):
    words = break_words(sentence)
    return sort_words(words)

def print_first-and_last(sentence):
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

people = 20
cats = 30
dogs = 15

if people < cats:
    print("Too many cats! The world is doomed!")
if people > cats:
    print("Not many cats!")
if people < dogs:
    print('The world is drooled on!')
if dogs < people:
    print("the world is dry")

dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs")
if people <= dogs:
    print("People are less than or equal to dogs")
if people == dogs:
    print("people are dogs.")

people = 30
cars = 40
trucks = 15

if cars > people:
    print("We should take the cars!")
elif cars < people:
    print("We should not take the cars!")
else: 
    print("We can't decide!")
if trucks > cars:
    print("That's too many trucks!")
elif trucks < cars:
    print("Maybe we could take the trucks")
else:
    print("We still can't decide")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")


print("""You enter a dark room with two doors. 
Do you go through door #1 or door #2?""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheesecake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")
    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better")
        print("Bear runs away.")

elif door == "2":
    print("TYou stare into the endless abyss at Cthulhi's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck!")
        print("Good job!")

else:
    print("You stumble around and fall on a knife and die. Good job!")
'''
def a(n, a0 = 0, a1 = 1):
    if n == 0:
        return a0
    elif n == 1:
        return a1
    else:
        a2 = 3*a0 + 2*a1
        return a(n-1, a1, a2)

print(a(4))

def m_a(n, D = {}):
    if n in D:
        return D[n]
    else:
        if n == 0:
            result = 0
        elif n == 1:
            result = 1
        else:
            result = 2*m_a(n-1) + 3*m_a(n-2)
    D[n] = result
    return result

print(m_a(4))