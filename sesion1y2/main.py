from sesion1y2.labyrinthviewer import LabyrinthViewer
from sesion1y2.createlabyrinth import create_labyrinth


if __name__ == "__main__":
    print("Ejecutando aplicación")
    # Laberinto en forma de grafo no dirigido
    graph = create_labyrinth(10, 20)

    # Obligatorio: Crea un LabyrinthViewer pasándole el grafo del laberinto
    lv = LabyrinthViewer(graph, canvas_width=600, canvas_height=400, margin=10)

    # Obligatorio: Muestra el laberinto
    lv.run()
