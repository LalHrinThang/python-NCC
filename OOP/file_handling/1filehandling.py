file = open("contents.txt","r")
file2 = open("create.txt","w")

if file:
    print("Success of Opening file")

else:
    print("There is no file")


file.close()