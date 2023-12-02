from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics.vertex_instructions import Ellipse, Line, Rectangle
from kivy.graphics.context_instructions import Color
from kivy.properties import Clock
from kivy.properties import NumericProperty
import random, time


class MainWidget(RelativeLayout):

    stars = list()
    stars1 = list()
    stars2 = list()
    stars3 = list()


    stars_coordinats = list()
    stars1_coordinats = list()
    stars2_coordinats = list()
    stars3_coordinats = list()


    star_x = 1
    star_y = 1
    star1_x = 1
    star1_y = 1
    star2_x = .5
    star2_y = .5
    star3_x = 2
    star3_y = 2

    STAR_NB = 60
    STAR1_NB = 50
    STAR2_NB = 800
    STAR3_NB = 40


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
                    Color(1, 174.0/255.0, 0)
                elif r == 1:
                    Color(29.0/255.0, 186.0/255.0, 255.0/255.0)
                else:
                    Color(1, 0, 0)
                self.stars1.append(Line())
        for i in range(self.STAR2_NB):
            with self.canvas:
                Color(1, 1, 1)
                self.stars2.append(Line())
        for i in range(self.STAR3_NB):
            with self.canvas:
                Color(1, 1, 1)
                self.stars3.append(Ellipse())

    def generate_stars_coordinate(self):
        for i in range(len(self.stars)):
            x = random.randint(0, 1400)
            y = random.randint(0, 800)
            self.stars_coordinats.append((x, y))
        for i in range(len(self.stars1)):
            x = random.randint(0, 1400)
            y = random.randint(0, 800)
            self.stars1_coordinats.append((x, y))
        for i in range(len(self.stars2)):
            x = random.randint(0, 1400)
            y = random.randint(0, 800)
            s = random.randint(1, 4)
            self.stars2_coordinats.append((x, y, s))
        for i in range(len(self.stars3)):
            x = random.randint(0, 1400)
            y = random.randint(0, 800)
            s = random.randint(1, 4)
            self.stars3_coordinats.append((x, y, s))


    def update_stars(self):
        for i in range(len(self.stars)):
            r = random.randint(0, 1)
            x, y = self.stars_coordinats[i][0], self.stars_coordinats[i][1]
            self.stars[i].ellipse = (x, y, self.star_x + r, self.star_y + r)
        for i in range(len(self.stars1)):
            r = random.randint(0, 1)
            x, y = self.stars1_coordinats[i][0], self.stars1_coordinats[i][1]
            self.stars1[i].ellipse = (x+self.SPEED_X, y+self.SPEED_Y, self.star1_x + r, self.star1_y + r)
        for i in range(len(self.stars2)):
            x, y, s = self.stars2_coordinats[i][0], self.stars2_coordinats[i][1], self.stars2_coordinats[i][2]
            self.stars2[i].ellipse = (x, y, self.star2_x + s/10, self.star2_y + s/10)
        for i in range(len(self.stars3)):
            x, y, s = self.stars3_coordinats[i][0], self.stars3_coordinats[i][1], self.stars3_coordinats[i][2]

            self.stars3[i].pos = (x, y)#, self.star2_x, self.star2_y)
            self.stars3[i].size = (self.star3_x + s, self.star3_y + s)


    def update(self, dt):
        self.update_stars()


class CosmoApp(App):
    pass

CosmoApp().run()