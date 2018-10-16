#Codebar has members
class Member:
    def __init__(self, full_name):
        self.name = full_name
    def introduce(self):
        return (f"Hi my name is " + {self.name})

#every member is eitehr a teacher or a
#class for students...
class Student(Member):
    def __init__(self, full_name, reason):
        super().__init__(full_name)
        self.reason = reason

#class for instructors...
class Instructor(Member):
    def __init__(self, fill_name, bio):
        super().__init__(full_name)
        self.bio = bio
        self.skill = []
    def add_skill(self,add_skill):
        self.skill.append(add_skill)

#A date. + A subject. + A group of instructors.+ A roster of students.
class Workshop:
    def __init__(self, date, subject):
        self.date = date
        self.subject = subject
        self.instructors = []
        self.participants = []

def add_participant(self, participant):
        if isinstance(participant, Instructor):
            self.instructors.append(participant)
        elif isinstance(participant, Student):
            self.participants.append(participant)

    def print_details(self):
        print("Workshop - {} - {}".format(self.date, self.subject))
        print("Students")
        for index, student in enumerate(self.participants):
            print("{}. {} - {}".format(index + 1, student.full_name, student.reason))
        print("Instructors")
        for index, instructor in enumerate(self.instructors):
            print("{}. {} - {} \n {}".format(index + 1, instructor.full_name,
', '.join(instructor.skills), instructor.bio))

student = Student('Andrew Foster', "I like stuff")
print(student)
print(student.introduce())
# print(student.greeting)

#Make your code work for the following calls...
#and print out the response you can see in the comments below...

workshop = Workshop("12/03/2014", "Shutl")

jane = Student("Jane Doe", "I am trying to learn programming and need some help")
lena = Student("Lena Smith", "I am really excited about learning to program!")
vicky = Instructor("Vicky Python", "I want to help people learn coding.")
vicky.add_skill("HTML")
vicky.add_skill("JavaScript")
nicole = Instructor("Nicole McMillan", "I have been programming for 5 years in Python and want to spread the love")
nicole.add_skill("Python")

workshop.add_participant(jane)
workshop.add_participant(lena)
workshop.add_participant(vicky)
workshop.add_participant(nicole)
workshop.print_details
=>
Workshop - 12/03/2014 - Shutl

Students
1. Jane Doe - I am trying to learn programming and need some help
2. Lena Smith - I am really excited about learning to program!

Instructors
1. Vicky Ruby - HTML, JavaScript
   I want to help people learn coding.
2. Nicole McMillan - Ruby
   I have been programming for 5 years in Ruby and want to spread the love
#













#     {
#     "reason": "I've always wanted to {reason}"
#     "bio": "bio"

# }


