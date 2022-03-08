import pygame
import wall
import config

class Layouts:
    layouts = []

    def __init__(self,layout_type : int):
        self.group = pygame.sprite.Group()
        self.wall_color = None
        self.bg_color = None

        self.set_layout1()
        self.set_layout2()
        
        for layout in self.layouts[layout_type-1]:
            self.group.add(wall.Wall(self.wall_color,layout[0],layout[1]))

        self.rectangle()

    def get_group(self):
        return self.group

    def get_bg_color(self):
        return self.bg_color

    def rectangle(self):
        self.group.add(wall.Wall(self.wall_color,(800,26),(400,70)))
        self.group.add(wall.Wall(self.wall_color,(800,26),(400,537)))

        self.group.add(wall.Wall(self.wall_color,(26,441),(13,303)))
        self.group.add(wall.Wall(self.wall_color,(26,441),(787,303)))

    def set_layout1(self):
        self.wall_color = "#EE9A50"
        self.bg_color = "#8A963B"

        layout_temp = []

        layout_temp.append([config.RECT7,(500, 308)])
        layout_temp.append([config.RECT7,(300, 308)])

        layout_temp.append([config.RECT8,(400, 203)])
        layout_temp.append([config.RECT8,(400, 403)])

        layout_temp.append([config.RECT5,(650, 303)])
        layout_temp.append([config.RECT5,(150, 303)])

        layout_temp.append([config.RECT1,(670, 259)])
        layout_temp.append([config.RECT1,(670, 347)])

        layout_temp.append([config.RECT1,(130,259)])
        layout_temp.append([config.RECT1,(130,347)])
        
        self.layouts.append(layout_temp)

    def set_layout2(self):
        self.wall_color = "#D8A93F"
        self.bg_color = "#902608"

        layout_temp = []

        layout_temp.append([config.RECT9,(650,303)])
        layout_temp.append([config.RECT9,(150,303)])

        layout_temp.append([config.RECT4,(400, 509)])
        layout_temp.append([config.RECT4,(400, 98)])

        layout_temp.append([config.RECT1,(670,229)])
        layout_temp.append([config.RECT1,(670,377)])

        layout_temp.append([config.RECT1,(130,229)])
        layout_temp.append([config.RECT1,(130,377)])

        layout_temp.append([config.RECT1,(291,407)])
        layout_temp.append([config.RECT2,(311,427)])

        layout_temp.append([config.RECT1,(509,407)])
        layout_temp.append([config.RECT2,(489,427)])

        layout_temp.append([config.RECT1,(291,199)])
        layout_temp.append([config.RECT2,(311,179)])

        layout_temp.append([config.RECT1,(509,199)])
        layout_temp.append([config.RECT2,(489,179)])

        layout_temp.append([config.RECT4,(225,303)])
        layout_temp.append([config.RECT4,(565,303)])

        layout_temp.append([config.RECT2,(180,131)])
        layout_temp.append([config.RECT2,(620,131)])
        layout_temp.append([config.RECT2,(180,466)])
        layout_temp.append([config.RECT2,(620,466)])

        self.layouts.append(layout_temp)
