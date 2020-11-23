from tkinter import ttk, constants

class Commands:
    def __init__(self, root,do_command):
        self.root = root
        self.frame = None
        self.initialize()
        self.do_command = do_command

    def initialize(self):
        
        self.frame = ttk.Frame(master=self.root)

        buttons = ['Frequency table','Summary','Load example-data']
        for idx,text in enumerate(buttons):
            btn = ttk.Button(master=self.frame, text=text, command = lambda text=text: self.analyze(text)  )
            btn.grid(row=idx+1, column=0)

    def analyze(self,which):
        print("Doing {}".format(which))

        self.do_command(which) 

    def destroy(self):
        self.frame.destroy()
    
    def pack(self):
        self.frame.pack()