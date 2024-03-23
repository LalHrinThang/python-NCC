file = open("contents.txt","r")
file2 = open("create.txt","w")
file3 = open("append.txt","a")

if file:
    print("Success of Opening file")

else:
    print("There is no file")


file.close()