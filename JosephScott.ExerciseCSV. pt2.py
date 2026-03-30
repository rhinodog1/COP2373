import csv


def read_grades():
    filename = "grades.csv"

    with open(filename, mode="r", newline="") as file:
        reader = csv.reader(file)

        # Read header
        header = next(reader)
        print(f"{header[0]:<12} {header[1]:<12} {header[2]:<7} {header[3]:<7} {header[4]:<7}")
        print("-" * 50)

        # Read each student record
        for row in reader:
            first_name, last_name, exam1, exam2, exam3 = row
            print(f"{first_name:<12} {last_name:<12} {exam1:<7} {exam2:<7} {exam3:<7}")


# Call the function to run
if __name__ == "__main__":
    read_grades()