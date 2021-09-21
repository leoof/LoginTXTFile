username = "username"
password = "password"

print("===================")
print("Welcome to the Grade Calculator.")
print("===================")
usernameAttempt = input("Please enter your username: ")
passwordAttempt = input("Please enter your password: ")
classCode = input("Enter the class code: ")
f = open(classCode, "w+")


def step1():
    while "no" or " " == end:

        print('Please enter your grades in the following format - FirstName-LastName-Grade,')
        x: str = input('Please enter your grades using the above format. ')
        f.write(x)
        f.write("\n")
        done = input("Are you finished? (Y/N) ")
        if done == "n" or done == "N":
            end = 'no'
        if done == "Y" or done == "y":
            end = 'yes'
        else:
            end = 'no'

        if end == 'yes':
            print("Thank you! Your grades have been recorded!")
            exit()
        if end == 'no':
            step1()


if usernameAttempt != username and passwordAttempt != username:
    print("You have entered an incorrect username or password. Please try again.")
    exit()
else:
    print("Welcome!")
    step1()