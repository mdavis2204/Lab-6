
def encode():
    encoded = ""
    password = (input("Please enter your password to encode: "))
    for i in range(len(password)):
        if int(password[i]) <= 6:
            encoded += str(int(password[i]) + 3)
        elif int(password[i]) >= 7:
            encoded += str(int(password[i]) - 7)
    return encoded




