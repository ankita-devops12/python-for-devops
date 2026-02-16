
choice = input("enter the choice q for quit:")
while choice != "q":
    num = int(input("enter number:"))
    for i in range (1, 11):
        print(f" {num} X {i} = {num*i}")
    choice = input("enter the choice q for quit:")