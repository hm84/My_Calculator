class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def sum(self):
        return self.num1+self.num2
    
    def sub(self):
        return self.num1-self.num2

    def mul(self):
        return self.num1*self.num2

    def div(self):
        return self.num1/self.num2
    

while 1:
    x=int(input("1.sum 2.sub 3.mul 4.div 5.exit : "))

    if x==5:
        exit(0)

    n1=int(input("number1 : "))
    n2=int(input("number2 : "))
    
    my_calculate=Calculator(n1,n2)

    if x==1:
        print(my_calculate.sum())

    if x==2:
        y=int(input("Do you want absolute value to be applied? 1.Yes  2.No  : "))
        if y==1:
            print(abs(my_calculate.sub()))
        else :
            print(my_calculate.sub())
        

    if x==3:
        if n1==0:
            z=int(input("The first number you want is zero. Do you want to make a change? 1.Yes  2.No  : "))
            if z==1:
                n1=int(input("number1 : "))
                my_calculate=Calculator(n1,n2)
                print(my_calculate.mul())
            else:
                print(my_calculate.mul())

        if n2==0:
            z=int(input("The second number you want is zero. Do you want to make a change? 1.Yes  2.No  : "))
            if z==1:
                n2=int(input("number2 : "))
                my_calculate=Calculator(n1,n2)
                print(my_calculate.mul())
            else:
                print(my_calculate.mul())
            

    if x==4:
        if n2==0:
            f=int(input("The second number you want is zero. Do you want to make a change? 1.Yes  2.No  : "))
            if f==1:
                n2=int(input("number2 : "))
                my_calculate=Calculator(n1,n2)
                print(my_calculate.div())
            else:
                print("error...")

        if isinstance(my_calculate.div(), float):
            t=int(input("Decimal division should be done? 1.Yes  2.No  : "))
            if t==1:
                q=int(input("Enter the number of decimal places? : "))
                print(round(my_calculate.div() , q))
            else:
                print(int(my_calculate.div()))
        
        

