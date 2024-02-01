list_1 = ["Are ", "you ", "OK ", "What ", "is ", "up "]

for char in list_1:
    print(char)

for i in range(len(list_1)):
    print(list_1[i])

i = 0
while i < len(list_1):
    print(list_1[i])
    i = i + 1

user_input = input("please input string: ")
while user_input != "quit":
    print("you input " + user_input)
    user_input = input("please input string: ")

