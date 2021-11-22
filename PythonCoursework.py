from tkinter import *
from random import *
import time
#Constants used throughout the program

Birds = []
left_bird = []
bullet = []
p=1
initial_score = 0
m=1
loadstate = []
scoress = {}

f = open("leaderboards.txt","r")
data = f.read()
data = data.strip()
data = data.strip("\n")
datas = data.split(",")
datas.pop()
for item in datas:
    sep = item.index(":")
    scoress[item[0:sep]] = item[sep+1:len(item)]

print(scoress)





# img = PhotoImage(file = "images/hunter.png")


def MenuScreen():
     Sky.delete("all")
     Sky.pack_forget()
     if len(loadstate) == 0:
         Menu.delete("all")
         Menu.pack()

         Gameplay = Button(Menu,width=10,text="New Game",font = ("Arial",25),fg="orange",command = nameandcontrol)
         wind1 = Menu.create_window(960,450,window=Gameplay)
         Leaderboards = Button(Menu,width=10,text="High Scores",font = ("Arial",25),fg = "orange",command = Displayleaders)
         wind2 = Menu.create_window(960,550,window=Leaderboards)
     else:
        Menu.delete("all")
        Menu.pack()

        Gameplay = Button(Menu,width=10,text="New Game",font = ("Arial",25),fg="orange",command = Gamespacecreate)
        wind1 = Menu.create_window(960,350,window=Gameplay)
        State = Button(Menu,width=10,text="Load Game",font = ("Arial",25),fg="orange",command = Gamespacecreate)
        wind3 = Menu.create_window(960,350,window=State)
        Leaderboards = Button(Menu,width=10,text="High Scores",font = ("Arial,25"),fg = "orange",command = Displayleaders)
        wind2 = Menu.create_window(960,550,window=Leaderboards)


def nameandcontrol():
    Menu.delete("all")
    Prompt = Label(Menu,text = "Enter your nickname",font = ("Arial",25))
    prompwindow = Menu.create_window(960,150,window=Prompt)
    nameentry = Entry(Menu)
    namewindow = Menu.create_window(960,300,window=nameentry)
    Prompt2 = Label(Menu,text = "Pick your controls",font = ("Arial",25))
    prompwindow = Menu.create_window(960,400,window=Prompt2)

    LorR = Button(Menu,width=10,text="Left and Right",font = ("Arial",25),fg="orange",command = leftandright)
    choice1 = Menu.create_window(700,600,window=LorR)
    AorD = Button(Menu,width=10,text="A and D",font = ("Arial",25),fg = "orange",command = AandD)
    choice2 = Menu.create_window(1200,600,window=AorD)

def leftandright():
    window.bind("<Left>",left)
    window.bind("<Right>",right)
    Gamespacecreate()

def AandD():
    window.bind("<a>",left)
    window.bind("<d>",right)
    Gamespacecreate()





def Displayleaders():
    global scoress
    Menu.delete("all")
    names = list(scoress.keys())
    names.sort()
    points = list(scoress.values())
    points.sort(reverse=True)
    highscores = [points[0],points[1],points[2]]
    scorers=[]
    for i in highscores:
        for j in names:
            if scoress[j] == i:
                scorers.append(j)
                break
    print(scorers,highscores)
    Title = Label(Menu,text = "LEADERBOARDS",font = ("Arial",50))
    Titlewindow = Menu.create_window(960,100,window = Title)
    Title1 = Label(Menu,text = scorers[0] + "   :    " + highscores[0],font = ("Arial",40),fg = "orange")
    Titlewindow1 = Menu.create_window(960,400,window = Title1)
    Title2 = Label(Menu,text = scorers[1] + "   :    " + highscores[1],font = ("Arial",40),fg = "orange")
    Titlewindow2 = Menu.create_window(960,500,window = Title2)
    Title3 = Label(Menu,text = scorers[2] + "   :    " + highscores[2],font = ("Arial",40),fg = "orange")
    Titlewindow3 = Menu.create_window(960,600,window = Title3)
    Backbutton = Button(Menu,text = "Back",font=("Arial",20),fg = "orange",command = MenuScreen)
    Backbuttonwindow = Menu.create_window(100,800,window=Backbutton)









def left(event):
    global Sky
    global Hunter
    global m
    Huntercoordinates = Sky.bbox(Hunter)
    if Huntercoordinates[0] == 0 or m == 0:
        pass
    else:
        Sky.move(Hunter,-10,0)


def right(event):
    global Sky
    global m
    global Hunter
    Huntercoordinates = Sky.bbox(Hunter)
    if Huntercoordinates[2] > 1920 or m == 0:
        pass
    else:
        Sky.move(Hunter,10,0)

def up(event):
    global Sky
    Huntercoordinates = Sky.coords(Hunter)
    if Huntercoordinates[0] == 0 or m == 0:
        pass
    else:
        Sky.move(Hunter,10,0)

def down(event):
    global Sky
    Huntercoordinates = Sky.coords(Hunter)
    if Huntercoordinates[0] == 0 or m == 0:
        pass
    else:
        Sky.move(Hunter,10,0)


def Cheats():
    global p
    global m
    global bullet
    global t
    global Cheat
    if p==1:
        p=0
        m=0
        boss = 0
        bullet.append(0)
        Cheatask = Label(Sky,text = "Enter Cheat",font = ("Arial",20))
        Cheatwindow = Sky.create_window(960,300,window = Cheatask,tags = "illegal")
        Cheat = Entry(Sky)
        Chwindow = Sky.create_window(960,400,window = Cheat,tags = "illeagle")
        Apply = Button(Sky,text = "Apply",font = ("Arial",20),command=Cheats)
        Applywindow = Sky.create_window(960,500,window = Apply,tags = "eagleill")
        pausebutton.configure(state=DISABLED)
        while 1>0:
            pass
            if p == 1:
                break
            window.update()
    else:
        cheatcode = Cheat.get()
        if cheatcode == "Scorepls":
            Scoreupdate(10)
        elif cheatcode == "Timepls":
            t = 0
            Countdown(t)
        else:
            pass
        Sky.delete("illegal")
        Sky.delete("illeagle")
        Sky.delete("eagleill")
        pausebutton.configure(state=NORMAL)
        p=1
        m=1
        boss = 1
        bullet.pop()










def Pausegame():
    global pausebutton
    global p
    global m
    global bullet
    if p == 1:
        pausebutton.configure(text = "Unpause")
        p = 0
        m = 0
        bullet.append(0)

        # Cheatask = Label(Sky,text = "Enter a Cheat(even though you shouldnt)",font = ("Arial",20))
        # Cheatask.pack(ipadx=800,ipady=400)
        # Cheat = Entry(Sky)
        # Cheat.place(x=910,y=540,width = 100,height = 20)
        while 1>0:
            pass
            if p == 1:
                break
            window.update()
    else:
        pausebutton.configure(text = "Pause")
        p = 1
        m = 1
        bullet.pop()



def Bosskey(event):
    if boss == 1:
        window.destroy()

def Gamespacecreate():
    global Hunter
    global Sky
    global Score
    global Time
    global score
    global tim
    global pausebutton
    global p
    global Menu
    Menu.delete("all")
    Menu.pack_forget()
    Sky.pack()
    Ground = Sky.create_rectangle(-100,1080,2020,780,fill = "green",outline = "green")
    Sun = Sky.create_oval(1600,100,1700,200,fill = "yellow")
    Hunter = Sky.create_image(960,540,anchor=NW,image=img)
    Score = Label(Sky,textvariable = score)
    Score.grid(row=0)
    Sky.create_window(960,50,window = Score,tags="scoreboard")
    Time = Label(Sky,textvariable = tim)
    Time.grid(row=0)
    Sky.create_window(1360,50,window= Time)
    pausebutton = Button(Sky,text = "Pause",command = Pausegame)
    pausebutton.place(x = 1720,y=50)
    Cheatbutton = Button(Sky,text = "Cheats",command = Cheats)
    Cheatbutton.place(x=100,y=50)
    print(Sky.bbox(Hunter))
    # Sky.bind("<Left>",left)
    # Sky.bind("<Right>",right)
    Gameinitialise()

def Countdown(t):
    global Time
    global tim
    cur_time = 12000 - t
    minute = cur_time//6000
    minute = int(minute)
    second = cur_time%6000
    second = second//100
    second = int(second)
    if second < 10:
        cur_time_words = "Time :" + str(minute) + ":0" + str(second)
    else:
        cur_time_words = "Time " + str(minute) + ":" + str(second)
    tim.set(cur_time_words)
    window.update()

def Shoot(event):
    global Sky
    global Hunter
    global bullet
    if len(bullet) == 0:
        shootingbullet = Sky.create_oval(Sky.coords(Hunter)[0],Sky.coords(Hunter)[1],Sky.coords(Hunter)[0]+10,Sky.coords(Hunter)[1]+10,fill = "black")
        bullet.append(shootingbullet)
    else:
        pass


def Scoreupdate(a=1):    #argument here will determine what type of object was hit
    global Score
    global score
    global initial_score
    initial_score+=a
    scor = "Score:" + str(initial_score)
    score.set(scor)




def Gameinitialise():
    global t
    global shootingbullet
    global bullet
    t = 0.0
    leftBirds = []
    rightbirds = []
    Birds = []
    while t<12000:
        if t<3000:
            if t%100 == 0.0:
                side = randint(1,2)
                if side == 1:
                    chance = randint(1,10)
                    if chance in [1,4,7,11]:
                        number = len(Birds)
                        Bird = "Bird" + str(number)
                        height = randint(10,300)
                        Bird = Sky.create_oval(0,height,40,height+40,fill = "red")
                        # Bird.pack()
                        leftBirds.append(Bird)
                        Birds.append(Bird)
                    else:
                        pass
                else:
                    chance = randint(1,20)
                    if chance in [1,4,7,11]:
                        number = len(Birds)
                        Bird = "Bird" + str(number)
                        height = randint(10,300)
                        Bird = Sky.create_oval(1880,height,1920,height+40,fill = "red")
                        #Bird.pack()
                        rightbirds.append(Bird)
                        Birds.append(Bird)
                    else:
                        pass
        elif t<6000:
            if t%100 == 0.0:
                side = randint(1,2)
                if side == 1:
                    chance = randint(1,20)
                    if chance in [1,4,7,11,15]:
                        height = randint(10,300)
                        number = len(Birds)
                        Bird = "Bird" + str(number)
                        Bird = Sky.create_oval(0,height,40,height + 40,fill = "red")
                        #Bird.pack()
                        leftBirds.append(Bird)
                        Birds.append(Bird)
                    else:
                        pass
                else:
                    chance = randint(1,20)
                    if chance in [1,4,7.11,15]:
                        number = len(Birds)
                        Bird = "Bird" + str(number)
                        height = randint(10,300)
                        Bird = Sky.create_oval(1880,height,1920,height+40,fill = "red")
                        #Bird.pack()
                        rightbirds.append(Bird)
                        Birds.append(Bird)
                    else:
                        pass
        elif t<9000:
            if t%100 == 0.0:
                side = randint(1,2)
                if side == 1:
                    chance = randint(1,20)
                    if chance in [1,4,7,11,15,19]:
                        number = len(Birds)
                        height = randint(10,300)
                        Bird = "Bird" + str(number)
                        Bird = Sky.create_oval(0,height,40,height+40,fill = "red")
                        #Bird.pack()
                        leftBirds.append(Bird)
                        Birds.append(Bird)
                    else:
                        pass
                else:
                    chance = randint(1,20)
                    if chance in [1,4,7,11,15,19]:
                        number = len(Birds)
                        Bird = "Bird" + str(number)
                        height = randint(10,300)
                        Bird = Sky.create_oval(1880,height,1920,height+40,fill = "red")
                        #Bird.pack()
                        rightbirds.append(Bird)
                        Birds.append(Bird)
                    else:
                        pass
        elif t<12000:
            if t%100 == 0.0:
                side = randint(1,2)
                if side == 1:
                    chance = randint(1,20)
                    if chance in [1,4,7,11,15,19,20]:
                        number = len(Birds)
                        height = randint(10,300)
                        Bird = "Bird" + str(number)
                        Bird = Sky.create_oval(0,height,40,height+40,fill = "red")
                        #Bird.pack()
                        leftBirds.append(Bird)
                        Birds.append(Bird)
                    else:
                        pass
                else:
                    chance = randint(1,20)
                    if chance in [1,4,7,11,15,19,20]:
                        number = len(Birds)
                        Bird = "Bird" + str(number)
                        height = randint(10,300)
                        Bird = Sky.create_oval(1880,height,1920,height+40,fill = "red")
                        #Bird.pack()
                        rightbirds.append(Bird)
                        Birds.append(Bird)
                    else:
                        pass
        if len(leftBirds) != 0:
            for bir in leftBirds:
                 Sky.move(bir,10,0)

        if len(rightbirds) != 0:
            for bir in rightbirds:
                Sky.move(bir,-10,0)

        if len(Birds) != 0:
            for bir in Birds:
                Birdcoord = Sky.coords(bir)
                if Birdcoord[0] < 0 or Birdcoord[2] > 1920:
                    Sky.delete(bir)
                    Birds.remove(bir)

        if len(bullet) != 0:
            bul = bullet[0]
            bulletcoord = Sky.coords(bul)
            if bulletcoord[1] < 0:
                Sky.delete(bul)
                bullet.remove(bul)
            else:
                Sky.move(bul,0,-10)

        if len(bullet) != 0 and len(Birds) != 0:
            bul = bullet[0]
            bullcoord = Sky.coords(bul)
            for bir in Birds:
                bircoord = Sky.coords(bir)
                if bullcoord[0] < bircoord[2] and bullcoord[2] > bircoord[0] and bullcoord[1] < bircoord[3] and bullcoord[3] > bircoord[1]:
                    Sky.delete(bir)
                    Sky.delete(bul)
                    Birds.remove(bir)
                    bullet.remove(bul)
                    Scoreupdate()
                    break
                else:
                    continue



        t+=1

        Countdown(t)

        time.sleep(0.01)
        window.update()
    else:

        MenuScreen()
















window = Tk()
window.geometry("1920x1080")
Menu = Canvas(window,width = "1920",heigh = "1080",bg = "#1D3E60",bd=-2)
Sky = Canvas(window,width = "1920",heigh = "1080",bg = "#ADD8E6",bd=-2)





score = StringVar()
tim = StringVar()
tim.set("2:00")
score.set("Score:0")
img = PhotoImage(file = "images/hunter.png")









window.bind("<b>",Bosskey)
window.bind("<space>",Shoot)

#Gamespacecreate()
MenuScreen()
window.mainloop()
