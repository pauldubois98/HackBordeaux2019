import tkinter as tk
import serial
import os
import time


class App(tk.Frame):
    def __init__(self, root, **arg):
        #inheritance
        tk.Frame.__init__(self, root, **arg)
        
        ###buttons
        fr=tk.Frame(self, bd=0)
        fr.grid(column=1, columnspan=2, row=2)
        #get
        self.bt_get=tk.Button(fr, text='get code', bg='yellow', \
                              command=self.readSerial)
        self.bt_get.grid(column=1, row=1)
        #save
        self.bt_save=tk.Button(fr, text='save code', bg='orange', \
                              command=self.save)
        self.bt_save.grid(column=2, row=1)
        #save
        self.bt_save=tk.Button(fr, text='clear code', bg='red', \
                              command=self.clear)
        self.bt_save.grid(column=3, row=1)
        #exec
        self.bt_exec=tk.Button(fr, text='execute code', bg='grey', \
                               command=self.execute)
        self.bt_exec.grid(column=4, row=1)

        #all
        self.bt_get=tk.Button(self, text='get&save&execute', bg='green', \
                              command=self.readSaveExec)
        self.bt_get.grid(column=3, row=2)

        ###serial
        fr=tk.Frame(self, bd=0)
        fr.grid(column=4, row=2, sticky='e')
        #label
        lab=tk.Label(fr, text='COM')
        lab.grid(column=1, row=1)
        #entry
        self.com_entry=tk.Entry(fr, width=3)
        self.com_entry.grid(column=2, row=1)
        self.com_entry.insert('end', '4')
        #btns
        self.bt_connect=tk.Button(self, text='(re)connect', bg='light green', \
                                  command=self.connect)
        self.bt_connect.grid(column=5, row=2, sticky='w')


        #text prgm
        self.text=tk.Text(self, bg='#EEE', height=5, takefocus=0)
        self.text.grid(column=1, row=4, columnspan=5, pady=2, padx=2)

        self.RES=[39000, 100000, 68000, 22000, 5600, 6800, 16000, 46000, 56000, 80000]
        self.KEY=['print(', 'while', 'i', 'end', ';', '=', '0', '<=', '*', '10']
        
        
        #inital connect
        #self.connect()
        #final pack
        self.pack()


    def connect(self, event=None):
        #delete last connection
        try:
            self.serial.close()
        except:
            pass
        #init serial connection
        self.serial = serial.Serial('COM'+self.com_entry.get())

        self.serial.write(b'rr')
        time.sleep(0.2)
        prgm=self.serial.readline()
        self.indentLevel=0

        self.first=True

        
        #print serial conected
        print('COM'+self.com_entry.get())

    def readSaveExec(self, event=None):
        self.readSerial()
        self.save()
        self.execute()
        
    def readSerial(self, event=None):
        if self.first:
            self.serial.write(b'r')
            self.first=False
        self.serial.write(b'r')
        time.sleep(0.2)
        prgm=self.serial.readline()
        vals=[float(a) for a in prgm.decode('ascii')[1:-3].split(',')]
        print(vals)
        res=[]
        line=[]
        for j in range(len(vals)):
            mini=abs(vals[j]-self.RES[0])
            ind=0
            for i in range(1, len(self.RES)):
                if abs(vals[j]-self.RES[i])<mini:
                    ind=i
                    mini=abs(vals[j]-self.RES[i])
            if self.KEY[ind]==';':
                print('ok')
                break
            else:
                res.append(self.RES[ind])
                line.append(self.KEY[ind])

            
        print(res)
        print(line)
        if line[0]=='end':
            line=[]
            self.indentLevel-=1
        code='    '*self.indentLevel
        code+=" ".join(line)
        if line[0]=='while':
            self.indentLevel+=1
            code+=':'
        if line[0]=='if':
            self.indentLevel+=1
            code+=':'
        if line[0]=='print(':
            code+=' )'
        print(code)
        self.text.insert('end', str(code)+'\n')

    def save(self, event=None):
        f=open("script.py", "w")
##        g=open('stdout.py', 'r')
##        for l in g.readlines():
##            f.write(l)
##        g.close()
        f.write(str(self.text.get('1.0', 'end')))
        f.close()

    def clear(self, event=None):
        self.text.delete('1.0', 'end')
        self.indentLevel=0

    def execute(self, event=None):
        os.system("python script.py")
        time.sleep(0.2)
        self.text.delete('1.0', 'end')
        f=open('output', 'r')
        for l in f.readlines():
            self.text.insert('end', l)
        f.close()
        
        

        
        













if __name__=='__main__':
    app=App(None, bg="white")
    app.master.title("Hack Bordeaux 2019 !!!")
    


