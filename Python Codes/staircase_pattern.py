def staircase(n):
    spaces = n-1
    hashtags = 1
    for i in range(n):
        for j in range(spaces):
            print(end =" ")
        for k in range(hashtags):
            print("#",end="")
        print()
        hashtags += 1
        spaces -= 1


def main():
    size = int(input("Enter the size : "))
    staircase(size)

main()