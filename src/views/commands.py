from tkinter import ttk, constants

class Commands:
    def __init__(self, root,display_analysis):
        self.root = root
        self.frame = None
        self.initialize()
        self.display_analysis = display_analysis

    def initialize(self):
        
        self.frame = ttk.Frame(master=self.root)

        buttons = ['Frequency table','Summary']

        for idx,text in enumerate(buttons):

            btn = ttk.Button(master=self.frame, text=text, command = lambda text=text: self.analyze(text)  )
            btn.grid(row=idx, column=0)

    def analyze(self,which):
        print("Doing {}".format(which))

        self.display_analysis(which) 

    def destroy(self):
        self.frame.destroy()
    
    def pack(self):
        self.frame.pack()