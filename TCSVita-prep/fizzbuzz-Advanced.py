# It’s the same as the basic problem but the conditions are taken as an input.
# For example, the  game can have 3 conditions
# if divisible by 4-Fizz, 5-Buzz, and 11-Plop
def fizzbuzz(num, keymap):
    output = ''
    for factor in keymap.keys():
        if(num % factor == 0):
            output += keymap[factor]
    if(not output):
        output = num
    return output


cycles = 100
argnum = int(input("Enter the number of conditions:\n"))

values = [int(x) for x in input().split()]
words = input().split()

conditions = dict(zip(values, words))

print("---Output---\n")
for num in range(1, cycles+1):
    print(fizzbuzz(num, conditions))
