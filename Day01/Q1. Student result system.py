# Input: students = {"Amit": {"maths": 80, "science": 70},
#                    "Riya": {"maths": 95, "science": 90},
#                    "Karan": {"maths": 35, "science": 50}}

# 1. Write calculate_average(marks) where marks is {subject: score}.
#    a. Set total = 0.
#    b. Repeat for each score in marks.values(): add it to total.
#    c. Return total / number of subjects.
# 2. Write get_grade(avg):
#    a. avg >= 85 → "A", avg >= 70 → "B", avg >= 50 → "C", else "Fail".
#    b. Return the grade.
# 3. Write process_students(students):
#    a. Create an empty dict called report.
#    b. Repeat for each name, marks in students.items():
#       - Call calculate_average(marks), then get_grade(avg).
#       - Store report[name] = (avg, grade).
#    c. Return report.
# 4. Write find_topper(report):
#    a. Set topper = None, best = None.
#    b. Repeat for each name, (avg, grade) in report.items():
#       - If best is None or avg > best, update topper and best.
#    c. Return topper.
# 5. Write every function with a docstring.
# 6. Run everything only under if __name__ == "__main__":
#    print each student's name, average and grade, then the topper.


students = {
    "Amit": {"maths": 80, "science": 70},
    "Riya": {"maths": 95, "science": 90},
    "Karan": {"maths": 35, "science": 50}
}

def calculate_average(marks):
    """Calculate and return the average of a student's marks."""
    total = 0

    for score in marks.values():
        total += score

    return total / len(marks)


def get_grade(avg):
    """Return the grade based on the student's average marks."""
    if avg >= 85:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "Fail"


def process_students(students):
    """Create a report containing each student's average and grade."""
    report = {}

    for name, marks in students.items():
        avg = calculate_average(marks)
        grade = get_grade(avg)

        report[name] = (avg, grade)

    return report


def find_topper(report):
    """Return the name of the student with the highest average."""
    topper = None
    best = None

    for name, (avg, grade) in report.items():
        if best is None or avg > best:
            topper = name
            best = avg

    return topper


if __name__ == "__main__":
    report = process_students(students)

    for name, (avg, grade) in report.items():
        print(f"{name}: Average = {avg:.2f}, Grade = {grade}")

    topper = find_topper(report)
    print(f"\nTopper: {topper}")
