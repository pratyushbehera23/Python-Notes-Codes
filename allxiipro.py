# Some basic python programs: 

print()
print("1.Arithmetic[+-*/], 2.odd/even, 3.multiplicationTABLE, 4.Power, 5.Divisibility, 6.Division, 7.Character?, 8.SwapCode, 9.AddDigits, 10.Calendar, 11.YearlyCalendar, 12.ASCII, 13.NumberSystem, 14., 15.Dice, 16.Choose, 17.LargestNo, 18., 19., 20., ")
print()

while True:

    # Choose program no. from above list to run 

    n = int(input("Which program do u want to run ? "))

    if n==1 :
        a = int(input("First no : "))
        b = int(input("Second no : "))
        op = input("Which operation do u want? [+ - * /] : ")
        result = 0
        if op=='+' :
            result = a + b
        elif op=='-' :
            result = a - b
        elif op=='*' :
            result = a * b
        elif op=='/' :
            result = a / b
        else :
            print("invalid operator")
            break
        print(a, op, b, '=', result)

    elif n==2 :
        n = int(input("Enter no : "))
        if n%2 == 0 :
            print(n,"is Even")
        else :
            print(n,"is Odd")

    elif n==3 :
        n = int(input("TABLE of : "))
        for i in range(1,11):
            print(n,'x',i,'=',n*i)

    elif n==4 :
        a = int(input("Enter base no : "))
        b = int(input("Enter power : "))
        power = a**b
        print(power)

    elif n==5 :
        a = int(input("Enter the no : "))
        b = int(input("Enter second no : "))
        if a%b == 0 :
            print(a,"is divisible by",b)
        else :
            print(a,"is not divisible by",b)

    elif n==6 :
        a = int(input("First no (Divident) : "))
        b = int(input("Second no (Divisor) : "))
        d = a/b
        q = a//b
        r = a%b
        print("Division :",d)
        print("Quotient :",q)
        print("Remainder :",r)

    elif n==7 :
        ch = input("Enter any character : ")
        if ch>='A' and ch<='Z' :
            print('You entered a Uppercase character')
        elif ch>='a' and ch<='z' :
            print('You entered a Lowercase character')
        elif ch>='0' and ch<='9' :
            print('You entered a Digit')
        else :
            print('You entered a Special character')

    elif n==8 :
        a = int(input("Enter no. a : "))
        b = int(input("Enter no. b : "))
        swap = a
        a = b
        b = swap
        #or without third variable:
        '''
        a += b
        b = a - b
        a = a - b'''
        print("a:",a,"b:",b)

    elif n==9 :
        num = int(input("Enter a no. : "))
        s = str(num)
        l = len(s)
        add = 0
        for i in range(l):
            add += int(s[i])
        print(add)

    elif n==10 :
        import calendar
        mm = int(input("Enter month : "))
        yy = int(input("Enter year : "))
        print(calendar.month(yy,mm))

    elif n==11 :
        import calendar
        yy = int(input("Enter year : "))
        for mm in range(1,13):
            print(calendar.month(yy,mm))

    elif n==12 :
        choose = input("What do u have? ord or chr : ")
        if choose=='ord' :
            a = int(input("Enter order : "))
            c = chr(a)
            print(c)
        elif choose=='chr' :
            a = str(input("Enter chracter : "))
            o = ord(a)
            print(o)
        else :
            print("Choose ord/chr ")

    elif n==13 :
        d = int(input("Enter decimal : "))
        b = bin(d)
        o = oct(d)
        h = hex(d)
        print('Binary :',b,'Octa :',o,'Hexa :',h)

# randomly print taken ; to be modified for input of bin;oct;hex
    elif n==14 :
        choose = input("binary,octa or hexa : ")
        if choose=='binary' :
            print("Write 0b'number' :")
        elif choose=='octa' :
            print("Write 0o'number' :")
        elif choose=='hexa' :
            print("Write 0x'number' :")
        else :
            print("invalid option")

    elif n==15 :
        import random
        dice = random.randint(1,6)
        print(dice)

    elif n==16 :
        import random
        ans = random.randint(1,2)
        if ans==1 :
            print("True")
        elif ans==2 :
            print("False")
        else :
            print("Doubt")
        print(ans)

    elif n==17 :
        x=y=z=0
        x = int(input("Enter 1st no. : "))
        y = int(input("Enter 2nd no. : "))
        z = int(input("Enter 3rd no. : "))
        max = x
        if y>max :
           max = y
        if z>max :
            max = z
        print("Largest no is",max)

    else :
        print("invalid number choosen")

# Confirmation to continue or break the loop
    
    ask = input("Do u want to continue ? ")

    if ask == 'YES' or ask == 'Yes' or ask == 'yes' or ask == 'y' :
        continue

    else :
        break
