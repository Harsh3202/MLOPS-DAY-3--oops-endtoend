class Employee:
    def __init__(self):
        print("the object creation starts")
        self.id = 100
        self.designation = "C1"
        print("the objection creation ends")
    def travel(self):
        self.travell = "JAMMU"
        print(f"The emloyee id: {self.id} is travelling to {self.travell}")
harsh = Employee()
harsh.travel()
        