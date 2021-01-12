import numpy as np
import math
while True:
  text= input("This is the PI Calculator. Type Enter to continue  ")
  if (text== "Enter"): break

a= input("Do you want to continue? Type Yes or No ")
if (a =="Yes"):
    print("Here are the options.\n 1. What is PI 2.What is the value of PI  3. Area Calculator 4.Circumfrence Calculator 5.diameter calculator ")
    b= int(input("Enter your choice."))
if (b==1):
    print("The number π is a mathematical constant. It is defined as the ratio of a circle's circumference to its diameter, and it also has various equivalent definitions.Regardless of the circle's size, this ratio will always equal pi.Pi is an irrational number, meaning that its decimal form neither ends (like 1/4 = 0.25) nor becomes repetitive It appears in many formulas in all areas of mathematics and physics. It is approximately equal to 3.14159.")
    c=input("Do you want more info on PI. Type Yes or No. ")
    if c=="Yes":
        print("Pi has been known for nearly 4,000 years and was discovered by ancient Babylonians. A tablet from somewhere between 1900-1680 B.C. found pi to be 3.125. The ancient Egyptians were making similar discoveries, as evidenced by the Rhind Papyrus of 1650 B.C. In this document, the Egyptians calculated the area of a circle by a formula giving pi an approximate value of 3.1605! Pi began being symbolized by the pi symbol (π) in the 1706 by the British mathematician William Jones. Jones used 3.14159 as the calculation for pi.")
        a1= input("Do you want to continue? Type Yes or No ")
        if (a1 =="Yes"):
            print("Here are the options.\n 1. What is PI 2.What is the value of PI  3. Area Calculator 4.Circumfrence Calculator 5.diameter calculator ")
            b= int(input("Enter your choice."))
        else:
            print("")
    else:
        a2= input("Do you want to continue? Type Yes or No ")
        if (a2 =="Yes"):
            print("Here are the options.\n 1. What is PI 2.What is the value of PI  3. Area Calculator 4.Circumfrence Calculator 5.diameter calculator")
            b= int(input("Enter your choice. "))  
        else:
            print("")
elif (b==2):
    def pi():
        pi=0
        d=4
        e=1
        pppiii= int(input("Enter a value to estimate pi. The higher the number the more acurate it is but it may take a while to compute the final value. "))
        for i in range(1,pppiii):
            a= 2*(i % 2)-1
            pi += a*d/e
            e+=2
            print("Pi approx. is",pi)
        print("Rounded Value of pi value of pi is ",np.pi, math.pi)
    pi()
    Pi = 0.0
    for i in range(1, 10000000, 4):
        Pi += 4/i
        Pi -= 4/(i+2)
    print("Another approx. Value of pi",Pi)
    
    a2= input("Do you want to continue? Type Yes or No ")
    if (a2 =="Yes"):
        print("Here are the options.\n 1. What is PI 2.What is the value of PI  3. Area Calculator 4.Circumfrence Calculator 5.diameter calculator ")
        b= int(input("Enter your choice."))
    else:
        print("")
elif (b==3):
    pi=3.14
    r = float(input ("Input the radius of the circle : "))
    print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))
    print("----------More acurate version------------")
    radius= float(input ("Input the radius of the circle : "))
    area = np.pi *(radius**2)

    print("Area is",area)
    a2= input("Do you want to continue? Type Yes or No ")
    if (a2 =="Yes"):
        print("Here are the options.\n 1. What is PI 2.What is the value of PI  3. Area Calculator 4.Circumfrence Calculator 5.diameter calculator")
        b= int(input("Enter your choice. "))
    else:
        print("")
elif(b==4):
    r=int(input("Enter the radius:"))
    area=2*3.14*r
    print("circumference: {}".format(area))
    print("-----------More Acurate Version---------------")
    radius = float(input("Enter the radius of the circle : "))
    circumference = 2 * math.pi * radius
    print("Circumference of the circle is : %.2f" % circumference)
    a2= input("Do you want to continue? Type Yes or No ")
    if (a2 =="Yes"):
        print("Here are the options.\n 1. What is PI 2.What is the value of PI  3. Area Calculator 4.Circumfrence Calculator 5.diameter calculator")
        b= int(input("Enter your choice. "))
    else:
        print("")
if (b==1):
    print("The number π is a mathematical constant. It is defined as the ratio of a circle's circumference to its diameter, and it also has various equivalent definitions.Regardless of the circle's size, this ratio will always equal pi.Pi is an irrational number, meaning that its decimal form neither ends (like 1/4 = 0.25) nor becomes repetitive It appears in many formulas in all areas of mathematics and physics. It is approximately equal to 3.14159.")
    c=input("Do you want more info on PI. Type Yes or No. ")
    if c=="Yes":
        print("Pi has been known for nearly 4,000 years and was discovered by ancient Babylonians. A tablet from somewhere between 1900-1680 B.C. found pi to be 3.125. The ancient Egyptians were making similar discoveries, as evidenced by the Rhind Papyrus of 1650 B.C. In this document, the Egyptians calculated the area of a circle by a formula giving pi an approximate value of 3.1605! Pi began being symbolized by the pi symbol (π) in the 1706 by the British mathematician William Jones. Jones used 3.14159 as the calculation for pi.")
        a1= input("Do you want to continue? Type Yes or No ")
        if (a1 =="Yes"):
            print("Here are the options.\n 1. What is PI 2.What is the value of PI  3. Area Calculator 4.Circumfrence Calculator 5.diameter calculator ")
            b= int(input("Enter your choice."))
        else:
            print("")
    else:
        a2= input("Do you want to continue? Type Yes or No ")
        if (a2 =="Yes"):
            print("Here are the options.\n 1. What is PI 2.What is the value of PI  3. Area Calculator 4.Circumfrence Calculator 5.diameter calculator")
            b= int(input("Enter your choice. "))  
        else:
            print("")
elif (b==2):
    def pi():
        pi=0
        d=4
        e=1
        pppiii= int(input("Enter a value to estimate pi. The higher the number the more acurate it is but it may take a while to compute the final value. "))
        for i in range(1,pppiii):
            a= 2*(i % 2)-1
            pi += a*d/e
            e+=2
            print("Pi approx. is",pi)
        print("Rounded Value of pi value of pi is ",np.pi, math.pi)
    pi()
    Pi = 0.0
    for i in range(1, 10000000, 4):
        Pi += 4/i
        Pi -= 4/(i+2)
    print("Another approx. Value of pi",Pi)
    
    a2= input("Do you want to continue? Type Yes or No ")
    if (a2 =="Yes"):
        print("Here are the options.\n 1. What is PI 2.What is the value of PI  3. Area Calculator 4.Circumfrence Calculator 5.diameter calculator ")
        b= int(input("Enter your choice."))
    else:
        print("")
elif (b==3):
    pi=3.14
    r = float(input ("Input the radius of the circle : "))
    print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))
    print("----------More acurate version------------")
    radius= float(input ("Input the radius of the circle : "))
    area = np.pi *(radius**2)

    print("Area is",area)
    a2= input("Do you want to continue? Type Yes or No ")
    if (a2 =="Yes"):
        print("Here are the options.\n 1. What is PI 2.What is the value of PI  3. Area Calculator 4.Circumfrence Calculator 5.diameter calculator")
        b= int(input("Enter your choice. "))
    else:
        print("")
elif(b==4):
    r=int(input("Enter the radius:"))
    area=2*3.14*r
    print("circumference: {}".format(area))
    print("-----------More Acurate Version---------------")
    radius = float(input("Enter the radius of the circle : "))
    circumference = 2 * math.pi * radius
    print("Circumference of the circle is : %.2f" % circumference)
    a2= input("Do you want to continue? Type Yes or No ")
    if (a2 =="Yes"):
        print("Here are the options.\n 1. What is PI 2.What is the value of PI  3. Area Calculator 4.Circumfrence Calculator 5.diameter calculator")
        b= int(input("Enter your choice. "))
    else:
        print("")
else:
    r = int(input("Enter radius"))
    print(2*r)
    a2= input("Do you want to continue? Type Yes or No ")
    if (a2 =="Yes"):
        print("Here are the options.\n 1. What is PI 2.What is the value of PI  3. Area Calculator 4.Circumfrence Calculator 5.diameter calculator")
        b= int(input("Enter your choice. "))
    else:
        print("")



if (b==1):
    print("The number π is a mathematical constant. It is defined as the ratio of a circle's circumference to its diameter, and it also has various equivalent definitions.Regardless of the circle's size, this ratio will always equal pi.Pi is an irrational number, meaning that its decimal form neither ends (like 1/4 = 0.25) nor becomes repetitive It appears in many formulas in all areas of mathematics and physics. It is approximately equal to 3.14159.")
    c=input("Do you want more info on PI. Type Yes or No. ")
    if c=="Yes":
        print("Pi has been known for nearly 4,000 years and was discovered by ancient Babylonians. A tablet from somewhere between 1900-1680 B.C. found pi to be 3.125. The ancient Egyptians were making similar discoveries, as evidenced by the Rhind Papyrus of 1650 B.C. In this document, the Egyptians calculated the area of a circle by a formula giving pi an approximate value of 3.1605! Pi began being symbolized by the pi symbol (π) in the 1706 by the British mathematician William Jones. Jones used 3.14159 as the calculation for pi.")
        a1= input("Do you want to continue? Type Yes or No ")
        if (a1 =="Yes"):
            print("Here are the options.\n 1. What is PI 2.What is the value of PI  3. Area Calculator 4.Circumfrence Calculator 5.diameter calculator ")
            b= int(input("Enter your choice."))
        else:
            print("")
    else:
        a2= input("Do you want to continue? Type Yes or No ")
        if (a2 =="Yes"):
            print("Here are the options.\n 1. What is PI 2.What is the value of PI  3. Area Calculator 4.Circumfrence Calculator 5.diameter calculator")
            b= int(input("Enter your choice. "))  
        else:
            print("")
elif (b==2):
    def pi():
        pi=0
        d=4
        e=1
        pppiii= int(input("Enter a value to estimate pi. The higher the number the more acurate it is but it may take a while to compute the final value. "))
        for i in range(1,pppiii):
            a= 2*(i % 2)-1
            pi += a*d/e
            e+=2
            print("Pi approx. is",pi)
        print("Rounded Value of pi value of pi is ",np.pi, math.pi)
    pi()
    Pi = 0.0
    for i in range(1, 10000000, 4):
        Pi += 4/i
        Pi -= 4/(i+2)
    print("Another approx. Value of pi",Pi)
    
    a2= input("Do you want to continue? Type Yes or No ")
    if (a2 =="Yes"):
        print("Here are the options.\n 1. What is PI 2.What is the value of PI  3. Area Calculator 4.Circumfrence Calculator 5.diameter calculator ")
        b= int(input("Enter your choice."))
    else:
        print("")
elif (b==3):
    pi=3.14
    r = float(input ("Input the radius of the circle : "))
    print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))
    print("----------More acurate version------------")
    radius= float(input ("Input the radius of the circle : "))
    area = np.pi *(radius**2)

    print("Area is",area)
    a2= input("Do you want to continue? Type Yes or No ")
    if (a2 =="Yes"):
        print("Here are the options.\n 1. What is PI 2.What is the value of PI  3. Area Calculator 4.Circumfrence Calculator 5.diameter calculator")
        b= int(input("Enter your choice. "))
    else:
        print("")
elif(b==4):
    r=int(input("Enter the radius:"))
    area=2*3.14*r
    print("circumference: {}".format(area))
    print("-----------More Acurate Version---------------")
    radius = float(input("Enter the radius of the circle : "))
    circumference = 2 * math.pi * radius
    print("Circumference of the circle is : %.2f" % circumference)
    a2= input("Do you want to continue? Type Yes or No ")
    if (a2 =="Yes"):
        print("Here are the options.\n 1. What is PI 2.What is the value of PI  3. Area Calculator 4.Circumfrence Calculator 5.diameter calculator")
        b= int(input("Enter your choice. "))
    else:
        print("")
if (b==1):
    print("The number π is a mathematical constant. It is defined as the ratio of a circle's circumference to its diameter, and it also has various equivalent definitions.Regardless of the circle's size, this ratio will always equal pi.Pi is an irrational number, meaning that its decimal form neither ends (like 1/4 = 0.25) nor becomes repetitive It appears in many formulas in all areas of mathematics and physics. It is approximately equal to 3.14159.")
    c=input("Do you want more info on PI. Type Yes or No. ")
    if c=="Yes":
        print("Pi has been known for nearly 4,000 years and was discovered by ancient Babylonians. A tablet from somewhere between 1900-1680 B.C. found pi to be 3.125. The ancient Egyptians were making similar discoveries, as evidenced by the Rhind Papyrus of 1650 B.C. In this document, the Egyptians calculated the area of a circle by a formula giving pi an approximate value of 3.1605! Pi began being symbolized by the pi symbol (π) in the 1706 by the British mathematician William Jones. Jones used 3.14159 as the calculation for pi.")
        a1= input("Do you want to continue? Type Yes or No ")
        if (a1 =="Yes"):
            print("Here are the options.\n 1. What is PI 2.What is the value of PI  3. Area Calculator 4.Circumfrence Calculator 5.diameter calculator ")
            b= int(input("Enter your choice."))
        else:
            print("")
    else:
        a2= input("Do you want to continue? Type Yes or No ")
        if (a2 =="Yes"):
            print("Here are the options.\n 1. What is PI 2.What is the value of PI  3. Area Calculator 4.Circumfrence Calculator 5.diameter calculator")
            b= int(input("Enter your choice. "))  
        else:
            print("")
elif (b==2):
    def pi():
        pi=0
        d=4
        e=1
        pppiii= int(input("Enter a value to estimate pi. The higher the number the more acurate it is but it may take a while to compute the final value. "))
        for i in range(1,pppiii):
            a= 2*(i % 2)-1
            pi += a*d/e
            e+=2
            print("Pi approx. is",pi)
        print("Rounded Value of pi value of pi is ",np.pi, math.pi)
    pi()
    Pi = 0.0
    for i in range(1, 10000000, 4):
        Pi += 4/i
        Pi -= 4/(i+2)
    print("Another approx. Value of pi",Pi)
    
    a2= input("Do you want to continue? Type Yes or No ")
    if (a2 =="Yes"):
        print("Here are the options.\n 1. What is PI 2.What is the value of PI  3. Area Calculator 4.Circumfrence Calculator 5.diameter calculator ")
        b= int(input("Enter your choice."))
    else:
        print("")
elif (b==3):
    pi=3.14
    r = float(input ("Input the radius of the circle : "))
    print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))
    print("----------More acurate version------------")
    radius= float(input ("Input the radius of the circle : "))
    area = np.pi *(radius**2)

    print("Area is",area)
    a2= input("Do you want to continue? Type Yes or No ")
    if (a2 =="Yes"):
        print("Here are the options.\n 1. What is PI 2.What is the value of PI  3. Area Calculator 4.Circumfrence Calculator 5.diameter calculator")
        b= int(input("Enter your choice. "))
    else:
        print("")
elif(b==4):
    r=int(input("Enter the radius:"))
    area=2*3.14*r
    print("circumference: {}".format(area))
    print("-----------More Acurate Version---------------")
    radius = float(input("Enter the radius of the circle : "))
    circumference = 2 * math.pi * radius
    print("Circumference of the circle is : %.2f" % circumference)
    a2= input("Do you want to continue? Type Yes or No ")
    if (a2 =="Yes"):
        print("Here are the options.\n 1. What is PI 2.What is the value of PI  3. Area Calculator 4.Circumfrence Calculator 5.diameter calculator")
        b= int(input("Enter your choice. "))
    else:
        print("")
else:
    r = int(input("Enter radius"))
    print(2*r)
    a2= input("Do you want to continue? Type Yes or No ")
    if (a2 =="Yes"):
        print("Here are the options.\n 1. What is PI 2.What is the value of PI  3. Area Calculator 4.Circumfrence Calculator 5.diameter calculator")
        b= int(input("Enter your choice. "))
    else:
        print("")
if (b==1):
    print("The number π is a mathematical constant. It is defined as the ratio of a circle's circumference to its diameter, and it also has various equivalent definitions.Regardless of the circle's size, this ratio will always equal pi.Pi is an irrational number, meaning that its decimal form neither ends (like 1/4 = 0.25) nor becomes repetitive It appears in many formulas in all areas of mathematics and physics. It is approximately equal to 3.14159.")
    c=input("Do you want more info on PI. Type Yes or No. ")
    if c=="Yes":
        print("Pi has been known for nearly 4,000 years and was discovered by ancient Babylonians. A tablet from somewhere between 1900-1680 B.C. found pi to be 3.125. The ancient Egyptians were making similar discoveries, as evidenced by the Rhind Papyrus of 1650 B.C. In this document, the Egyptians calculated the area of a circle by a formula giving pi an approximate value of 3.1605! Pi began being symbolized by the pi symbol (π) in the 1706 by the British mathematician William Jones. Jones used 3.14159 as the calculation for pi.")
        a1= input("Do you want to continue? Type Yes or No ")
        if (a1 =="Yes"):
            print("Here are the options.\n 1. What is PI 2.What is the value of PI  3. Area Calculator 4.Circumfrence Calculator 5.diameter calculator ")
            b= int(input("Enter your choice."))
        else:
            print("")
    else:
        a2= input("Do you want to continue? Type Yes or No ")
        if (a2 =="Yes"):
            print("Here are the options.\n 1. What is PI 2.What is the value of PI  3. Area Calculator 4.Circumfrence Calculator 5.diameter calculator")
            b= int(input("Enter your choice. "))  
        else:
            print("")
elif (b==2):
    def pi():
        pi=0
        d=4
        e=1
        pppiii= int(input("Enter a value to estimate pi. The higher the number the more acurate it is but it may take a while to compute the final value. "))
        for i in range(1,pppiii):
            a= 2*(i % 2)-1
            pi += a*d/e
            e+=2
            print("Pi approx. is",pi)
        print("Rounded Value of pi value of pi is ",np.pi, math.pi)
    pi()
    Pi = 0.0
    for i in range(1, 10000000, 4):
        Pi += 4/i
        Pi -= 4/(i+2)
    print("Another approx. Value of pi",Pi)
    
    a2= input("Do you want to continue? Type Yes or No ")
    if (a2 =="Yes"):
        print("Here are the options.\n 1. What is PI 2.What is the value of PI  3. Area Calculator 4.Circumfrence Calculator 5.diameter calculator ")
        b= int(input("Enter your choice."))
    else:
        print("")
elif (b==3):
    pi=3.14
    r = float(input ("Input the radius of the circle : "))
    print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))
    print("----------More acurate version------------")
    radius= float(input ("Input the radius of the circle : "))
    area = np.pi *(radius**2)

    print("Area is",area)
    a2= input("Do you want to continue? Type Yes or No ")
    if (a2 =="Yes"):
        print("Here are the options.\n 1. What is PI 2.What is the value of PI  3. Area Calculator 4.Circumfrence Calculator 5.diameter calculator")
        b= int(input("Enter your choice. "))
    else:
        print("")
elif(b==4):
    r=int(input("Enter the radius:"))
    area=2*3.14*r
    print("circumference: {}".format(area))
    print("-----------More Acurate Version---------------")
    radius = float(input("Enter the radius of the circle : "))
    circumference = 2 * math.pi * radius
    print("Circumference of the circle is : %.2f" % circumference)
    a2= input("Do you want to continue? Type Yes or No ")
    if (a2 =="Yes"):
        print("Here are the options.\n 1. What is PI 2.What is the value of PI  3. Area Calculator 4.Circumfrence Calculator 5.diameter calculator")
        b= int(input("Enter your choice. "))
    else:
        print("")
else:
    r = int(input("Enter radius"))
    print(2*r)
    a2= input("Do you want to continue? Type Yes or No ")
    if (a2 =="Yes"):
        print("Here are the options.\n 1. What is PI 2.What is the value of PI  3. Area Calculator 4.Circumfrence Calculator 5.diameter calculator")
        b= int(input("Enter your choice. "))
    else:
        print("")
        