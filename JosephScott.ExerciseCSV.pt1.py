import csv


def write_grades():
    filename = "grades.csv"

    # Ask how many students to enter
    num_students = int(input("Enter the number of students: "))

    # Open CSV file for writing
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)

        # Write header
        writer.writerow(["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"])

        # Enter student data
        for _ in range(num_students):
            first_name = input("Enter student's first name: ")
            last_name = input("Enter student's last name: ")
            exam1 = int(input("Enter Exam 1 grade: "))
            exam2 = int(input("Enter Exam 2 grade: "))
            exam3 = int(input("Enter Exam 3 grade: "))

            writer.writerow([first_name, last_name, exam1, exam2, exam3])

    print(f"{filename} has been created successfully!")


# Call the function to run
if __name__ == "__main__":
    write_grades()