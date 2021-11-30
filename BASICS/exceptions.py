#this will throw an exception!
try:
    d={}
    d["a"]
    int("a")
except ValueError:
    print("An value exception happened")
except KeyError:
    print("A key was not found")

print("End of program")