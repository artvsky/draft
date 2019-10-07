from graphics import *
import math 
"""
    Солнце
    x, y - координаты центра
    radius - радиус
    color - цвет двери
    size - масштаб
    """
def Draw_Sun(x, y, radius, color, size = 1):
    obj = Circle(Point(x, y), radius * size)
    obj.setFill(color)
    obj.draw(win)
    """
    Крыша
    x, y - координаты левого верхнего угла стены
    size - масштаб
    roof_color - цвет крыши
    win_color - цвет окон
    """
def Draw_Roof(x, y, size, roof_color, win_color):
    w = 174*size #ширина потолка
    h = 99*size #высота крыши
    obj = Polygon(Point(x - 34*size, y), Point( (x + w/2), y-h) , Point(x + w + 34*size, y))
    obj.setFill(roof_color)
    obj.draw(win)
    obj = Polygon(Point(x, y), Point( (x + w/2), y-h) , Point(x + w, y))
    obj.draw(win)
    obj.setFill(roof_color)
    Draw_Window1(x + w/3, y - 27*size, 14*size, size, win_color)
    Draw_Window1(x + w/3*2, y - 27*size, 14*size, size, win_color)
    """
    Круглое окно на крыше
    x, y - координаты центра окна
    radius - радиус
    size - масштаб
    color - цвет окна
    draw_line - рисовать ли рамы
    """
def Draw_Window1(x, y, radius, size, color, draw_line = True):
    obj = Circle(Point(x, y), radius)
    obj.setFill(color)
    obj.draw(win)
    if draw_line:
        line1 = Line(Point(x - radius*2/2, y), Point(x + radius*2/2, y))
        line2 = Line(Point(x, y - radius*2/2), Point(x, y + radius*2/2))
        line1.draw(win)
        line2.draw(win)
    """
    Прямоугольное окно
    x, y - координаты верхнего левого угла окна
    w, h - ширина и высота
    color - цвет окна
    draw_line - рисовать ли рамы
    """
def Draw_Window2(x, y, w, h, color, draw_line = True):
    obj = Rectangle(Point(x, y), Point(x + w, y + h))
    obj.setFill(color)
    obj.draw(win)
    if draw_line:
        line1 = Line(Point(x + w/2, y), Point(x + w/2, y + h))
        line1.draw(win)
        line1 = Line(Point(x + w/2, y + h/4), Point(x + w, y + h/4))
        line1.draw(win)
    """
    Дверь
    x, y - координаты верхнего левого угла
    size - масштаб
    color - цвет двери
    handlePos - местоположение ручки
    """
def Draw_Door(x, y, size, color, handlePos = "Right"):
    w = 32*size #ширина
    h = 66*size #высота 
    obj = Rectangle(Point(x, y), Point(x + w, y + h))
    obj.setFill(color)
    obj.draw(win)
    if (handlePos == "Right"):
        h = Circle(Point(x + w - 5*size, y + h/2), 2*size)
        h.setFill("#008000")
    else:
        h = Circle(Point(x + 5*size, y + h/2), 2*size)
        h.setFill("#008000")
    h.draw(win)        
    """
    Дом
    x, y - координаты верхнего левого угла стены
    size - масштаб
    house_color  - цвет дома
    roof_color  - цвет крыши
    win1_color  - цвет окон на крыше
    win2_color  - цвет окон в доме
    handlePos - местоположение ручки
    """
def Draw_House(x, y, size, house_color, roof_color, win1_color, win2_color):
    w = 174*size #ширина
    h = 136*size #высота
    obj = Rectangle(Point(x, y), Point(x + w, y + h))
    obj.setFill(house_color)
    obj.draw(win)
    Draw_Roof(x, y, size, roof_color, win1_color)
    Draw_Window2(x + 21*size, y + 18*size, 61*size, 31*size, win2_color,0 )
    Draw_Window2(x + 112*size, y + 18*size, 43*size, 19*size, win2_color,0 )
    Draw_Window2(x + 21*size, y + 68*size, 62*size, 48*size, win2_color,1 )
    Draw_Door(x + 118*size, y + 68*size, size, "#ff8040", "Right")
    """
    Облако
    x, y - координаты центра
    h, w - высота, ширина
    color - цвет
    size - масштаб
    """
def Draw_Cloud(x, y, h, w, color, size = 1):
    obj = Oval(Point(x - w/2*size, y - h/2*size ), Point(x + w/2*size, y + h/2*size))
    obj.setFill(color)
    obj.draw(win)
    """
    Дерево
    x, y - координаты верхнего левого угла ствола
    radius - радиус кроны
    size - масштаб
    """
def Draw_Tree(x, y, radius, size = 1):
    obj = Rectangle(Point(x, y), Point(x + 20*size, y + 130*size))
    obj.setFill("brown")
    obj.draw(win)
    obj = Circle(Point(x + 10*size, y), radius * size)
    obj.setFill("green")
    obj.draw(win)
    """
    Ребенок
    x, y - координаты центра головы
    size - масштаб
    """
def Draw_Child(x, y, size = 1):
    obj = Circle(Point(x, y), 20*size)
    obj.setFill("white")
    obj.draw(win)
    obj = Polygon(Point(x, y + 20*size), Point(x - 40*size, y + 80*size), Point(x + 40*size, y + 80*size))
    obj.setFill("red")
    obj.draw(win)
    obj = Line(Point(x, y + 20*size), Point(x + 40*size, y + 60*size))
    obj.draw(win)
    obj = Line(Point(x, y + 20*size), Point(x - 40*size, y + 60*size))
    obj.draw(win)
    obj = Line(Point(x - 10*size, y + 80*size), Point(x - 10*size, y + 110*size))
    obj.draw(win)
    obj = Line(Point(x + 10*size, y + 80*size), Point(x + 10*size, y + 110*size))
    obj.draw(win)


win = GraphWin("Home2D", 800, 600)

size1 = 1
size2 = 0.5

x1 = 247
y1 = 200
dx1 = 30
dy1 = 20

x2 = 50
y2 = 50
dx2 = 30
dy2 = 10

w="#804000"
t="red"
while True:
    r = Rectangle(Point(0,0), Point(800, 600))
    r.setFill("blue")
    r.draw(win)
    Draw_Cloud(200, 50, 20, 50, "lightblue",1)
    Draw_Cloud(300, 50, 20, 50, "lightblue", 2)
    Draw_Sun(568, 68, 32, "#ffff00", 1.5)
    Draw_Tree(600, 200, 50, 1.5)
    Draw_Child(100, 300, 1)
    time.sleep(0.01)
    
    x1+=dx1
    y1+=dy1

    x2+=dx2
    y2+=dy2
    
    if y1 >= 600 - 136*size1 or y1 <= 99*size1:
        dy1*=-1
        w,t=t,w
        
    if x1 >= 800 - (174+34)*size1 or x1 <= 34*size1:
        dx1*=-1
        w,t=t,w

    if y2 >= 600 - 136*size2 or y2 <= 99*size2:
        dy2*=-1
        w,t=t,w
    if x2 >= 800 - (174+34)*size2 or x2 <=34*size1:
        dx2*=-1
        w,t=t,w
    if (math.fabs( y2 + 18.5*size2 - (y1 + 18.5*size1) ) <= math.fabs(235*size1/2 + 235*size2/2 )) and (math.fabs(x2 + 174/2*size2 - (x1 + 174/2*size1)) <= math.fabs(174/2*size1 + 174/2*size2)) : 
        dy2*=-1
        dy1*=-1
        dx2*=-1
        dx1*=-1
        w,t=t,w
        
    Draw_House(x1, y1, size1, w , "#008080", "#00ffff", "#0080ff")
    Draw_House(x2, y2, size2,t , "#008080", "#00ffff", "#0080ff")       
        
    
    
win.getMouse()    
win.close()


