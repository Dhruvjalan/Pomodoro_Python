from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_S = 10
SHORT_BREAK_S = 5
LONG_BREAK_S = 20
reps=0
timer = None
# App to manage time with Pomodoro technique. Set the number of seconds for work, long and short break.
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_clicked():
    canvas.itemconfig(timer_text, text=f"00:00")
    check_mark["text"] = ""
    timer_label["text"] = "TIMER"
    window.after_cancel(timer)
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_clicked():
    global reps
    reps+=1

    if reps % 2 == 1:
        count_down(WORK_S)
        timer_label["text"]="WORK"
    elif reps % 8 == 0:
        count_down(LONG_BREAK_S)
        timer_label["text"]="LONG BREAK"

    else:
        count_down(SHORT_BREAK_S)
        timer_label["text"]="SHORT BREAK"




    # count_down(5)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    if count%60<10:
        canvas.itemconfig(timer_text, text=f"{count // 60}:0{count%60}")
    else:
        canvas.itemconfig(timer_text, text=f"{count//60}:{count%60}")
    if count>0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_clicked()
        check_mark["text"]="✔️"*(reps//2)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("POMODORO")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
timer_label.grid(column=1, row=0)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)





start_button = Button(text="Start", command=start_clicked, highlightthickness=0)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", command=reset_clicked, highlightthickness=0)
reset_button.grid(column=2, row=2)

check_mark = Label(fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=3)

window.mainloop()
