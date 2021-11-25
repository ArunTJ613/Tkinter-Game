from tkinter import *
from random import *
import time
# Constants used throughout the program

Birds = []
left_bird = []
bullet = []
p = 1
initial_score = 0
m = 1
loadstate = []
scoress = {}

f1 = open("leaderboards.txt", "r")
data = f1.read()
data = data.strip()
data = data.strip("\n")
datas = data.split(",")
datas.pop()
for item in datas:
    sep = item.index(":")
    scoress[item[0:sep]] = item[sep+1:len(item)]
f1.close()

f2 = open("loadstate.txt", "r")
data = f2.read()
print(data)
if data == "":
    pass
else:
    data = data.strip()
    data = data.strip("\n")
    print(data)
    loadstate = data.split(",")
f2.close()
# have to append control state to load function


def MenuScreen():
    Sky.delete("all")
    Sky.pack_forget()
    window.update()
    if len(loadstate) == 0:
        Menu.delete("all")
        Menu.pack()

        Gameplay = Button(Menu, width=10, text="New Game", font=("Arial", 25), fg="orange", command=nameandcontrol, bg="#1D3E60")
        wind1 = Menu.create_window(960, 450, window=Gameplay)
        Leaderboards = Button(Menu, width=10, text="High Scores", font=("Arial", 25), fg="orange", command=Displayleaders, bg="#1D3E60")
        wind2 = Menu.create_window(960, 550, window=Leaderboards)
    else:
        Menu.delete("all")
        Menu.pack()

        Gameplay = Button(Menu, width=10, text="New Game", font=("Arial", 25), fg="orange", command=nameandcontrol, bg="#1D3E60")
        wind1 = Menu.create_window(960, 350, window=Gameplay)
        State = Button(Menu, width=10, text="Load Game", font=("Arial", 25), fg="orange", command=loadgame, bg="#1D3E60")
        wind3 = Menu.create_window(960, 450, window=State)
        Leaderboards = Button(Menu, width=10, text="High Scores", font=("Arial", 25), fg="orange", command=Displayleaders, bg="#1D3E60")
        wind2 = Menu.create_window(960, 550, window=Leaderboards)


def nameandcontrol():
    global nameentry
    Menu.delete("all")
    Prompt = Label(Menu, text="Enter your nickname", font=("Arial", 25), fg="orange", bg="#1D3E60")
    prompwindow = Menu.create_window(960, 150, window=Prompt)
    nameentry = Entry(Menu)
    namewindow = Menu.create_window(960, 300, window=nameentry)
    Prompt2 = Label(Menu, text="Pick your controls", font=("Arial", 25), fg="orange", bg="#1D3E60")
    prompwindow = Menu.create_window(960, 400, window=Prompt2)

    LorR = Button(Menu, width=10, text="Left and Right", font=("Arial", 25), fg="orange", command=leftandright, bg="#1D3E60")
    choice1 = Menu.create_window(700, 600, window=LorR)
    AorD = Button(Menu, width=10, text="A and D", font=("Arial", 25), fg="orange", command=AandD, bg="#1D3E60")
    choice2 = Menu.create_window(1200, 600, window=AorD)


def leftandright():
    global nameentry
    global control
    naming = nameentry.get()
    control = 1
    if naming == "":
        pass
    else:
        window.bind("<Left>", left)
        window.bind("<Right>", right)
        Gamespacecreate(naming)


def AandD():
    global nameentry
    global control
    naming = nameentry.get()
    control = 0
    if naming == "":
        pass
    else:
        window.bind("<a>", left)
        window.bind("<d>", right)
        Gamespacecreate(naming)


def loadgame():
    global loadstate
    global control
    nam = loadstate[0]
    timm = int(loadstate[1])
    curscore = int(loadstate[2])
    control = int(loadstate[3])
    loadstate.clear()
    if control == 1:
        window.bind("<Left>", left)
        window.bind("<Right>", right)
        Gamespacecreate(nam, timm, curscore)
    else:
        window.bind("<a>", left)
        window.bind("<d>", right)
        Gamespacecreate(namm, timm, curscore)


def Displayleaders():
    global scoress
    Menu.delete("all")
    Sky.delete("all")
    Sky.pack_forget()
    Menu.pack()
    names = list(scoress.keys())
    print(scoress)
    names.sort()
    print(names)
    points = list(scoress.values())
    numberpoints = []
    for a in points:
        numberpoints.append(int(a))
    numberpoints.sort(reverse=True)
    print(numberpoints)
    highscores = [numberpoints[0], numberpoints[1], numberpoints[2]]
    scorers = []
    for i in highscores:
        for j in names:
            if scoress[j] == str(i):
                scorers.append(j)
                names.remove(j)
                break
    print(scorers, highscores)
    Title = Label(Menu, text="LEADERBOARDS", font=("Arial", 50), fg="orange", bg="#1D3E60")
    Titlewindow = Menu.create_window(960, 100, window=Title)
    Title1 = Label(Menu, text=scorers[0] + "   :    " + str(highscores[0]), font=("Arial", 40), fg="orange", bg="#1D3E60")
    Titlewindow1 = Menu.create_window(960, 400, window=Title1)
    Title2 = Label(Menu, text=scorers[1] + "   :    " + str(highscores[1]), font=("Arial", 40), fg="orange", bg="#1D3E60")
    Titlewindow2 = Menu.create_window(960, 500, window=Title2)
    Title3 = Label(Menu, text=scorers[2] + "   :    " + str(highscores[2]), font=("Arial", 40), fg="orange", bg="#1D3E60")
    Titlewindow3 = Menu.create_window(960, 600, window=Title3)
    Backbutton = Button(Menu, text="Back", font=("Arial", 20), fg="orange", command=MenuScreen, bg="#1D3E60")
    Backbuttonwindow = Menu.create_window(100, 800, window=Backbutton)


def left(event):
    global Sky
    global Hunter
    global m
    Huntercoordinates = Sky.bbox(Hunter)
    if Huntercoordinates[0] == 0 or m == 0:
        pass
    else:
        Sky.move(Hunter, -14, 0)


def right(event):
    global Sky
    global m
    global Hunter
    Huntercoordinates = Sky.bbox(Hunter)
    if Huntercoordinates[2] > 1920 or m == 0:
        pass
    else:
        Sky.move(Hunter, 14, 0)


def up(event):
    global Sky
    Huntercoordinates = Sky.coords(Hunter)
    if Huntercoordinates[0] == 0 or m == 0:
        pass
    else:
        Sky.move(Hunter, 12, 0)


def down(event):
    global Sky
    Huntercoordinates = Sky.coords(Hunter)
    if Huntercoordinates[0] == 0 or m == 0:
        pass
    else:
        Sky.move(Hunter, 12, 0)


def Cheats():
    global p
    global m
    global bullet
    global t
    global Cheat
    global pierce
    if p == 1:
        p = 0
        m = 0
        boss = 0
        bullet.append(0)
        Cheatask = Label(Sky, text="Enter Cheat", font=("Arial", 20))
        Cheatwindow = Sky.create_window(960, 300, window=Cheatask, tags="illegal")
        Cheat = Entry(Sky)
        Chwindow = Sky.create_window(960, 400, window=Cheat, tags="illeagle")
        Apply = Button(Sky, text="Apply", font=("Arial", 20), command=Cheats)
        Applywindow = Sky.create_window(960, 500, window=Apply, tags="eagleill")
        pausebutton.configure(state=DISABLED)
        while 1 > 0:
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
        elif cheatcode == "Piercing":
            pierce = 1
        else:
            pass
        Sky.delete("illegal")
        Sky.delete("illeagle")
        Sky.delete("eagleill")
        pausebutton.configure(state=NORMAL)
        p = 1
        m = 1
        boss = 1
        bullet.pop()


def SaveandQuit():
    global name
    global t
    global initial_score
    global control
    global pausebutton
    global Cheatbutton
    global q
    global p
    global m
    global bullet
    q = 1
    loadstate.append(name)
    loadstate.append(t)
    loadstate.append(initial_score)
    loadstate.append(control)
    loadentry = name + "," + str(t) + "," + str(initial_score) + "," + str(control)
    f4 = open("loadstate.txt", "w")
    f4.write(loadentry)
    f4.close()
    p = 1
    m = 1
    bullet.clear()


def Quit():
    global p
    global q
    global m
    global bullet
    q = 1
    p = 1
    m = 1
    bullet.clear()


def Pausegame():
    global pausebutton
    global p
    global m
    global bullet
    global Loadbutton
    global Quitbutton
    if p == 1:
        pausebutton.configure(text="Unpause")
        Loadbutton = Button(Sky, text="Save and Quit", font=("Arial", 25), command=SaveandQuit)
        Loadbuttonwindow = Sky.create_window(850, 540, window=Loadbutton)
        Quitbutton = Button(Sky, text="Quit", font=("Arial", 25), command=Quit)
        Quitbuttonwindow = Sky.create_window(1070, 540, window=Quitbutton)
        p = 0
        m = 0
        bullet.append(0)

        # Cheatask = Label(Sky,text = "Enter a Cheat(even though you shouldnt)",font = ("Arial",20))
        # Cheatask.pack(ipadx=800,ipady=400)
        # Cheat = Entry(Sky)
        # Cheat.place(x=910,y=540,width = 100,height = 20)
        while 1 > 0:
            pass
            if p == 1:
                break
            window.update()
    else:
        pausebutton.configure(text="Pause")
        Loadbutton.destroy()
        Quitbutton.destroy()
        p = 1
        m = 1
        bullet.pop()


def Bosskey(event):
    global p
    global m
    global bullet
    global Work
    if p == 1:
        p = 0
        m = 0
        bullet.append(0)
        #Work = Sky.create_image(960, 0, anchor=NW, image=codeimg, tags="work")
        Sky.pack_forget()
        Menu.pack()
        Work = Menu.create_image(0, 0, anchor=NW, image=codeimg, tags="work")
        while 1 > 0:
            pass
            if p == 1:
                break
            window.update()
    else:
        #Sky.delete("work")
        Menu.delete("all")
        Menu.pack_forget()
        Sky.pack()
        p = 1
        m = 1
        bullet.pop()


def Gamespacecreate(nam, timee=0, scoreee=0):
    global Hunter
    global Sky
    global Score
    global Time
    global score
    global tim
    global pausebutton
    global p
    global Menu
    global scoress
    global name
    global initial_score
    global Cheatbutton
    name = nam
    Menu.delete("all")
    Menu.pack_forget()
    Sky.pack()
    Ground = Sky.create_rectangle(-100, 1080, 2020, 780, fill="green", outline="green")
    Sun = Sky.create_oval(1600, 100, 1700, 200, fill="yellow")
    Backgrnd = Sky.create_image(0, 0, anchor=NW, image=backimg)
    Hunter = Sky.create_image(960, 670, anchor=NW, image=img)
    initial_score = scoreee
    Score = Label(Sky, textvariable=score)
    score.set("Score:" + str(scoreee))
    Sky.create_window(960, 50, window=Score, tags="scoreboard")
    Time = Label(Sky, textvariable=tim)
    tim.set("")
    a = timee
    Countdown(a)
    Sky.create_window(1360, 50, window=Time)
    playername = Label(Sky, text=name)
    playernamewindow = Sky.create_window(760, 50, window=playername)
    pausebutton = Button(Sky, text="Pause", command=Pausegame)
    pausebutton.place(x=1720, y=50)
    Cheatbutton = Button(Sky, text="Cheats", command=Cheats)
    Cheatbutton.place(x=100, y=50)
    # Sky.bind("<Left>",left)
    # Sky.bind("<Right>",right)
    Gameinitialise(a)


def Countdown(t):
    global Time
    global tim
    cur_time = 12000 - t
    minute = cur_time//6000
    minute = int(minute)
    second = cur_time % 6000
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
        # shootingbullet = Sky.create_oval(Sky.coords(Hunter)[0],Sky.coords(Hunter)[1],Sky.coords(Hunter)[0]+10,Sky.coords(Hunter)[1]+10,fill = "black")
        shootingbullet = Sky.create_image(int((Sky.bbox(Hunter)[2] + Sky.bbox(Hunter)[0])/2), Sky.bbox(Hunter)[1], anchor=NW, image=arrimg)
        bullet.append(shootingbullet)
    else:
        pass


def Scoreupdate(a):    # argument here will determine what type of object was hit
    global Score
    global score
    global initial_score
    initial_score += a
    if initial_score >= 0:
        pass
    else:
        initial_score = 0
    scor = "Score:" + str(initial_score)
    score.set(scor)


def Gameinitialise(starttime=0):
    global t
    global shootingbullet
    global bullet
    global scoress
    global score
    global name
    global Cheatbutton
    global pausebutton
    global loadstate
    global q
    global initial_score
    global pierce
    window.bind("<b>", Bosskey)
    loadstate = []
    f3 = open("loadstate.txt", "w")
    f3.write("")
    f3.close()
    t = starttime
    q = 0
    pierce = 0
    leftredBirds = []
    rightredbirds = []
    redBirds = []
    leftgreenBirds = []
    rightgreenBirds = []
    greenBirds = []
    leftblueBirds = []
    rightblueBirds = []
    blueBirds = []
    leftgreyBirds = []
    rightgreyBirds = []
    greyBirds = []
    leftblackBirds = []
    rightblackBirds = []
    blackBirds = []
    while t < 12000 and q == 0:
        if t < 3000:
            if t % 100 == 0.0:
                side = randint(1, 2)
                if side == 1:
                    chance = randint(1, 20)
                    if chance in [1, 4, 7, 11, 13, 14]:
                        height = randint(10, 300)
                        Bird = Sky.create_oval(0, height, 80, height+80, fill="red")
                        # Bird.pack()
                        leftredBirds.append(Bird)
                        redBirds.append(Bird)
                    elif chance in [2, 5, 8]:
                        height = randint(10, 300)
                        Bird = Sky.create_oval(0, height, 60, height+60, fill="green")
                        leftgreenBirds.append(Bird)
                        greenBirds.append(Bird)
                    else:
                        pass

                else:
                    chance = randint(1, 20)
                    if chance in [1, 4, 7, 11, 13, 14]:
                        number = len(Birds)
                        Bird = "Bird" + str(number)
                        height = randint(10, 300)
                        Bird = Sky.create_oval(1840, height, 1920, height+80, fill="red")
                        # Bird.pack()
                        rightredbirds.append(Bird)
                        redBirds.append(Bird)
                    elif chance in [2, 5, 8]:
                        height = randint(10, 300)
                        Bird = Sky.create_oval(1860, height, 1920, height+60, fill="green")
                        rightgreenBirds.append(Bird)
                        greenBirds.append(Bird)
                    else:
                        pass
        elif t < 6000:
            if t % 100 == 0.0:
                side = randint(1, 2)
                if side == 1:
                    chance = randint(1, 20)
                    if chance in [1, 4, 7, 11, 15]:
                        height = randint(10, 300)
                        number = len(Birds)
                        Bird = "Bird" + str(number)
                        Bird = Sky.create_oval(0, height, 80, height + 80, fill="red")
                        # Bird.pack()
                        leftredBirds.append(Bird)
                        redBirds.append(Bird)
                    elif chance in [2, 5, 8]:
                        height = randint(10, 300)
                        Bird = Sky.create_oval(0, height, 60, height+60, fill="green")
                        leftgreenBirds.append(Bird)
                        greenBirds.append(Bird)
                    elif chance in [3, 6]:
                        height = randint(10, 300)
                        Bird = Sky.create_oval(0, height, 40, height+40, fill="yellow")
                        leftblueBirds.append(Bird)
                        blueBirds.append(Bird)

                    else:
                        pass
                else:
                    chance = randint(1, 20)
                    if chance in [1, 4, 7, 11, 15]:
                        number = len(Birds)
                        Bird = "Bird" + str(number)
                        height = randint(10, 300)
                        Bird = Sky.create_oval(1840, height, 1920, height+80, fill="red")
                        # Bird.pack()
                        rightredbirds.append(Bird)
                        redBirds.append(Bird)
                    elif chance in [2, 5, 8]:
                        height = randint(10, 300)
                        Bird = Sky.create_oval(1860, height, 1920, height+60, fill="green")
                        rightgreenBirds.append(Bird)
                        greenBirds.append(Bird)
                    elif chance in [3, 6]:
                        height = randint(10, 300)
                        Bird = Sky.create_oval(1880, height, 1920, height+40, fill="yellow")
                        rightblueBirds.append(Bird)
                        blueBirds.append(Bird)
                    else:
                        pass
        elif t < 9000:
            if t % 100 == 0.0:
                side = randint(1, 2)
                if side == 1:
                    chance = randint(1, 20)
                    if chance in [1, 4, 7, 11, 15, 19]:
                        number = len(Birds)
                        height = randint(10, 300)
                        Bird = "Bird" + str(number)
                        Bird = Sky.create_oval(0, height, 80, height+80, fill="red")
                        # Bird.pack()
                        leftredBirds.append(Bird)
                        redBirds.append(Bird)
                    elif chance in [2, 5, 8]:
                        height = randint(10, 300)
                        Bird = Sky.create_oval(0, height, 60, height+60, fill="green")
                        leftgreenBirds.append(Bird)
                        greenBirds.append(Bird)
                    elif chance in [3, 6]:
                        height = randint(10, 300)
                        Bird = Sky.create_oval(0, height, 40, height+40, fill="yellow")
                        leftblueBirds.append(Bird)
                        blueBirds.append(Bird)
                    elif chance in [12, 13, 14]:
                        height = randint(10, 300)
                        Bird = Sky.create_oval(0, height, 60, height+60, fill="grey")
                        leftgreyBirds.append(Bird)
                        greyBirds.append(Bird)

                    else:
                        pass
                else:
                    chance = randint(1, 20)
                    if chance in [1, 4, 7, 11, 15, 19]:
                        number = len(Birds)
                        Bird = "Bird" + str(number)
                        height = randint(10, 300)
                        Bird = Sky.create_oval(1840, height, 1920, height+80, fill="red")
                        # Bird.pack()
                        rightredbirds.append(Bird)
                        redBirds.append(Bird)
                    elif chance in [2, 5, 8]:
                        height = randint(10, 300)
                        Bird = Sky.create_oval(1860, height, 1920, height+60, fill="green")
                        rightgreenBirds.append(Bird)
                        greenBirds.append(Bird)
                    elif chance in [3, 6]:
                        height = randint(10, 300)
                        Bird = Sky.create_oval(1880, height, 1920, height+40, fill="yellow")
                        rightblueBirds.append(Bird)
                        blueBirds.append(Bird)
                    elif chance in [12, 13, 14]:
                        height = randint(10, 300)
                        Bird = Sky.create_oval(1860, height, 1920, height+60, fill="grey")
                        rightgreyBirds.append(Bird)
                        greyBirds.append(Bird)
                    else:
                        pass
        elif t < 12000:
            if t % 100 == 0.0:
                side = randint(1, 2)
                if side == 1:
                    chance = randint(1, 20)
                    if chance in [1, 4, 7, 11, 15, 19, 20]:
                        number = len(Birds)
                        height = randint(10, 300)
                        Bird = "Bird" + str(number)
                        Bird = Sky.create_oval(0, height, 80, height+80, fill="red")
                        # Bird.pack()
                        leftredBirds.append(Bird)
                        redBirds.append(Bird)
                    elif chance in [2, 5, 8]:
                        height = randint(10, 300)
                        Bird = Sky.create_oval(0, height, 60, height+60, fill="green")
                        leftgreenBirds.append(Bird)
                        greenBirds.append(Bird)
                    elif chance in [3, 6]:
                        height = randint(10, 300)
                        Bird = Sky.create_oval(0, height, 40, height+40, fill="yellow")
                        leftblueBirds.append(Bird)
                        blueBirds.append(Bird)
                    elif chance in [12, 13, 14]:
                        height = randint(10, 300)
                        Bird = Sky.create_oval(0, height, 60, height+60, fill="grey")
                        leftgreyBirds.append(Bird)
                        greyBirds.append(Bird)
                    elif chance in [16, 17]:
                        height = randint(10, 300)
                        Bird = Sky.create_oval(0, height, 80, height+80, fill="black")
                        leftblackBirds.append(Bird)
                        blackBirds.append(Bird)
                    else:
                        pass
                else:
                    chance = randint(1, 20)
                    if chance in [1, 4, 7, 11, 15, 19, 20]:
                        number = len(Birds)
                        Bird = "Bird" + str(number)
                        height = randint(10, 300)
                        Bird = Sky.create_oval(1840, height, 1920, height+80, fill="red")
                        # Bird.pack()
                        rightredbirds.append(Bird)
                        redBirds.append(Bird)
                    elif chance in [2, 5, 8]:
                        height = randint(10, 300)
                        Bird = Sky.create_oval(1860, height, 1920, height+60, fill="green")
                        rightgreenBirds.append(Bird)
                        greenBirds.append(Bird)
                    elif chance in [3, 6]:
                        height = randint(10, 300)
                        Bird = Sky.create_oval(1880, height, 1920, height+40, fill="blue")
                        rightblueBirds.append(Bird)
                        blueBirds.append(Bird)
                    elif chance in [12, 13, 14]:
                        height = randint(10, 300)
                        Bird = Sky.create_oval(1860, height, 1920, height+60, fill="grey")
                        rightgreyBirds.append(Bird)
                        greyBirds.append(Bird)
                    elif chance in [16, 17]:
                        height = randint(10, 300)
                        Bird = Sky.create_oval(1840, height, 1920, height+80, fill="black")
                        rightblackBirds.append(Bird)
                        blackBirds.append(Bird)
                    else:
                        pass
        if len(leftredBirds) != 0:
            for bir in leftredBirds:
                Sky.move(bir, 3, 0)

        if len(rightredbirds) != 0:
            for bir in rightredbirds:
                Sky.move(bir, -3, 0)

        if len(redBirds) != 0:
            for bir in redBirds:
                Birdcoord = Sky.coords(bir)
                if Birdcoord[0] < 0 or Birdcoord[2] > 1920:
                    Sky.delete(bir)
                    redBirds.remove(bir)

        if len(leftgreenBirds) != 0:
            for gir in leftgreenBirds:
                Sky.move(gir, 4, 0)

        if len(rightgreenBirds) != 0:
            for gir in rightgreenBirds:
                Sky.move(gir, -4, 0)

        if len(greenBirds) != 0:
            for gir in greenBirds:
                Birdcoord = Sky.coords(gir)
                if Birdcoord[0] < 0 or Birdcoord[2] > 1920:
                    Sky.delete(gir)
                    greenBirds.remove(gir)

        if len(leftblueBirds) != 0:
            for gir in leftblueBirds:
                Sky.move(gir, 8, 0)

        if len(rightblueBirds) != 0:
            for gir in rightblueBirds:
                Sky.move(gir, -8, 0)

        if len(blueBirds) != 0:
            for gir in blueBirds:
                Birdcoord = Sky.coords(gir)
                if Birdcoord[0] < 0 or Birdcoord[2] > 1920:
                    Sky.delete(gir)
                    blueBirds.remove(gir)

        if len(leftgreyBirds) != 0:
            for gir in leftgreyBirds:
                Sky.move(gir, 4, 0)

        if len(rightgreyBirds) != 0:
            for gir in rightgreyBirds:
                Sky.move(gir, -4, 0)

        if len(greyBirds) != 0:
            for gir in greyBirds:
                Birdcoord = Sky.coords(gir)
                if Birdcoord[0] < 0 or Birdcoord[2] > 1920:
                    Sky.delete(gir)
                    greyBirds.remove(gir)

        if len(leftblackBirds) != 0:
            for gir in leftblackBirds:
                Sky.move(gir, 3, 0)

        if len(rightblackBirds) != 0:
            for gir in rightblackBirds:
                Sky.move(gir, -3, 0)

        if len(blackBirds) != 0:
            for gir in blackBirds:
                Birdcoord = Sky.coords(gir)
                if Birdcoord[0] < 0 or Birdcoord[2] > 1920:
                    Sky.delete(gir)
                    blackBirds.remove(gir)

        if len(bullet) != 0:
            bul = bullet[0]
            bulletcoord = Sky.bbox(bul)
            if bulletcoord[1] < 0:
                Sky.delete(bul)
                bullet.remove(bul)
            else:
                Sky.move(bul, 0, -15)

        if len(bullet) != 0 and len(redBirds) != 0:
            bul = bullet[0]
            bullcoord = Sky.bbox(bul)
            for bir in redBirds:
                bircoord = Sky.coords(bir)
                if bullcoord[0] < bircoord[2] and bullcoord[2] > bircoord[0] and bullcoord[1] < bircoord[3] and bullcoord[3] > bircoord[1]:
                    Sky.delete(bir)
                    if pierce == 0:
                        Sky.delete(bul)
                        bullet.remove(bul)
                    else:
                        pass
                    redBirds.remove(bir)
                    Scoreupdate(1)
                    break
                else:
                    continue

        if len(bullet) != 0 and len(greenBirds) != 0:
            bul = bullet[0]
            bullcoord = Sky.bbox(bul)
            for bir in greenBirds:
                bircoord = Sky.coords(bir)
                if bullcoord[0] < bircoord[2] and bullcoord[2] > bircoord[0] and bullcoord[1] < bircoord[3] and bullcoord[3] > bircoord[1]:
                    Sky.delete(bir)
                    if pierce == 0:
                        Sky.delete(bul)
                        bullet.remove(bul)
                    else:
                        pass
                    greenBirds.remove(bir)
                    Scoreupdate(2)
                    break
                else:
                    continue

        if len(bullet) != 0 and len(blueBirds) != 0:
            bul = bullet[0]
            bullcoord = Sky.bbox(bul)
            for bir in blueBirds:
                bircoord = Sky.coords(bir)
                if bullcoord[0] < bircoord[2] and bullcoord[2] > bircoord[0] and bullcoord[1] < bircoord[3] and bullcoord[3] > bircoord[1]:
                    Sky.delete(bir)
                    if pierce == 0:
                        Sky.delete(bul)
                        bullet.remove(bul)
                    else:
                        pass
                    blueBirds.remove(bir)
                    Scoreupdate(5)
                    break
                else:
                    continue

        if len(bullet) != 0 and len(greyBirds) != 0:
            bul = bullet[0]
            bullcoord = Sky.bbox(bul)
            for bir in greyBirds:
                bircoord = Sky.coords(bir)
                if bullcoord[0] < bircoord[2] and bullcoord[2] > bircoord[0] and bullcoord[1] < bircoord[3] and bullcoord[3] > bircoord[1]:
                    Sky.delete(bir)
                    if pierce == 0:
                        Sky.delete(bul)
                        bullet.remove(bul)
                    else:
                        pass
                    greyBirds.remove(bir)
                    Scoreupdate(-1)
                    break
                else:
                    continue

        if len(bullet) != 0 and len(blackBirds) != 0:
            bul = bullet[0]
            bullcoord = Sky.bbox(bul)
            for bir in blackBirds:
                bircoord = Sky.coords(bir)
                if bullcoord[0] < bircoord[2] and bullcoord[2] > bircoord[0] and bullcoord[1] < bircoord[3] and bullcoord[3] > bircoord[1]:
                    Sky.delete(bir)
                    if pierce == 0:
                        Sky.delete(bul)
                        bullet.remove(bul)
                    else:
                        pass
                    blackBirds.remove(bir)
                    Scoreupdate(-10)
                    break
                else:
                    continue

        t += 1
        Countdown(t)
        time.sleep(0.01)
        window.update()
    else:
        if q == 0:
            final_score = score.get()
            sepe = final_score.index(":")
            point = final_score[sepe+1:]
            name = name.strip("\n")
            # scoress[name] = point
            if name in list(scoress.keys()):
                if scoress[name] in list(scoress.values()):
                    if int(point) > int(scoress[name]):
                        print(int(point), int(scoress[name]))
                        scoress[name] = point
                        fileentry = name + ":" + point + ","
                        f = open("leaderboards.txt", "a")
                        f.write(fileentry)
                        f.close()
                    else:
                        pass
            else:
                scoress[name] = point
                fileentry = name + ":" + point + ","
                f = open("leaderboards.txt", "a")
                f.write(fileentry)
                f.close()

            Sky.delete("all")
            print(scoress)

            pausebutton.destroy()
            Cheatbutton.destroy()
            Gameover = Label(Sky, text="Game Over", font=("Arial", 50), bg="#ADD8E6", fg="orange")
            Gameoverwindow = Sky.create_window(960, 100, window=Gameover)
            fina_score = Label(Sky, text="Your Score:" + point, font=("Arial", 25), bg="#ADD8E6", fg="orange")
            fina_scorewindow = Sky.create_window(960, 500, window=fina_score)
            backbutton = Button(Sky, text="Back", fg="orange", command=MenuScreen, bg="#ADD8E6")
            backbuttonwindow = Sky.create_window(200, 700, window=backbutton)
            leaderbutton = Button(Sky, text="Leaderboards", fg="orange", command=Displayleaders, bg="#ADD8E6")
            leaderbuttonwindow = Sky.create_window(1700, 700, window=leaderbutton)
            window.unbind("<b>")
        else:
            Sky.delete("all")
            window.unbind("<b>")
            pausebutton.destroy()
            Cheatbutton.destroy()
            MenuScreen()


window = Tk()
window.geometry("1920x1080")
window.title("StraightShootez")

Menu = Canvas(window, width="1920", heigh="1080", bg="#1D3E60", bd=-2) # Canvases used in the game
Sky = Canvas(window, width="1920", heigh="1080", bg="#ADD8E6", bd=-2)


score = StringVar() # Variable strings used in the Game
tim = StringVar()


img = PhotoImage(file="images/archer.png") # Images used in the Game
backimg = PhotoImage(file="background.png")
arrimg = PhotoImage(file="images/arrow.png")
codeimg = PhotoImage(file="images/bosskey.png")

window.bind("<space>", Shoot)

# Gamespacecreate()
MenuScreen()
window.mainloop()
