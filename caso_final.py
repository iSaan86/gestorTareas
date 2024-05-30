from colorama import Fore, Style, init

""" Esta clase es para un programa que gestiona una lista de tareas. 
Tiene métodos que permiten agregar una nueva tarea, marcar una tarea como completada, 
cambiar una tarea completada a pendiente, eliminar una tarea y mostrar todas 
las tareas.
--> Desarrollado por Alexandra Ferrera Arenas para el Ejercicio Práctico Final del Curso de Python Full Stack de IBM """

init(autoreset=True)  # Inicializa colorama para poder aplicar colores a los textos de la consola

class ListaTareas:
    def __init__(self):
        self.tareas = []  # Lista para almacenar las tareas

    def agregar_tarea(self, tarea):
        # Convierte la primera letra en mayúscula y el resto en minúscula
        tarea = tarea.capitalize()
        # Agrega la tarea a la lista con el estado 'completada' como False
        self.tareas.append({"descripcion": tarea, "completada": False})

    def marcar_completada(self, posicion):
        # Marca una tarea como completada si la posición es válida
        if 0 <= posicion < len(self.tareas):
            self.tareas[posicion]["completada"] = True
        else:
            # Lanza una excepción si la posición no es válida
            raise IndexError("La posición de la tarea no es válida")

    def mostrar_tareas(self):
        # Muestra todas las tareas con sus estados (completada o pendiente)
        if self.tareas:
            for i, tarea in enumerate(self.tareas):
                estado = "Completada" if tarea["completada"] else "Pendiente"
                # Aplica color según el estado de la tarea
                if tarea["completada"]:
                    estado_coloreado = f"{Fore.GREEN}{estado}{Style.RESET_ALL}"  # Verde para completada
                else:
                    estado_coloreado = f"{Fore.RED}{estado}{Style.RESET_ALL}"  # Rojo para pendiente
                print(f"{i + 1}. {tarea['descripcion']} - Estado: {estado_coloreado}")
        else:
            # Mensaje si no hay tareas pendientes
            print(f"{Fore.RED}No hay tareas pendientes{Style.RESET_ALL}")

    def eliminar_tarea(self, posicion):
        # Elimina una tarea si la posición es válida
        if 0 <= posicion < len(self.tareas):
            del self.tareas[posicion]
        else:
            # Lanza una excepción si la posición no es válida
            raise IndexError("La posición de la tarea no es válida")


# Función principal de interacción con el usuario
def main():
    lista_tareas = ListaTareas()  # Crea una instancia de ListaTareas

    while True:
        # Menú de opciones, incluyo encabezado con estilo personal
        print("\n")
        print(f"{Fore.CYAN}╔══════════════════════════════════════╗{Style.RESET_ALL}")
        print(f"{Fore.CYAN}║{Style.BRIGHT}          GESTION DE TAREAS           {Style.RESET_ALL}{Fore.CYAN}║{Style.RESET_ALL}")
        print(f"{Fore.CYAN}║{Style.BRIGHT}  Desarrollado por Alexandra Ferrera  {Style.RESET_ALL}{Fore.CYAN}║{Style.RESET_ALL}")
        print(f"{Fore.CYAN}╚══════════════════════════════════════╝{Style.RESET_ALL}")
        print("1. Agregar una nueva tarea")
        print("2. Marcar una tarea como completada")
        print("3. Mostrar todas las tareas")
        print("4. Eliminar una tarea")
        print("5. Salir")
        print("\n")

        # Solicita al usuario que ingrese una opción
        opcion = input("Ingrese el número de la opción que desea realizar: ")

        if opcion == "1":
            # Agrega una nueva tarea
            nueva_tarea = input("Ingrese la nueva tarea: ")
            lista_tareas.agregar_tarea(nueva_tarea)
            print(f"{Fore.GREEN}Tarea agregada correctamente.{Style.RESET_ALL}")

        elif opcion == "2":
            try:
                # Marca una tarea como completada
                posicion = int(input("Ingrese la posición de la tarea a marcar como completada: ")) - 1
                lista_tareas.marcar_completada(posicion)
                print(f"{Fore.GREEN}Tarea marcada como completada.{Style.RESET_ALL}")
            except (IndexError, ValueError):
                # Maneja errores de posición no válida
                print(f"{Fore.RED}Error: Posición de tarea no válida.{Style.RESET_ALL}")

        elif opcion == "3":
            # Muestra todas las tareas
            print("\n------- Listado de Tareas -------")
            lista_tareas.mostrar_tareas()

        elif opcion == "4":
            try:
                # Elimina una tarea
                posicion = int(input("Ingrese la posición de la tarea a eliminar: ")) - 1
                lista_tareas.eliminar_tarea(posicion)
                print(f"{Fore.GREEN}Tarea eliminada correctamente.{Style.RESET_ALL}")
            except (IndexError, ValueError):
                # Maneja errores de posición no válida
                print(f"{Fore.RED}Error: Posición de tarea no válida.{Style.RESET_ALL}")

        elif opcion == "5":
            # Sale del programa
            print("¡Hasta luego!")
            break

        else:
            # Maneja opción no válida
            print(f"{Fore.RED}Opción no válida. Por favor, ingrese un número válido.{Style.RESET_ALL}")

# Verifica si el script se está ejecutando como un programa independiente
if __name__ == "__main__":
    main()
