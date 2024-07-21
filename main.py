import customtkinter as ctk
import random

ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
ctk.set_widget_scaling(1)  # widget dimensions and text size
ctk.set_window_scaling(1)  # window geometry dimensions

root = ctk.CTk()
root.title("Tic Tac Toe")
root.geometry("1920x1080")

titletext = ctk.CTkLabel(root, text="Welcome to Tic Tac Toe", height=100, width=200, font=("Default", 20))
titletext.grid(column=2)


Win1 = []
Win2 = []
Win3 = []
Win4 = []
Win5 = []
Win6 = []
Win7 = []
Win8 = []

Win10 = []
Win20 = []
Win30 = []
Win40 = []
Win50 = []
Win60 = []
Win70 = []
Win80 = []

KI1 = []
KI2 = []


def Randint2():

    i = random.randint(1, 9)

    KI2.append(i)
    Randint1()

def Randint1():

    if len(KI2) == 0:
        Randint2()
    else:

        i = KI2[0]

        if i in Win1:
            KI2.clear()
            Randint2()
        else:
            if i in Win2:
                KI2.clear()
                Randint2()
            else:
                if i in Win3:
                    KI2.clear()
                    Randint2()
                else:
                    Meddler = KI1.copy()
                    if i in Meddler:
                        KI2.clear()
                        Randint2()
                    else:

                        KI1.append(i)
                        execution()

def Mustercheck():

    if 5 in Win2:
        print("schon vorhanden")
    else:
        if 5 in Win20:
            print("schon vorhanden")
        else:
            KI1.append(5)
            execution()
            return True

    if len(Win10) == 2:
        i = 1
        if i in Win10:
            if i not in Win1:
                i = 4
                if i in Win10:
                    if i not in Win1:
                        i = 7
                        if i in Win10:
                            if i not in Win1:
                                print("schon vorhanden")
                            else:

                                if i in KI1:
                                    print("schon vorhanden")
                                else:
                                    KI1.append(7)
                                    return True
            else:
                i = 4
                if i not in Win1:
                    if i in KI1:
                        print("schon vorhanden")
                    else:
                        KI1.append(4)
                        return True
        else:
            i = 1
            if i not in Win1:
                if i in KI1:
                    print("schon vorhanden")
                else:
                    KI1.append(1)
                    return True

    if len(Win20) == 2:
        i = 2
        if i in Win20:
            if i not in Win2:
                i = 5
                if i in Win20:
                    if i not in Win2:
                        i = 8
                        if i in Win20:
                            if i not in Win2:
                                print("schon vorhanden")
                            else:

                                if i in KI1:
                                    print("schon vorhanden")
                                else:
                                    KI1.append(8)
                                    return True
            else:
                i = 5
                if i not in Win2:
                    if i in KI1:
                        print("schon vorhanden")
                    else:
                        KI1.append(5)
                        return True
        else:
            i = 2
            if i not in Win2:
                if i in KI1:
                    print("schon vorhanden")
                else:
                    KI1.append(2)
                    return True

    if len(Win30) == 2:
        i = 3
        if i in Win30:
            if i not in Win3:
                i = 6
                if i in Win30:
                    if i not in Win3:
                        i = 9
                        if i in Win30:
                            if i not in Win3:
                                print("schon vorhanden")
                            else:

                                if i in KI1:
                                    print("schon vorhanden")
                                else:
                                    KI1.append(9)
                                    return True
            else:
                i = 6
                if i not in Win3:
                    if 6 in KI1:
                        print("schon vorhanden")
                    else:
                        KI1.append(4)
                        return True
        else:
            i = 3
            if i not in Win3:
                if 3 in KI1:
                    print("schon vorhanden")
                else:
                    KI1.append(1)
                    return True

    if len(Win40) == 2:
        i = 1
        if i in Win40:
            if i not in Win4:
                i = 2
                if i in Win40:
                    if i not in Win4:
                        i = 3
                        if i in Win40:
                            if i not in Win4:
                                print("schon vorhanden")
                            else:

                                if i in KI1:
                                    print("schon vorhanden")
                                else:
                                    KI1.append(3)
                                    return True
            else:
                i= 2
                if i not in Win4:
                    if i in KI1:
                        print("schon vorhanden")
                    else:
                        KI1.append(2)
                        return True
        else:
            i = 1
            if i not in Win4:
                if i in KI1:
                    print("schon vorhanden")
                else:
                    KI1.append(1)
                    return True

    if len(Win50) == 2:
        i = 4
        if i in Win50:
            if i not in Win5:
                i = 5
                if i in Win50:
                    if i not in Win5:
                        i = 6
                        if i in Win50:
                            if i not in Win5:
                                print("schon vorhanden")
                            else:

                                if i in KI1:
                                    print("schon vorhanden")
                                else:
                                    KI1.append(6)
                                    return True
            else:
                i = 5
                if i not in Win5:
                    if i in KI1:
                        print("schon vorhanden")
                    else:
                        KI1.append(5)
                        return True
        else:
            i = 4
            if i not in Win5:
                if i in KI1:
                    print("schon vorhanden")
                else:
                    KI1.append(4)
                    return True

    if len(Win60) == 2:
        i = 7
        if i in Win60:
            if i not in Win6:
                i = 8
                if i in Win60:
                    if i not in Win6:
                        i = 9
                        if i in Win60:
                            if i not in Win6:
                                print("schon vorhanden")
                            else:

                                if i in KI1:
                                    print("schon vorhanden")
                                else:
                                    KI1.append(9)
                                    return True
            else:
                i = 8
                if i not in Win6:
                    if i in KI1:
                        print("schon vorhanden")
                    else:
                        KI1.append(8)
                        return True
        else:
            i = 7
            if i not in Win6:
                if i in KI1:
                    print("schon vorhanden")
                else:
                    KI1.append(7)
                    return True

    if len(Win70) == 2:
        i = 1
        if i in Win70:
            if i not in Win7:
                i = 5
                if i in Win70:
                    if i not in Win7:
                        i = 9
                        if i in Win70:
                            if i not in Win7:
                                print("schon vorhanden")
                            else:

                                if i in KI1:
                                    print("schon vorhanden")
                                else:
                                    KI1.append(9)
                                    return True
            else:
                i = 5
                if i not in Win7:
                    if i in KI1:
                        print("schon vorhanden")
                    else:
                        KI1.append(5)
                        return True
        else:
            i = 5
            if i not in Win7:
                if i in KI1:
                    print("schon vorhanden")
                else:
                    KI1.append(1)
                    return True

    if len(Win80) == 2:
        i = 3
        if i in Win80:
            if i not in Win8:
                i = 5
                if i in Win80:
                    if i not in Win8:
                        i = 7
                        if i in Win80:
                            if i not in Win8:
                                print("schon vorhanden")
                            else:

                                if i in KI1:
                                    print("schon vorhanden")
                                else:
                                    KI1.append(7)
                                    return True
            else:
                i = 5
                if i not in Win8:
                    if i in KI1:
                        print("schon vorhanden")
                    else:
                        KI1.append(5)
                        return True
        else:
            i = 3
            if i not in Win8:
                if i in KI1:
                    print("schon vorhanden")
                else:
                    KI1.append(3)
                    return True

    if len(Win1) == 2:
        i = 1
        if i in Win1:
            i = 4
            if i in Win1:
                i = 7
                if i in Win1:
                    print("schon vorhanden")
                else:

                    if i in KI1:
                        print("schon vorhanden")
                    else:
                        KI1.append(7)
                        return True
            else:
                if 4 in KI1:
                    print("schon vorhanden")
                else:
                    KI1.append(4)
                    return True
        else:
            if 1 in KI1:
                print("schon vorhanden")
            else:
                KI1.append(1)
                return True

    elif len(Win2) == 2:
        i = 2
        if i in Win2:
            i = 5
            if i in Win2:
                i = 8
                if i in Win2:
                    print("schon vorhanden")
                else:
                    if i in KI1:
                        print("schon vorhanden")
                    else:
                        KI1.append(8)
                        return True
            else:
                if 5 in KI1:
                    print("schon vorhanden")
                else:
                    KI1.append(5)
                    return True
        else:
            if 2 in KI1:
                print("schon vorhanden")
            else:
                KI1.append(2)
                return True

    elif len(Win3) == 2:
        i = 3
        if i in Win3:
            i = 6
            if i in Win3:
                i = 9
                if i in Win3:
                    print("schon vorhanden")
                else:
                    if i in KI1:
                        print("schon vorhanden")
                    else:
                        KI1.append(9)
                        return True
            else:
                if 6 in KI1:
                    print("schon vorhanden")
                else:
                    KI1.append(6)
                    return True
        else:
            if 3 in KI1:
                print("schon vorhanden")
            else:
                KI1.append(3)
                return True

    elif len(Win4) == 2:
        i = 1
        if i in Win4:
            i = 2
            if i in Win4:
                i = 3
                if i in Win4:
                    print("schon vorhanden")
                else:
                    if i in KI1:
                        print("schon vorhanden")
                    else:
                        KI1.append(3)
                        return True
            else:
                if 2 in KI1:
                    print("schon vorhanden")
                else:
                    KI1.append(2)
                    return True
        else:
            if 1 in KI1:
                print("schon vorhanden")
            else:
                KI1.append(1)
                return True

    elif len(Win5) == 2:
        i = 4
        if i in Win5:
            i = 5
            if i in Win5:
                i = 6
                if i in Win5:
                    print("schon vorhanden")
                else:
                    if i in KI1:
                        print("schon vorhanden")
                    else:
                        KI1.append(6)
                        return True
            else:
                if 5 in KI1:
                    print("schon vorhanden")
                else:
                    KI1.append(5)
                    return True
        else:
            if 4 in KI1:
                print("schon vorhanden")
            else:
                KI1.append(4)
                return True

    elif len(Win6) == 2:
        i = 7
        if i in Win6:
            i = 8
            if i in Win6:
                i = 9
                if i in Win6:
                    print("schon vorhanden")
                else:
                    if i in KI1:
                        print("schon vorhanden")
                    else:
                        KI1.append(9)
                        return True
            else:
                if 8 in KI1:
                    print("schon vorhanden")
                else:
                    KI1.append(8)
                    return True
        else:
            if 7 in KI1:
                print("schon vorhanden")
            else:
                KI1.append(7)
                return True

    elif len(Win7) == 2:
        i = 1
        if i in Win7:
            i = 5
            if i in Win7:
                i = 9
                if i in Win7:
                    print("schon vorhanden")
                else:
                    if i in KI1:
                        print("schon vorhanden")
                    else:
                        KI1.append(9)
                        return True
            else:
                if 5 in KI1:
                    print("schon vorhanden")
                else:
                    KI1.append(5)
                    return True
        else:
            if 1 in KI1:
                print("schon vorhanden")
            else:
                KI1.append(1)
                return True

    elif len(Win8) == 2:
        i = 3
        if i in Win8:
            i = 5
            if i in Win8:
                i = 7
                if i in Win8:
                    print("schon vorhanden")
                else:
                    if i in KI1:
                        print("schon vorhanden")
                    else:
                        KI1.append(7)
                        return True
            else:
                if 5 in KI1:
                    print("schon vorhanden")
                else:
                    KI1.append(5)
                    return True
        else:
            if 3 in KI1:
                print("schon vorhanden")
            else:
                KI1.append(3)
                return True


def KI():
    if Gewonnen() == True:

        print("Spieler hat gewonnen")
    else:
        if Mustercheck() == True:
            execution()

        else:
           Randint1()

def execution():

    print(KI1)
    KI_copy = KI1.copy()

    i = 1
    if i  in KI_copy:

        Eins.configure(fg_color="Red", text="O")
        Verloren()

        if i in Win10:
            print("Meddler")
        else:
            Win10.append(1)
            Win40.append(1)
            Win70.append(1)
        KI2.clear()

    i = 2
    if i  in KI_copy:

        Zwei.configure(fg_color="Red", text="O")
        Verloren()
        if i in Win20:
            print("Meddler")
        else:
            Win20.append(2)
            Win40.append(2)
        KI2.clear()

    i = 3
    if i in KI_copy:


        Drei.configure(fg_color="Red", text="O")
        Verloren()
        if i in Win30:
            print("Meddler")
        else:
            Win30.append(3)
            Win40.append(3)
            Win80.append(3)
        KI2.clear()

    i = 4
    if i in KI_copy:

        Vier.configure(fg_color="Red", text="O")
        Verloren()
        if i in Win10:
            print("Meddler")
        else:
            Win10.append(4)
            Win50.append(4)
        KI2.clear()

    i = 5
    if i  in KI_copy:

        Fünf.configure(fg_color="Red", text="O")
        Verloren()
        if i in Win20:
            print("Meddler")
        else:
            Win20.append(5)
            Win50.append(5)
            Win70.append(5)
            Win80.append(5)
        KI2.clear()

    i = 6
    if i in KI_copy:

        Sechs.configure(fg_color="Red", text="O")
        Verloren()
        if i in Win30:
            print("Meddler")
        else:

            Win30.append(6)
            Win50.append(6)
        KI2.clear()

    i = 7
    if i  in KI_copy:


        Sieben.configure(fg_color="Red", text="O")
        Verloren()
        if i in Win10:
            print("Meddler")
        else:

            Win10.append(7)
            Win60.append(7)
            Win80.append(7)
        KI2.clear()

    i = 8
    if i  in KI_copy:

        Acht.configure(fg_color="Red", text="O")
        Verloren()
        if i in Win20:
            print("Meddler")
        else:

            Win20.append(8)
            Win60.append(8)
        KI2.clear()

    i = 9
    if i  in KI_copy:

        Neun.configure(fg_color="Red", text="O")
        Verloren()
        if i in Win30:
            print("Meddler")
        else:
            Win30.append(9)
            Win60.append(9)
            Win70.append(9)
        KI2.clear()

def Winner():

    titletext.configure(text="Du hast gewonnen")


def Gewonnen():

    if len(Win1) == 3:
        Winner()
        return True
    elif len(Win2) == 3:
        Winner()
        return True
    elif len(Win3) == 3:
        Winner()
        return True
    elif len(Win4) == 3:
        Winner()
        return True
    elif len(Win5) == 3:
        Winner()
        return True
    elif len(Win6) == 3:
        Winner()
        return True
    elif len(Win7) == 3:
        Winner()
        return True
    elif len(Win8) == 3:
        Winner()
        return True

def Looser():

    titletext.configure(text="Du hast verloren")

def Verloren():

    if Gewonnen() == True:

        print("Der Spieler hat gewonnen")
    else:

        if len(Win10) == 3:
            Looser()
        elif len(Win20) == 3:
            Looser()
        elif len(Win30) == 3:
            Looser()
        elif len(Win40) == 3:
            Looser()
        elif len(Win50) == 3:
            Looser()
        elif len(Win60) == 3:
            Looser()
        elif len(Win70) == 3:
            Looser()
        elif len(Win80) == 3:
            Looser()

def Eins_Command():
    i = 1
    if i in Win10:
        print("geht nicht")
    else:
        if i in Win1:
            print("Alredy pressed")
        else:

            Eins.configure(fg_color="blue", text="X")
            Win1.append(1)
            Win4.append(1)
            Win7.append(1)
            Gewonnen()
            KI()

def Zwei_Command():
    i = 2
    if i in Win20:
        print("geht nicht")
    else:

        if i in Win2:
            print("Alredy pressed")
        else:

            Zwei.configure(fg_color="blue", text="X")
            Win2.append(2)
            Win4.append(2)
            Gewonnen()
            KI()

def Drei_Command():
    i = 3
    if i in Win30:
        print("geht nicht")
    else:
        if i in Win3:
            print("Alredy pressed")
        else:

            Drei.configure(fg_color="blue", text="X")
            Win3.append(3)
            Win4.append(3)
            Win8.append(3)
            Gewonnen()
            KI()

def Vier_Command():
    i = 4
    if i in Win10:
        print("geht nicht")
    else:
        if i in Win1:
            print("Alredy pressed")
        else:

            Vier.configure(fg_color="blue", text="X")
            Win1.append(4)
            Win5.append(4)
            Gewonnen()
            KI()

def Fünf_Command():
    i = 5
    if i in Win20:
        print("geht nicht")
    else:
        if i in Win2:
            print("Alredy pressed")
        else:

            Fünf.configure(fg_color="blue", text="X")
            Win2.append(5)
            Win5.append(5)
            Win7.append(5)
            Win8.append(5)
            Gewonnen()
            KI()

def Sechs_Command():
    i = 6
    if i in Win30:
        print("geht nicht")
    else:
        if i in Win3:
            print("Alredy pressed")
        else:

            Sechs.configure(fg_color="blue", text="X")
            Win3.append(6)
            Win5.append(6)
            Gewonnen()
            KI()

def Sieben_Command():
    i = 7
    if i in Win10:
        print("geht nicht")
    else:
        if i in Win1:
            print("Alredy pressed")
        else:

            Sieben.configure(fg_color="blue", text="X")
            Win1.append(7)
            Win6.append(7)
            Win8.append(7)
            Gewonnen()
            KI()

def Acht_Command():
    i = 8
    if i in Win20:
        print("geht nicht")
    else:
        if i in Win2:
            print("Alredy pressed")
        else:

            Acht.configure(fg_color="blue", text="X")
            Win2.append(8)
            Win6.append(8)
            Gewonnen()
            KI()

def Neun_Command():
    i = 9
    if i in Win30:
        print("geht nicht")
    else:
        if i in Win3:
            print("Alredy pressed")
        else:

            Neun.configure(fg_color="blue", text="X")
            Win3.append(9)
            Win6.append(9)
            Win7.append(9)
            Gewonnen()
            KI()

def Reset_Command():

    Eins.configure(fg_color="grey", text="  ")
    Zwei.configure(fg_color="grey", text="  ")
    Drei.configure(fg_color="grey", text="  ")
    Vier.configure(fg_color="grey", text="  ")
    Fünf.configure(fg_color="grey", text="  ")
    Sechs.configure(fg_color="grey", text="  ")
    Sieben.configure(fg_color="grey", text="  ")
    Acht.configure(fg_color="grey", text="  ")
    Neun.configure(fg_color="grey", text="  ")

    Win1.clear()
    Win2.clear()
    Win3.clear()
    Win4.clear()
    Win5.clear()
    Win6.clear()
    Win7.clear()
    Win8.clear()

    Win10.clear()
    Win20.clear()
    Win30.clear()
    Win40.clear()
    Win50.clear()
    Win60.clear()
    Win70.clear()
    Win80.clear()

    KI1.clear()
    titletext.configure(text="Welcome to Tic Tac Toe")



Eins =ctk.CTkButton(root,text="", command=Eins_Command)

Zwei =ctk.CTkButton(root,text="",command=Zwei_Command)

Drei =ctk.CTkButton(root,text="", command=Drei_Command)

Vier =ctk.CTkButton(root,text="", command=Vier_Command)

Fünf =ctk.CTkButton(root,text="", command=Fünf_Command)

Sechs =ctk.CTkButton(root,text="", command=Sechs_Command)

Sieben =ctk.CTkButton(root,text="",command=Sieben_Command)

Acht =ctk.CTkButton(root,text="", command=Acht_Command)

Neun =ctk.CTkButton(root,text="", command=Neun_Command)

Space = ctk.CTkButton(root,text="")

Reset = ctk.CTkButton(root,text="Reset", command=Reset_Command, width=250, height=100)
Reset.grid(row=4, column=2, pady=10)


Zahlen = [Eins,Zwei,Drei,Vier,Fünf,Sechs,Sieben,Acht,Neun]
for index, i in enumerate(Zahlen):
    i.configure(fg_color="grey", height=250, width=250, font=("Default", 30))
    i.grid(padx=5, pady=5)


Column1 = [Eins, Vier, Sieben]

for index, i in enumerate(Column1):
    i.grid(column=1)

Column2 = [Zwei, Fünf, Acht]

for index, i in enumerate(Column2):
    i.grid(column=2)

Column3 = [Drei, Sechs, Neun]

for index, i in enumerate(Column3):
    i.grid(column=3)


Row111 = [Space]

for index, i in enumerate(Row111):
    i.grid(row=0)
    i.configure(width=500, height=0)

Row0 = [ Eins, Zwei, Drei]

for index, i in enumerate(Row0):
    i.grid(row=1)

Row1 = [ Vier, Fünf, Sechs]

for index, i in enumerate(Row1):
    i.grid(row=2)

Row2 = [ Sieben, Acht, Neun]

for index, i in enumerate(Row2):
    i.grid(row=3)


root.mainloop()