import tkinter as tk
import tkinter.font as font
import random

p_score = 0
c_score = 0

options = [("rock", 0), ("paper", 1), ("scissors", 2)]

def computer_win():
    global p_score, c_score
    c_score +=1
    result.config(text="Computer Won!")
    c_score.config(text="Computer's Score :" + str(c_score))
    score_label.config(text="Player's score: " + str(p_score))

#def player_win():
#    global p_score
#    p_score +=1
    



scr = tk.Tk()
scr.title("Rock Paper Scissors Game")


frame = tk.Frame(scr, borderwidth=3, relief="ridge", bg="lightblue", padx=10, pady=10)
frame.pack(expand=True, fill=tk.BOTH)


option_frame = tk.Frame(frame, borderwidth=3, relief="groove", bg="lightgreen")
option_label = tk.Label(option_frame, text="Your Options:")
option_label.pack(padx=15, pady=15, expand=True)
option_frame.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)


rock = tk.Button(option_frame, text="Rock", width=15, bg="red")
rock.pack(padx=5, pady=5, expand=True)

paper = tk.Button(option_frame, text="Paper", width=15, bg="lightgray")
paper.pack(padx=5, pady=5, expand=True)

scissors = tk.Button(option_frame, text="Scissors", width=15, bg="lightblue")
scissors.pack(padx=5, pady=5, expand=True)


score_frame = tk.Label(frame, text="Score", font="Times", relief="flat")
score_frame.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)



result = tk.Label(score_frame, text="you Won!!!", font="Times", fg="green")
#result.pack(padx=10, pady=10, expand=True)



choice_label = tk.Label(score_frame, text="You Selected: paper")
choice_label.pack(side=tk.LEFT, padx=5, pady=5)


score_label = tk.Label(score_frame, text="Player Score: 1")
score_label.pack(side=tk.LEFT, padx=10, pady=10)

cp_choice_label = tk.Label(score_frame, text="Cp Selected: rock")
cp_choice_label.pack(side=tk.RIGHT, padx=5, pady=5)

cp_score_label = tk.Label(score_frame, text="CP Score: 0")
cp_score_label.pack(side=tk.RIGHT, padx=10, pady=10)


scr.mainloop()
