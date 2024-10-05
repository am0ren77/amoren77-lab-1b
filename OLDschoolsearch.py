# Ashley Moreno
# Lab 1 Part a
# OLDschoolsearch.py

import sys
students = list()

# Function to read students.txt file and store student data
def read_students(filename):
    global students
    with open(filename, 'r') as file:
        for line in file:
	    data = line.strip().split(',')
	    if len(data) != 8:
		sys.exit(1)

	    student_info = [
		data[0],		# StLastName
		data[1],		# StFirstName
		int(data[2]),		# Grade
		int(data[3]),		# Classroom
		int(data[4]),		# Bus
		float(data[5]),		# GPA
		data[6],		# TLastName
		data[7]			# TFirstName
	    ]
	    students.append(student_info)

# R4. S[tudent]: <lastname>
def find_by_last_name(last_name):
    results = [student for student in students if student[0] == last_name]
    if results:
        for student in results:
	    print(str(student[0]) + " " +
                  str(student[1]) + " " +
                  str(student[2]) + " " +
                  str(student[3]) + " " +
                  str(student[6]) + " " +
		  str(student[7])
                )

# R5. S[tudent]: <lastname> B[us]
def find_by_last_name_bus(last_name):
    results = [student for student in students if student[0] == last_name]
    if results:
	for student in results:
	    print(student[0] + " " + student[1] + " " + str(student[4]))

# R6. T[eacher]: <lastname>
def find_by_tlast_name(tlast_name):
    results = [student for student in students if student[6] == tlast_name]
    if results:
	for student in results:
	    print(student[0] + " " + student[1])

# R7. G[rade]: <Number>
def find_by_grade(grade):
    results = [student for student in students if student[2] == grade]
    if results:
        for student in results:
            print(student[0] + " " + student[1])

# R8. B[us]: <Number>
def find_by_bus(bus_route):
    results = [student for student in students if student[4] == bus_route]
    if results:
        for student in results:
            print(student[0] + " " + student[1] + " " + str(student[2]) + " " + str(student[3]))

# R9a. G[rade]: <Number> H[igh]
def find_highest_gpa_in_grade(grade):
    results = [student for student in students if student[2] == grade]
    if results:
        highest_gpa_student = max(results, key=lambda student: student[5])
        print(str(highest_gpa_student[0]) + " " + 
              str(highest_gpa_student[1]) + " " +
              str(highest_gpa_student[5]) + " " +
              str(highest_gpa_student[7]) + " " +
	      str(highest_gpa_student[6]) + " " +
              str(highest_gpa_student[4]))

# R9b. G[rade]: <Number> L[ow]
def find_lowest_gpa_in_grade(grade):
    results = [student for student in students if student[2] == grade]
    if results:
	lowest_gpa_student = min(results, key=lambda student: student[5])
	print(str(lowest_gpa_student[0]) + " " +
	      str(lowest_gpa_student[1]) + " " +
              str(lowest_gpa_student[5]) + " " +
              str(lowest_gpa_student[7]) + " " +
	      str(lowest_gpa_student[6]) + " " +
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

# Main loop to handle user input
def main():
    filename = "students.txt"
    read_students(filename)

    while True:
	command = input("Enter command: ")
	command = command.strip() ## Failure unless quotations ' ' around command
	
	if command.startswith('Q'):
            break

	parts = command.split()
	main_command = parts[0]

        if command.startswith('S'):
	  if len(parts) > 1:
              last_name = parts[1]
	      if len(parts) > 2 and parts[2].startswith('B'):
                  find_by_last_name_bus(last_name) 
	      else:
		  find_by_last_name(last_name) 
        
	elif command.startswith('T'):
	  if len(parts) > 1:
                tlast_name = parts[1]
                find_by_tlast_name(tlast_name)	

	elif command.startswith('G'):
	  if len(parts) > 1:
		grade = int(parts[1])
		if len(parts) == 2:	
	       	   find_by_grade(grade)
		elif len(parts) > 2:
                   option = parts[2]
                   if option.startswith('H'):
                      find_highest_gpa_in_grade(grade)
                   elif option.startswith('L'):
                      find_lowest_gpa_in_grade(grade)

	 elif command.startswith('B'):
	  if len(parts) > 1:
		bus_route = int(parts[1])
		find_by_bus(bus_route)
	
	elif command.startswith('A'):
	  if len(parts) > 1:
		grade = int(parts[1])
		avg_gpa_score(grade)

	elif command.startswith('I'):
	  student_info()


if __name__ == "__main__":
    main()
