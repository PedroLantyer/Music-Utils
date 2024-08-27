def getStringTension(frequency: float, scaleLength: float, stringLinearDensity: float):
    try:
        if(type(frequency) != float and type(frequency) != int):
            raise TypeError("Frequency value must be float or integer")
        if(type(scaleLength) != float and type(scaleLength) != int):
            raise TypeError("Scale Length must be float or integer")
        if(type(stringLinearDensity) != float and type(stringLinearDensity) != int):
            raise TypeError("String Linear Density must be float or integer")

        G = 9.81
        INCH_MOD = 39.3701
        tension = pow((frequency * 2 * scaleLength), 2) * (stringLinearDensity/(G*INCH_MOD))
        return tension

    except Exception as err:
        print(err)
        return None