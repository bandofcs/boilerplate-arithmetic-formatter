import re
#Enable checking by printing to console
DEBUG= False

def arithmetic_arranger(problems, count=None):
    #Variables definition
    #To be printed out
    firstrow=list()
    secondrow=list()
    thirdrow=list()
    forthrow=list()
    #Length of each operand
    firstlen=0
    secondlen=0
    thirdlen=0
    maxlen=0
    #Result variable
    third=None

    #Check that no more than 5 problems
    if len(problems)  > 5:
        return "Error: Too many problems."

    #Go through each problem
    for problem in problems:
        #Make sure that inputs are only digits
        try:
            first=int(''.join(re.findall("^([^\s]+)", problem)))
        except:
            if DEBUG:
                print("regex is"+''.join(re.findall("^./S", problem)))
            return "Error: Numbers must only contain digits."
        #Make sure that operand cannot be more than 4 digits
        if first > 9999:
            return "Error: Numbers cannot be more than four digits."
        if DEBUG:
            print(first)
        #Make sure that inputs are only digits
        try:
            second=int(''.join(re.findall("([^\s]+)$", problem)))
        except:
            return "Error: Numbers must only contain digits."
        #Make sure that operand cannot be more than 4 digits
        if second > 9999:
            return "Error: Numbers cannot be more than four digits."
        if DEBUG:
            print(second)
        #Make sure that operator is only +/-
        operator=''.join(re.findall("[+-]", problem))
        if operator != "+" and operator != "-":
            return "Error: Operator must be '+' or '-'."
        if DEBUG:
            print(operator)
        
        #print empty spaces for second problem and beyond
        if maxlen>0:
            firstrow.append("    ")
            secondrow.append("    ")
            thirdrow.append("    ")

        if count==True and maxlen>0:
            forthrow.append("    ")

        #Find the number of digits in the first operand
        if first>999:
                firstlen=4
        elif first>99:
                firstlen=3
        elif first>9:
                firstlen=2
        elif first<10:
                firstlen=1
        #Find the number of digits in the second operand
        if second>999:
            secondlen=4
        elif second>99:
            secondlen=3
        elif second>9:
            secondlen=2     
        elif second<10:
            secondlen=1
        #Find the bigger number of digits between the 2 operands
        maxlen=max(secondlen,firstlen)+2

        if count==True:
            if operator =="+":
                third=first+second
            elif operator == "-":
                third=first-second
            if third>9999:
                thirdlen=5
                for i in range(maxlen-thirdlen):
                    forthrow.append(" ")
                forthrow.append(str(third))
            elif third>999:
                thirdlen=4
                for i in range(maxlen-thirdlen):
                    forthrow.append(" ")
                forthrow.append(str(third))
            elif third>99:
                thirdlen=3
                for i in range(maxlen-thirdlen):
                    forthrow.append(" ")
                forthrow.append(str(third))
            elif third>9:
                thirdlen=2
                for i in range(maxlen-thirdlen):
                    forthrow.append(" ")
                forthrow.append(str(third))
            elif third>-1:
                thirdlen=1
                for i in range(maxlen-thirdlen):
                    forthrow.append(" ")
                forthrow.append(str(third))
            elif third>-10:
                thirdlen=2
                for i in range(maxlen-thirdlen):
                    forthrow.append(" ")
                forthrow.append(str(third))
            elif third>-100:
                thirdlen=3
                for i in range(maxlen-thirdlen):
                    forthrow.append(" ")
                forthrow.append(str(third))
            elif third>-1000:
                thirdlen=4
                for i in range(maxlen-thirdlen):
                    forthrow.append(" ")
                forthrow.append(str(third))
            elif third>-10000:
                thirdlen=5
                for i in range(maxlen-thirdlen):
                    forthrow.append(" ")
                forthrow.append(str(third))

        #Append spaces followed by first operand
        for i in range(maxlen-firstlen):
            firstrow.append(" ")
        firstrow.append(str(first))
        #Append operator followed by spaces and second operand
        secondrow.append(operator)
        for i in range(maxlen-secondlen-1):
            secondrow.append(" ")
        secondrow.append(str(second))
        #Append "-" equals to the bigger number of digits between the 2 operands +2
        for i in range(maxlen):
            thirdrow.append("-")

        if DEBUG:
            print(''.join(firstrow))
            print(''.join(secondrow))
            print(''.join(thirdrow))
            print(''.join(forthrow))
        
    firstrow.append("\n")
    secondrow.append("\n")
    if count==True:
        thirdrow.append("\n")
        arranged_problems=''.join(firstrow + secondrow + thirdrow + forthrow)
        return arranged_problems
    
    arranged_problems=''.join(firstrow + secondrow + thirdrow)
    if DEBUG:
        print(type(arranged_problems))
    return arranged_problems