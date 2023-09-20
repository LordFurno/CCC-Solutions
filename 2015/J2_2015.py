string=str(input(""))
if string.count(":-)")==0 and string.count(":-(")==0:
    print("none")
elif string.count(":-)")>string.count(":-("):
    print("happy")
elif string.count(":-(")>string.count(":-)"):
    print("sad")
elif string.count(":-(")==string.count(":-)"):
    print("unsure")