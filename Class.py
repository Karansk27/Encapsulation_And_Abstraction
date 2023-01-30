print("Function Over Writing ")
class Staff():
    def working_hrs(self):
        workinghrs=50
        
    def Teching_hrs(self):
        techhrs=10

    def display(self):
        print("Total Number of staff working in Hrs In : ",workinghrs)
        print("Total Number of staff teching in Hrs In : ",techhrs)
        

class students(Staff):
    def working_hrs(self):
        working_hrs=30
    def studying_hrs(self):
        study_hrs=study_hrs
    def display(self):
        print("Total Number of students Studeying in Hrs : ",working_hrs)
        print("Total Number of Students  Student  in Hrs : ",study_hrs)
        
Human=Staff()
Human.display()
