# Ashley Moreno
# Lab 1 Part b
# schoolsearch.py

import sys

students = []
teachers = {}

def read_students(filename):
    students = []
    try:
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
	    students.append(student_info)

    except FileNotFoundError:
	sys.exit(1)
    except ValueError
	sys.exit(1)

    return students


def read_teachers(filename):
    teachers = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                if len(data) != 3:
                    print("Invalid data format in teachers list.")
                    sys.exit(1)
	
		classroom = int(data[2])
                teacher_info = data[0] + " " + data[1]  #TLastName #
		teachers[classroom] = teacher_info

    except FileNotFoundError:
        sys.exit(1)

    return teachers


