import csv


FILE_NAME = "students.csv"
 

# -------------------------------
# Add Student
# -------------------------------
def add_student():
    student_id = input("Enter Student ID: ")

    # Check duplicate ID
    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["StudentID"] == student_id:
                print("\nStudent ID already exists!\n")
                return

    name = input("Enter Name: ")
    age = input("Enter Age: ")
    gender = input("Enter Gender: ")
    department = input("Enter Department: ")
    year = input("Enter Year: ")
    email = input("Enter Email: ")
    phone = input("Enter Phone Number: ")
    cgpa = input("Enter CGPA: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            student_id,
            name,
            age,
            gender,
            department,
            year,
            email,
            phone,
            cgpa
        ])

    print("\nStudent Added Successfully!\n")


# -------------------------------
# View Students
# -------------------------------
def view_students():
    print("\n---------------- STUDENT RECORDS ----------------")

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        found = False

        for row in reader:
            found = True
            print(
                f"{row['StudentID']:5} | "
                f"{row['Name']:15} | "
                f"{row['Department']:8} | "
                f"{row['Year']:4} | "
                f"{row['CGPA']}"
            )

        if not found:
            print("No student records found.")


# -------------------------------
# Search Student
# -------------------------------
def search_student():
    sid = input("Enter Student ID: ")

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["StudentID"] == sid:
                print("\nStudent Found\n")
                for key, value in row.items():
                    print(f"{key}: {value}")
                return

    print("\nStudent Not Found.\n")


# -------------------------------
# Update Student
# -------------------------------
def update_student():
    sid = input("Enter Student ID to Update: ")

    rows = []

    updated = False

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:

            if row["StudentID"] == sid:

                print("\nLeave blank to keep old value.\n")

                row["Name"] = input(f"Name ({row['Name']}): ") or row["Name"]
                row["Age"] = input(f"Age ({row['Age']}): ") or row["Age"]
                row["Gender"] = input(f"Gender ({row['Gender']}): ") or row["Gender"]
                row["Department"] = input(f"Department ({row['Department']}): ") or row["Department"]
                row["Year"] = input(f"Year ({row['Year']}): ") or row["Year"]
                row["Email"] = input(f"Email ({row['Email']}): ") or row["Email"]
                row["Phone"] = input(f"Phone ({row['Phone']}): ") or row["Phone"]
                row["CGPA"] = input(f"CGPA ({row['CGPA']}): ") or row["CGPA"]

                updated = True

            rows.append(row)

    if updated:

        with open(FILE_NAME, "w", newline="") as file:

            fieldnames = [
                "StudentID",
                "Name",
                "Age",
                "Gender",
                "Department",
                "Year",
                "Email",
                "Phone",
                "CGPA"
            ]

            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()

            writer.writerows(rows)

        print("\nStudent Updated Successfully!\n")

    else:
        print("\nStudent Not Found.\n")


# -------------------------------
# Delete Student
# -------------------------------
def delete_student():
    sid = input("Enter Student ID to Delete: ")

    rows = []

    deleted = False

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:

            if row["StudentID"] == sid:
                deleted = True
                continue

            rows.append(row)

    if deleted:

        with open(FILE_NAME, "w", newline="") as file:

            fieldnames = [
                "StudentID",
                "Name",
                "Age",
                "Gender",
                "Department",
                "Year",
                "Email",
                "Phone",
                "CGPA"
            ]

            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()

            writer.writerows(rows)

        print("\nStudent Deleted Successfully!\n")

    else:
        print("\nStudent Not Found.\n")


# -------------------------------
# Count Students
# -------------------------------
def count_students():

    count = 0

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for _ in reader:
            count += 1

    print(f"\nTotal Students: {count}\n")


# -------------------------------
# Main Menu
# -------------------------------
while True:

    print("\n========== STUDENT MANAGEMENT SYSTEM ==========")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Count Students")
    print("7. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        count_students()

    elif choice == "7":
        print("\nThank You!")
        break

    else:
        print("\nInvalid Choice!\n")