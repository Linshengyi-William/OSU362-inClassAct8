#partial code adapted from:https://www.javatpoint.com/python-check-leap-year
year = int(input("Enter a year: "))  
if (999 < year <= 10000):
    if (year % 4) == 0:  
        if (year % 100) == 0:  
            if (year % 400) == 0:  
                print(year,"is a leap year")  
            else:  
                print(year,"is not a leap year")  
        else:  
            print(year,"is a leap year")  
    else:  
        print(year,"is not a leap year") 
else:
    print("Invlid year, entered year should be a four digit number.")