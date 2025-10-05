employees=[]
#ADDING EMPLOYEE
def add_employee(employees):
    if len(employees)>=8:
        print("cannot add more than 8 employee")
        return
    emp_id=int(input("enter the employee id:"))
    for i in employees:
        if i["id"]==emp_id:
            print("employee already exist")
            return
    name=input("enter the name of employee:")
    department=input("enter the department:")
    role=input("enter the role:")
    try:
        salary=float(input("enter the salary:"))
    except ValueError:
        print("invalid salary")
        return
    
    employees.append({"id":emp_id,"name":name,"department":department,"role":role,"salary":salary})
    print("Employee added!!")

#VIEW EMPLOYEE
def view_employee(employees):
    if not employees:
        print("no employee")
        return
    
    #table format
    print("\n============EMPLOYEE DETAILS================")
    print(f"{'ID':<5}{'Name':<12}{'Department':<12}{'Role':<12}{'Salary':<10}")
    print("-"*45)
    for i in employees:
        print(f"{i['id']:<5}{i['name']:<12}{i['department']:<12}{i['role']:<12}{i['salary']:<10}")
    print()

#SEARCH EMPLOYEE
def search_employee(employees):
    x=input("search by ID or name:")  #x is str
    for i in employees:
        if str(i["id"])==x or i["name"].lower()==x.lower():  #emp_id stored as int but x is str, not matches
            print("\n Employee found")
            print(f"ID: {i['id']},Name:{i['name']},Department:{i['department']},Role:{i['role']},Salary:{i['salary']}\n")
            return
    print("employee not found")

#UPDATE EMPLOYEE
def update_employee(employees):
    emp_id=input("enter the ID to update:")
    for i in employees:
        if str(i["id"])==emp_id:
            print("what do you want to update:")
            print("1. Department")
            print("2. Role")
            print("3. Salary")
            choice=input("enter your choice:")
            if choice=="1":
                i["department"]=input("enter new Department:")
            elif choice=="2":
                i["role"]=input("enter the new Role:")
            elif choice=="3":
                try:
                    i["salary"]=float(input("enter new Salary:"))
                except ValueError:
                    print("Error!\n")
                    return
            else:
                print("Invalid choice!!\n")
                return
            
            print("Employees detailes updates Successfully!")
            return
    print("Employee not found\n")

#DELETE EMPLOYEE
def delete_employee(employees):
    emp_id=input("enter the ID:")
    for i in employees:
        if str(i["id"])==emp_id:
            employees.remove(i)
            print("Employee Deleted successfully\n")
            return
    print("Employee not found\n")


