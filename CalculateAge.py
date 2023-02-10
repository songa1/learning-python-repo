class CalculateAge:
    age = ''
    yob = ''
    
    def giveYob(self):
        yob = input("Enter your Year Of Birth: ")
        self.yob = yob
    def calculateHere(self):
        aged = 2023 - int(self.yob)
        if aged < 0:
            print("Please add the right Year of birth!")
            self.age = '';
        else:
            self.age = aged
            
    def getAge(self):
        if(self.age == ''):
            return "Your age can not be negative!"
        else:
            return self.age