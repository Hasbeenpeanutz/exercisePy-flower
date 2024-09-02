import turtle

# engine = pyttsx3.init("sapi5")
# # kecepatan baca
# rate = engine.getProperty('rate')
# engine.setProperty('rate', 125)
# # jenis suara [0] male, [1] female
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id )

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('#262626')
t.pencolor('purple')
t.speed(100)
col = ('light blue', 'light green', 'yellow', 'orange', 'red')
for n in range (6):#loop warna
    for x in range (8):#loop jumplh kelopak bunga
        t.speed(x+10)
        for i in range (2):#garis untuk membuat kelopak
            t.pensize (2)
            t.circle (80+n*20, 90)
            t.lt (90)
        t.lt (45)
    t.pencolor (col[n%5])#jumplah warna yg ingin di loop
s.exitonclick()