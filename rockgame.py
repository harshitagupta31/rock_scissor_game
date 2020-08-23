from tkinter import*
import random
window= Tk()
stats=[]

def get_winner(call):
    if random.random() <= (1/3):
        throw="Rock"
    elif (1/3) <random.random()<=(2/3):
        throw="Scissor"
    else:
        throw="Paper"

    if (throw=="Rock" and call=="Paper") or (throw=="Paper" and call== "Scissor") or (throw=="Scissor"  and call=="Rock"):
        stats.append('W')
        result="You Win!"
    elif throw == call:
        stats.append('D')
        result="Draw"
    else:
        stats.append("L")
        result="You Lost!"
    global output
    output.config(text="Computer did:" + throw + "\n"+ result)


def pass_s():
    get_winner("Scissor")
def pass_r():
     get_winner("Rock")
def pass_p():
    get_winner("Paper")


window.geometry("500x600")
Scissor=Button(window,text="Scissor", bg= "#ff9999", padx=10, pady=5, command= pass_s,width=20, height=10)

Rock=Button(window,text="Rock", bg= "#80ff80", padx=10, pady=5, command= pass_r,width=20, height=10)
Paper=Button(window,text="Paper", bg= "#3399ff", padx=10, pady=5, command= pass_p,width=20, height=10)
output=Label(window,width=20,fg= "red", text= " Whats your call", height=10)

Scissor.pack(side="left")
Rock.pack(side="left")
Paper.pack(side="left")
output.pack(side="right")

window.mainloop()

for i in stats: print(i, end="")
if stats.count('L')> stats.count('W'):
    result= "\nYou loose the series"
elif stats.count('L') ==stats.count('W'):
    result="\nSeries is draw"
else:
    result="\n You win the series."

print(result)

    



