import tkinter as tk
from tkinter import *
import os
import tkinter.font as font

#from turtle import bgcolor

descryption = '''CyberSecurity Tool developed by Group 2
It's an open Source project.
Tools included NetworkScanner and WebCrawler'''

def WindowConfiguration(tk,windowtitle):
    windowWidth = 600
    windowHeight = 400

    screenWidth = tk.winfo_screenwidth()
    screenHeight = tk.winfo_screenheight()

    centreX = int(screenWidth / 2 - windowWidth / 2)
    centreY = int(screenHeight / 2 - windowHeight / 2)

    defaultGeometry = f'{windowWidth}x{windowHeight}+{centreX}+{centreY}'
    
    tk.geometry(defaultGeometry)
    tk.configure(bg='#34495e')
    tk.resizable(False, False)
    tk.title(windowtitle)
    tk.attributes('-alpha', 1)
    #tk.iconbitmap('image.ico')

    
NetworkScannerFrame = None

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        WindowConfiguration(self,"CyberSecurity Multi-Tool")
        self.DisplayToolDescryption()
        self.CreateMenuButtons()

    def DisplayToolDescryption(self):
        global descryption
        descryptionLabel = Label(self,text = descryption, bg='#666699', fg='white',width=200, height=10, font= ('Courier New',12))
        descryptionLabel.pack()

    def OnNetworkScannerButtonClick(self):
        '''global NetworkScannerFrame
        NetworkScannerFrame = tk.Toplevel(self)
        WindowConfiguration(NetworkScannerFrame, windowtitle='NetWorkScanner')'''
        os.system("python3 NetworkScanner.py")

    def OnWebCrawlerButtonClick(self):
        os.system("python3 crawler.py")

    def OnDNSLookupButtonClick(Self):
        os.system("python3 .\DNS\dnsGui.py")
        
    def CreateMenuButtons(self):
        myFont = font.Font(size=15)
        networkScannerBtn = tk.Button(self,text='Network Scanner', command=lambda: self.OnNetworkScannerButtonClick(), bg='#2980B9', fg='white')
        networkScannerBtn.pack(side='left', padx=20, pady=20)
        networkScannerBtn['font'] = myFont
        WebScraperBtn = tk.Button(self,text='Web Crawler', command=lambda: self.OnWebCrawlerButtonClick(),bg='#2980B9', fg='white')
        WebScraperBtn.pack(side='right', padx=20, pady=20)
        WebScraperBtn['font'] = myFont
        GetDNSBtn = tk.Button(self,text='DNS', command=lambda: self.OnDNSLookupButtonClick(), bg='#2980B9', fg='white')
        GetDNSBtn.pack(side='bottom', padx=40, pady=20)
        GetDNSBtn['font'] = myFont


if __name__ == '__main__':
    app = App()
    app.mainloop()
