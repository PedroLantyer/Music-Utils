import math

def getCents(f_1: float, f_2: float):
    try:
        if(type(f_1) != int and type(f_1) != float ) or (type(f_2) != int and type(f_2) != float):
            raise TypeError("Frequency Values must be integers or floats")
        
        ratio = f_2 / f_1
        cents = 1200 * math.log2(ratio) #The distance between each octave is 1200 cents
        return cents
    
    except Exception as err:
        print(err)
        return None
    
def getAdjustedFrequency(f_1: float, cents: float):
    # cents = 1200 * math.log2(ratio)
    # (cents/1200) = math.log2(f_2) - math.log2(f_1)

    try:
        if(type(f_1) != float and type(f_1) != int):
            raise TypeError("Frequency value must be integer or float")
        if(type(cents) != float and type(cents) != int):
            raise TypeError("cents value must be integer or float")

        deltaLogs = (cents/1200.0) #Difference between the Log2(f_2) and Log2(f_1)
        log_of_f_2 = deltaLogs + math.log2(f_1)
        f_2 = pow(2, log_of_f_2)
        return f_2
        
    except Exception as err:
        print(err)
        return None