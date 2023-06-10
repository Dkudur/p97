def leapyear(year1):
    if year1%4 == 0:
        if year1%100 != 0:  
        
            if year1%400 != 0:
                print("The given year is a leap year")
            else:
                print("The given year is not a leap year")
        else:   
            print("The given year is not a leap year")
    else:
        print("The given year is not a leap year")
    


chosenyear = int(input("Enter a year that you wanna check if its a leap year or not: "))

leapyear(chosenyear)