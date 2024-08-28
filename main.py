import pygame, math, os, sys
from pygame.locals import *
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QComboBox, QPushButton, QLineEdit
from PyQt6.QtGui import QColor, QIntValidator, QDoubleValidator

class MainWindow(QWidget):  
    def __init__(self):  

        super().__init__()   
        self.initUI()
    def initUI(self):  
        
        #init main window
        self.setWindowTitle('Configuration')  
        self.setGeometry(100, 100, 400, 300)  
        mainlayout=QVBoxLayout
        
        """
        huge amounts of pyqt gui code. no more explaination.
        """
        
        """row 1"""
        layout1 = QHBoxLayout()  
        self.label1 = QLabel('Config Circle Color', self)  
        layout1.addWidget(self.label1)  
        self.combo1 = QComboBox(self)  
        self.combo2 = QComboBox(self)  
        self.combo3 = QComboBox(self)  
        for i in range(256):
            self.combo1.addItem(str(i))
            self.combo2.addItem(str(i))
            self.combo3.addItem(str(i))
        self.combo1.currentIndexChanged.connect(self.updateColor1)
        self.combo2.currentIndexChanged.connect(self.updateColor2)
        self.combo3.currentIndexChanged.connect(self.updateColor3)
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.combo1)
        hbox1.addWidget(self.combo2)
        hbox1.addWidget(self.combo3) 
        self.colorLabel1=QLabel(' ', self)
        self.colorLabel1.setFixedSize(40, 40)
        layout1.addLayout(hbox1)
        layout1.addWidget(self.colorLabel1)
        
        """row 2"""
        layout2 = QHBoxLayout()
        self.label2 = QLabel('Config Track Color', self)
        layout2.addWidget(self.label2)
        self.combo4 = QComboBox(self)
        self.combo5 = QComboBox(self)
        self.combo6 = QComboBox(self)
        for i in range(256):
            self.combo4.addItem(str(i))
            self.combo5.addItem(str(i))
            self.combo6.addItem(str(i))
        self.combo4.currentIndexChanged.connect(self.updateColor2)
        self.combo5.currentIndexChanged.connect(self.updateColor2)
        self.combo6.currentIndexChanged.connect(self.updateColor2)
        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.combo4)
        hbox2.addWidget(self.combo5)
        hbox2.addWidget(self.combo6)
        self.colorLabel2=QLabel(' ', self)
        self.colorLabel2.setFixedSize(40, 40)
        layout2.addLayout(hbox2)
        layout2.addWidget(self.colorLabel2)
        
        """row 3"""
        layout3 = QHBoxLayout()
        label3 = QLabel('Config Background Color', self)
        layout3.addWidget(label3)
        self.combo7 = QComboBox(self)
        self.combo8 = QComboBox(self)
        self.combo9 = QComboBox(self)
        for i in range(256):
            self.combo7.addItem(str(i))
            self.combo8.addItem(str(i))
            self.combo9.addItem(str(i))
        self.combo4.currentIndexChanged.connect(self.updateColor3)
        self.combo5.currentIndexChanged.connect(self.updateColor3)
        self.combo6.currentIndexChanged.connect(self.updateColor3)
        hbox3 = QHBoxLayout()
        hbox3.addWidget(self.combo4)
        hbox3.addWidget(self.combo5)
        hbox3.addWidget(self.combo6)
        self.colorLabel3=QLabel(' ', self)
        self.colorLabel3.setFixedSize(40, 40)
        layout3.addLayout(hbox3)
        layout3.addWidget(self.colorLabel3)
        """
        combobox 1-3 control circle color = circle color(tuple)
        combobox 4-6 control track color = track color(tuple)
        combobox 7-9 control bgcolor = background color(tuple)
        """
        
        """row 4:window W&H"""
        layout4 = QHBoxLayout()
        label4 = QLabel("Demo Window Size")
        self.input1 = QLineEdit(self)
        self.input2 = QLineEdit(self)
        int_positive_validator = QIntValidator(1, 2147483647, self)
        self.input1.setValidator(int_positive_validator)  
        self.input2.setValidator(int_positive_validator)
        hbox4=QHBoxLayout()
        hbox4.addWidget(self.input1)
        hbox4.addWidget(self.input2)
        hbox4_widget=QWidget()
        hbox4_widget.setLayout(hbox4)
        layout4.addWidget(label4)
        layout4.addWidget(hbox4_widget)
        
        """row 5:graph offset x,y"""
        layout5 = QHBoxLayout()
        self.label5 = QLabel("Graph offset")
        self.input3 = QLineEdit(self)
        self.input4 = QLineEdit(self)
        int_validator = QIntValidator(-2147483648, 2147483647, self)
        self.input3.setValidator(int_validator)  
        self.input4.setValidator(int_validator)
        hbox5=QHBoxLayout()
        hbox5.addWidget(self.input3)
        hbox5.addWidget(self.input4)
        layout5.addWidget(self.label5)
        layout5.addWidget(hbox5)
        
        """row 6:scale (double) and fps (int)"""
        layout6=QHBoxLayout()
        self.label6=QLabel("Graph Scale")
        self.double_input=QLineEdit(self)
        double_validator = QDoubleValidator(0.001, sys.float_info.max, 3, self)
        self.double_input.setValidator(double_validator)
        self.label7=QLabel("Framerate")
        self.input5=QLineEdit(self)
        self.input5.setValidator(int_positive_validator)
        layout6.addWidget(self.label6)
        layout6.addWidget(self.double_input)
        layout6.addWidget(self.label7)
        layout6.addWidget(self.input5)
        
        """row 7"""
        layout7=QHBoxLayout
        btn_close = QPushButton('Continue', self)
        btn_close.clicked.connect(self.close)
        layout7.addWidget(btn_close)

        mainlayout.addLayout(layout1)
        mainlayout.addLayout(layout2)
        mainlayout.addLayout(layout3)
        mainlayout.addLayout(layout4)
        mainlayout.addLayout(layout5)
        mainlayout.addLayout(layout6)
        mainlayout.addLayout(layout7)
        self.setLayout(mainlayout)

    """
    handle 3 color displayer. used label to save some work.
    color1-3 = combobox 1-3,4-6,7-9
    """
    def updateColor1(self):
        rgb1 = (int(self.combo1.currentText()), int(self.combo2.currentText()), int(self.combo3.currentText()))  
        color = QColor(*rgb1)  
        self.colorLabel1.setStyleSheet(f"background-color: rgb({', '.join(map(str, rgb1))});")  
    def updateColor2(self):  
        rgb2 = (int(self.combo4.currentText()), int(self.combo5.currentText()), int(self.combo6.currentText()))  
        color = QColor(*rgb2)  
        self.colorLabel2.setStyleSheet(f"background-color: rgb({', '.join(map(str, rgb2))});")  
    def updateColor3(self):  
        rgb3 = (int(self.combo7.currentText()), int(self.combo8.currentText()), int(self.combo9.currentText()))  
        color = QColor(*rgb3)  
        self.colorLabel3.setStyleSheet(f"background-color: rgb({', '.join(map(str, rgb3))});")
    
    def closeEvent(self, event):
        circle_color = (int(self.combo1.currentText()), int(self.combo2.currentText()), int(self.combo3.currentText()))
        track_color = (int(self.combo4.currentText()), int(self.combo5.currentText()), int(self.combo6.currentText()))
        background_color = (int(self.combo4.currentText()), int(self.combo5.currentText()), int(self.combo6.currentText()))
        window_W=(int(self.input1.text()))
        window_H=(int(self.input2.text()))
        offsetx=(int(self.input3.text()))
        offsety=(int(self.input4.text()))
        scale=(float(self.double_input.text))
        fps=(float(self.input5.text()))
        
        game(circle_color,track_color,background_color,window_W,window_H,offsetx,offsety,scale,fps)
        
        # 如果不需要阻止关闭，可以简单地让事件继续  
        event.accept()  

def game(ccolor,tcolor,bgcolor,window_W,window_H,offx,offy,scale,fps):
    
    """
    window_W = 1500
    window_H = 1000
    one_time = 1  # time speed (1 by default)
    scale = 0.75  # scale
    fps = 144
    b_scale = 1
    ccolor = (250, 220, 70) # circle color
    """
    
    point_size = 1
    start_xy = (window_W // 2+offx, window_H // 2+offy)  # offset for everything.
    b_length = 16384

    from fourier import PP

    fourier_list = PP[:]

    # initialize pygame
    pygame.init()
    pygame.mixer.init()
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (10, 70)
    # show window
    screen = pygame.display.set_mode((window_W, window_H), pygame.DOUBLEBUF, 32)
    pygame.display.set_caption("FFT-image-drawing DEMO")
    #font = pygame.font.SysFont('simhei', 20)

    class Circle():
        x, y = 0, 0
        r = 0
        angle = 0
        angle_v = 0
        color = (0, 0, 0)
        father = None

        def __init__(self, r, angle_v, angle, color=None, father=None):
            self.r = r
            self.angle_v = angle_v
            self.angle = angle
            self.father = father
            if color is None:
                self.color = (250, 250, 250)
            else:
                self.color = color

        def set_xy(self, xy):
            self.x, self.y = xy

        def get_xy(self):
            return self.x, self.y

        def set_xy_by_angle(self):
            self.x = self.father.x + self.r * math.cos(self.angle) * scale
            self.y = self.father.y + self.r * math.sin(self.angle) * scale

        def run(self, step_time):
            if self.father is not None:
                self.angle += self.angle_v * step_time
                self.set_xy_by_angle()

        def draw(self, screen):
            color_an = tuple(map(lambda x: x // 3, self.color))
            """ draw circle
            print(color_an, int(round(self.x)), self.y) """
            pygame.draw.circle(screen, self.color, (int(round(self.x)), int(round(self.y))), point_size)
            if self.father is not None:
                """ print(color_an, self.father.x, self.father.y) """
                pygame.draw.circle(screen, color_an, (int(round(self.father.x)), int(round(self.father.y))),max(int(round(abs(self.r) * scale)), 1),1)
                pygame.draw.line(screen, self.color, (self.father.x, self.father.y), (self.x, self.y),1)

    class Boxin():
        xys = []

        def add_point(self, xy):
            self.xys.append(xy)
            if len(self.xys) > b_length:
                self.xys.pop(0)

        def draw(self, screen):
            bl = len(self.xys)
            for i in range(bl - 1):
                pygame.draw.line(screen, tcolor, self.xys[i], self.xys[i + 1], 2) #draw track

    super_circle = Circle(0, 0, 0, color=ccolor)
    super_circle.set_xy(start_xy)
    circle_list = [super_circle]
    for i in range(len(fourier_list)):
        p = fourier_list[i]
        circle_list.append(Circle(p[0], p[1], p[2], color=ccolor, father=circle_list[i]))

    bx = Boxin()
    clock = pygame.time.Clock()

    # game main cycle
    while True:
        
        # handle exit operation
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        # background
        screen.fill(bgcolor)
        # run
        for i, circle in enumerate(circle_list):
            circle.run(1)
            circle.draw(screen)

        last_circle = circle_list[-1]
        bx.add_point((last_circle.x, last_circle.y))
        bx.draw(screen)

        pygame.display.update()
        time_passed = clock.tick(fps)
if __name__ == '__main__':  
    app = QApplication(sys.argv)  
    ex = MainWindow()  
    ex.show()  
    sys.exit(app.exec())