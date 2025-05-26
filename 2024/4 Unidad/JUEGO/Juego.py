import tkinter as tk
from tkinter import simpledialog, messagebox, Toplevel, Label, Button, DISABLED
import random
import json
from datetime import datetime
import sys
import os

# Clase Jugador
class Jugador:
    def __init__(self, nombre, puntaje, fecha, hora, nivel):
        self.__nombre = nombre
        self.__puntaje = puntaje
        self.__fecha = fecha
        self.__hora = hora
        self.__nivel = nivel

    def __gt__(self, other):
         return self.__puntaje > other.__puntaje
    def getnombre(self):
        return self.__nombre
    def getpuntaje(self):
        return self.__puntaje
    def getfecha(self):
        return self.__fecha
    def gethora(self):
        return self.__hora
    def getnivel(self):
        return self.__nivel
# Clase GestorJugadores
class GestorJugadores:
    def __init__(self):
        self.jugadores = []

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)

    def cargar_puntajes(self, archivo):
        try:
            with open(archivo, 'r') as f:
                datos = json.load(f)
                for dato in datos:
                    jugador = Jugador(dato['nombre'], dato['puntaje'], dato['fecha'], dato['hora'], dato['nivel'])
                    self.agregar_jugador(jugador)
        except FileNotFoundError:
            pass

    def guardar_puntajes(self, archivo):
        with open(archivo, 'w') as f:
            datos = [{'nombre': jugador.getnombre(), 'puntaje': jugador.getpuntaje(), 'fecha': jugador.getfecha(), 'hora': jugador.gethora(), 'nivel': jugador.getnivel()} for jugador in self.jugadores]
            json.dump(datos, f)

    def obtener_puntajes_ordenados(self):
        return sorted(self.jugadores, reverse=True)

# Clase principal del juego
class jugateya:
    def __init__(self, root):
        self.root = root
        self.root.title("Jugate Ya")

        self.__colores = ['#ff0000', '#00ff00', '#0000ff', '#ffff00']
        self.__botones = []
        self.__secuencia = []
        self.__inicio_actual = 0
        self.__puntaje = 0
        self.__nivel = "Principiante"  # Nivel por defecto
        self.__duracion = 1000
        self.__timer_activo = False
        self.__timer_general = None  # Timer para el nivel Experto y Super Experto

        self.crear_menu()
        self.crear_interfaz()

    def crear_menu(self):
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)
        
        archivo_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Archivo", menu=archivo_menu)
        archivo_menu.add_command(label="Ver puntajes", command=self.mostrar_puntajes)
        archivo_menu.add_separator()
        archivo_menu.add_command(label="Salir", command=self.salir_juego)

    def crear_interfaz(self):
        self.frame_controles = tk.Frame(self.root)
        self.frame_controles.pack()

        self.boton_start = tk.Button(self.frame_controles, text="Start", command=self.iniciar_juego)
        self.boton_start.pack(side=tk.LEFT)

        niveles = ["Principiante", "Experto", "Super Experto"]
        self.var_nivel = tk.StringVar(self.root)
        self.var_nivel.set(niveles[0])  # Valor por defecto

        self.lista_niveles = tk.OptionMenu(self.frame_controles, self.var_nivel, *niveles)
        self.lista_niveles.pack(side=tk.LEFT)

        self.frame_botones = tk.Frame(self.root)
        self.frame_botones.pack()

        # Crear botones de colores en una cuadrícula 2x2
        for i, color in enumerate(self.__colores):
            boton = tk.Canvas(self.frame_botones, width=100, height=100, bg=color)
            boton.bind("<Button-1>", self.jugar)
            boton.grid(row=i//2, column=i%2, padx=10, pady=10)
            self.__botones.append(boton)
        


    def iniciar_juego(self):
            self.nombre_jugador = ""
            while not self.nombre_jugador:
                self.nombre_jugador = simpledialog.askstring("Nombre del Jugador", "Ingrese su nombre:")
                if not self.nombre_jugador:
                    messagebox.showwarning("Advertencia", "Debe ingresar un nombre para continuar.")
            
            self.__nivel = self.var_nivel.get()
            messagebox.showinfo("Nivel Seleccionado", f"Has seleccionado el nivel: {self.__nivel}")
            self.mostrar_puntaje()
            self.boton_start.config(state=DISABLED)

            self.__secuencia = []
            self.__inicio_actual = 0
            self.puntaje = 0
            self.__timer_activo = False

            if self.__nivel in ["Experto", "Super Experto"]:
                self.__duracion = 700
                self.iniciar_timer_general()

            self.mostrar_secuencia()
   

    def iniciar_timer_general(self):
        if self.__timer_general:
            self.root.after_cancel(self.__timer_general)
        self.__timer_general = self.root.after(5000, self.game_over)  # 5 segundos de tiempo general

    def mostrar_puntaje(self):
        self.label_puntaje = tk.Label(self.root, text=f"{self.nombre_jugador} - Puntaje: {self.__puntaje}")
        self.label_puntaje.pack()

    def mostrar_secuencia(self):
        self.root.after(1000, self.siguiente_ronda)

    def siguiente_ronda(self):
        if self.__nivel == "Super Experto" and len(self.__secuencia) > 0:
            self.__secuencia.append(random.choice(self.__botones))
        self.__secuencia.append(random.choice(self.__botones))
        self.__inicio_actual = 0
        self.mostrar_botones()

    def mostrar_botones(self):
        if self.__inicio_actual < len(self.__secuencia):
            if self.__nivel == "Super Experto" and self.__inicio_actual < len(self.__secuencia) - 1:
                boton1 = self.__secuencia[self.__inicio_actual]
                boton2 = self.__secuencia[self.__inicio_actual + 1]
                self.cambiar_color(boton1, "#ffffff")
                self.cambiar_color(boton2, "#ffffff")
                self.root.after(500, self.restaurar_color, boton1)
                self.root.after(500, self.restaurar_color, boton2)
                self.__inicio_actual += 2
            else:
                boton = self.__secuencia[self.__inicio_actual]
                self.cambiar_color(boton, "#ffffff")
                self.root.after(500, self.restaurar_color, boton)
                self.__inicio_actual += 1
            self.root.after(self.__duracion, self.mostrar_botones)
        else:
            self.__inicio_actual = 0
            self.__timer_activo = True
            if self.__nivel in ["Experto", "Super Experto"]:
                self.iniciar_timer_general()

    def cambiar_color(self, boton, color):
        boton.configure(bg=color)
        self.root.update()

    def restaurar_color(self, boton):
        color = self.__colores[self.__botones.index(boton)]
        self.cambiar_color(boton, color)

    def jugar(self, event):
        if self.__timer_activo:
            boton = event.widget
            self.cambiar_color(boton, "#808080")  # Cambiar a color gris
            self.root.after(500, self.restaurar_color_seleccionado, boton)
            if boton == self.__secuencia[self.__inicio_actual]:
                self.__inicio_actual += 1
                if self.__inicio_actual == len(self.__secuencia):
                    self.__puntaje += 1
                    self.label_puntaje.configure(text=f"{self.nombre_jugador} - Puntaje: {self.__puntaje}")
                    self.__timer_activo = False
                    self.root.after(1000, self.mostrar_secuencia)
                if self.__nivel in ["Experto", "Super Experto"]:
                    self.iniciar_timer_general()
            else:
                self.game_over()

    def restaurar_color_seleccionado(self, boton):
        color = self.__colores[self.__botones.index(boton)]
        self.cambiar_color(boton, color)

    def game_over(self):
        self.__timer_activo = False
        if self.__timer_general:
            self.root.after_cancel(self.__timer_general)
            self.__timer_general = None
        messagebox.showinfo("GAME OVER", f"Puntaje: {self.__puntaje}")
        self.guardar_puntaje()
        self.reiniciar_juego()

    def guardar_puntaje(self):
        __fecha = datetime.now().strftime("%Y-%m-%d")
        __hora = datetime.now().strftime("%H:%M:%S")
        jugador = Jugador(self.nombre_jugador, self.__puntaje, __fecha, __hora, self.__nivel)
        gestor.agregar_jugador(jugador)
        gestor.guardar_puntajes('pysimonpuntajes.json')

    def reiniciar_juego(self):
        self.__secuencia = []
        self.__inicio_actual = 0
        self.__puntaje = 0
        self.boton_start.config(state=tk.NORMAL)
        if hasattr(self, 'label_puntaje'):
            self.label_puntaje.destroy()

    def mostrar_puntajes(self):
        dialogo_puntajes = tk.Toplevel(self.root)
        dialogo_puntajes.title("Galería de Puntajes")
        dialogo_puntajes.resizable(False, False)  # Deshabilitar redimensionamiento
        dialogo_puntajes.config(bg='white')  # Establecer color de fondo blanco
        
        # Verificar si el sistema operativo es Windows
        if sys.platform.startswith('win'):
            # Ocultar los botones de minimizar y cerrar en Windows
            dialogo_puntajes.overrideredirect(True)
            dialogo_puntajes.attributes('-toolwindow', True)
        
        puntajes_ordenados = gestor.obtener_puntajes_ordenados()

        # Encabezado del cuadro de diálogo
        Label(dialogo_puntajes, text="Nombre             Fecha             Hora             Puntaje             Nivel", bg='white').pack()

        # Mostrar puntajes en el cuadro de diálogo
        for jugador in puntajes_ordenados:
            Label(dialogo_puntajes, text=f"{jugador.getnombre():<15} {jugador.getfecha():<15} {jugador.gethora():<15} {jugador.getpuntaje():<15} {jugador.getnivel()}", bg='white').pack()

        # Botón "Cerrar"
        btn_cerrar = tk.Button(dialogo_puntajes, text="Cerrar", command=dialogo_puntajes.destroy)
        btn_cerrar.pack(pady=10)

        # Centrar la ventana en la pantalla principal
        dialogo_puntajes.update_idletasks()
        width = dialogo_puntajes.winfo_width()
        height = dialogo_puntajes.winfo_height()
        x = (dialogo_puntajes.winfo_screenwidth() // 2) - (width // 2)
        y = (dialogo_puntajes.winfo_screenheight() // 2) - (height // 2)
        dialogo_puntajes.geometry(f'+{x}+{y}')

    def salir_juego(self):
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    root.protocol("WM_DELETE_WINDOW", lambda: None)
    gestor = GestorJugadores()
    gestor.cargar_puntajes('pysimonpuntajes.json')
    juego = jugateya(root)
    root.mainloop()
