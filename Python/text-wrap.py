import textwrap

def wrap(string, max_width):
    n = len(string)//max_width
    for i in range(n+1):
        print(string[max_width*i:max_width*(i+1)])
    return('')

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)