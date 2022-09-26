class calculator:
    def addition(self):
        print(a+b)
    def subtraction(self):
        print(a-b)
    def multiplication(self):
        print(a*b)
    def divison(self):
        print(a/b)

a=float(input())
b=float(input())

cal=calculator()

operation=input()

if(operation == 'Addition'):
    cal.addition()
elif(operation == 'Subtraction'):
    cal.subraction()
elif(operation == 'Multiplication'):
    cal.multiplication()
elif(operation == 'Division'):
    cal.divison()
