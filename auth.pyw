
import random
import database


database = {} #dictionary

def init():


    print("Welcome to bankPHP")
    haveAccount = int(input("Do you have account with us: 1 (yes) 2 (no) \n"))

    if(haveAccount == 1):
        have_account = int(input("Do you have account with us: 1 (yes) 2 (no) \n"))

    if have_account == 1:
        login()

    elif have_account == 2:
        register()

    else:
        print("You have selected invalid option")
        init()


def login():

    print("********* Login ***********")
    accountNumberFromUser = int(input("What is your account number? \n"))
    password = input("What is your password \n")
    account_number_from_user = input("What is your account number? \n")

    for accountNumber,userDetails in database.items():
        if(accountNumber == accountNumberFromUser):
            if(userDetails[3] == password):
                bankOperation(userDetails)


    print('Invalid account or password')
    login()

    is_valid_account_number = validation.account_number_validation(account_number_from_user)

    if is_valid_account_number:

def register():
        password = getpass("What is your password \n")

        user = database.authenticated_user(account_number_from_user, password);

        if user:
            bank_operation(user)

        print('Invalid account or password')
        login()

    else:
        print("Account Number Invalid: check that you have up to 10 digits and only integers")
        init()


def register():
    print("****** Register *******")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
     last_name = input("What is your last name? \n")
    password = input("create a password for yourself \n")
    password = getpass("Create a password for yourself \n")

    accountNumber = generationAccountNumber()
    account_number = generation_account_number()

    database[accountNumber] = [ first_name, last_name, email, password ]
    is_user_created = database.create(account_number, first_name, last_name, email, password)

    print("Your Account Has been created")
    print(" == ==== ====== ===== ===")
    print("Your account number is: %d" % accountNumber)
    print("Make sure you keep it safe")
    print(" == ==== ====== ===== ===")
    if is_user_created:
        
    login()
        print("Your Account Has been created")
        print(" == ==== ====== ===== ===")
        print("Your account number is: %d" % account_number)
        print("Make sure you keep it safe")
        print(" == ==== ====== ===== ===")

        login()

    else:
        print("Something went wrong, please try again")
        register()

def bankOperation(user):

    print("Welcome %s %s " % ( user[0], user[1] ) )
def bank_operation(user):
    print("Welcome %s %s " % (user[0], user[1]))
     selectedOption = int(input("What would you like to do? (1) deposit (2) withdrawal (3) Logout (4) Exit \n"))
    selected_option = int(input("What would you like to do? (1) deposit (2) withdrawal (3) Logout (4) Exit \n"))

    if selected_option == 1:

        deposit_operation()
    elif selected_option == 2:

        withdrawal_operation()
    elif selected_option == 3:

    if(selectedOption == 1):

        depositOperation()
    elif(selectedOption == 2):

        withdrawalOperation()
    elif(selectedOption == 3):

        logout()
    elif(selectedOption == 4):
        
    elif selected_option == 4:

        exit()
    else:
      

        print("Invalid option selected")
        bankOperation(user)
        bank_operation(user)


def withdrawalOperation():
def withdrawal_operation():
    print("withdrawal")
    # get current balance
    # get amount to withdraw
    # check if current balance > withdraw balance
    # deduct withdrawn amount form current balance
    # display current balance


def depositOperation():
def deposit_operation():
    print("Deposit Operations")
    # get current balance
    # get amount to deposit
    # add deposited amount to current balance
    # display current balance


def generationAccountNumber():
def generation_account_number():
    return random.randrange(1111111111, 9999999999)

    return random.randrange(1111111111,9999999999)

def logout():
    login()
def set_current_balance(user_details, balance):
    user_details[4] = balance

