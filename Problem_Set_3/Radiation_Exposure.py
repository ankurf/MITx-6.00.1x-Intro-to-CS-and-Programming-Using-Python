##https://courses.edx.org/courses/course-v1:MITx+6.00.1x_8+1T2016/courseware/sp13_Week_3/sp13_Problem_Set_3/
##
##Radiation Exposure

def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)
def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
      between start and stop times.
    '''
    r=(stop-start)/step
    total_area=0
    for i in range(int(r)):
        area=f(start+(i*step))*step
        total_area+=area
    return total_area
