stack = []

def insert():
    inp = int(input("Enter the number of elements to insert: "))
    for i in range(inp):
        n = input(f"Enter Element {i + 1}: ")
        stack.append(n)
    print("Stack after insertion:", stack)

def remove():
    if stack:
        stack.pop(-1)
        print("Stack after removing:", stack)
    else:
        print("Stack is empty, cannot remove.")

while True:
    print("\n1. Insert")
    print("2. Remove")
    print("3. Exit")

    ope = int(input("Enter the operation you want to perform: "))

    if ope == 1:
        insert()
    elif ope == 2:
        remove()
    elif ope == 3:
        print("Exiting.")
        break
    else:
        print("Enter a valid option!")
