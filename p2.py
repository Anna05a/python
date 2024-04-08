def distance(x, y):
  return ((x**2) + (y**2))**0.5

def Closer(x1, y1, x2, y2):
  
  distance_to_a = distance(x1, y1)
  distance_to_b = distance(x2, y2)

  if distance_to_a < distance_to_b:
    return "Точка A ближче до початку координат."
  elif distance_to_a > distance_to_b:
    return "Точка B ближче до початку координат."
  else:
    return "Точки A і B знаходяться на однаковій відстані від початку координат."

x1 = float(input("Координата x точки A: "))
y1 = float(input("Координата y точки A: "))
x2 = float(input("Координата x точки B: "))
y2 = float(input("Координата y точки B: "))

result = Closer(x1, y1, x2, y2)

print(result)