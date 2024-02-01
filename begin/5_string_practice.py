# title() ： 将字符串中的每个单词首字母大写
book_name = "python crash course"
new_book_name = book_name.title()
print(new_book_name)
print(book_name)

# upper() ： 将字符串中的每个字母大写
print(book_name.upper())
# lower() ： 将字符串中的每个字母小写
print(book_name.lower())

# lstrip() ： 删除字符串开头的空白
# rstrip() ： 删除字符串末尾的空白
# strip() ： 删除字符串两端的空白

# removeprefix() ： 删除字符串开头的指定字符
print(book_name.removeprefix("python"))
# removesuffix() ： 删除字符串末尾的指定字符
print(book_name.removesuffix("course"))

# f ： 格式化字符串
name = "Eric zhang".title()
print(f"Hello {name}, would you like to learn some python today?")

