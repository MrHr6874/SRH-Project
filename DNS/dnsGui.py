import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import dnsGui_support
import dns

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    dnsGui_support.set_Tk_var()
    top = DNS_Lookup (root)
    dnsGui_support.init(root, top)
    root.mainloop()

w = None
def create_DNS_Lookup(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    dnsGui_support.set_Tk_var()
    top = DNS_Lookup (w)
    dnsGui_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_DNS_Lookup():
    global w
    w.destroy()
    w = None




class DNS_Lookup:

    

    def something(self):
        result = dns.guiBuilder(self.domainName.get(), self.qType.get(), self.dnsIP.get()) 
        self.textBox.delete("1.0", END)
        for i in range(len(result)):

            #print(line[i])
            words = result[i].split(' ')
            #print(words)
            for i in range(len(words)):
                    if words[i] == 'Question:':
                        self.textBox.insert(END, 'Host Name: ')
                        self.textBox.insert(END, words[i+1].strip(".'")) 
                        self.textBox.insert(END, '\n')
                        #print('Host name: ' + words[i+1].strip(".'"))
                    elif words[i] == 'rtype=A' or words[i] == 'rtype=AAAA':
                        ip = words[-1][7:].strip("'>")
                        if (len(ip) > 20):
                            self.textBox.insert(END, 'IPv6: ')
                            self.textBox.insert(END, words[-1][7:].strip("'>")) 
                            self.textBox.insert(END, '\n')
                            #print("IPv6: " + ip)
                        else:
                            self.textBox.insert(END, 'IPv4: ')
                            self.textBox.insert(END, words[-1][7:].strip("'>"))  
                            self.textBox.insert(END, '\n')
                            #print("IPv4: " + ip)
                    elif words[i] == 'rtype=MX':
                        self.textBox.insert(END, 'MX: ')
                        self.textBox.insert(END, words[-1].strip(".'>"))  
                        self.textBox.insert(END, '\n')
                        #print("MX: " + words[-1].strip(".'>"))
                    elif words[i] == 'rtype=CNAME':
                        self.textBox.insert(END, 'CNAME: ')
                        self.textBox.insert(END, words[-1][7:].strip(".'>"))  
                        self.textBox.insert(END, '\n')
                        #print("CNAME: " + words[-1][7:].strip(".'>"))
                    elif words[i] == 'rtype=PTR':
                        self.textBox.insert(END, 'Inverse: ')
                        self.textBox.insert(END, words[-1][7:].strip(".'>"))  
                        self.textBox.insert(END, '\n')
                        #print("Inverse: " + words[-1][7:].strip(".'>"))
            

    # self.textBox.insert(END, result[i]) 
    # self.textBox.insert(END, '\n')  
        


    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("621x450+616+189")
        top.title("DNS Lookup")



        self.domainName = ttk.Entry(top)
        self.domainName.place(relx=0.1, rely=0.09, relheight=0.06, relwidth=0.31)
        
        self.domainName.configure(width=194)
        self.domainName.configure(takefocus="")
        self.domainName.configure(cursor="xterm")
        


        self.dnsIP = ttk.Entry(top)
        self.dnsIP.place(relx=0.43, rely=0.09, relheight=0.06, relwidth=0.23)
        self.dnsIP.configure(takefocus="")
        self.dnsIP.configure(cursor="xterm")

        self.dnLabel = Label(top)
        self.dnLabel.place(relx=0.09, rely=0.04, height=18, width=83)
        self.dnLabel.configure(text='''Domain Name''')

        self.dnsLabel = Label(top)
        self.dnsLabel.place(relx=0.43, rely=0.04, height=18, width=40)
        self.dnsLabel.configure(text='''Dns IP''')

        self.qtLabel = Label(top)
        self.qtLabel.place(relx=0.68, rely=0.04, height=18, width=67)
        self.qtLabel.configure(text='''Query Type''')

        self.qType = ttk.Combobox(top)
        self.qType.place(relx=0.69, rely=0.09, relheight=0.06, relwidth=0.22)
        self.value_list = ['AA', 'MX', 'PTR', 'CNAME', 'AAAA']
        self.qType.configure(values=self.value_list)
        self.qType.configure(textvariable=dnsGui_support.combobox)
        self.qType.configure(width=137)
        self.qType.configure(takefocus="")

        self.searchButton = Button(top)
        self.searchButton.place(relx=0.1, rely=0.16, height=26, width=65)
        self.searchButton.configure(activebackground="#d9d9d9")
        self.searchButton.configure(text='''Search''')
        self.searchButton.configure(command=self.something)

        self.textBox = Text(top)
        self.textBox.place(relx=0.1, rely=0.29, relheight=0.58, relwidth=0.81)
        self.textBox.configure(background="white")
        self.textBox.configure(font="TkTextFont")
        self.textBox.configure(selectbackground="#c4c4c4")
        self.textBox.configure(width=506)
        self.textBox.configure(wrap=WORD)
        





if __name__ == '__main__':
    vp_start_gui()






