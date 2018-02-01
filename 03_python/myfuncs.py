def fahrenheit2kelvin(theta):
    """fahrenheit2kelvin"""
    T = (theta - 32) * (5/9) + 273.15
    return(T)

def kelvin2celsius(kelvin):
    T = kelvin - 273.15
    return(T)

def heaviside(x):
   """Heaviside step function"""

   theta = None
   if x < 0:
      theta = 0.
   elif x == 0:
      theta = 0.5
   else:
      theta = 1.

   return theta
