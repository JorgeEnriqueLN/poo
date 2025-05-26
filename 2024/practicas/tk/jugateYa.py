import tkinter as tk
from tkinter import simpledialog, messagebox
import random
import json
from datetime import datetime
import os

class Jugador:
    """Clase que representa a un jugador."""
    def __init__(self, nombre, puntaje, fecha, hora, nivel):
        self.nombre = nombre
        self.puntaje = puntaje
        self.fecha = fecha
        self.hora = hora
        self.nivel = nivel

    def __gt__(self, other):
        return self.puntaje > other.puntaje

class GestorJugadores:
    """Clase que gestiona los jugadores y sus puntajes."""
    def __init__(self):
        self.jugadores = []

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)

    def cargar_puntajes(self, archivo):
        try:
            with open(archivo, 'r') as f:
                datos = json.load(f)
                self.jugadores.clear()  # Limpiar la lista antes de cargar nuevos datos
                for dato in datos:
                    jugador = Jugador(dato['nombre'], dato['puntaje'], dato['fecha'], dato['hora'], dato['nivel'])
                    self.agregar_jugador(jugador)
        except FileNotFoundError:
            pass

    def guardar_puntajes(self, archivo):
        with open(archivo, 'w') as f:
            datos = [{'nombre': jugador.nombre, 'puntaje': jugador.puntaje, 'fecha': jugador.fecha, 'hora': jugador.hora, 'nivel': jugador.nivel} for jugador in self.jugadores]
            json.dump(datos, f, indent=4)

    def obtener_puntajes_ordenados(self):
        return sorted(self.jugadores, reverse=True)

class JugateYa:
    """Clase principal del juego Simon."""
    def __init__(self, root):
        self.root = root
        self.root.title("Jugate Ya")

        self.colores = ['#ff0000', '#00ff00', '#0000ff', '#ffff00']
        self.botones = []
        self.secuencia = []
        self.index_actual = 0
        self.puntaje = 0
        self.nivel = "Principiante"
        self.duracion = 1000
        self.timer_activo = False

        self.frame_controles = tk.Frame(self.root)
        self.frame_controles.pack()

        self.boton_start = tk.Button(self.frame_controles, text="Start", command=self.iniciar_juego)
        self.boton_start.pack(side=tk.LEFT)

        # self.boton_puntajes = tk.Button(self.frame_controles, text="Ver Puntajes", command=self.mostrar_puntajes_guardados)
        # self.boton_puntajes.pack(side=tk.LEFT)

        # self.boton_salir = tk.Button(self.frame_controles, text="Salir", command=self.salir_y_borrar_puntajes)
        # self.boton_salir.pack(side=tk.LEFT)

        self.frame_botones = tk.Frame(self.root)
        self.frame_botones.pack()

        for i, color in enumerate(self.colores):
            boton = tk.Canvas(self.frame_botones, width=100, height=100, bg=color)
            boton.bind("<Button-1>", self.jugar)
            boton.grid(row=i//2, column=i%2, padx=10, pady=10)
            self.botones.append(boton)


 # Configurar el menú de opciones
        self.menu_opciones = tk.Menu(self.root)
        self.root.config(menu=self.menu_opciones)

        # Submenú de Juego
        self.submenu_juego = tk.Menu(self.menu_opciones, tearoff=0)
        self.menu_opciones.add_cascade(label="Opciones", menu=self.submenu_juego)
        self.submenu_juego.add_command(label="Start", command=self.iniciar_juego)
        self.submenu_juego.add_command(label="Ver Puntajes", command=self.mostrar_puntajes_guardados)
        self.submenu_juego.add_command(label="Salir", command=self.salir_y_borrar_puntajes)
        # # Submenú de Puntajes
        # self.submenu_puntajes = tk.Menu(self.menu_opciones, tearoff=0)
        # self.menu_opciones.add_cascade(label="Puntajes", menu=self.submenu_puntajes)
        # self.submenu_puntajes.add_command(label="Ver Puntajes", command=self.mostrar_puntajes_guardados)

        # # Submenú de Salir
        # self.submenu_salir = tk.Menu(self.menu_opciones, tearoff=0)
        # self.menu_opciones.add_cascade(label="Salir", menu=self.submenu_salir)
        # self.submenu_salir.add_command(label="Salir y Borrar Puntajes", command=self.salir_y_borrar_puntajes)



    def iniciar_juego(self):
        self.nombre_jugador = simpledialog.askstring("Nombre del Jugador", "Ingrese su nombre:")
        if self.nombre_jugador:
            self.mostrar_puntaje()
            self.boton_start.config(state=tk.DISABLED)
            self.secuencia = []
            self.index_actual = 0
            self.puntaje = 0
            self.timer_activo = False
            self.mostrar_secuencia()

    def mostrar_puntaje(self):
        if hasattr(self, 'label_puntaje'):
            self.label_puntaje.destroy()
        self.label_puntaje = tk.Label(self.root, text=f"{self.nombre_jugador} - Puntaje: {self.puntaje}")
        self.label_puntaje.pack()

    def mostrar_secuencia(self):
        self.root.after(1000, self.siguiente_ronda)

    def siguiente_ronda(self):
        self.secuencia.append(random.choice(self.botones))
        self.index_actual = 0
        self.mostrar_botones()

    def mostrar_botones(self):
        if self.index_actual < len(self.secuencia):
            boton = self.secuencia[self.index_actual]
            self.cambiar_color(boton, "#ffffff")
            self.root.after(500, self.restaurar_color, boton)
        else:
            self.index_actual = 0
            self.timer_activo = True

    def cambiar_color(self, boton, color):
        boton.configure(bg=color)
        self.root.update()

    def restaurar_color(self, boton):
        color = self.colores[self.botones.index(boton)]
        self.cambiar_color(boton, color)
        self.index_actual += 1
        self.root.after(500, self.mostrar_botones)

    def jugar(self, event):
        if self.timer_activo:
            boton = event.widget
            self.cambiar_color(boton, "#808080")
            self.root.after(500, self.restaurar_color_seleccionado, boton)
            if boton == self.secuencia[self.index_actual]:
                self.index_actual += 1
                if self.index_actual == len(self.secuencia):
                    self.puntaje += 1
                    self.mostrar_puntaje()
                    self.timer_activo = False
                    self.root.after(1000, self.mostrar_secuencia)
            else:
                self.game_over()

    def restaurar_color_seleccionado(self, boton):
        color = self.colores[self.botones.index(boton)]
        self.cambiar_color(boton, color)

    def game_over(self):
        self.timer_activo = False
        messagebox.showinfo("GAME OVER", f"Puntaje: {self.puntaje}")
        self.guardar_puntaje()
        self.reiniciar_juego()

    def guardar_puntaje(self):
        fecha = datetime.now().strftime("%Y-%m-%d")
        hora = datetime.now().strftime("%H:%M:%S")
        jugador = Jugador(self.nombre_jugador, self.puntaje, fecha, hora, self.nivel)
        gestor.agregar_jugador(jugador)
        gestor.guardar_puntajes('pysimonpuntajes.json')

    def reiniciar_juego(self):
        self.secuencia = []
        self.index_actual = 0
        self.puntaje = 0
        self.boton_start.config(state=tk.NORMAL)
        if hasattr(self, 'label_puntaje'):
            self.label_puntaje.destroy()

    def mostrar_puntajes_guardados(self):
        gestor.cargar_puntajes('pysimonpuntajes.json')
        jugadores = gestor.obtener_puntajes_ordenados()
        if jugadores:
            texto = "\n".join(f"{j.nombre}: {j.puntaje} puntos - {j.fecha} {j.hora} - Nivel: {j.nivel}" for j in jugadores)
            messagebox.showinfo("Puntajes Guardados", texto)
        else:
            messagebox.showinfo("Puntajes Guardados", "No hay puntajes guardados.")

    def salir_y_borrar_puntajes(self):
        respuesta = messagebox.askyesno("Confirmar", "¿Estás seguro de que quieres salir?")
        if respuesta:
            # try:
            #     os.remove('pysimonpuntajes.json')
            # except FileNotFoundError:
            #     pass
            # self.root.destroy()
            self.root.destroy()
        

if __name__ == "__main__":
    root = tk.Tk()
    gestor = GestorJugadores()
    gestor.cargar_puntajes('pysimonpuntajes.json')
    juego = JugateYa(root)
    root.mainloop()
