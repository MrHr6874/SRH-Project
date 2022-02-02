from tkinter import *
import tkinter as tk
from tkinter import messagebox as ms
from PIL import ImageTk, Image
from bs4 import BeautifulSoup
import urllib.request

def Scrape(arg=None):
    

    if url_entry.get() == '':
        ms.showerror('Oops', 'Enter A Valid URL !!!')
        
    else:
        try:
            
            
            url = url_entry.get()
            
            
            content = urllib.request.urlopen(url).read()
            
            
            soup = BeautifulSoup(content, features="lxml")

            
            info = soup.prettify()
            


            root = tk.Toplevel()

            
            root.title('Thank You For Using Our Service !!!!')

            
            root.iconbitmap('img/logo.ico')

            
            root.resizable(width=False, height=False)
            
            
            
            
            scrollbar = Scrollbar(root)
            scrollbar.pack(side=RIGHT, fill=Y)

            
            text = Text(root, yscrollcommand=scrollbar.set, wrap = WORD)
            text.insert(INSERT, info)
            text.pack()

            
            scrollbar.config(command=text.yview)

        except ValueError:
            ms.showerror('Error', 'Enter A Valid URL !!!')
    


crawler = tk.Tk()


crawler.geometry('600x400')


crawler.resizable(width=False, height=False)


crawler.title('Web Crawler')


crawler.iconbitmap('img/logo.ico')
''' Window Setting End '''


top_frame = Label(crawler, text='WEB SCRAPER',font = ('Courier New', 25, 'bold'), bg='#2980B9', fg='white', relief='groove',padx=500, pady=30, bd='5')
top_frame.pack(side='top')



canvas = Canvas(crawler, width=500, height=500)


image = ImageTk.PhotoImage(Image.open('img/bg1.jpg'))


canvas.create_image(0,0, anchor=NW, image=image)
canvas.pack()


frame = LabelFrame(crawler, padx=30, pady=40, bg='white', bd='5', relief='groove')
frame.place(relx = 0.5, rely = 0.5, anchor = CENTER)

 
url_add = tk.Label(frame, text = 'Enter a URL or Web Address',font=('Courier New',10, 'bold'),bg='white', fg='#34495e').pack()

url_entry = tk.Entry(frame, font=('Courier New',10,'normal'), justify = 'center', bg='#FBB13C', width='30')


url_entry.bind('<Return>', Scrape)


url_entry.focus_set()


url_entry.pack()


label = Label(frame, bg='white').pack()


crawl = tk.Button(frame, text = "Scrape", width="10", bd = '3', command = Scrape, font = ('Courier New', 12, 'bold'), bg='#7268A6',relief='groove', justify = 'center', pady='5').pack()


crawler.mainloop()

 
