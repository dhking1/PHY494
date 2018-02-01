# Heaviside step function

def heaviside(x):
   """Heaviside step function

   Arguments
   ---------
   x = float
        input value

    Returns
   ---------
   Theta : float
   value of heaviside

   """

   theta = None
   if x < 0:
      theta = 0.
   elif x == 0:
      theta = 0.5
   else:
      theta = 1.

   return theta

   x = 3
   theta = heaviside(x)
   print("heaviside", str(x), "|:", str(theta))
