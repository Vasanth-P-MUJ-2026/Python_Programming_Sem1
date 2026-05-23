# Base class: student
class student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

# child class: Marks(inherits from student)
class Marks(student):
    def __init__(self,name,roll_no,m1,m2,m3):
        #call parent constructor
        super().__init__(name,roll_no)
        self.marks = (m1,m2,m3) #store marks as tuple

#child class: Result(inherits from Marks)
class Result(Marks):
    def __init__(self, name, roll_no,m1, m2, m3):
        #call parent constructor
        super().__init__(name, roll_no, m1, m2, m3)

    def calculate_result(self):
        total = sum(self.marks)
        percentage = round(total/3,2) #round to 2 decimals
        #store final output in dictionary
        result_dict = {
            'name':self.name,
            'roll_no': self.roll_no,
            'marks': self.marks,
            'total': total,
            'percentage': percentage
        }
        return result_dict

#---main Execution---
# take custom input
name = input()
roll_no = int(input())
m1 = int(input())
m2 = int(input())
m3 = int(input())

student_result = Result(name, roll_no, m1, m2, m3)
output = student_result.calculate_result()

#print dictionary directly
print(output)
