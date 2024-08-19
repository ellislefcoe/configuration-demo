# a file fib.py
import sys

if __name__ == "__main__":
    number = int(sys.argv[1])
    a = 0
    b = 1
    for i in range(number):
        print(a)
        c = a
        a += b
        b = c

# when we run this file we will get the first n fibonacci numbers
# we can run it like this
# python3 fib.py <n>
