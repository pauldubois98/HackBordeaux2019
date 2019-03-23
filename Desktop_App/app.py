import tkinter as tk


class App(tk.Frame):
    def __init__(self, root, **arg):
        tk.Frame.__init__(self, root, **arg)

        self.text=tk.Text(self, bg='#EEE')
        self.text.grid(column=1, row=1, columnspan=2)
        
        self.bt_exec=tk.Button(self, text='executer', bg='red')
        self.bt_exec.grid(column=2, row=2)
        
        self.bt_get=tk.Button(self, text='get code', bg='orange')
        self.bt_get.grid(column=1, row=2)
        
        self.pack()
        
        













if __name__=='__main__':
    root=tk.Tk()
    root.title("Hack Bordeaux 2019 !!!")
    app=App(root, bg="white")
    root.mainloop()
    









