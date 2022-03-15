x = input("Enter username:")
print("Username is: " + x)

def my_function(x):
  return list(dict.fromkeys(x))

mylist = my_function(x)

print(mylist)