# Síncrono: las tareas se ejecutan una detrás de otra, bloqueando el flujo.
import time

def sync_tarea(nombre):
    print(f"{nombre} iniciada")
    time.sleep(1)  # Espera 1 segundo
    print(f"{nombre} terminada")

def main_sync():
    # Ejecutamos en bucle varias tareas síncronas
    for i in range(3):
        sync_tarea(f"Tarea {i+1}")

main_sync()
