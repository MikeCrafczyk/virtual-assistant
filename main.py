from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

root = Tk()
#ikonka okna 
#
#nazwa okna 
root.title("wirtualny asystent")
#wysokość okna 
root.geometry("800x600")
# root.call("wm", "iconphoto", root._w, PhotoImage(file=""))

#działąnia funkcji
def  openNewWindow():
    newWindow = Toplevel(master)
    newWindow.title("ustawienia")
    newWindow.geometry("")
    Label(newWindow,text="aaaaa").pack()

def my_func1(event)
    
def my_func2(event)

def my_func3(event)

def my_func4(event)
    
#kolar okna aplikacji
root.config(background="dark green")        
#konfiguracja przyciskow schemat : nazwa kostruktor (rodzic , nazwa , czynosc)
btn1 = Button(root, text="ładowanie",)      
btn2 = Button(root, text="tryby",)          
btn3 = Button(root, text="ustawienia",)     
btn4 = Button(root, text="wyjście",)        

#pozycjonowanie przyciskow
btn1.place(x=,y=,height=,width=)            
btn2.place(x=,y=,height=,width=)            
btn3.place(x=,y=,height=,width=)            
btn4.place(x=,y=,height=,width=)            

root.mainloop() #zapętlenia kacji