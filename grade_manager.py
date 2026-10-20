
def calculate_grade(mark):
    if 90 <= mark <= 100:
        return "A"
    elif 80 <= mark < 90:
        return "B"
    elif 70 <= mark < 80:
        return "C"
    elif 60 <= mark < 70:
        return "D"
    elif 0 <= mark < 60:
        return "E"
    else:
        return None


def get_student_details():
    students = []

    for i in range(10):
        print(f"\nEnter details for Student {i + 1}")

        name = input("Enter student name: ")

        while True:
            try:
                mark = float(input("Enter student mark (0-100): "))

                if 0 <= mark <= 100:
                    break
                else:
                    print("Mark must be between 0 and 100.")

            except ValueError:
                print("Please enter a valid number.")

        grade = calculate_grade(mark)

        student = {
            "name": name,
            "mark": mark,
            "grade": grade
        }

        students.append(student)

    return students


def display_results(students):
    print("\n========== STUDENT RESULTS ==========")
    print(f"{'Name':<20}{'Mark':<10}{'Grade':<10}")
    print("-" * 40)

    for student in students:
        print(
            f"{student['name']:<20}"
            f"{student['mark']:<10.1f}"
            f"{student['grade']:<10}"
        )


def main():
    students = get_student_details()
    display_results(students)


if __name__ == "__main__":
    main()
