import asyncio

# Función que simula una tarea que tarda 'segundos' en completarse
async def tarea(nombre, segundos):
    print(f"{nombre} iniciada")
    # Pauso esta tarea (1) y dejo pasar otras
    await asyncio.sleep(segundos)
    print(f"{nombre} completada")

async def main():
    # Ejecutamos varias tareas en paralelo con asyncio.gather()
    await asyncio.gather(
        tarea("Tarea 1", 2),
        tarea("Tarea 2", 1),
        tarea("Tarea 3", 3)
    )

# Lanza todas las tareas y espera a que terminen
asyncio.run(main())

