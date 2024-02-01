from pathlib import Path

names = ""

user_input = input("Enter your name (end of \"q\"): ")
while user_input != "q":
    names += user_input + "\n"
    user_input = input("Enter your name (end of \"q\"): ")

path = Path("./file_write_operation.txt")
path.write_text(names)