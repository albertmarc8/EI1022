from sesion1y2.createlabyrinth import create_labyrinth
from sesion1y2.labyrinthviewer import LabyrinthViewer
from sesion1y2.path import path, shortest_path

if __name__ == "__main__":
    graph = create_labyrinth(10, 20, 25)
    camino = path(graph, (0,0), (9,19))
    caminocorto = shortest_path(graph, (0,0), (9, 19))
    print(camino)

    lv = LabyrinthViewer(graph, canvas_width=600, canvas_height=400, margin=10)

    lv.set_input_point((0, 0))
    lv.set_output_point((9, 19))

    lv.add_path(camino, 'blue')
    lv.add_path(caminocorto, offset=3, color='red')

    lv.run()