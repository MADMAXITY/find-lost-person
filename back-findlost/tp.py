file = open("auth.txt")
print(file.readline() == "False")
file.close()

file = open("auth.txt", "w")
file.write("True")
file.close()


file = open("auth.txt")
print(file.readline() == "True")
file.close()