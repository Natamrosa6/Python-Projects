hora_del_dia = int(input("Ingrese la hora actual (en formato 24 horas): "))

if hora_del_dia <6 or hora_del_dia > 22:
    print(f"Son las {hora_del_dia} hora de descansar")
elif hora_del_dia < 12:
    print(f"Son las {hora_del_dia} buen día!")
elif hora_del_dia < 18:
    print(f"Siendo las {hora_del_dia} deberías estar currando o buscando curro. Pero no haciendo lo que estás haciendo")
else:
    print("A disfrutar del ocio sin culpa!")


