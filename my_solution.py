import sys

#This function turns a string into an array of characters
def split(string):
    return [char for char in string]

#This will normalise the symbols eg if it is meant to be ['', '', '+'] my functions will output ['+'] so this reverses that behaviour
def make_array_length(arrangement, length):
    if len(arrangement) == length:
        return arrangement
    arrangement.insert(0, '')
    return make_array_length(arrangement, length)

#Every symbol arangement is mapped to a base three number this function turns a base 10 number into a symbol arrangement
def return_symbol_arrangement(number, bits):
    remainder = number % 3
    if remainder == 0:
        bits.append("")
    elif remainder == 1:
        bits.append("+")
    else:
        bits.append("-")
    integer = number // 3
    if integer == 0:
        return [bits[len(bits)-1-i] for i in range(len(bits))]
    return return_symbol_arrangement(integer, bits)

#this gives an array filled with all the different possible 1+11 and 1+1-1 stuff etc
def expression_possibilities(number):
    starting_length = len(number)
    possibilities = []
    for i in range(3**(starting_length - 1)):
        arrangement = return_symbol_arrangement(i, [])
        if len(arrangement) != starting_length - 1 and starting_length != 1:
            make_array_length(arrangement, starting_length-1)
        split_number = split(number)
        symbol_count = 0
        for j in range(starting_length):
            if ((j*2)+1 < (starting_length * 2) - 2):
                split_number.insert((j*2)+1, arrangement[symbol_count])
                symbol_count += 1
        possibilities.append(split_number)
    return possibilities

#function determine if a number is ugly:
def is_ugly(number):
    if number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or number % 7 == 0:
        return True
    return False

#this checks if a given expression possibility produces an ugly number
def is_possibility_ugly(arr):
    expression = []
    symbol_count = 0
    buffer = []
    for c in arr:
        try:
            int(c)
            buffer.append(c)
        except:
            if c != "":
                symbol_count += 1
                expression.append(int(''.join(buffer)))
                expression.append(c)
                buffer = []
    expression.append(int(''.join(buffer)))
    number = expression[0]
    for a in range(symbol_count):
        if expression[(2*a)+1] == '+':
            number += expression[(2*a)+2]
        else:
            number -= expression[(2*a)+2]
    return is_ugly(number)

for line in sys.stdin:
    #sanitise the line by removing the linebreak from the string.
    line = split(line)
    line.pop()
    line = ''.join(line)
    #work out the possibilities 
    possible_expressions = expression_possibilities(line)
    #count the ugly results 
    ugly_count = 0
    for arr in possible_expressions:
        ugly_count += is_possibility_ugly(arr)
    print(ugly_count, end="")
