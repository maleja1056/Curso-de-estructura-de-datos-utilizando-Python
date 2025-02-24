
estudianteusuario= { 
    "nombre": "Pepito",
    "id": 12,
    "calculo":25,
    "fisica":30,
    "ingles":14,
    "quimica":50   
}
estudiante1 = {
      "nombre":"Camila",
      "calculo": 40
    }
    
x = True
print(x)
print(estudianteusuario)
while x:   
    print("1. Desea registrar un estudiante ") 
    print("2. Desea asignar calificaciones al estudiante")
    print("3. Desea ver el promedio del estudiante")
    print("4. Mostrar estudiantes reporbados y aprovados")
    print("5. Consultar estudiantes y materias registadas")
    print("Para salir digite 0")
    menu = int(input("Por favor seleccione alguna de las partes del menu: "))
    
    if menu == 1:
        estudianteusuario["nombre"] = input("Por favor escriba el nombre del estudiante: ")
        estudianteusuario["id"] = int(input("digite el codigo del estudiante"))

    elif menu ==2:
        estudianteusuario["calculo"] = float(input("Registre su nota definitiva de calculo: "))
        estudianteusuario["fisica"] = float(input("Registre su nota definitiva de fisica: "))
        estudianteusuario["ingles"] = float(input("Registre su nota definitiva de ingles: "))
        estudianteusuario["quimica"] = float(input("Registre su nota definitiva de quimica: "))
    elif menu ==3:
            print("hola")
    elif menu ==4:
            print("hola")
    elif menu ==5:
            print("hola")
    else:
        x = False           
   