class TermPaper:
    student = []
    author = []
    subject = []
    grade = []
    def setStudent(self, value):
        self.student.append(value)
    
    def getStudent(self):
        return self.student
    def setAuthor(self, value):
        self.author.append(value)

    def getAuthor(self):
        return self.author

    def setSubject(self, value):
        self.subject.append(value)

    def getSubject(self):
        return self.subject

    def setGrade(self, value):
        self.grade.append(value)

    def getGrade(self):
        return self.grade

t1 = TermPaper()

method_list = ["Student", "Author", "Subject", "Grade" ]

while True:
    decision = input("Do you want to input or output?").lower()

    if decision =="input":
        for value in method_list:
            term  = input(f"Enter the {value} ")
            set_method = getattr(t1,f"set{value}")
            set_method(term)
    elif decision == "output":
        for num, value in enumerate(method_list):
            get_method = getattr(t1, f"get{value}")
            print(get_method())
            
        for student, author, subject, grade in zip(t1.student, t1.author, t1.subject, t1.grade):
            print(f'Student: {student.title()} | Author: {author.title()} | Subject: {subject.title()} | Grade: {grade.capitalize()}')
    else:
        print("Please enter a valid input")
        continue
