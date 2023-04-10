class Student:
    def __init__(self, name, cohort):
        self.name = name
        self.cohort = cohort

# single_class_lab.md questions to create methods for functions
    # A) Part 1: talk_method for class 
    # Linked to # 5
    def talk(self):
        return "I can talk!"
    # Linked to # 6
    # A) Part 2: say_favourite_language method for functions
    def say_favourite_language(self, student_fave_language):
        return "I love " + student_fave_language
    

# 1
def student_has_name(self):
    return self.student.name

# 2
def student_has_cohort(self):
    return self.student.cohort

# 3
def student_can_update_name(self): 
    return self.student.name 

# 4
def test_student_can_change_cohort(self, name, cohort):
    return self.student.cohort


# # 5   
def student_can_talk(self):
    return self.student.talk()

# 6 
def student_has_favourite_language(self):
    return self.student.say_favourite_language()

# All of the tests passed :)



