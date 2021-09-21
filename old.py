username1 = "username"
password1 = "password"
attempts = 0
usernameAttempt = ""
passwordAttempt = ""


def startUp():
  print("________________________________")
  print("Welcome to the A.R.S.E.S (Automated Reader for Securely Encrypted Stuff)")
  print("________________________________")
  usernameAttempt = str(input("Please enter your username: "))
  passwordAttempt = str(input("Please enter your password: "))

startUp()
if usernameAttempt == "username1" and passwordAttempt == "password1":
  print("User Authenticated")
  print("________________________________")
  document = input("What is the name of the document you would like to load? ")
  documentv = document, ".txt"
else:
  print("You have entered an incorrect username or password. Please try again.")
  attempts = attempts + 1
  if attempts > 3:
    print("ATTEMPT LIMIT EXCEEDED. THERMONUCLEAR HYDROCHLORIC SULFURIC CLUBHOUSE BOMB DETONATION SEQUENCE INITIATED.")
    exit()
  else:
    startUp()
  


  if document == "private":
    t = open("private.txt", "r")
    print(t.read())