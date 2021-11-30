password="12345"
pwd=input("enter your password")
if(password== pwd):
    print("You have successfully logged in")
elif(password!=pwd):
    for x in range(1,3):
         print("enter password")
         pwd=input()
else:
        print("Access denied")
print("thankyou")
