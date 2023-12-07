from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics.vertex_instructions import Ellipse, Line, Quad
from kivy.graphics.context_instructions import Color
from kivy.properties import Clock
from kivy.properties import NumericProperty
import random, time
from kivy.graphics import Mesh


class MainWidget(RelativeLayout):
    stars = list()
    stars1 = list()
    stars2 = list()
    stars3 = list()
    stars4 = list()
    stars5 = list()


    stars_coordinats = list()
    stars1_coordinats = list()
    stars2_coordinats = list()
    stars3_coordinats = list()
    stars4_coordinats = list()
    stars5_coordinats = list()


    star_x = 1
    star_y = 1
    star1_x = 2
    star1_y = 2
    star2_x = .5
    star2_y = .5
    star3_x = 2
    star3_y = 2
    star4_x = 2
    star4_y = 2
    star5_x = 2
    star5_y = 2

    STAR_NB = 0#200
    STAR1_NB = 0#50
    STAR2_NB = 0#500
    STAR3_NB = 0#100
    STAR4_NB = 0#10
    STAR5_NB = 1


    direction = True

    SPEED_X = 0
    SPEED_Y = 0
    SIZE_X = 0
    SIZE_Y = 0

    perspective_point_x = NumericProperty(0)
    perspective_point_y = NumericProperty(0)



    def __init__(self, **kw):
        super(MainWidget, self).__init__(**kw)
        self.init_stars()
        self.generate_stars_coordinate()
        self.update_stars()

        Clock.schedule_interval(self.update, 1.0 / 60.0)

    def init_stars(self):
        for i in range(self.STAR_NB):
            with self.canvas:
                Color(1, 1, 1)
                self.stars.append(Line())
        for i in range(self.STAR1_NB):
            r = random.randint(0, 2)
            with self.canvas:
                if r == 0:
                    Color(207.0/255.0, 100.0/255.0, 235.0/255.0)
                elif r == 1:
                    Color(252.0/255.0, 255.0/255.0, 147.0/255.0)
                else:
                    Color(134.0/255.0, 191.0/255.0, 213.0/255.0)
                self.stars1.append(Line())
        for i in range(self.STAR2_NB):
            with self.canvas:
                Color(1, 1, 1)
                self.stars2.append(Line())
        for i in range(self.STAR3_NB):
            with self.canvas:
                Color(1, 1, 1)
                self.stars3.append(Ellipse())

        with self.canvas:
            Color(178.0/255.0, 220.0/255.00, 255.0/255.0)
            for i in range(self.STAR4_NB):
                self.stars4.append(Mesh(mode='triangle_fan')) # 'points', 'line_strip', 'line_loop', 'lines', 'triangle_strip', 'triangle_fan'
        with self.canvas:
            Color(178.0/255.0, 220.0/255.00, 255.0/255.0)
            for i in range(self.STAR5_NB):
                self.stars5.append(Mesh(mode='triangle_fan')) 

    def generate_stars_coordinate(self):
        for i in range(len(self.stars)):
            x = random.randint(-700, 700)
            y = random.randint(-600, 600)
            self.stars_coordinats.append((x, y))
        for i in range(len(self.stars1)):
            x = random.randint(-700, 700)
            y = random.randint(-600, 600)
            self.stars1_coordinats.append((x, y))
        for i in range(len(self.stars2)):
            x = random.randint(-700, 700)
            y = random.randint(-600, 600)
            s = random.randint(1, 4)
            self.stars2_coordinats.append((x, y, s))
        for i in range(len(self.stars3)):
            x = random.randint(-700, 700)
            y = random.randint(-600, 600)
            s = random.randint(1, 4)
            self.stars3_coordinats.append((x, y, s))
        for i in range(len(self.stars4)):
            x1 = random.randint(-200, 200)
            y1 = random.randint(-100, 100)
            self.stars4_coordinats.append((x1, y1))
        for i in range(len(self.stars5)):
            x1 = random.randint(-200, 200)
            y1 = random.randint(-100, 100)
            self.stars5_coordinats.append((x1, y1))

    def update_stars(self):
        alfa = 10
        for i in range(len(self.stars)):
            r = random.randint(0, 1)
            x, y = self.perspective_point_x + self.stars_coordinats[i][0], self.perspective_point_y + self.stars_coordinats[i][1]
            if r == 1:
                self.stars[i].ellipse = (x, y, self.star_x + r, self.star_y + r)
            else:
                self.stars[i].ellipse = (x, y, self.star_x + r/2, self.star_y + r/2)

        for i in range(len(self.stars1)):
            r = random.randint(0, 1)
            x, y = self.perspective_point_x + self.stars1_coordinats[i][0], self.perspective_point_y + self.stars1_coordinats[i][1]
            if r == 1:
                self.stars1[i].ellipse = (x+self.SPEED_X, y+self.SPEED_Y, self.star1_x + r, self.star1_y + r)
            else:
                self.stars1[i].ellipse = (x+self.SPEED_X, y+self.SPEED_Y, self.star1_x + r/2, self.star1_y + r/2)
        for i in range(len(self.stars2)):
            x, y, s = self.perspective_point_x + self.stars2_coordinats[i][0], self.perspective_point_y + self.stars2_coordinats[i][1], self.stars2_coordinats[i][2]
            self.stars2[i].ellipse = (x, y, self.star2_x + s/5, self.star2_y + s/5)
        for i in range(len(self.stars3)):
            x, y, s = self.perspective_point_x + self.stars3_coordinats[i][0], self.perspective_point_y + self.stars3_coordinats[i][1], self.stars3_coordinats[i][2]
            self.stars3[i].pos = (x, y)#, self.star2_x, self.star2_y)
            self.stars3[i].size = (self.star3_x + s, self.star3_y + s)

        for i in range(len(self.stars4)):
            x1, y1  = (self.perspective_point_x + self.stars4_coordinats[i][0]) + i * 10, (self.perspective_point_y + self.stars4_coordinats[i][1]) + i * 10
            self.stars4[i].vertices = [
            x1-1*alfa, y1+12*alfa, 0, 0,
            x1, y1+22*alfa, 0, 0,
            x1+1*alfa, y1+10*alfa, 0, 0,
            x1+11*alfa, y1+11*alfa, 0, 0,
            x1-1*alfa, y1+10*alfa, 0, 0,
            x1, y1, 0, 0,
            x1+1*alfa, y1+10*alfa, 0, 0,
            x1-11*alfa, y1+11*alfa, 0, 0,
            ]
            self.stars4[i].indices = [0, 1, 2, 3, 4, 5, 6, 7]

        for i in range(len(self.stars5)):
            x1, y1  = (self.perspective_point_x + self.stars5_coordinats[i][0]) + i * 10, (self.perspective_point_y + self.stars5_coordinats[i][1]) + i * 10
            self.stars5[i].vertices = [
            x1-1*alfa, y1+10*alfa, 0, 0, #0
            x1-11*alfa, y1+11*alfa, 0, 0, #1
            x1-1*alfa, y1+12*alfa, 0, 0, # 2
            x1, y1+22*alfa, 0, 0,        # 3
            x1+1*alfa, y1+12*alfa, 0, 0, # 4
            x1+11*alfa, y1+11*alfa, 0, 0, # 5
            x1+1*alfa, y1+10*alfa, 0, 0, #6
            x1, y1, 0, 0, #7
            ]
            self.stars5[i].indices = [0, 1, 2, 3, 4, 5, 6, 7]

    def update(self, dt):
        self.update_stars()

    def on_perspective_point_y(self, widget, value):
        print("PY: " + str(value))


class CosmoApp(App):
    pass

CosmoApp().run()