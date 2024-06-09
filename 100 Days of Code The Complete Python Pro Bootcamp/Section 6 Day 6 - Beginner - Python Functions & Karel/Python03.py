# While Loops
def check_password(s):
    if s == "mypassword":
        return True
    else:
        return False


password = str("")
while not check_password(password):
    print("Enter Password : ", end="")
    password = input()
    if check_password(password):
        print("Access Allowed")
    elif not check_password(password):
        print("Access Denied")


