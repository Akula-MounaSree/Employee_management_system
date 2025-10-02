from sam import add_employee, view_employee, search_employee, update_employee,delete_employee
def dashboard():
    employees=[]
    while True:
        print("----------EMPLOYEE MANAGEMENT SYSTEM----------")
        print("1. Add Employee")
        print("2. View Employee")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit")
        choice=input("Enter your choice:")

        if choice=="1":
            add_employee(employees)
        elif choice=="2":
            view_employee(employees)
        elif choice=="3":
            search_employee(employees)
        elif choice=="4":
            update_employee(employees)
        elif choice=="5":
            delete_employee(employees)
        elif choice=="6":
            print("Exit the program, Bye!!")
            return
        else:
            print("Invalid choice, Try again.\n")

#direct calling
dashboard()
