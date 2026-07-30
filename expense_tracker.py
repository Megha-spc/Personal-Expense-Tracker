import mysql.connector

# ---------------- DATABASE CONNECTION ----------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql@123",      # Apna MySQL password
    database="expensetracker1"
)

cursor = conn.cursor()

print("Connected Successfully!")

# ---------------- ADD EXPENSE ----------------
def add_expense():
    date = input("Enter Date (YYYY-MM-DD): ")
    category = input("Enter Category: ")
    amount = float(input("Enter Amount: "))

    query = "INSERT INTO expenses(date, category, amount) VALUES(%s, %s, %s)"
    values = (date, category, amount)

    cursor.execute(query, values)
    conn.commit()

    print("Expense Added Successfully!")

# ---------------- VIEW EXPENSES ----------------
def view_expenses():

    query = "SELECT * FROM expenses"
    cursor.execute(query)

    records = cursor.fetchall()

    if len(records) == 0:
        print("No Expenses Found!")

    else:
        print("\nID\tDATE\t\tCATEGORY\tAMOUNT")
        print("-" * 45)

        for row in records:
            print(f"{row[0]}\t{row[1]}\t{row[2]}\t\t{row[3]}")

# ---------------- SEARCH EXPENSE ----------------
def search_expense():

    category = input("Enter Category: ")

    query = "SELECT * FROM expenses WHERE category=%s"
    value = (category,)

    cursor.execute(query, value)

    records = cursor.fetchall()

    if len(records) == 0:
        print("No Expense Found!")

    else:
        print("\nID\tDATE\t\tCATEGORY\tAMOUNT")
        print("-" * 45)

        for row in records:
            print(f"{row[0]}\t{row[1]}\t{row[2]}\t\t{row[3]}")

# ---------------- DELETE EXPENSE ----------------
def delete_expense():

    expense_id = int(input("Enter Expense ID: "))

    query = "DELETE FROM expenses WHERE id=%s"
    value = (expense_id,)

    cursor.execute(query, value)
    conn.commit()

    if cursor.rowcount > 0:
        print("Expense Deleted Successfully!")

    else:
        print("Expense ID Not Found!")

# ---------------- MENU ----------------
while True:

    print("\n========== PERSONAL EXPENSE TRACKER ==========")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search Expense")
    print("4. Delete Expense")
    print("5. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        add_expense()

    elif choice == 2:
        view_expenses()

    elif choice == 3:
        search_expense()

    elif choice == 4:
        delete_expense()

    elif choice == 5:
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")

cursor.close()
conn.close()