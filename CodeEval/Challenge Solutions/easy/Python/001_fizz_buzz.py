import sys


def fizzbuzz(x, y, n):
    for i in range(1, n + 1):
        if i % x == 0:
            print("F", end="")
        if i % y == 0:
            print("B", end=" ")
            continue
        if not i % x == 0:
            print(i, end=" ")
        else:
            print(" ", end="")
    print()


def main():
    # opens a file as first argument
    file = open(sys.argv[1], "r")
    
    # print fizzbuzz x y 
    for line in file:
        args = line.split(" ")
        if len(args) == 0:
            continue
        fizzbuzz(int(args[0]), int(args[1]), int(args[2]))
    
    file.close()

    
    
main()        