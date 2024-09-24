#!/usr/bin/env python3

import matplotlib.pyplot as mpl
import os
import subprocess
import networkx

# Reset
RESTART='\033[0m' # No Color (reset to default)

# Regular Colors
B ='\033[0;30m' # Black
R ='\033[0;31m' # Red
G ='\033[0;32m' # Green
Y ='\033[0;33m' # Yellow
B ='\033[0;34m' # Blue
P ='\033[0;35m' # Purple
C ='\033[0;36m' # Cyan
W ='\033[0;37m' # White


banner00=G+'''

⠀⢀⣠⣄⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⣶⡾⠿⠿⠿⠿⢷⣶⣦⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢰⣿⡟⠛⠛⠛⠻⠿⠿⢿⣶⣶⣦⣤⣤⣀⣀⡀⣀⣴⣾⡿⠟⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠻⢿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⣀⡀
⠀⠻⣿⣦⡀⠀⠉⠓⠶⢦⣄⣀⠉⠉⠛⠛⠻⠿⠟⠋⠁⠀⠀⠀⣤⡀⠀⠀⢠⠀⠀⠀⣠⠀⠀⠀⠀⠈⠙⠻⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠟⠛⠛⢻⣿
⠀⠀⠈⠻⣿⣦⠀⠀⠀⠀⠈⠙⠻⢷⣶⣤⡀⠀⠀⠀⠀⢀⣀⡀⠀⠙⢷⡀⠸⡇⠀⣰⠇⠀⢀⣀⣀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣤⣶⡶⠶⠶⠒⠂⠀⠀⣠⣾⠟
⠀⠀⠀⠀⠈⢿⣷⡀⠀⠀⠀⠀⠀⠀⠈⢻⣿⡄⣠⣴⣿⣯⣭⣽⣷⣆⠀⠁⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣦⡀⠀⣠⣾⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⣠⣾⡟⠁⠀
⠀⠀⠀⠀⠀⠈⢻⣷⣄⠀⠀⠀⠀⠀⠀⠀⣿⡗⢻⣿⣧⣽⣿⣿⣿⣧⠀⠀⣀⣀⠀⢠⣿⣧⣼⣿⣿⣿⣿⠗⠰⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⡿⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠙⢿⣶⣄⡀⠀⠀⠀⠀⠸⠃⠈⠻⣿⣿⣿⣿⣿⡿⠃⠾⣥⡬⠗⠸⣿⣿⣿⣿⣿⡿⠛⠀⢀⡟⠀⠀⠀⠀⠀⠀⣀⣠⣾⡿⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⣷⣶⣤⣤⣄⣰⣄⠀⠀⠉⠉⠉⠁⠀⢀⣀⣠⣄⣀⡀⠀⠉⠉⠉⠀⠀⢀⣠⣾⣥⣤⣤⣤⣶⣶⡿⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⢻⣿⠛⢿⣷⣦⣤⣴⣶⣶⣦⣤⣤⣤⣤⣬⣥⡴⠶⠾⠿⠿⠿⠿⠛⢛⣿⣿⣿⣯⡉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣧⡀⠈⠉⠀⠈⠁⣾⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⠟⠉⣹⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣸⣿⣿⣦⣀⠀⠀⠀⢻⡀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣶⣿⠋⣿⠛⠃⠀⣈⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡿⢿⡀⠈⢹⡿⠶⣶⣼⡇⠀⢀⣀⣀⣤⣴⣾⠟⠋⣡⣿⡟⠀⢻⣶⠶⣿⣿⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣷⡈⢿⣦⣸⠇⢀⡿⠿⠿⡿⠿⠿⣿⠛⠋⠁⠀⣴⠟⣿⣧⡀⠈⢁⣰⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⢻⣦⣈⣽⣀⣾⠃⠀⢸⡇⠀⢸⡇⠀⢀⣠⡾⠋⢰⣿⣿⣿⣿⡿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠿⢿⣿⣿⡟⠛⠃⠀⠀⣾⠀⠀⢸⡇⠐⠿⠋⠀⠀⣿⢻⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠁⢀⡴⠋⠀⣿⠀⠀⢸⠇⠀⠀⠀⠀⠀⠁⢸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡿⠟⠋⠀⠀⠀⣿⠀⠀⣸⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣁⣀⠀⠀⠀⠀⣿⡀⠀⣿⠀⠀⠀⠀⠀⠀⢀⣈⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠟⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
'''+RESTART


def screenClear(): # Simple function that clears the screen
    if os.name == 'posix':
        x = os.system('clear')
    else:
        x = os.system('cls')

def simpleView():
    # ejecutamos con subprocess el comando ps y guardamos los datos de la salida de dicho comando
    result = subprocess.run(['ps', '-eo', 'pid,comm'], stdout=subprocess.PIPE)
    # tratamos el contenido de la salida del comando para tener texto y lineas separadas
    process_data = result.stdout.decode().splitlines()  
    
    # eliminamos el PID command
    process_data = process_data[1:]
    
    # eliminamos lineas vacias y convertimos "process_data" a el formato (PID, nombre)
    processes = [line.split(maxsplit=1) for line in process_data if line]
    
    # chivatazo de chatgpt para que se trate la salida de "processes" y ordene las salidas de los PID de menor a mayor
    for pid, name in sorted(processes, key=lambda x: int(x[0])):
        print(f"{pid: <10} {name}")
    print("-"*64)
    print("Process list shown, press enter to return to main menu...")
    x = input("-"*64)
    if(x != "josu"):
        screenClear();
        startingMenu();
    else:
        print('-'*64)
        print(P+"EasterEgg Found"+RESTART)
        print('-'*64)
        print("QUE LAS PRACTIQUES NO SON REMUNERADES CULLONS")
        print("att. Josue Sallent")


def graphicalView():
    print(G+"Loading map..."+RESTART)
    result = subprocess.run(['ps', '-eo', 'pid,ppid,comm'], stdout=subprocess.PIPE)
    process_data = result.stdout.decode().splitlines()

    process_data = process_data[1:]

    processes = [line.split(maxsplit=2) for line in process_data if line]

    # Guardamos el gráfico dentro de una variable con la función "DiGraph" de networkx
    Graph = networkx.DiGraph()

    # Proceso de filtrado y adición del modelo de padre e hijos
    for pid, ppid, name in processes:
        Graph.add_node(pid)  # Solo añadimos el PID como nodo
        if ppid != '0':  # Solo hacemos la unión si tiene un proceso padre válido
            Graph.add_edge(ppid, pid)  # Hacemos la relación

    # Dibujamos el gráfico
    mpl.figure(figsize=(12, 8))
    pos = networkx.spring_layout(Graph)  # Distribución de nodos

    # Dibujamos y configuramos cómo se verán los nodos
    networkx.draw(Graph, pos, with_labels=False, node_size=525, node_color='purple', arrows=True)

    # Añadimos las etiquetas que corresponden solo a los PIDs
    labels = {pid: pid for pid, _, _ in processes}  # Usamos solo el PID como etiqueta
    networkx.draw_networkx_labels(Graph, pos, labels, font_size=11)

    mpl.title('ProcessMap')  # Título
    mpl.show()  # Mostramos el mapa

def viewGeneralMap():
    screenClear();
    print("="*32)
    Pid = input("Ingresa un PID valido: ")
    print("="*32)
    screenClear();
    print(G+"Loading map..."+RESTART)

    # esto esta explicado en otras 2 funciones porfavor
    result = subprocess.run(['ps', '-eo', 'pid,ppid,comm'], stdout=subprocess.PIPE)
    process_data = result.stdout.decode().splitlines()[1:]  # Ignorar la primera línea

    processes = [line.split(maxsplit=2) for line in process_data if line]

    # otra ve
    Graph = networkx.DiGraph()

    # lo mismo de siempre
    for pid, ppid, name in processes:
        Graph.add_node(pid, label=name)  # Añadir nodo
        if ppid != '0':
            Graph.add_edge(ppid, pid)  # Añadir relación padre-hijo

    # mas ede lo mismo
    mpl.figure(figsize=(12, 8))
    pos = networkx.spring_layout(Graph)

    # unico cambio, vamoas a hacer que aquellos que esten relacionados con el pid que introduzca el usuario sean amarillos
    node_colors = [] # creamos el listado de colores
    for node in Graph.nodes():
        if node == Pid or node in Graph.successors(Pid):  # si el pid esta relacionado con el que ha introducido el usuario...
            node_colors.append('yellow') # color amarillo
        else:
            node_colors.append('purple') # default para el resto

    #sigue igual que antes
    networkx.draw(Graph, pos, with_labels=False, node_size=525, node_color=node_colors, arrows=True)

    # igual que antes pero igual
    labels = {pid: pid for pid in Graph.nodes()}
    networkx.draw_networkx_labels(Graph, pos, labels, font_size=11)

    mpl.title('Process Map with Highlighted PID')  # titulacion
    mpl.show()  # mostramos el mapa

def viewPrivateMap():
    screenClear();
    print("=" * 40)
    print("View Private Map")
    print("=" * 40)
    # solicitamos el pid
    pid_input = input("Enter a valid PID: ")
    screenClear();
    print(G+"Loading map..."+RESTART)
    # lo mismo que hemos hecho 2000 veces
    result = subprocess.run(['ps', '-eo', 'pid,ppid,comm'], stdout=subprocess.PIPE)
    process_data = result.stdout.decode().splitlines()

    process_data = process_data[1:]  # Ignorar la línea de encabezado
    processes = [line.split(maxsplit=2) for line in process_data if line]

    # creamos el grafico como siempre
    Graph = networkx.DiGraph()

    # Añadimos unicamente los procesos padres e hijos, como si fuese una reunion del ampa
    for pid, ppid, name in processes:
        if pid == pid_input or ppid == pid_input:  # si el pid es el que el usuario ha puesto o un hijo...
            Graph.add_node(pid, label=name) # añadimos el nodo
            if ppid != '0':
                Graph.add_edge(ppid, pid)

    # simplemente miramos que haya un grafico, ya que sino significa que no habia un proceso con ese nuemro
    if len(Graph.nodes) == 0:
        print("No processes found related to the specified PID.")
        return

    # dibujamos el grafico por 38576202384 vez
    mpl.figure(figsize=(12, 8))
    pos = networkx.spring_layout(Graph)

    # dibujamos los nodos en color amarillo yta que son los seleccionados
    networkx.draw(Graph, pos, with_labels=False, node_size=525, node_color='yellow', arrows=True)

    # etiquetacion como si fuese el ikea
    labels = {pid: pid for pid in Graph.nodes()}
    networkx.draw_networkx_labels(Graph, pos, labels, font_size=11)

    mpl.title('Private Process Map') # titulo del mapa
    mpl.show() # mostramos el mapa

def graphicalResults():
    print("="*40)
    print("Graphical Process Viewer with Highlights")
    print("="*40)
    print("1. View General Map (Highlighting)")
    print("2. View Private Map")
    print("="*40)

    # seleccion
    selection = input("Select an option (1 or 2): ")

    # verificar si esta dentro de las opciones del menu
    if selection == "1":
        viewGeneralMap()
    elif selection == "2":
        viewPrivateMap()
    else:
        print("Invalid option, returning to main menu...")
        startingMenu()

def processInfo():
    screenClear()
    print("=" * 32)
    print("Process Info Menu")
    print("=" * 32)
    pid = input("Enter a valid PID to show its metrics: ")
    screenClear();
    try:
        # misma manera de obtencion de datos que siempre cambiando los parametros
        cpuInfo = subprocess.run(['ps', '-p', pid, '-o', '%cpu,%mem'], stdout=subprocess.PIPE)
        processInfo = cpuInfo.stdout.decode().splitlines()

        # Mostrar información del proceso
        if len(processInfo) > 1:
            cpuMem = processInfo[1].split()
            cpuUsage = cpuMem[0]  # %CPU
            memUsage = cpuMem[1]  # %MEM
            print(f"Process {pid} - \033[0;33mCPU Usage\033[0m: {cpuUsage}%, \033[0;33mMemory Usage\033[0m: {memUsage}%")
            print("="*64)

            # Obtener información de los procesos hijos
            childrenInfo = subprocess.run(['pgrep', '-P', pid], stdout=subprocess.PIPE)
            childrenPids = childrenInfo.stdout.decode().splitlines()
            
            # igual que con lo anterior, pero relacionandolo con los hijos
            for child_pid in childrenPids:
                cpuInfo_c = subprocess.run(['ps', '-p', child_pid, '-o', '%cpu,%mem'], stdout=subprocess.PIPE)
                childInfo = cpuInfo_c.stdout.decode().splitlines()
                if len(childInfo) > 1:
                    cpuMem_c = childInfo[1].split()
                    print(f"\033[0;33mChild Process\033[0m: {child_pid} || \033[0;33mCPU Usage\033[0m: {cpuMem_c[0]}%, \033[0;33mMemory Usage\033[0m: {cpuMem_c[1]}%")  ## hehe es un poquito trampita

        else:
            print(f"No process found with PID: {pid}")
    
    # sacado de chatgpt porque me ha obligado el programa
    except Exception as e:
        print(f"Error: {e}")

    input("Press ENTER to return to the main menu...")
    startingMenu()

def ToolInfo():
    print("="*32)
    print("|| \033[0;33mVersion:\033[0m 1.0.0")
    print("|| \033[0;33mFunctionality:\033[0m This program is made for the user to interact with the processes in the system.")
    print("|| \033[0;33mAuthor:\033[0m Guillermo Gomez Sanchez")
    print("|| \033[0;33mGithub:\033[0m https://github.com/Zer0plusOne")
    print("="*32)
    print("Press any key to return to main menu...")
    anykey = input()
    screenClear()
    startingMenu()

def startingMenu():
    screenClear();
    print(banner00)
    print("="*48)
    print("||\033[0;33m1.\033[0m Simple Process Viewer")
    print("||\033[0;33m2.\033[0m Graphical Process Viewer")
    print("||\033[0;33m3.\033[0m Show Graphical view and mark a process")
    print("||\033[0;33m4.\033[0m Process Info")
    print("||\033[0;33m?.\033[0m Tool Info")
    print("||\033[0;33m0.\033[0m Exit")
    print("="*48)
    selection = input("Select an option: ")
    screenClear()
    if selection == "1":
        simpleView();
    elif selection == "2":
        graphicalView();
    elif selection == "3":
        graphicalResults();
    elif selection == "0":
        exit()
    elif selection == "4":
        processInfo();
    elif selection == "?":
        ToolInfo()
        startingMenu()
    else:
        print("Invalid option, try again")


screenClear();
startingMenu();

