from tkinter import ttk


class Commands:
    def __init__(self, root, do_command, available_commands):
        self.root = root
        self.frame = None
        self.available_commands = available_commands
        self.initialize()
        self.do_command = do_command


    def initialize(self):

        self.frame = ttk.Frame(master=self.root)

        for idx, text in enumerate(self.available_commands):
            btn = ttk.Button(master=self.frame, text=text,
                             command=lambda text=text: self.analyze(text))
            btn.grid(row=idx+1, column=0)

    def analyze(self, which):
        print("Doing {}".format(which))

        self.do_command(which)

    def destroy(self):
        self.frame.destroy()

    def pack(self):
        self.frame.pack()
