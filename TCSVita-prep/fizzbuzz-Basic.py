# Writing a program to output the first 100 FizzBuzz
def fizzbuzz(num):
    output = ''
    if(num % 3 == 0):
        output += 'Fizz'
    if(num % 5 == 0):
        output += 'Buzz'
    if(not output):
        output = num
    return output


cycle = 100

for i in range(1, cycle+1):
    print(fizzbuzz(i))
