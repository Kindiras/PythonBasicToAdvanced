from math import pi

def circleArea(r):
    try:
        if r < 0:
            raise ValueError("radius should be positive numbers")
        
        if type(r) in [int, float]:
            return pi*(r**2) 

    except TypeError as err:
        print("radius should be integers or float",err)
        return err
    
if __name__ == '__main__':
    radii = [2,0,-3,2+3j,True]
    for r in radii:
        A = circleArea(r)
        print(f'areaa of circle of {r} is {A}')    