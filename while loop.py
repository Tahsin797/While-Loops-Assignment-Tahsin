# Create employee list

employee_list = []

# Enter information for up to 5 employees

for employee in range(5):
    print("\nEnter Employee Information")

    # Employee ID
    employee_id = input("Enter Employee ID: ")
    while not employee_id.isdigit() or len(employee_id) > 7:
        print("Invalid ID. Please try again.")
        employee_id = input("Enter Employee ID: ")

    # Employee Name
    employee_name = input("Enter Employee Name: ")
    bad_name = ['!', '"', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '=', '+', ',', '<', '>', '/', '?', ';', ':', '[', ']', '{', '}', '\\']
    name_ok = False

    while name_ok == False:
        name_ok = True
        name_letters = 0
        for character in employee_name:
            if character.isalpha():
                name_letters += 1
            if character in bad_name:
                name_ok = False
        if employee_name == "" or name_letters <= len(employee_name) / 2:
            name_ok = False
        if name_ok == False:
            print("Invalid Name. Please try again.")
            employee_name = input("Enter Employee Name: ")

    # Employee Email
    employee_email = input("Enter Employee Email Address: ")
    bad_email = ['!', '"', "'", '#', '$', '%', '^', '&', '*', '(', ')', '=', '+', ',', '<', '>', '/', '?', ';', ':', '[', ']', '{', '}', '\\']
    email_ok = False

    while email_ok == False:
        email_ok = True
        email_letters = 0
        for character in employee_email:
            if character.isalnum():
                email_letters += 1
            if character in bad_email:
                email_ok = False
        if employee_email == "" or email_letters <= len(employee_email) / 2:
            email_ok = False
        if email_ok == False:
            print("Invalid Email. Please try again.")
            employee_email = input("Enter Employee Email Address: ")

    # Employee Address
    employee_address = input("Enter Employee Address (optional): ")
    bad_address = ['!', '"', "'", '@', '$', '%', '^', '&', '*', '_', '=', '+', '<', '>', '?', ';', ':', '[', ']', '{', '}']
    address_ok = False

    while address_ok == False:
        address_ok = True
        address_letters = 0
        for character in employee_address:
            if character.isalnum():
                address_letters += 1
            if character in bad_address:
                address_ok = False
        if employee_address != "" and address_letters <= len(employee_address) / 2:
            address_ok = False
        if address_ok == False:
            print("Invalid Address. Please try again.")
            employee_address = input("Enter Employee Address (optional): ")

    # Create employee dictionary
    employee_info = {
        "Employee ID": employee_id,
        "Employee Name": employee_name,
        "Employee Email": employee_email,
        "Employee Address": employee_address
    }

    # Add dictionary to employee list
    employee_list.append(employee_info)

    # Ask if user wants to enter another employee
    if employee < 4:
        answer = input("Would you like to enter another employee? (yes/no): ")
        if answer.lower() != "yes":
            break

# Display employee list
print("\nAll Employee Information:")
print(employee_list)
