import statistics

students = {}

def add_student():
    name = input("Student name: ")
    scores = input("Enter scores separated by spaces: ")
    scores = [int(s) for s in scores.split()]
    students[name] = scores
    print(f"{name} added.\n")

def calculate_average(name):
    return statistics.mean(students[name])

def show_report():
    print("\n--- Student Report ---")
    for name, scores in students.items():
        avg = calculate_average(name)
        print(f"{name}: Scores={scores}, Average={avg:.2f}")
    print()

def top_student():
    best = None
    best_avg = 0
    for name in students:
        avg = calculate_average(name)
        if avg > best_avg:
            best_avg = avg
            best = name
    print(f"Top student: {best} ({best_avg:.2f})\n")

def menu():
    while True:
        print("1. Add student")
        print("2. Show report")
        print("3. Top student")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            show_report()
        elif choice == "3":
            top_student()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.\n")

if __name__ == "__main__":
    menu()
