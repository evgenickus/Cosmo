from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Mesh

class MainWidget(Widget):
    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        self.init_star()
    
    def init_star(self):
        x, y = 500, 100
        step_x = 25
        step_y = 25
        with self.canvas:
            # mesh = Mesh(mode="triangle_fan")
            # mesh.vertices = [
            #     x - step_x, y + step_y * 4, 0, 0, # 7
            #     x - step_x * 5, y + step_y * 5, 0, 0, # 6
            #     x - step_x, y + step_y * 6, 0, 0, # 5
            #     x, y + step_x * 10, 0, 0, # 4
            #     x + step_x, y + step_y * 6, 0, 0, # 3
            #     x + step_x * 5, y + step_y * 5, 0, 0, # 2
            #     x + step_x, y + step_y * 4, 0, 0, # 1
            #     x, y, 0, 0] # 0
            # mesh.indices = [0, 1, 2, 3, 4, 5, 6, 7]

            mesh1 = Mesh(mode="triangle_fan")
             #line_loop, triangle_strip, triangle_fan
            mesh1.vertices = [
                300, 300, 0, 0,
                300-25, 300+100, 0, 0,
                300-75, 300+75, 0, 0,
                300-45, 300+125, 0, 0,
                300-150, 300+150, 0, 0,
                300-45, 300+175, 0, 0,
                300-75, 300+225, 0, 0,
                300-25, 300+200, 0, 0,
                300, 600, 0, 0,
                300+25, 300+200, 0, 0,
                300+75, 300+225, 0, 0,
                300+45, 300+175, 0, 0,
                300+150, 300+150,
                300+45, 300+125, 0, 0,
                300+75, 300+75, 0, 0,
                300+25, 300+100,

                ] # 0
            mesh1.indices = [0,
            1, 2, 3, 4, 5, 6, 7,
            8, 9, 10, 11, 12, 13, 14, 15]



class TestMesh(App):
    pass

TestMesh().run()