estudianteusuario = { 
    "Nombre": "Pepito",
    "Id": 12,
    "Calculo": 25,
    "Física": 30,
    "Inglés": 14,
    "Química": 50   
}
estudiante1 = {
    "Nombre": "Camila",
    "Id": 13,
    "Calculo": 40,
    "Física": 45,
    "Inglés": 30,
    "Química": 50 
}
estudiante2 = {
    "Nombre": "Pablito",
    "Id": 15,
    "Calculo": 40,
    "Física": 30,
    "Inglés": 14,
    "Química": 50 
}

x = True

while x:   
    print("1. Desea registrar un estudiante") 
    print("2. Desea asignar calificaciones al estudiante")
    print("3. Desea ver el promedio del estudiante")
    print("4. Mostrar estudiantes reprobados y aprobados")
    print("5. Consultar estudiantes y materias registradas")
    print("Para salir digite 0")
  
    try:
        menu = int(input("Seleccione una opción: "))
    except ValueError:
        print("Error")
        continue

    if menu == 1:
        estudianteusuario["Nombre"] = input("Por favor escriba el nombre del estudiante: ")
        try:
            estudianteusuario["Id"] = int(input("Digite el código del estudiante: "))
        except ValueError:
            print("Error")
            continue
        
        t = input()

    elif menu == 2:
        estudianteusuario["Calculo"] = float(input("Registre su nota definitiva de cálculo: "))
        estudianteusuario["Física"] = float(input("Registre su nota definitiva de física: "))
        estudianteusuario["Inglés"] = float(input("Registre su nota definitiva de inglés: "))
        estudianteusuario["Química"] = float(input("Registre su nota definitiva de química: "))

        t = input()
    elif menu == 3:
        while True:
            try:
                menu2 = int(input(f"\n¿El promedio de cuál estudiante desea ver (1) {estudiante2['Nombre']}, (2) {estudiante1['Nombre']}, (3) {estudianteusuario['Nombre']}, (0) salir: "))
            except ValueError:
                print("Error")
                continue

            if menu2 == 1:
                prom = (estudiante2["Calculo"] + estudiante2["Física"] + estudiante2["Inglés"] + estudiante2["Química"]) / 4
                print(f"El promedio del estudiante Pablito es: {prom}")
                t = input()
            elif menu2 == 2:
                prom = (estudiante1["Calculo"] + estudiante1["Física"] + estudiante1["Inglés"] + estudiante1["Química"]) / 4
                print(f"El promedio de la estudiante Camila es: {prom}")
                t = input()
            elif menu2 == 3:
                prom = (estudianteusuario["Calculo"] + estudianteusuario["Física"] + estudianteusuario["Inglés"] + estudianteusuario["Química"]) / 4
                print(f"El promedio del estudiante Pepito es: {prom}")
                t = input()
            elif menu2 == 0:
                break
        t = input()      

    elif menu == 4:
        prom1 = (estudiante2["Calculo"] + estudiante2["Física"] + estudiante2["Inglés"] + estudiante2["Química"]) / 4
        prom2 = (estudiante1["Calculo"] + estudiante1["Física"] + estudiante1["Inglés"] + estudiante1["Química"]) / 4
        prom3 = (estudianteusuario["Calculo"] + estudianteusuario["Física"] + estudianteusuario["Inglés"] + estudianteusuario["Química"]) / 4
        #print("\nAprobados: Pablito y Camila. Reprobados: Pepito")
        print("\nAprobados: ")
        if prom1 >= 30:
            print(estudiante2["Nombre"])
        if prom2 >= 30:
            print(estudiante1["Nombre"])
        if prom3 >= 30:
            print(estudianteusuario["Nombre"])
        print("\nReprovados: ")
        if prom1 < 30:
            print(estudiante2["Nombre"])
        if prom2 < 30:
            print(estudiante1["Nombre"])
        if prom3 < 30:
            print(estudianteusuario["Nombre"])
        t = input()
    elif menu == 5:
        print("Los estudiantes con sus materias son: ")
        print("\nEl primer estudiante: ")
        for x, y in estudianteusuario.items():
            print(x, y)
        print("\nEl segundo estudiante: ")
        for x, y in estudiante1.items():
            print(x, y)
        print("\nEl tercer estudiante: ")
        for x, y in estudiante2.items():
            print(x, y)
        t = input()
    elif menu == 0:
        x = False
