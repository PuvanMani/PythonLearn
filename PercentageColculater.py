choice='y'
while choice=='y':
    try:
        print("\n---------> Toatal And Avarage Colculator <---------\n")
        sub=int(float(input("How Many Subject You Have :")))
        total=0
        avg=0
        while choice=='y':
            try:
                for mark in range(sub):
                    marks=float(input("Enter Your Mark :"))
                    total+=marks
                avg=total//sub
                print("Your Total Mark is :",int(total))
                print("Your Avarage is :",int(avg),"%")
                choice=input("""\nEnter Your Choice,Type Y or N
                         Y is Yes Try Again, N is No Exit This Process :""").lower()
            except:
                print("\nCheck Your Input,Enter Your Mark In Number")
                choice=input("""\nEnter Your Choice,Type Y or N
                         Y is Yes Try Again, N is No Exit This Process :""").lower()
    except:
        print("\nCheck Your Input,Enter Your Subject Count In Number\n")
        choice=input("""\nEnter Your Choice,Type Y or N
                     Y is Yes Try Again, N is No Exit This Process :""").lower()
else:
    print("Exited...")
