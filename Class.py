class TermPaper:
    def __init__(self):
        self.student = []
        self.author = []
        self.subject = []
        self.grade = []
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
    #---------------------
    # Updates and returns a list of attributes present in the TermPaper class instance, 
    # ensuring they are formatted in title case for consistency.
    # The 'vars(self)' function retrieves the dictionary of attributes and their values for the current object instance.
    #((Yes it is using an instance, not the class itself which would be))
    # Each attribute is represented as a key-value pair in the dictionary.

    # The 'listAttributes' variable is created using list comprehension, 
    # which is a concise way to build a list by applying an expression to each item in an iterable (here, the dictionary items).
    # The expression 'attr.title()' formats each attribute name in title case, ensuring consistent capitalization.

    # The resulting list contains the formatted attribute names, and it is returned by the method.
    def updateListAttributes(self):
        listAttributes = [attr.title() for attr in vars(self)]
        return listAttributes

#----------------------------------------- Functions

counter = 1 # Number used to dynamically name object instances t1, t2, t3, ect.
def createTerm():
    global counter # Makes counter variable global so that it can be changed
    termPapers[f"t{counter}"] = TermPaper() # Creates term paper objects dynamically and adds them to a Dictonary
    print(f"Term t{counter} created")
    counter += 1 
#---------------------------------
def nicePrint2(attrValue): # Dynamic print statement
    for i in range(len(attrValue.getStudent())):  # Assuming all lists have the same length iterate through each "student"
        attributesStr = "" # Assigns an empty string to have values added to it
        for attrName, attributeValue in vars(attrValue).items(): # Iterates through a dictonary of the specific class instance
            if isinstance(attributeValue, list): # if the type of attribute is a list
                attributesStr += f"{attrName.title()}: {attributeValue[i].title()} | " # Appends formatted info to the empty string
        print(attributesStr)
#---------------------------------
def processInput():
    for value in attributeList: # For each method in the class(defined in a list)
        term  = input(f"Enter the {value} ") # Set term variable equal to the input. Dynamically change input.
        set_method = getattr(paperChoice,f"set{value}") # Sets the variable to a function(Class, Dynamic method within class) method needs to be a string and therefore can be dynamic 
        set_method(term) # Calls function above with argument. example setMethod(term) = a setmethod(userinput)
#---------------------------------
def processOutput():
    for num, value in enumerate(attributeList):
        get_method = getattr(paperChoice, f"get{value}")#
        print(get_method())
                                
    nicePrint2(paperChoice)
    
#-------------------------------------------------------------------------------------------------------------------


attributeList = [] # Dynamic list
termPapers = {} # Dynamic dictonary holding class instances
 # Counter used to automatically name termpapers with increments to avoid overwriting
while True:
    termChoice = input("Pick or create a term ").lower()
    if termChoice == "create":
        createTerm()

    elif termChoice == "pick":
        if len(termPapers) == 0: # Filter  if no papers are made yet
            print("No term papers have been created yet")
            continue # Sends you back to start

        else: # If there are any TermPaper objects in the dict, we execute below

            for pos,(term_name, term_paper_instance) in enumerate(termPapers.items()): # Prints all term paper objects created
                print(f"{pos+1}: {term_name}") # Prints the position + 1(filter 0) and the name of the term Ex: t1
                if len(attributeList) == 0: # If there are no attributes in the list(there are none by default)
                    attributeList.extend(term_paper_instance.updateListAttributes()) 
                # Dynamically extends the attributeList with the attributes present in the TermPaper class instance,
                # ensuring that the list contains all relevant attributes for displaying and manipulating term paper information.

            while True:
                paperChoice = "t" + input("Enter the number associated with the paper you want to select ")
                if paperChoice not in termPapers:
                    print("Invalid Entry, Just input the number")
                    continue
                else:
                    paperChoice = termPapers[paperChoice]
                    print("You can enter 'q' to go back to the term creation and selection prompt")
                    while True:
                        decision = input("Do you want to input or output on the current term? ").lower()

                        if decision =="input": # If they want to input values for a term
                            processInput()
                        elif decision == "output":
                            processOutput()
                        elif decision == "q":
                            break
                break
    else:
        print("Please enter a valid input")




# Old non dynamic printing function
# def nicePrint():
#     for student, author, subject, grade in zip(paperChoice.student, paperChoice.author, paperChoice.subject, paperChoice.grade):
#         print(f'Student: {student.title()} | Author: {author.title()} | Subject: {subject.title()} | Grade: {grade.capitalize()}')
