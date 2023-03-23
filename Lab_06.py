password = ""

def decode(password_in):
    password_out = ""
    for i in range(len(password_in)):
        if int(password_in[i]) >= 3 and int(password_in[i]) <= 9:
            password_out += str(int(password_in[i]) - 3)
        elif int(password_in[i]) >= 0 and int(password_in[i]) <= 2:
            password_out += str(int(password_in[i]) + 7)

    return password_out # Test

def encode():
    encoded = ""
    password = (input("Please enter your password to encode: "))
    for i in range(len(password)):
        if int(password[i]) <= 6:
            encoded += str(int(password[i]) + 3)
        elif int(password[i]) >= 7:
            encoded += str(int(password[i]) - 7)
    return encoded

def main():
    password = ""

    while True:
        print("\nMenu \n"
              "------------- \n"
              "1. Encode \n"
              "2. Decode \n"
              "3. Quit ")

        user_in = input("\nPlease enter an option: ")

        if user_in[0] == "1":
            password = encode()
            print("Your password has been encoded and stored! ")
        elif user_in[0] == "2":
            print(f"The encoded password is {password}, and the original password is {decode(password)}.")
        elif user_in[0] == "3":
            break

main()
