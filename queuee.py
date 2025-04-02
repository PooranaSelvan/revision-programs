queue = []

def insert():
     inp = int(input("Enter The Number Of Elements You Want: "))
     for i in range(1, inp + 1):
          n = input(f"Enter The Element {i}: ")
          queue.append(n)
     print("After Inserting All Elements", queue)
     
def remove(queue):
     if queue:
          queue.pop(0)
          print("After Removing Element", queue)
     else:
          print("Queue Is Empty Cant Remove Anything!!")
          
while True:
     print("1. Insert")
     print("2. Remove")
     print("3. Exit")
     
     num = int(input("Enter The Operation You Want To Perform: "))
     
     if num == 1:
          insert()
     elif num == 2:
          remove(queue)
     elif num == 3:
          print("Exiting!!")
          break
     else:
          print("Select The Correct Option To Perform a Operation")
     