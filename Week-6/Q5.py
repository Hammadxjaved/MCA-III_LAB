def store_student_details(filename):
    with open(filename, 'w') as file:
        while True:
            roll_number = input("Enter roll number: ")
            name = input("Enter name: ")
            marks = input("Enter marks: ")
            file.write(f"{roll_number},{name},{marks}\n")
            cont = input("Do you want to add another student? (yes/no): ")
            if cont.lower() != 'yes':
                break

store_student_details("Marks.data")
