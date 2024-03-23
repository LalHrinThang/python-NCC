file = open("contents.txt","r")

if file:
    print("Success of Opening file")

else:
    print("There is no file")


file.close()