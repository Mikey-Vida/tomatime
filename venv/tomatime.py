import tkinter as tk


class Tomatimer(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.worktime = 2
        self.short_break_break = 2
        self.long_break = 2
        self.working = True
        self.completed_num = 0
        self.counter = self.worktime
        self.paused = True
        self.title("Tomatimer")
        self.work = tk.Label(self, fg="red")
        self.work.pack()
        self.checks = tk.Label(self, fg="red")
        self.checks.pack()
        self.timer = tk.Label(self, fg="green")
        self.timer.pack()
        self.update()
        self.button_start = tk.Button(self, text='Start', width=25, command=self.toggle_pause)
        self.button_skip = tk.Button(self, text='Skip', width=25, command=self.end_countdown)
        self.button_reset_timer = tk.Button(self, text="Reset Timer", width=25,command=self.reset_timer)
        self.button = tk.Button(self, text='Exit', width=25, command=self.destroy)
        self.button_reset_all = tk.Button(self, text='Reset All', width=25, command=self.reset_all)
        self.button_start.pack()
        self.button_skip.pack()
        self.button_reset_timer.pack()
        self.button_reset_all.pack()
        self.button.pack()
        self.tick()

    def update(self):
        self.timer.config(text=self.seconds_to_string(self.counter))
        if self.working:
            self.work.config(text="Work")
        elif self.completed_num >= 4:
            self.work.config(text="long_break Break")
        else:
            self.work.config(text="short_break Break")
        check_marks = "checks "
        for i in range(0,self.completed_num):
            check_marks = check_marks + " #"
        self.checks.config(text=check_marks)

    def reset_timer(self):
        self.paused = True
        self.button_start.config(text="Start")
        if self.working:
            self.counter = self.worktime
        else:
            if self.completed_num < 4:
                self.counter = self.short_break
            else:
                self.counter = self.long_break
        self.update()

    def reset_all(self):
        self.working = True
        self.completed_num = 0
        self.counter = self.worktime
        self.reset_timer()



    def toggle_pause(self):
        self.paused = not self.paused
        if self.paused:
            self.button_start.config(text="Resume")
        else:
            self.configure(background="white")
            self.button_start.config(text="Pause")

    def end_countdown(self):
        self.attributes('-topmost', 1)
        self.attributes('-topmost', 0)
        self.configure(background="red")
        if self.working:
            self.completed_num += 1
        elif self.completed_num >= 4:
            self.completed_num = 0
        else:
            if self.completed_num >= 4:
                self.completed_num = 0
        self.working = not self.working
        self.reset_timer()


    def tick(self):
        if not self.paused:
            self.counter -= 1
            self.timer.config(text=self.seconds_to_string(self.counter))
            if self.counter <= 0:
                self.end_countdown()
        self.after(1000,self.tick)

    def seconds_to_string(self, seconds):
        counter_min = str(int(seconds / 60))
        counter_sec = str(int(seconds % 60))
        if len(counter_sec) < 2:
            counter_sec = "0" + counter_sec
        return counter_min + ":" + counter_sec

if __name__ == "__main__":
    app = Tomatimer()
    app.mainloop()