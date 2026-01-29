#ATM Stimulator
file_name = "atm_data.txt"
#Balance is a global variable that stores money
balance = 1000
#pin is a global varibale that stores ATM pin
pin = "1234"
#Load Data
def load_data():
    #global variable allow us to modify outside variable
    global balance,pin
    try:
        #open files in read mode
        file = open(file_name, "r")
        #read all lines from the file into a list
        lines = file.readlines()
        #close the file after reading
        file.close()
        #first line contains pin, strip removes \n
        pin = lines[0].strip()
        #Second line contains balance
        balance = int(lines[1].strip())
    except:
        #if file does not exist or error occurs
        #pass means 'Do nothing'
        #program will use default balance and pin
        pass
#Check Balance
def check_balance():
    global balance
    print("Your balance is: ",balance)
#Save Data
def save_data():
    #opening a file in write mode
    file = open(file_name,"w")
    #write a pin into the file and go to next line
    file.write(pin+"\n")
    #write balance as string
    file.write(str(balance))
    #close the file
    file.close()
#Deposite Money
def deposit_money():
    global balance
    try:
        amount = int(input("Enter amount to deposit:"))
        balance = balance+amount
        #save updated balance to the file
        save_data()
        print("Money deposited successfully!")
    except:
        print("Please enter numbers only")
#Withdraw Money
def withdraw_money():
    global balance
    try:
        amount = int(input("enter the amount you want to withdraw:"))
        if amount>balance:
            print("Insufficient balance!")
        else:
            balance = balance-amount
            save_data()
            print("Please collect your cash!")
    except:
        print("Please enter number only")
#Change Pin
def change_pin():
    global pin
    #ask user for old pin
    old_pin = input("enter the old pin:")
    #check if old pin matches
    if old_pin==pin:
        #then ask for new pin
        new_pin = input("enter your new pin:")
        pin = new_pin
        save_data()
        print("Pin changed successfully!")
    else:
        print("Incorrect pin")
#Main Program
def main():
    #load data when progress starts
    load_data()
    #ask user to enter a pin
    user_pin = input("enter the pin:")
    #if pin is wrong stop the program
    if user_pin != pin:
        print("Incorrect pin")
        return
    while True:
        print("\n----ATM Menu----")
        print("1. Check Balance")
        print("2. Deposite Money")
        print("3. Withdraw Money")
        print("4. Change Pin")
        print("5. Exit")

        choice = input("Enter your choice:")
        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit_money()
        elif choice == "3":
            withdraw_money()
        elif choice == "4":
            change_pin()
        elif choice == "5":
            print("Thank you for using ATM")
            break
        else:
            print("Invalid Choice")
main()
