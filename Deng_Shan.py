#import matplotlib for graphing
import matplotlib.pyplot as plt

#Create a class for students
class Student:

        #All students will have a Student ID, First Name, Last Name, and a list of Classes
	def __init__(self, sid, first, last, classes):
		self.first = first
		self.last = last
		self.sid = sid
		self.classes = classes
		
#Create a class for courses
class Course:

        #All courses will have a CourseID, Class Name, Professor, Current Enrollment, and Max Capacity
	def __init__(self, cid, name, prof, enrolled, capacity):
		self.cid = cid
		self.name = name
		self.prof = prof
		self.enrolled = enrolled
		self.capacity = capacity

#Creating a new student - Takes in Student ID, and current Students dictionary to update
def create_student(sid,students):

    while True:
        #Takes in needed student parameters (First and last name)
        print("What is your first name?")
        first = input()
        print("What is your last name?")
        last = input()
        print("Is this information correct?")
        print("First Name: " + first)
        print("Last Name: " + last)
        print()
        print('Enter "Y" to continue or any other button to try again:')
        flag = input()

        if flag == "y" or flag == "Y":
            break
            
        
    #Creates a new student in the dictionary with the given student ID and name.
    #New students will start off enrolled in 0 classes.
    students[sid] = Student(sid, first, last, [])

    #Yay the code ran
    print("You have been registered as a new student!")

    #Returns updated dictionary of students
    return students

#Creates updated text file of students - takes in dictionary of students
def write_students_back(students):

    #creating updated text file on student info 
    studentFile = open("student-updated.txt", "w")

    #For each ID in the dictionary
    for sid in students.keys():

        #Store the student info associated with that ID
        student = students[sid]
        #Break that info down into 4 categories - Student ID, First Name, Last Name, and Classes)
        items = [sid, student.first, student.last, ":".join(student.classes)]
        #Add that information to the updated text file, splitting the categories by a ":"
        studentFile.write(":".join(items) + "\n\n")

    #Close the students file
    studentFile.close()

#Creates updated text file of courses - takes in the courses dictionary
def write_courses_back(courses):

    #Creates/Initiating updated courses file
    coursesFile = open("courses-updated.txt", "w")

    #Same Process/logic as writing the students - See Above
    for cid in courses.keys():
        course = courses[cid]
        items = [cid, course.name, course.prof, str(course.enrolled), str(course.capacity)]
        coursesFile.write(";".join(items) + "\n\n")

    #close the courses file
    coursesFile.close()

def courseSchedule(courses):
    #For each courseID in the course dictionary
    for cid in courses.keys():
        #initialize the course as a course class, ...
        #given the parameters associated with the course ID in the dictionary
            course = courses[cid]
            print()

            #Name
            print("Course name:", course.name)
            #Professor
            print("Professor:", course.prof)
            #Course ID
            print("ID:", course.cid)
            #Current number of students enrolled
            print("Current # Enrolled:", str(course.enrolled))

            #Max capacity of class
            print("Capacity:", str(course.capacity))

            #Remaining seats
            print("Available Seats Remaining:", str(course.capacity - course.enrolled))
            print()

#Gets student info from the dictionary of students
def studentInfo(students):
    #Takes in Student ID to return info on
    print("Please enter the student's id.")
    sid = input()

    #If the student doesn't exist, let the user know
    if sid not in students.keys():
        print("No student exists with that id.")
        print()
        
    #Otherwise, extract student information from the student dictionary
    #And return...
    else:
        student = students[sid]
        #...Name
        print("Name:", student.first, student.last)
        #...Student ID
        print("ID:", student.sid)
        #...And the list of the student's enrolled classes
        print("Classes:", str(student.classes))
        print()

#Checks if student already exists in the students dictionary
def newStudent(sid, students):


    #If not, ask if the student is new
    if sid not in students.keys():
        print(sid + " is not a valid current student ID")
        print("Would you like to be added as a new student?")
        print('Enter "Y" to continue or any other button to return to main menu')
        userResp = input()

        #If so, create a new student
        if userResp == 'y' or userResp == "Y":
            students = create_student(sid,students)
            return True, students

        #If not, dont create anything and dont add/drop classes
        else:
            return False, students
    #If the student already exists, then continue.
    return True, students

#Creating the startup menu    
def print_menu():

    #Initiates a dictionary of students
    students = {}

    # Open students-sample.txt file
    origStudentFile = open("students-sample.txt", "r")
    #Stores all student information in the list sLines
    sLines = origStudentFile.readlines()

    for student in sLines:

        #Removing useless whitespace
        if student != '\n':
        #Each line will contain a StudentID, First name, last name, ...
        #and all remaining list points will be assumed to be unique course numbers
        #No classes for the student can be the same
                sid, first, last, *classes = [s.strip() for s in student.split(":")]
                students[sid] = Student(sid, first, last, set(classes))
    origStudentFile.close()

    
    courses = {}
    # Open courses-sample.txt and place the data in courses dictionary
    origCourseFile = open("courses-sample.txt", "r")

    #Stores all course info in cLines
    cLines = origCourseFile.readlines()

    #Same logic as extracting student info - See above
    for course in cLines:
        #Removing useless whitespace
        if course != '\n':
              cid, name, prof, enrolled, capacity = [c.strip() for c in course.split(";")]
              courses[cid] = Course(cid, name, prof, int(enrolled), int(capacity))

    #Startup menu will always appear until broken at "6".
    while True:
        #Menu items
        print("1. Add course")
        print("2. Drop course")
        print("3. Print student's schedule")
        print("4. Print course schedule")
        print("5. Plot a bar graph of course number on X-axis, capacity and actual enrollment on the Y-axis")
        print("6. Done\n")

        #Taking in input
        response = input()

        #If changes to the students/course list is wanted
        if response == "1" or response == "2":

            #Gets StudentID
            print("Please enter your student id.")
            sid = input()
            
            #Checks if Valid
            validStudent, students = newStudent(sid, students)

            #Continues to run if the student is registered
            if (validStudent):
                #Asks for course info to be added/removed from
                print("Please enter the course id.")
                cid = input()

                #If the course already exists
                if cid in courses.keys():

                    #And the student wants to be added
                    if response == "1":

                        #Check to see if the class is full
                        if courses[cid].enrolled == courses[cid].capacity:
                            print("The class is full.")

                        #Checks if student is already enrolled
                        elif cid in students[sid].classes:
                            print("Student is already enrolled in the class")
                        
                        #If the class isnt at capacity, add the student
                        else:

                            #Increase course enrollment by 1
                            courses[cid].enrolled += 1
                            #Add course to list of classes that the student's taking
                            students[sid].classes.append(cid)
                            #Let user know that the class has been successfully added
                            print("You have been added to class " + courses[cid].cid)
                        
                    #But if the student wants to be removed
                    elif response == "2":
                        student = students[sid]
                        course = courses[cid]

                        #remove the student only if the student already enrolled
                        if cid in student.classes:
                            classes = student.classes
                            classes.remove(cid)
                            student.classes = classes
                            courses[cid].enrolled -= 1
                        #If he's not in the class, let the student know
                        else:
                            print("Student is not enrolled in that class.")

                #If the course doesn't exist
                else:
                    #Let the user know that the course can't be found
                    #And that no edits have been made
                    print("No course exists with that id.")

            print()

  	#If the user wants a student's info
        elif response == "3":
            studentInfo(students)

  	#If the user wants the info for all courses    
        elif response == "4":
            courseSchedule(courses)
            
  	#If the user wants a chart of course enrollment statuses
        elif response == "5":

            #Get enrollment and capacity values for each course
            cids = courses.keys()
            enrolled = [courses[c].enrolled for c in cids]
            capacity = [courses[c].capacity for c in cids]

            #plot max capacities
            cap = plt.bar(cids, capacity)
            #Overlap that plot with current enrollments
            enr = plt.bar(cids, enrolled)

            #Labels
            plt.title("Course Availabilities by ID")
            plt.xlabel("Class Unique IDs")
            plt.ylabel("Number of spots")
            plt.legend([cap, enr], ["capacity", "students enrolled"])

            #Show the graph
            plt.show()

  	#Stop infinite while loop if "6" is hit.
        elif response == "6":
            #Create updated student and course files
            write_students_back(students)
            write_courses_back(courses)
            break

        #Error message if another key is pressed.
        else:
            print("Unrecognized input.")
    

#Main
def main():
    #Runs the print menu and it's properties
    print_menu()

#Calls main function
main()
