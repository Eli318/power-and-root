# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 13:57:11 2021

@author: Eliezer
"""


def exponent (x:float) -> float:
    i = 0
    prev_result = 0
    result = 1
    numerator = 1
    denominator = 1
    
    while prev_result != result:

        numerator = numerator * x
        denominator = denominator * (i+1)
                    
        prev_result = result
        result += (numerator / denominator)
        i+=1
        
    return(result)



def ln (x:float) -> float:
    if x <= 0:
        return 0
    else:
        result = 0
        prev_result = 1
        i = 0
        while prev_result != result and i  < 1000000:
            prev_result = result
            result = result - 1 + ( x / exponent(result))
            i+=1
        return result
 
   
 
def XtimesY (x:float, y:float) -> float:
    if x <= 0: 
        return 0
    result = exponent( y * ln(x))
    result = float('%0.6f' % result)
    return result



def sqrt (x:float, y:float) -> float:
    if x == 0:
        return 0
    else:
        result = XtimesY(y, 1/x)
        return result



def calculate(x:float) -> float:
    result = exponent(x) * XtimesY(7, x) * XtimesY(x, -1) * sqrt(x, x)
    result = float('%0.6f' % result)
    return result

