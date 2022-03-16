class Student:
    # data members of the student class
    name = "DEFAULT_NAME"
    age = "18"
    gender = "MALE_DEFAULT"
    roll_no = 92
    # constructor class...

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def set_roll_no(self, roll_no):
        self.roll_no = roll_no


class Exam(Student):
    # data members of the exam...
    sub_list = []
    total_subjects = 6
    marks_of_student = {}
    # per subjects, maximum marks can be stored...
    __marks_criteria = 100
    # to be able to pass the information that whether the marks for subjects have been updated?
    __gotMarks = False  # initially it is false...
    # simple methods ===================================================================================================


    def __init__(self, name, age, gender, sub_length):
        # calling the student class to make a reference of 'Student' type
        super().__init__(name, age, gender)
        self.total_subjects = sub_length
        # getting names of subjects...
        for i in range(self.total_subjects):
            sub_name = input(f"Enter name of the subject {i + 1} : ")
            self.sub_list.append(sub_name)

    def show_subject_list(self):  # to print the all the subjects...
        print("The subjects are : ")
        for subject in self.sub_list:
            print(subject)

 # for some alteration or changes in subjects=======================================================
    def change_subject_list(self):
        confirmation = input(
            "Are you sure you want to change the subjects? (y/n) : ")
        if 'y' in confirmation or 'Y' in confirmation:
            print("Enter all the subject's name again!")
            for i in range(self.total_subjects):
                self.sub_list.append(input("Enter subject name : "))
            print("All subject's name changed successfully!")
        else:
            print("Operation cancelled successfully!")
            # changing the references because the subjects are changed...
            self.__gotMarks = False

    def alter_subjects(self, start, end):
        if start <= 0 or end > self.total_subjects:
            print("There is some error in arguments passed for alteration!")
        else:
            for i in range(start, end + 1):
                self.sub_list.pop(i - 1)
                self.sub_list.insert(
                    i - 1, input(f"Enter name of the subject {i} : "))
        # changing the references because the subjects are altered...
        self.__gotMarks = False

    def alter_subject(self, index):
        self.alter_subjects(index, index)
    # for alteration in marks or storing the marks=====================================================================

 # for storing the marks...
    def __getMarks(self):
        self.marks_of_student.clear()  # clearing the old mark sheet...
        for subject in self.sub_list:  # generating new mark sheet...
            marks = int(input(f"Enter marks for {subject} : "))
            if marks < 0 or (marks > self.__marks_criteria):
                print("Error in marks...entered...!")
                return
            else:
                self.marks_of_student.update({subject: marks})
        # changing the references because the marks are updated...
        self.__gotMarks = True
        print("Mark-sheet has been updated!")

    def grab_marks(self):  # for getting marks of the students...
        if self.__gotMarks:
            confirmation = input(
                """Are you sure you want to grab the marks again, because the subjects are neither changed nor altered! (y/n) : """)
            if 'y' in confirmation or 'Y' in confirmation:
                self.__getMarks()
            else:
                print("Operation of getting new Mark-sheet has been cancelled!")
        else:
            self.__getMarks()

    def change_marks_criteria(self, max_marks):
        self.__marks_criteria = max_marks

    def show_marks_criteria(self):
        print(self.__marks_criteria)

    def get_marks_criteria(self):
        return self.__marks_criteria



class Result:
 # initial exam class reference...
    exam = ""
    passing_criteria = 100  # passing criteria...
    grade_list = {"A": 90, "B": 80, "C": 60, "D": 50}  # grade list...

    # constructor...
    def __init__(self, exam):
        self.exam = exam
        self.passing_criteria = (
            exam.get_marks_criteria() * exam.total_subjects) * 0.5
    # grade making according to marks...

    def __getGrade(self, marks):
        for grades in self.grade_list.keys():
            if marks >= self.grade_list.get(grades):
                return grades
        return "Fail"

    # for printing the mark-sheet...
    def show_mark_sheet(self):
        if len(self.exam.marks_of_student) == self.exam.total_subjects:
            print("\n=================================================================")
            print(f"Mark-sheet of Student : {self.exam.name}")
            print(f"Roll no : {self.exam.roll_no}")
            for subject in self.exam.marks_of_student.keys():
                print(f"Marks in {subject} : ", self.exam.marks_of_student.get(
                    subject), "Grade : ", self.__getGrade(self.exam.marks_of_student.get(subject)))
            print(f"Total marks : {self.exam.total_subjects * self.exam.get_marks_criteria()}/{sum(self.exam.marks_of_student.values())}"
)
            print(
                f"Overall Grade : {self.__getGrade(sum(self.exam.marks_of_student.values())/self.exam.total_subjects)}")
        else:
            print("Marks has not been updated!")


if __name__ == "__main__":
    ExamA = Exam("Meshv_p", 18, "MALE", 4)
    ResultA = Result(ExamA)
    ResultA.exam.grab_marks()
    ResultA.show_mark_sheet()