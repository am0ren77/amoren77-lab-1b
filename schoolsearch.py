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
                    sys.exit(1)
	
		classroom = int(data[2])
                teacher_info = data[0] + " " + data[1]  #TLast #TFirst
		teachers_dict[classroom] = teacher_info

		if classroom in teachers_dict:
		   if isinstance(teachers_dict[classroom], list):
                      teachers_dict[classroom].append(teacher_info)
		   else:
		      teachers_dict[classroom] = [teachers_dict[classroom], teacher_info]
		else: 
		   teachers_dict[classroom] = [teacher_info]
    except IOError:
        sys.exit(1)
    return teachers_dict

#--------------------------------------------------------------------------------------------------

# NR1 - NR4

# NR1. C[lassroom]: <number>
# Given a classroom number, list all students assigned to it.
def find_by_classroom(classroom):
    results = [student for student in students if student[3] == classroom]
    for student in results:
        teacher_name = teachers.get(student[3], "Unknown")
	print(student[0] + " " + student [1])
           

# NR2. TC: <classnumber>
# Given a classroom number, find the teacher (or teachers) teaching in it
def find_teachers_by_classroom(classroom):
    teacher_name = teachers.get(classroom, ["Unknown"])
    unique_teacher_names = list(set(teacher_name))
    teacher_names_str = ", ".join(unique_teacher_names)
    print(teacher_names_str)    
   

# NR3. GT: <Number>
# Given a grade, find all teachers who teach it.
def find_teachers_by_grade(grade):
    classrooms_with_grade = set()
    for student in students:
        if student[2] == grade:
           classrooms_with_grade.add(student[3])
    if classrooms_with_grade:
        teachers_set = set()
        for classroom in classrooms_with_grade:
            if classroom in teachers:
                for teacher in teachers[classroom]:
 		    teachers_set.add(teacher) 

        if teachers_set:
            print("\n".join(teachers_set))
        

# NR4. E[nrollment]
# Report the enrollments broken down by classroom (i.e., output a
# list of classrooms ordered by classroom number, with a total number of students in each
# of the classrooms).
def report_enrollment_by_classroom():
    classroom_enrollments = {}
    for student in students:
        classroom = student[3]
        if classroom in classroom_enrollments:
            classroom_enrollments[classroom] += 1
        else:
            classroom_enrollments[classroom] = 1
    
    sorted_classrooms = sorted(classroom_enrollments.items())
    for classroom, count in sorted_classrooms:
        print("{}: {} students".format(classroom, count))



#--------------------------------------------------------------------------------------------------

# NR5. Analytics

# GGPA: <grade_number>
# Info by grade
def gpa_by_grade(grade):
    gpas = []
    for student in students:
        if student[2] == grade:
            gpas.append(student[5])
    
    if gpas:
        total_students = len(gpas)
        total_gpa = sum(gpas)
        avg_gpa = total_gpa / total_students if total_students > 0 else 0
        print("Grade {}\nTotal GPA: {:.2f}\nAverage GPA: {:.2f}\nNumber of Students: {}".format(grade, total_gpa, avg_gpa, total_students))
        print("GPAs: {}".format(", ".join("{:.2f}".format(gpa) for gpa in gpas)))  


# TGPA: <teacher>
# Info by teacher
def gpa_by_teacher(teacher):
    matching_classrooms = set()
    for classroom, teachers_list in teachers.items():
        for t in teachers_list:
            if t.split()[0] == teacher:
                matching_classrooms.add(classroom)
    
    gpas = [student[5] for student in students if student[3] in matching_classrooms]
    
    if gpas:
        total_students = len(gpas)
        total_gpa = sum(gpas)
        avg_gpa = total_gpa / total_students if total_students > 0 else 0
        print("Teacher {}\nTotal GPA: {:.2f}\nAverage GPA: {:.2f}\nNumber of Students: {}".format(teacher, total_gpa, avg_gpa, total_students))
        print("GPAs: {}".format(", ".join("{:.2f}".format(gpa) for gpa in gpas)))


# BGPA: <bus_route>
# Info by bus
def gpa_by_bus_route(bus):
    gpas = [student[5] for student in students if student[4] == bus]
    
    if gpas:
        total_students = len(gpas)
        total_gpa = sum(gpas)
        avg_gpa = total_gpa / total_students if total_students > 0 else 0
        print("Bus Route {}\nTotal GPA: {:.2f}\nAverage GPA: {:.2f}\nNumber of Students: {}".format(bus, total_gpa, avg_gpa, total_students))
        print("GPAs: {}".format(", ".join("{:.2f}".format(gpa) for gpa in gpas)))
    
#--------------------------------------------------------------------------------------------------

# R4 - R11

# R4. S[tudent]: <lastname> 
def find_by_last_name(last_name):
    results = [student for student in students if student[0] == last_name]
    if results:
        for student in results:
            teacher_name = teachers.get(student[3], ["Unknown"])
            unique_teacher_names = list(set(teacher_name))
            teacher_names_str = ", ".join(unique_teacher_names)
            print(student[0] + " " + student[1] + " " + str(student[2]) + 
                  " " + str(student[3]) + " " + teacher_names_str)

# R5. S[tudent]: <lastname> B[us]
def find_by_last_name_bus(last_name):
    results = [student for student in students if student[0] == last_name]
    for student in results:
            print(student[0] + " " + student[1] + " " + str(student[4]))

# R6. T[eacher]: <lastname>
def find_by_tlast_name(tlast_name):
    matching_classrooms = []
    for classroom, teachers_list in teachers.items():
        for teacher in teachers_list:
            if teacher.split()[0] == tlast_name: 
		matching_classrooms.append(classroom)
    if matching_classrooms:
        found_students = False
        for student in students:
            if student[3] in matching_classrooms:
		found_students = True
		print(str(student[0]) + " " + str(student[1]))

# R7. G[rade]: <Number>
def find_by_grade(grade):
    results = [student for student in students if student[2] == grade]
    for student in results:
            print(student[0] + " " + student[1])

# R8. B[us]: <Number>
def find_by_bus(bus):
    results = [student for student in students if student[4] == bus]
    for student in results:
            print(student[0] + " " + student[1] + " " + str(student[2]) + 
                  " " + str(student[3]))

# R9a. G[rade]: <Number> H[igh]
def find_highest_gpa_in_grade(grade):
    results = [student for student in students if student[2] == grade]
    if results:
        highest_gpa_student = max(results, key=lambda student: student[5])
        teacher_name = teachers.get(highest_gpa_student[3], "Unknown")
        teacher_names_str = ", ".join(teacher_name)
        print(str(highest_gpa_student[0]) + " " +
 	      str(highest_gpa_student[1]) + " " +
	      str(highest_gpa_student[5]) + " " +
	      teacher_names_str 	  + " " +
	      str(highest_gpa_student[4]))

# R9b. G[rade]: <Number> L[ow]
def find_lowest_gpa_in_grade(grade):
    results = [student for student in students if student[2] == grade]
    if results:
        lowest_gpa_student = min(results, key=lambda student: student[5])
        teacher_name = teachers.get(lowest_gpa_student[3], "Unknown")
        teacher_names_str = ", ".join(teacher_name)
        print(str(lowest_gpa_student[0]) + " " +
              str(lowest_gpa_student[1]) + " " +
              str(lowest_gpa_student[5]) + " " +
              teacher_names_str          + " " +
              str(lowest_gpa_student[4]))

# R10. A[verage]: <Number>
def avg_gpa_score(grade):
    results = [student for student in students if student[2] == grade]
    if results:
        total_gpa = sum(student[5] for student in results)
        average_gpa = total_gpa / len(results)
        print(str(grade) + " " + str(round(average_gpa, 2)))

# R11. I[nfo]
def student_info():
    grade_counts = {grade: 0 for grade in range(7)}
    for student in students:
        grade = student[2] 
        if grade in grade_counts:
            grade_counts[grade] += 1
    for grade in sorted(grade_counts):
        print(str(grade) + ": " + str(grade_counts[grade]) + " students")


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
            if len(parts) > 2 and parts[2].startswith('B'):
                find_by_last_name_bus(last_name)
            else:
                find_by_last_name(last_name)

	#NR2 command
        elif main_command.startswith('TC') and len(parts) > 1:
            classroom = int(parts[1])
            find_teachers_by_classroom(classroom)

	elif main_command.startswith('TGPA') and len(parts) > 1:
            teacher_lastname = parts[1]
            gpa_by_teacher(teacher_lastname)

	elif main_command.startswith('T') and len(parts) > 1:
            tlast_name = parts[1]
            find_by_tlast_name(tlast_name)
	
	#NR5 commands
        elif main_command.startswith('GGPA') and len(parts) > 1:
            grade = int(parts[1])
            gpa_by_grade(grade)

	#NR3 command
        elif main_command.startswith('GT') and len(parts) > 1:
            grade = int(parts[1])
            find_teachers_by_grade(grade)

	elif main_command.startswith('G') and len(parts) > 1:
            grade = int(parts[1])
            if len(parts) == 2:
                find_by_grade(grade)
            elif len(parts) > 2:
                option = parts[2]
                if option.startswith('H'):
                    find_highest_gpa_in_grade(grade)
                elif option.startswith('L'):
                    find_lowest_gpa_in_grade(grade)
	
	elif main_command.startswith('BGPA') and len(parts) > 1:
            bus_route = int(parts[1])
            gpa_by_bus_route(bus_route)

        elif main_command.startswith('B'):
	  if len(parts) > 1:
		bus_route = int(parts[1])
		find_by_bus(bus_route)
	
	elif main_command.startswith('A') and len(parts) > 1:
            grade = int(parts[1])
            avg_gpa_score(grade)

	elif main_command.startswith('I'):
            student_info()

	#NR1 command
	elif main_command.startswith('C') and len(parts) > 1:
	    classroom = int(parts[1])
            find_by_classroom(classroom)

        #NR4 command
	elif main_command.startswith('E'):
            report_enrollment_by_classroom()

        

if __name__ == "__main__":
    main()  
