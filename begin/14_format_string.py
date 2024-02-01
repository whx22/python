gpa_dict = {"Huxin": 2.0, "xianqi": 3.0, "yang": 4.0, "xiangyu": 5.0}

for name, gpa in gpa_dict.items():
    print("{0}, hello, you GPA is {1:.2f}".format(name, gpa))
    print("{current_name}, hello, you GPA is {current_gpa:.2f}".format(current_name = name, current_gpa = gpa))
    print(f"{name}, hello, you GPA is {gpa:.2f}")

