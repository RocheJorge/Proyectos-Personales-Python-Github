"""
Crear un programa que a traves de funciones se pueda apreciar una lista o un menu de opciones, donde cada opcion debe ser una funcion distinta de acuerdo a lo que seleccione el usuario. Cada cliente debe contener la informacion de su nombre, apellido o DNI y el menu o las funciones de cada seccion son las siguientes:

1. Agregar nuevo cliente
2. Mostrar todos los clientes
3. Mostrar cliente por DNI
4. Eliminar cliente
5. Salir

Realizado por Jorge Roche
"""
#####Inicio del Programa#####

#inicializamos la variable lista vacia

listaClientes = []

#inicializamos las variables listas pararelas vacias

almacenarNombre = []
almacenarApellido = []
almacenarDni = []

#####Definimos las Funciones#####

#####Entrada de la Funcion agregarCliente#####

def agregarCliente(listaClientes):
    
    print("\nAgregar Nuevo Cliente\n")
    
    nombreCliente = input("Ingrese el Nombre del Cliente: ")
    almacenarNombre.append(nombreCliente)
    print()
    
    apellidoCliente = input("Ingrese el Apellido del Cliente: ")
    almacenarApellido.append(apellidoCliente)
    print()
    
    cedulaCliente = input("Ingrese el DNI del Cliente: ")
    almacenarDni.append(cedulaCliente)
    print()
    
    #####agregamos los usuarios a la listaClientes
    
    almacenarClientes = ["Nombre: ", nombreCliente, "Apellido: ", apellidoCliente, "Cedula: ", cedulaCliente]
    
    listaClientes.extend(almacenarClientes) #se agregaran a listaClientes[]

    opcionCliente = input("¿Desea Agregar Otro Cliente?: Si(s) o No(n): ")
    opcionCliente = opcionCliente.lower()
    
    #####Entrada del Ciclo While de agregarCliente#####
    
    while opcionCliente == "s" or opcionCliente == "si":
        
        print("\nAgregar Nuevo Cliente\n")
        
        nombreCliente = input("Ingrese el Nombre del Cliente: ")
        almacenarNombre.append(nombreCliente)
        print()
        
        apellidoCliente = input("Ingrese el Apellido del Cliente: ")
        almacenarApellido.append(apellidoCliente)
        print()
        
        cedulaCliente = input("Ingrese el DNI del Cliente: ")
        almacenarDni.append(cedulaCliente)
        print()
        
        almacenarClientes = ["Nombre: ", nombreCliente, "Apellido: ", apellidoCliente, "Cedula: ", cedulaCliente]
        
        listaClientes.extend(almacenarClientes)
        
        opcionCliente = input("¿Desea Agregar Otro Cliente?: Si(s) o No(n): ")
        opcionCliente = opcionCliente.lower()
        print()
        
    else:
        
        print("\nClientes Agregados.....\n")
        print()
        
        input("Presione Enter para continuar.......")
        print()
    
    #return listaClientes #retorna la listaClientes
     
    #####Salida del Ciclo While de agregarCliente#####
            
#####Salida de la Funcion agregarCliente#####

#####Entrada de la Funcion mostrarCliente#####

def mostrarCliente(listaClientes):
    
    if len(listaClientes) > 0: #si no hay clientes agregados marcara error
        
        for i in range(len(listaClientes)):
        
            print(listaClientes[i])
    
    else:
        
        print("No se encuentran clientes registrados")
    
    input("\nPresione una Tecla para Continuar......")
    
#####Salida de la Funcion mostrarCliente#####

#####Entrada de la Funcion BuscarCliente#####
    
def buscarCliente(listaClientes):
    
    if len(listaClientes) > 0: #si no hay clientes agregados marcara error
        
        #encontrarCliente = False
        
        #print("El valor se encuentra?: ", (clienteDni in listaClientes))
        #print("En que posicion se encuentra?: ", listaClientes.index(clienteDni))
        
        print("\nBuscar Cliente.....\n")
        
        clienteDni = input("Ingrese DNI del cliente: ")
        print()
        
        if clienteDni in listaClientes: #verificamos si el cliente se encuentra en la listaClientes
            
        #   for i in listaClientes:
        #       if encontrarCliente == False:
        #           if i == clienteDni:
        #               print("usuario encontrado")
        #               return True
                
        #   if encontrarCliente == False:
        #     print("No existe el DNI")
            
            posicionDni = almacenarDni.index(clienteDni) #verificamos la posicion del DNI en la que se encuentra lo que ingreso el usuario en la lista almacenarDni con index, ejemplo, [0,1,2,3,4,5,6,7......] y lo almacenamos en la variable posicionDni
            
            mostrarNombre = almacenarNombre[posicionDni] # hallamos la misma posicion en la lista almacenarNombre y la guardamos en la variable mostrarNombre
            
            mostrarApellido = almacenarApellido[posicionDni] #hallamos la misma posicion en la lista almacenarApellido y la guardamos en la variable mostrarApellido
            
            #ejemplo:
            # clienteDni = 1 
            # almacenarDni = ["1"]
            #        index =   0  
            # almacenarNombre = ["jorge"]
            #        posicion =     0 
            # print("El Nombre del Cliente es: ", jorge)
            
            print("DNI Encontrado......\n")

            print("El Nombre del Cliente es:", mostrarNombre)
            print()
            
            print("El Apellido del Cliente es:", mostrarApellido)
            print()
            
            #Cliclo While que repite si el usuario desea buscar otro cliente
            
            opcionBusqueda = input("\nDesea Realizar otra Busqueda?: Si(s) o No (n) ")
            opcionBusqueda = opcionBusqueda.lower()
            
            while opcionBusqueda == "s" or opcionBusqueda == "si":
                
                clienteDni = input("\nIngrese DNI del cliente: ")
                print()
        
                if clienteDni in listaClientes:

                    posicionDni = almacenarDni.index(clienteDni)
            
                    mostrarNombre = almacenarNombre[posicionDni]
            
                    mostrarApellido = almacenarApellido[posicionDni]
            
                    print("DNI Encontrado......\n")

                    print("El Nombre del Cliente es:", mostrarNombre)
                    print()
            
                    print("El Apellido del Cliente es:", mostrarApellido)
                    print()
                    
                else:
                    
                    print("El DNI Ingresado No existe.....\n")   
                    
                opcionBusqueda = input("Desea Realizar otra Busqueda? Si(s) o No (n): ")
                opcionBusqueda = opcionBusqueda.lower()                 
                
        else:
            print("El DNI Ingresado No existe.....\n")
        
    else:
        
        print("\nAun no se han Registrado DNI\n")
        print("Intente Nuevamente....\n")
    
    input("\nPresione una Tecla para Continuar......")
    
    #encontrarCliente = False
    
#####Salida de la Funcion BuscarCliente#####

#####Entrada de la Funcion BuscarCliente #####

def eliminarCliente(listaClientes):
    
    if len(listaClientes) > 0: #si no hay clientes agregados marcara error
    
        clienteEliminar = input("\nIngrese Nombre del Cliente a eliminar: ")
        
        if clienteEliminar in listaClientes:
            
            #eliminar de la listaClientes
            
            posicionNombre = listaClientes.index(clienteEliminar) #guardara la posicion donde se encuentra el nombre del usuario en la lista
            
            del listaClientes[posicionNombre - 1:posicionNombre + 5] # me eliminara desde ["Nombre: " hasta "Cedula: "]
            
            #print(listaClientes)
            
            #eliminar de la lista almacenarNombre
            
            eliminarListasParalelas = almacenarNombre.index(clienteEliminar)
            
            del almacenarNombre[eliminarListasParalelas]
            
            #print(almacenarNombre)
            
            #eliminar de la lista almacenarApellido
            
            del almacenarApellido[eliminarListasParalelas]
            
            #print(almacenarApellido)
            
            #eliminar de la lista almacenarDni
            
            del almacenarDni[eliminarListasParalelas]
            
            #print(almacenarDni)
            
            print("\nCliente Eliminado.....\n")
            
            #Ciclo while que repite si el usuario desea eliminar cliente
            
            opcionEliminar = input("\nDesea Eliminar Otro Cliente?: Si(s) o No(n): ")
            opcionEliminar = opcionEliminar.lower()
            
            while opcionEliminar == "s" or opcionEliminar =="si":
                
                clienteEliminar = input("\nIngrese Nombre del Cliente a eliminar: ")
                        
                if clienteEliminar in listaClientes:
            
                    posicionNombre = listaClientes.index(clienteEliminar)
            
                    del listaClientes[posicionNombre - 1:posicionNombre + 5]
            
                    eliminarListasParalelas = almacenarNombre.index(clienteEliminar)
            
                    del almacenarNombre[eliminarListasParalelas]
            
                    del almacenarApellido[eliminarListasParalelas]
            
                    del almacenarDni[eliminarListasParalelas]
            
                    print("\nCliente Eliminado.....\n")
                    
                else:
                    
                    print("El Cliente No existe en la Lista.....\n")
                    print("Intente Nuevamente....\n")
            
                opcionEliminar = input("Desea Eliminar Otro Cliente?: Si(s) o No(n): ")
                opcionEliminar = opcionEliminar.lower()
            
        else:
            
            print("El Cliente No existe en la Lista.....\n")
            print("Intente Nuevamente....\n")
            
    else:
        
        print("\nAun no hay Usuarios Registrados\n")
        print("Intente Nuevamente....\n")
        
    input("\nPresione una Tecla para Continuar......")

#####Salida de la Funcion eliminarCliente #####

#####Salimos de Definir las Funciones#####

################### Lo que Visualizara el usuario ##########################

#####Entrada de las opciones del menu#####
    
print("\nBienvenido al Programa Menu de Clientes...")
print()

print("\nTenemos las Siguientes Opciones....")
print()

print("1. Agregar Nuevo Cliente\n")
print("2. Mostrar Todos los Clientes\n")
print("3. Buscar Cliente por DNI\n")
print("4. Eliminar Cliente\n")
print("5. Salir\n")

opcionCliente = int(input("¿Que Opcion Deseas Realizar: 1, 2, 3, 4, 5?: "))
print()

#El cliente elige las opciones y entra al ciclo while mientras que la opcion sea igual o diferente de 5

#####Salida de las opciones del menu#####

#####Entrada del Ciclo While#####

while opcionCliente != 5:

    if opcionCliente == 1:
        
        agregarCliente(listaClientes)
        
    elif opcionCliente == 2:
        
        mostrarCliente(listaClientes)
    
    elif opcionCliente == 3:
        
        buscarCliente(listaClientes)
    
    elif opcionCliente == 4:
        
        eliminarCliente(listaClientes)
    
    else:
        
        print("Opcion No valida intente nuevamente\n")
    
    print("\nBienvenido al Programa Menu de Clientes...\n")
    print("Tenemos las Siguientes Opciones....\n")

    print("1. Agregar Nuevo Cliente\n")
    print("2. Mostrar Todos los Clientes\n")
    print("3. Mostrar Cliente por DNI\n")
    print("4. Eliminar Cliente\n")
    print("5. Salir\n")

    opcionCliente = int(input("¿Que Opcion Deseas Realizar: 1, 2, 3, 4, 5?: "))
    print()
    
else:
    
    print("Gracias Por usar nuestro Programa\n")
    
#####Salida del Ciclo While#####

#####Fin del Programa#####
