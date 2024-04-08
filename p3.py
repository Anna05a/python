def Trucutnuk(Cut1, Cut2):
  
  if Cut1 <= 0 or Cut1 >= 180:
    return False
  if Cut2 <= 0 or Cut2 >= 180:
    return False
  if Cut1 + Cut2 >= 180:
    return False
  return True

def RightTruc(Cut1, Cut2):

  return Cut1 + Cut2 == 90

Cut1 = float(input("Величина першого кута: "))
Cut2 = float(input("Величина другого кута: "))

if not Trucutnuk(Cut1, Cut2):
  print("Два введених кута не можуть бути кутами трикутника.")

if  RightTruc(Cut1, Cut2):
  print("Трикутник з даними кутами є прямокутним.")
else:
  print("Трикутник з даними кутами не є прямокутним.")