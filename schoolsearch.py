# Ashley Moreno
# Lab 1 Part b
# schoolsearch.py

import sys

students = []
teachers = {}

def read_students(filename):
    students_list = []
    with open(filename, 'r') as file:
        for line in file:
	    data = line.strip().split(',')
	    if len(data) != 6:
		sys.exit(1)

	    student_info = [
		data[0],		# StLastName
		data[1],		# StFirstName
		int(data[2]),		# Grade
		int(data[3]),		# Classroom
		int(data[4]),		# Bus
		float(data[5]),		# GPA
	    ]
	    students_list.append(student_info)
    return students_list

def read_teachers(filename):
    teachers_dict = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                if len(data) != 3:
                    sys.exit("Incorrect format in teachers file")
	
		classroom = int(data[2])
                teacher_info = data[0] + " " + data[1]  #TLastName #TFirstName
		teachers_dict[classroom] = teacher_info

    except FileNotFoundError:
        sys.exit("Teachers file not found")
    return teachers_dict

#--------------------------------------------------------------------------------------------------

# R4. S[tudent]: <lastname> 
def find_by_last_name(last_name):
    results = [student for student in students if student[0] == last_name]
    if results:
        for student in results:
            teacher_name = teachers.get(student[3], "Unknown")
            print(student[0] + " " + student[1] + " " + str(student[2]) + 
                  " " + str(student[3]) + " " + teacher_name)
    else:
        print("No student found with last name: " + last_name)





#--------------------------------------------------------------------------------------------------
def main():

    global students, teachers
    students = read_students("list.txt")
    teachers = read_teachers("teachers.txt")

    while True:
        command = input("Enter command: ")
	command = command.strip()

        if command == 'Q':
           break
  
        parts = command.split()
        if len(parts) == 0:
           continue

        main_command = parts[0]

        if main_command.startswith('S') and len(parts) > 1:
           last_name = parts[1]
           find_by_last_name(last_name)




if __name__ == "__main__":
    main()  












