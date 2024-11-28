import json

datos= {}
datos['medicos'] = []

#Para guardad datossssssssssssssssssssss!!
def guardarjson():
    with open("consultas.json", "w", encoding = "utf-8") as f:
        json.dump(datos, f, indent = 4, ensure_ascii = False)
    print("Datos guardados")


def loadjson():
    global datos
    try: 
        with open("consultas.json", "r", encoding="utf-8") as f:
            datos = json.load(f)
    except ValueError:
        print("No se encontró el archivo. Se creará un nuevo al guardar.")

def pedir_entrada_int(mensaje, mensaje_error="Entrada inválida. Intenta de nuevo."):
    """Función para pedir un número entero con validación"""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print(mensaje_error)

def pedir_entrada_float(mensaje, mensaje_error="Entrada inválida. Intenta de nuevo."):
    """Función para pedir un número decimal con validación"""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print(mensaje_error)

def pedir_entrada_string(mensaje, mensaje_error="Entrada inválida. Intenta de nuevo."):
    """Función para pedir una cadena de texto"""
    while True:
        entrada = input(mensaje).strip()
        if entrada:
            return entrada
        else:
            print(mensaje_error)

def agregar_paciente():
    """Función para pedir los datos de un paciente y devolverlos en un diccionario"""
    paciente = {}
    paciente['nombre'] = pedir_entrada_string("Ingresa el nombre de la mascota: ")
    paciente['edad'] = pedir_entrada_int("Edad: ")
    paciente['especie'] = pedir_entrada_string("Especie: ")
    paciente['sexo'] = pedir_entrada_string("Sexo: ")
    paciente['peso'] = pedir_entrada_float("Peso: ")
    paciente['diagnostico'] = pedir_entrada_string("Diagnóstico: ")
    return paciente

def agregar_nombre():
    """Función para agregar un nuevo médico y su paciente al sistema"""
    medico = {}
    medico['nombre'] = pedir_entrada_string("Ingrese el nombre del médico veterinario: ")
    medico['pacientes'] = []

    # Llamar a la función que agrega un paciente
    paciente = agregar_paciente()

    # Agregar paciente al médico
    medico['pacientes'].append(paciente)
    
    # Guardar los datos
    datos['medicos'].append(medico)
    guardarjson()
    print("Paciente agregado al sistema.")

def buscar_nombre_paciente():
    # Verifica si hay médicos registrados
    if not datos['medicos']:
        print(f"No hay médicos registrados {datos['medicos']}")
    
    criterio = input("Ingresa el nombre del paciente a buscar: ").lower()
    resultados = []  # Lista para almacenar los pacientes encontrados

    # Itera sobre los médicos
    for medico in datos['medicos']:
        # Verifica si el médico tiene pacientes
        if 'pacientes' in medico and medico['pacientes']:
            # Itera sobre los pacientes de ese médico
            for paciente in medico['pacientes']:
                # Verifica si el nombre del paciente coincide con el criterio
                if criterio in paciente['nombre'].lower():
                    resultados.append(paciente)

    # Mostrar los resultados
    if resultados:
        print("Paciente(s) encontrado(s): ")
        for paciente in resultados:
            print(f"- {paciente['nombre']} (Edad: {paciente['edad']}, Especie: {paciente['especie']}, Sexo: {paciente['sexo']}, Peso: {paciente['peso']}, Diagnóstico: {paciente['diagnostico']})")
    else:
        print("Paciente no encontrado")

def borrar_pacientes():
    # Verifica si hay médicos registrados
    if not datos['medicos']:
        print("No hay médicos registrados")
        return

    nombre = input("Ingrese el nombre del paciente que desea eliminar: ").lower()
    registro_eliminado = False  

    # Itera sobre los médicos
    for medico in datos['medicos']:
        # Verifica si el médico tiene pacientes
        if 'pacientes' in medico and medico['pacientes']:
            # Recorre los pacientes de ese médico
            for i, paciente in enumerate(medico['pacientes']):
                if paciente['nombre'].lower() == nombre:
                    print(f"Eliminado: {paciente['nombre']}") 
                    # Elimina el paciente usando pop() en el índice i
                    medico['pacientes'].pop(i)
                    guardarjson()  # Guarda después de eliminar
                    print("Registro de paciente eliminado")
                    registro_eliminado = True
                    return  # Salimos de la función después de eliminar un paciente

    # Si no se encontró el paciente
    if not registro_eliminado:
        print("No se encontró registro con ese nombre")

def principal_consultas():
    while True:
        try:
            print("""
                    Selecciona
                    1. Añadir registro de pacientes
                    2. Buscar registro de pacientes
                    3. Eliminar registro de pacientes
                    4. Salir del programa

            """)
            op = int(input("Ingrese una opción del Menú: "))

            if op == 1:
                print("Registro Nuevo")
                agregar_nombre()
            elif op == 2:
                print("Buscar registro")
                buscar_nombre_paciente()
            elif op == 3:
                print("Eliminar registro")
                borrar_pacientes()
            elif op == 4:
                print("Guardando y saliendo ...")
                guardarjson()
                break
        except ValueError:
            print("Opción inválida")
