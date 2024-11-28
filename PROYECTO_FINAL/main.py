import json
import consultas
import peluqueria

def principal():
    sw = True
    while True:
        try:
            print("""
                    Seleccionar 
                    1. Añadir Consulta Veterinaria
                    2. Añadir Servicio de Peluquería
                    3. Salir del programa
            """)
            op = int(input("Ingrese una opcion: "))
            if op == 1:
                consultas.principal_consultas()
            elif op == 2:
                peluqueria.principal_peluqueria()
            elif op == 3:
                sw = False
                print("Programa Terminando")
        except ValueError:
            print("Debes ingresar una opción válida")
        
        break

if __name__ == '__main__':
    principal()