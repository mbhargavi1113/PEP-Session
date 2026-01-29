#Expense Tracker
file_name = "Expense_data.txt"
expenses = []
#load data
def load_data():
    global expenses
    try:
        file = open(file_name,"r")
        lines = file.readlines()
        file.close()
        for line in lines:
            line = line.strip()
            amount, category, note = line.split(",")
            expense = {
                "amount":int(amount),
                "category":category,
                "note":note
            }
            exp
    except:
        pass
def save_data():
    file = open(file_name,"w")
    
    