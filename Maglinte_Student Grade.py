#Variables-------------------------------------------
Name=input("Name: ")
Section=input("Section: ")
Prelim_Grade=float(input("Prelim Grade: "))
if Prelim_Grade < 40 or Prelim_Grade > 100:
    print("Invalid Output, Must be between in the range of 40-100")
    exit ()
Midterm_Grade=float(input("Midterm Grade: "))
if Midterm_Grade < 40 or Prelim_Grade > 100:
    print("Invalid Output, Must be between in the range of 40-100")
    exit ()
Final_Grade=float(input("Final grade: "))
if Final_Grade < 40 or Prelim_Grade > 100:
    print("Invalid Output, Must be between in the range of 40-100")
    exit ()
#---------------------------------------------------
#Grade Computation----------------------------------
Student_Grade = (Prelim_Grade * .3333) + (Midterm_Grade * .3333) + (Final_Grade * .3333)
print(f"Total Grade for this Semester: {Student_Grade:.0f}")
#---------------------------------------------------
#GPA------------------------------------------------
if Student_Grade > 99 and Student_Grade < 100:
    print ("Your GPA is 1.00, Excellent!")
elif Student_Grade > 96 and Student_Grade < 98:  
    print ("Your GPA is 1.25, Outstanding!")
elif Student_Grade > 93 and Student_Grade < 95:  
    print ("Your GPA is 1.50, Superior!")
elif Student_Grade > 90 and Student_Grade < 92:  
    print ("Your GPA is 1.75, Very Good!")
elif Student_Grade > 87 and Student_Grade < 89:  
    print ("Your GPA is 2.00, Good!")
elif Student_Grade > 84 and Student_Grade < 86:  
    print ("Your GPA is 2.25, Satisfactory!")        
elif Student_Grade > 81 and Student_Grade < 83:  
    print ("Your GPA is 2.50, Fairly Satisfactory!")
elif Student_Grade > 78 and Student_Grade < 80:  
    print ("Your GPA is 2.75, Fair!")
elif Student_Grade > 75 and Student_Grade < 77:  
    print ("Your GPA is 3.00, Passed!")
elif Student_Grade < 75 :  
    print ("Your GPA is 5.00, Failed!")
#---------------------------------------------------