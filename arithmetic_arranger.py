import re
#Enable checking
DEBUG= True

def arithmetic_arranger(problems):

    if len(problems)  > 5:
        return "Error: Too many problems"

    for problem in problems:
        try:
            first=int(''.join(re.findall("^\d*", problem)))
        except:
                return "Error: Numbers must only contain digits."
        if first > 9999:
            return "Error: Numbers cannot be more than four digits."
        if DEBUG:
            print(first)

        try:
            second=int(''.join(re.findall("\d*$", problem)))
        except:
            return "Error: Numbers must only contain digits."
        if first > 9999:
            return "Error: Numbers cannot be more than four digits."
        if DEBUG:
            print(second)

        operator=''.join(re.findall("[+-]", problem))
        if operator != "+" and operator != "-":
            return "Error: Operator must be '+' or '-'."

    return arranged_problems