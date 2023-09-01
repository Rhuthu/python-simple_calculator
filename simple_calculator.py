num1=input("First number: ")
operator=input("Enter oprator(+,-,/,*,%,power): ")
num2=input("Second number: ")

if operator=='+' :
    print(int(num1)+int(num2))
elif operator=='-':
    print(int(num1)-int(num2))
elif operator=='*':
    print(int(num1)*int(num2))
elif operator=='/':
    print(int(num1)/int(num2))
elif operator=='%' :
    print(int(num1)%int(num2))
elif operator=="power" :
    print(int(num1)**int(num2))
else :
    print("Invalid operator")

