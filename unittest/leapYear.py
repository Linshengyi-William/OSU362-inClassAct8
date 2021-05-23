#partial code adapted from:https://www.javatpoint.com/python-check-leap-year
def isLeapYear(year):
    if (999 < year <= 10000):
        if (year % 4) == 0:  
            if (year % 100) == 0:  
                if (year % 400) == 0:  
                    return True
                    #print(year,"is a leap year")  
                else:  
                    return False
                    #print(year,"is not a leap year")  
            else:  
                return True
                #print(year,"is a leap year")  
        else: 
            return False 
            #print(year,"is not a leap year") 
    else:
        return False
        #print("Invlid year, entered year should be a four digit number.")