# registration

# login

# bank operations

#system initialization
def init():
    print("Welcome to BankPHP")
    haveAccount = int(input("Do you have an account with us: 1 (yes) 2 (no) \n"))
    if(haveAccount == 1):
        login()
    elif(haveAccount == 2):
        register()
    else:
        print("The option you selected an invalid option")

def login():
    print("login")

def register():
    print('registered')

def bankOperation():
    print('bankoperations')

def generateAccountNumber():
    print("account number generated")


###After Initialization####
init