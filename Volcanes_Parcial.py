def registrar():
    while True:
        nombre=input('Ingrese Nombre del Volcán: ')
        if nombre.isalpha():
            break
        else:
            print('Sólo Letras')
    while True:
        pais=input('Ingrese Nombre del País: ') 
        if pais.isalpha():
            break
        else:
            print('Sólo Letras')
   
    altura=int(input('Ingrese Altura del Volcán: '))  
    agno=int(input('Ingrese Año Última Erupción: '))   
    volcanes[nombre]=[pais,altura,agno]  

def buscar():
    nombre=input('Ingrese Nombre del Volcán: ')
    if nombre in volcanes:
        pais,altura,agno=volcanes[nombre]
        print('Pais: ',pais)
        print('Altura: ',altura)
        print('Año: ',agno)
    else:
        print('Volcán NO Encontrado')

def eliminar():
    nombre=input('Ingrese Nombre del Volcán: ')
    if nombre in volcanes:
 #       print(volcanes.pop(nombre))
        del volcanes[nombre]
        print('Volcán Eliminado Exitosamente!!!!!')
    else:
        print('Volcán NO Encontrado')

def actualizar():
    nombre=input('Ingrese Nombre del Volcán: ')
    if nombre in volcanes:
        pais,altura,agno=volcanes[nombre]
        print('Pais: ',pais)
        print('Altura: ',altura)
        print('Año: ',agno)
        print('===============================')
        pais=input('Ingrese Nombre del País: ') 
        altura=int(input('Ingrese Altura del Volcán: '))  
        agno=int(input('Ingrese Año Última Erupción: '))   
        volcanes[nombre]=pais,altura,agno
    else:
        print('Volcán NO Encontrado')

def mostrar():    
    print('Volcán           País   Altura   Año')
    for clave,valor in volcanes.items():
        print(f'{clave}           {valor[0]}    {valor[1]}     {valor[2]}')  

# Programa Principal

volcanes = {
    "Villarrica": ["Chile", 2847, 2020],
    "Llaima": ["Chile", 3125, 2009],
    "Osorno": ["Chile", 2652, 1835],
    "Calbuco": ["Chile", 2015, 2015],
    "Nevados de Chillán": ["Chile", 3212, 2022]
}

while True:
    print('Menú Principal')
    print('''
        1. Registrar volcán
        2. Buscar volcán
        3. Actualizar volcán
        4. Eliminar volcán
        5. Mostrar todos los volcanes
        6. Salir
    ''')
    opc=input('Ingrese Opción: ')
    if opc=='1':
        registrar()
    elif opc=='2':
        buscar()
    elif opc=='3':
        actualizar()
    elif opc=='4':
        eliminar()
    elif opc=='5':
        mostrar()
    elif opc=='6':
        print('Ha salido exitosamente del programa.') #salida
        break
    else:
        print('Opción Invalida')