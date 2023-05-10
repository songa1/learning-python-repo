class AverageCalc:
    
    stInfo = {}
    
    # A method to set student info into the dictionary
    def setStInfo(self):
        name = input("Enter your name: ")
        y1 = int(input("Enter Y1 marks: "))
        y2 = int(input("Enter Y2 marks: "))
        y3 = int(input("Enter Y3 marks: "))
        self.stInfo[name] = [name, [y1,y2,y3]]
    
    # Display student information stored in a dictionary
    def getStudents(self):
        print(self.stInfo)
        
    # Calculate the total marks and percentage
    def totalMarks(self):
        finalInfo = {} # Store the disctionaly with sum of marks
        finalInfoPercent = {} # Store the dictionary with percentages
        
        # Loop through dictionary data
        for p in self.stInfo:
            marks = self.stInfo[p][1]
            
            # Calculate the sum of marks
            s = 0
            for m in marks:
                s += m
            #Percentage calculation 
            percentage = (s * 100)/300
            av = s / 3;
            
            finalInfo[p] = [p, s] # Information with total marks
            finalInfoPercent[p] = int(percentage) # Information with percentages
            
        print("This is the total of your marks: ",finalInfo)
        print("This is your marks per cent: ", finalInfoPercent)
        print("This is your marks average: ", av)
                