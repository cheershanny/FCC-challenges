import re

def arithmetic_arranger(problems, solver = False):
    if len(problems) > 5:
        return "Error: Too many problems."
    
    firstLine =list()
    secondLine = list()
    dashLine = list()
    solvedLine = list()

    for problem in problems:
        first = problem.replace(" ", "")
        operators = re.findall(r"[-+]", first)
        if len(operators) == 0:
            return "Error: Operator must be '+' or '-'."
        oprtIndex = first.index(operators[0])
        #print("operators' index:", oprtIndex)
        #print("operators: ", operators)    
        beforeOprt = first[:oprtIndex]
        afterOprt = first[oprtIndex + 1:]
        if not beforeOprt.isdigit() or not afterOprt.isdigit():
            return "Error: Numbers must only contain digits."
        firstNo = int(beforeOprt)
        secondNo = int(afterOprt)
        if len(beforeOprt) > 4 or len(afterOprt) > 4:
            return "Error: Numbers cannot be more than four digits."
        if operators[0] == "+":
            solvedNo = firstNo + secondNo
        if operators[0] == "-":
            solvedNo = firstNo - secondNo

        totalDashes = max(len(beforeOprt),len(afterOprt)) + 2
        firstLine.append((totalDashes-len(beforeOprt))*" " + beforeOprt)
        secondLine.append(operators[0]+(totalDashes-len(afterOprt)-1)*" " + afterOprt)
        dashLine.append("-"*totalDashes)
        solvedLine.append((totalDashes-len(str(solvedNo)))*" "+ str(solvedNo))

    if solver == False:
        return("    ".join(firstLine) + "\n" + "    ".join(secondLine) + "\n" + "    ".join(dashLine))
    
    elif solver == True:
       return("    ".join(firstLine) + "\n" + "    ".join(secondLine) + "\n" + "    ".join(dashLine) + "\n" + "    ".join(solvedLine)) 
              
print(arithmetic_arranger(["32 + 692", "3801 + 2", "45 + 43", "123 + 49", "3-1"], True))


