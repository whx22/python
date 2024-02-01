"""
Exception Type
IndexError
ZeroDivisionError
FileNotFoundError
TypeError

Exception Catching
try:
    statement(may cause an exception)
except ExceptionType1:
    statement1(Executed when there is ExceptionType1)
except ExceptionType2:
    statement2(Executed when there is ExceptionType2)
except:
    statement3(Executed when there is an exception other than ExceptionType1 and ExceptionType2)
else:
    statement4(Executed when there is no exception)
finally:
    statement5(Always executed)
"""

user_input_1 = input("Please input the first number: ")
user_input_2 = input("Please input the second number: ")
try:
    result = int(user_input_1) + int(user_input_2)
except ValueError:
    print("Please input a valid value")
else:
    print(str(result))
