# -*- coding: utf-8 -*-
from __cs1graphics import *
from time import sleep
MN1B = Canvas(1000,600, (240,240,240) , "Geometric Planes")

detail = Text('' , 17,Point(500 ,250))
#'',17,Point(500 ,250)
detail.setFontColor('white')
detail.setJustification('center')
_BGCOLOR = (179, 59, 36)

def setBG():
    BgImage = Image("Image/bg.gif")
    BgImage.moveTo(500,300)
    MN1B.add(BgImage)

def circle():
        _ = Circle(220)
        _.moveTo(500,250)
        _.setBorderWidth(0)
        _.setFillColor(_BGCOLOR)
        return _
    
def square():
    _ = Square(400)
    _.moveTo(500 , 250)
    _.setBorderWidth(0)
    _.setFillColor(_BGCOLOR)
    return _

def rectangle():
    _ = Rectangle(500,300)
    _.moveTo(500,250)
    _.setFillColor(_BGCOLOR)
    _.setBorderWidth(0)
    return _

def triangle():
    _ = Polygon(Point(500,30),Point(300,430) , Point(700,430))
    _.setFillColor(_BGCOLOR)
    _.setBorderWidth(0)
    return _

def pentagon():
    _ = Polygon(Point(500,30) , Point(250,250) , Point(350,500) , Point(650,500) , Point(750,250))
    _.setFillColor(_BGCOLOR)
    _.setBorderWidth(0)
    return _

def hexagon():
    _ = Polygon(Point(350,30) , Point(250,250) , Point(350,500) , Point(650,500) , Point(750,250) ,Point(650,30))
    _.setFillColor(_BGCOLOR)
    _.setBorderWidth(0)
    return _

def heptagon():
    _ = Polygon(Point(400,30) , Point(250,150) , Point(250,380) , Point(500,500) , Point(750,380) , Point(750,150) ,
                Point(600,30))
    _.setFillColor(_BGCOLOR)
    _.setBorderWidth(0)
    return _

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#

def cube():
    _ = Layer()
    l = Square(250)
    l.moveTo(400 , 300)
    l.setBorderWidth(0)
    l.setFillColor((31, 106, 125))
    _.add(l)
    
    h = Polygon(Point(525,425) , Point(675,325) , Point(675, 75) , Point(525,175))
    h.setFillColor((61, 113, 136))
    h.setBorderWidth(0)
    _.add(h)
    
    w = Polygon(Point(525,175), Point(675,75) , Point(425,75) ,Point(275,175))
    w.setFillColor((68, 121, 142))
    w.setBorderWidth(0)
    _.add(w)
    return _

def Cuboid():
    _ = Layer()
    l = Polygon(Point(525,425) , Point(525,175) , Point(100, 175) , Point(100,425))
    l.setBorderWidth(0)
    l.setFillColor((31, 106, 125))
    _.add(l)
    
    h = Polygon(Point(525,425) , Point(675,325) , Point(675, 75) , Point(525,175))
    h.setFillColor((61, 113, 136))
    h.setBorderWidth(0)
    _.add(h)
    
    w = Polygon(Point(525,175), Point(675,75) , Point(275,75) ,Point(100,175))
    w.setFillColor((68, 121, 142))
    w.setBorderWidth(0)
    _.add(w)

    _.move(30,0)
    return _
def Sphere():
    x ,y = 200,100
    _ = Layer()
    while x > 0 and y != 0:
        M = Circle(x , Point(500,250))
        M.setBorderWidth(0)
        M.setFillColor((205 - y, 221-y, 242 - y))
        _.add(M)
        x -= 7
        y -= 3
    return _
def ellipse():
    x , z , y = 400 , 290 , 130 
    el = Layer()
    while x > 0 and y != 0:
        M = Ellipse( x , z, Point(500,250))
        M.setBorderWidth(0)
        M.setFillColor((255 - y, 255 -  y, 255 - y))
        el.add(M)
        x -= 15
        z -= 10
        y -= 5
    return el

def cylinder():
    x , y = 400 , 171
    _ = Layer()
    while x > 0 and y != 0:
        M = Rectangle( x , 300, Point(500,250))
        M.setBorderWidth(0)
        M.setFillColor((200 - y, 245-y, 242 - y))
        _.add(M)
        x -= 15
        y -= 6
    c = Ellipse(400 , 50 , Point(500,100))
    c.setFillColor('white')
    c1 = Ellipse(400,50,Point(500 , 400))
    c1.setFillColor((205,221,242))
    _.add(c)
    _.add(c1)
    return _
def cone():
    _ = Layer()
    x , y ,z , k = 350 , 100 , 650 , 0
    while y < 400:
        Tri = Polygon(Point(500,y),Point(350,400) , Point(650 ,400))
        Tri.setFillColor((20 + k , 50 + k , 80 + k))
        Tri.setBorderWidth(0)
        _.add(Tri)
        y += 15
        x += 3.759398496
        z -= 3.759398496
        k += 3
        e = Ellipse(300 , 50 , Point(500,400))
        e.setFillColor('snow')
        _.add(e)
    return _

def Triangular_prism():
    _ = Layer()
    r = Polygon(Point(300,200) , Point(200,350) , Point(400,350))
    
    _.add(r)
    R = Rectangle(300,180 , Point(475,191))
    R.setFillColor((31, 106, 125))
    R.rotate(-33.5)
    R.setBorderWidth(0)
    r1 = Polygon(Point(200,350) , Point(400,350) , Point(652,184) , Point(454 , 184))
    r2 = r.clone()
    r.setFillColor((61, 113, 136))
    r.setBorderWidth(0)
    r2.move(250,-165)
    _.add(R)
    _.add(r1)
    _.add(r2)
    return _


twoD = [(1,'Circle' , circle()  , "Area of Circle \n" +
         "= %sr%s"%(u'\u03C0',u'\u00b2')),
        (2  , 'Square' , square(),'Area of Square \n'+
         "= x%s"%(u'\u00b2')),
        (3,'Rectangle'  , rectangle() , 'Area of a Rectangle \n = a x b'),
        (4 , 'Triangle' , triangle() , 'Area of Triangle \n = %s (b x h)'%(u'\u00BD')),
        (5 , 'Pentagon' , pentagon() , 'Angle: 108%s Interior angles add up to 540%s'%(u'\u030A',u'\u030A')),
        (6 , 'Hexagon' , hexagon() , 'Angle: 120%s Interior angles add up to 720%s'%(u'\u030A',u'\u030A')),
        (6 , 'Heptagon' , heptagon() , 'Angle: 128.6%s (to 1dp) Interior angles add up to 900%s'%(u'\u030A',u'\u030A'))
        ]

threeD = [(1,'Cubes' , cube()  , "Volume of a cube: \n = a%s \n Surface area of a cube: \n = 6s%s \nwhere a is the length of each side."%(u'\u00b3' ,u'\u00b2')),
          (2  , 'Cuboid' , Cuboid(),'Volume of a cuboid: \n= length x width x height = lwh \nSurface area of a cuboid: \n= 2lw + 2wh + 2lh '),
            (3, 'Sphere' , Sphere() , "Volume of a sphere: \n  4/3 πr3 \n Surface area of a sphere:  \n = 4πr2  \n where r is the radius of the sphere."),
          (4, 'Ellipse' , ellipse() , "Ellipse has no definite \nFormula to caclculate area and \nVolume"),
           (5, 'Cylinder' , cylinder() , "Volume of a cylinder \n = πr2h \nSurface area of an open cylinder:\n= 2πrh\nSurface area of a closed cylinder:\n= 2πrh + 2πr2 = 2πr(r+h)\nwhere r is the radius \nof the cylinder and h is the height. "),
          (6, 'Cone' , cone() , "where r is the radius of the \n widest part of the cone, and \nh is the height of the cone.\nSurface area of a cone \n(including base):\n= πr2 + πrs \n Surface area of a cone \n(excluding base):\n= πrs") ,
          (6, 'Triangular Prism' , Triangular_prism() , "Trianglur Prism has no definite \nFormula to caclculate area and \nVolume")
                    ]

class Next(EventHandler):
    def handle(self, event):
        global x , y
        x += 0.5
        y =  True
        
class Prev(EventHandler):
    def handle(self, event):
        global x , y
        x -= 0.5
        y =  True
        
class Main_BT(EventHandler):   
    def handle(self, event):
        global y
        MN1B.clear()
        y = '$'
class _2DBT(EventHandler):   
    def handle(self, event):
        global bt , y , x , size  , _X_
        bt , y , x  , size  , _X_ = '2D' , True , 1 , 1 , twoD
        
class _3DBT(EventHandler):   
    def handle(self, event):
        global bt , y , x ,size , _X_
        bt , y , x ,size , _X_= '3D' , True , 1  , 1, threeD
class _N(EventHandler):   
    def handle(self, event):
        print '%-25s  %-30s'%('Name ','ID')
        print '='*20
        for i, j in [('Wendirad Demelash', 'UGR/17757/11' ), ('Tefera Abebe' , 'UGR/17896/11')]:
            print '%-25s  %-30s'%(i,j)
        print '='*12 
    
        
   
def Main_menu():
    __2D_ = _2DBT()
    __3D_ = _3DBT()
    __D = _N()
    MN1B.setTitle('Main Menu')
    setBG()
    _2D = Button('2D', Point(300,300))
    _2D.setBorderWidth(3)
    _2D.setBorderColor((0,0,128))
    _2D.setFillColor((0,0,128))
    _2D.setFontColor('white')
    _2D.setFontSize(75)
    _2D.setHeight(170)
    _2D.setWidth(170)
    
    _3D = Button('3D', Point(500,300))
    _3D.setBorderWidth(3)
    _3D.setBorderColor((0,0,128))
    _3D.setFillColor((0,0,128))
    _3D.setFontColor('white')
    _3D.setFontSize(75)
    _3D.setHeight(170)
    _3D.setWidth(170)
    _3D.move(200,0)
    _2D.addHandler(__2D_)
    _3D.addHandler(__3D_)

    _D = Button('Team Name', Point(500,500))
    _D.setBorderWidth(3)
    _D.setBorderColor((0,0,128))
    _D.setFillColor((0,0,128))
    _D.setFontColor('white')
    _D.setFontSize(14)
    _D.setHeight(70)
    _D.setWidth(270)
    _D.addHandler(__D)
    
    MN1B.add(_2D)
    MN1B.add(_3D)
    MN1B.add(_D)
def BT():
    Next_ = Next()
    Prev_ = Prev()
    Main_ = Main_BT()


    _M = Button('Main Menu' ,Point(920,40))
    _M.setBorderWidth(3)
    _M.setBorderColor((0,128,128))
    _M.setFillColor((0,128,128))
    _M.setFontColor('white')
    _M.setFontSize(15)
    _M.setHeight(30)
    _M.setWidth(120)
    _M.addHandler(Main_)
    
    _ = Button('Next' ,Point(800,550))
    _.setBorderColor((0,128,128))
    _.setFillColor((0,128,128))
    _.setFontColor('white')
    _.setFontSize(17)
    _.setHeight(30)
    _.setWidth(120)

    __ = Button('Prev' ,Point(200,550))
    __.setBorderColor((0,128,128))
    __.setFillColor((0,128,128))
    __.setFontColor('white')
    __.setFontSize(17)
    __.setHeight(30)
    __.setWidth(120)
    
    _.addHandler(Next_)
    __.addHandler(Prev_)
    _M.addHandler(Main_)
    
    MN1B.add(_)
    MN1B.add(__)
    MN1B.add(_M)    

setBG()
man = Layer()
face = Ellipse(100,120,Point(250,180))
face.setBorderWidth(0)
face.setFillColor((222, 184, 135))

left_eye = Ellipse(24,9,Point(225,175))
left_eye.setFillColor('white')

right_eye =  left_eye.clone()
right_eye.move(50,0)

eye_ball_left = Ellipse(5,7,Point(225 , 175))
eye_ball_left.setFillColor((128, 0, 0))

eye_ball_right = eye_ball_left.clone()
eye_ball_right.move(50 , 0)

eye_lash = Spline(Point(210,168) , Point(230,158) ,Point(240,169))
eye_lash.setBorderWidth(3)

eyelash = Spline(Point(260,169),Point(270,158),Point(290,168)) 
eyelash.setBorderWidth(3)

nose = Ellipse(10,30,Point(249,190))
nose.setBorderWidth(0)
nose.setFillColor((200, 160, 110))
nose.setDepth(0)
Nose = Ellipse(22,9,Point(249,197))
Nose.setDepth(10)
Nose.setBorderWidth(0)
Nose.setFillColor((190, 150, 100))


mouse_ = ClosedSpline(Point(230,217),Point(250,229),Point(270,217))
mouse_.setBorderWidth(2)
mouse_.setBorderColor('brown')
mouse_.setFillColor('white')
Hat = ClosedSpline(Point(185,30),Point(182,110),Point(170,115),Point(250,125),
               Point(325,115) , Point(315,114),Point(315,30))
Hat.scale(0.65)
Hat.move(25,68)
Hat.setFillColor('brown')


_ = Ellipse(60 , 50 ,Point(250,230))
_.setBorderWidth(0)
_.setFillColor('grey')


ear = Ellipse(115 ,50,Point(250,180))
ear.setDepth(100)
ear.setBorderWidth(0)
ear.setFillColor((200, 162, 113))
ear_ = Ellipse(110,30,Point(250,190))
ear_.setBorderWidth(0)
ear_.setDepth(101)
ear_.setFillColor((200, 162, 113))


body = ClosedSpline(Point(190,230),Point(220,310),Point(190,470),
                    Point(250,480),Point(320,470),Point(280,310),Point(310,230))
body.setBorderWidth(0)
body.setFillColor('maroon')

hand =Rectangle(20,50,Point(197,280))
hand.setFillColor('maroon')
hand.setBorderWidth(0)
hand.rotate(30)


hand_ = Rectangle(20,60,Point(176,315))
hand_.setFillColor('maroon')
hand_.setBorderWidth(0)
hand_.rotate(30)
ha = Rectangle(20,30 ,Point(160,340))
ha.rotate(30)
ha.setBorderWidth(0)
ha.setFillColor('sandybrown')

lhand = hand.clone()
lhand.move(105,0)
lhand.rotate(-60)

lhand_ = hand_.clone()
lhand_.move(145,0)
lhand_.rotate(-60)


lha = ha.clone()
lha.move(175,0)
lha.rotate(-60)

Leg=Layer()
MN1B.add(Leg)

shu1=Rectangle(23,43,Point(223,500))
shu1.rotate(30)
shu1.setFillColor('maroon')
shu2=shu1.clone()
shu2.moveTo(288,500)
shu2.rotate(-60)
Leg.add(shu1)
Leg.add(shu2)

leg1 = Rectangle(20,80,Point(230,450))
leg1.setFillColor('sandybrown')
Leg.add(leg1)
leg2=leg1.clone()
leg2.moveTo(280,450)
Leg.add(leg2)



man.add(lha)
man.add(lhand)
man.add(lhand_)
man.add(ha)
man.add(hand_)

man.add(body)
man.add(face)
man.add(hand)

man.add(left_eye)
man.add(right_eye)
man.add(eye_ball_left)
man.add(eye_ball_right)
man.add(eye_lash)
man.add(eyelash)
man.add(nose)
man.add(Nose)
man.add(ear)
man.add(ear_)
man.add(Hat)
man.add(_)
man.add(mouse_)


MN1B.add(man)
sleep(1)
hand_.rotate(-60)
ha.rotate(-60)
hand_.move(0,-40)
ha.move(0,-90)

t = TextBox(500 , 450 , Point(650 , 300))
MN1B.add(t)
t.setMessage('Hello , I\'m Euclid of Alexandria \nThe Father of Geometry! \nNow i\'m Gone show you some Plane')
t.setFontSize(20)
t.setFontColor('brown')
sleep(2)
hand_.rotate(60)
ha.rotate(60)
hand_.move(0,40)
ha.move(0,90)
sleep(2)
t.setMessage('Select which Geometrical Plane \nDo you Want To See on The next Screen\nEvery time when you want change \nPress The Main menu button \n on the top right corner')
t.setFontSize(20)
t.setFontColor('brown')
sleep(5)




def start():
    global y , x , size , _X_
    if y:
        x = 1
        setBG()
        BT()
        MN1B.add(detail)
        MN1B.add(_X_[0][2])
        MN1B.setTitle(twoD[0][1])
        removed = _X_[0][2]
    while True:
        if y is '$':
            Menu()
            MN1B.remove(detail)
        elif  y:
            if len(MN1B.getContents()) > 0:
                MN1B.remove(removed)
                MN1B.remove(detail)
                removed = _X_[int(x-1)%size][2]
                MN1B.add(removed)
                MN1B.add(detail)
                detail.setMessage(_X_[int(x-1)%size][-1])
                MN1B.setTitle(_X_[int(x-1) % size][1])
                if _X_ == threeD:
                    detail.setFontSize(17)
                    detail.moveTo(850,300)
                    detail.setFontColor('black')
                else:
                    detail.moveTo(500 ,250)
                    detail.setFontColor('white')
                    
                y = False
def Menu():
    global bt , size , _X_ 
    bt = 0
    Main_menu()
    while True:
        if bt == '2D':
            _X_ = twoD
            size = len(_X_)
            start()
        elif bt == '3D':
            _X_ = threeD
            size = len(_X_)
            start()
        
Menu()
