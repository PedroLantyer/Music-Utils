import math

def frequencyAdjust(reference:float, semitones:int):
    try:
        if(type(reference) != float and type(reference) != int):
            raise TypeError("Reference frequency value must be integer or float")
        if(type(semitones) != int):
            raise TypeError("Semitone count must be integer")
        
        f_2 = reference * pow(2, (semitones/12))
        return f_2
    
    except Exception as err:
        print(err)
        return None
    
def getSemitoneDelta(f_1, f_2):
    #f_2 = f_1 * pow(2, (semitones/12))
        #f_2/f_1 = pow(2, (semitones/12))
        #f_2/f_1 = pow(2, semitones) ** (1/12)
        #2 ** semitones = (f_2/f_1) ** 12

    try:
        if(type(f_1) != float and type(f_1) != int) or (type(f_2) != float and type(f_2) != int):
            raise TypeError("Frequency values must be integers or floats")
        
        ratio = f_2/f_1
        b = pow(ratio, 12)
        a = 2
        semitoneDelta = math.log(b, a)
        return semitoneDelta    
    
    except Exception as err:
        print(err)
        return None