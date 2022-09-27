# Write a Python program which iterates the integers list.
# For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".

def fizz_buzz(begin, end):
    for mix in range(begin, end):
        if mix % 3 == 0 and mix % 5 == 0 and mix % 15 == 0:
            print("FizzBuzz")
        elif mix % 3 == 0:
            print("Fizz")
        elif mix % 5 == 0:
            print("Buzz")
        else:
            print(mix)




