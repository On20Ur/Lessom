from tkinter import *
from tkinter import messagebox

def Person():
    daxil_login = "person123"
    daxil_password = "12345"
    if entry_Login.get() == daxil_login and entry_password.get() == daxil_password:
        loginFrame.place_forget()
        Anbar.place(x=0,y=0)
    else:
        messagebox.showerror("ERROR","login ve ya Password yanlisdir")

class Phone:
    def _init_(self,model,name,price):
        self.__price = price
        self.__model = model
        self.__name = name

    def getModel(self):
        return self.__model

    def getName(self):
        return self.__name

    def getPrice(self):
        return self.__price


class User:
    def _init_(self,name,surname,age,login,password,position):
        self.__name = name
        self.__surname = surname
        self.__age = age
        self.__login = login
        self.__password = password
        self.__position = position

    def getPosition(self):
        return self.__position

    def getName(self):
        return self.__name

    def getSurname(self):
        return self.__surname

    def getAge(self):
        return self.__age

    def getLogin(self):
        return self.__login

    def changeLogin(self,login):
        self.__login = login

    def changePassword(self,password):
        self.__password = password

    def getPassword(self):
        return self.__password

def Qeyydiyat():
    loginFrame.place_forget()
    Giris.place(x=0,y=0)

def Genel():
    loginFrame.place_forget()
    genel.place(x=0,y=0)

    Giris.place_forget()
    Genel.place(x=0,y=0)


#Fuksiya hissei

def DaxilOl():
    for i in user:
        if i.getlogin() == entry_Login.get() and i.getPassword() == entry_password.get() and i.getPosition() == "anbar":
            Giris.place_forget()
            Anbar.place(x=0,y=0)
        else:
            messagebox.showerror("Error","Error")

usre1 = ("Onur","Bagirov",15,"onur123","123454","anbar")
usre2 = ("Ali","Agazade",15,"ali123","1233","satis")

user = [usre1,usre2]
Window1 = Tk()
Window1.geometry("500x500")
Window1.title("STEP PETROL")



#Pencere Hissei

loginFrame = Frame(bg="cyan",width=500,height=500,background="#809fff")
loginFrame.place(x=0,y=0)

genel = Frame(bg="Blue",width=500,height=500,background="Red")

Anbar = Frame(bg="red",width=500,height=500,background="Black")

Giris = Frame(width=500,height=500,background="#809fff")

#Esas Sehive

loginFrame = Frame(bg="cyan",width=500,height=500,background="#809fff")
loginFrame.place(x=0,y=0)


label_loginfarme1 = Label(loginFrame,text="Qeydiyyat Seyfesi",width=30,height=2,
            background="#809fff",fg="white",font=(2))
label_loginfarme1.place(x=90,y=0)

lable_sayfa1 = Label(loginFrame,text="Qeyydiyat",height=2,width=15,
            background="green",fg="white",font=(2))
lable_sayfa1.place(x=170,y=80)


lable_Login1 = Label(loginFrame,text="Login: ",height=2,
            background="#809fff",fg="white",font=(2))
lable_Login1.place(x=0,y=187)

entry_Login = Entry(loginFrame,width=20,font=(3))
entry_Login.place(x=130,y=195)

label_password = Label(loginFrame,text="Password: ",height=2,
            background="#809fff",fg="white",font=(2))
label_password.place(x=0,y=270)

entry_password= Entry(loginFrame,width=20,font=(2))
entry_password.place(x=130,y=280)

button = Button(loginFrame,text="Daxil ol",width=10,command=Person)
button.place(x=150,y = 330)

button_daxil_ol = Button(loginFrame,text="Qeydiyyat",width=10,command=Qeyydiyat)
button_daxil_ol.place(x=250,y = 330)

#Qeydiyyat Bolmesi====================================================================

label_loginfarme1 = Label(Giris,text="Qeydiyyat bolmsei",width=30,height=2,
            background="Black",fg="white",font=(2))
label_loginfarme1.place(x=90,y=0)

lable_name = Label(Giris,text="Name",bg="Red")
lable_name.place(x=10,y=100)

entry_name1 = Entry(Giris)
entry_name1.place(x=70,y=100)

lbale_surname = Label(Giris,text="Surname",bg="Red")
lbale_surname.place(x=10,y=140)

entry_surname1 = Entry(Giris)
entry_surname1.place(x=90,y=140)

lable_age = Label(Giris,text="Age",bg="red")
lable_age.place(x=10,y=180)

entry_age1 = Entry(Giris)
entry_age1.place(x=60,y=180)

lable_login = Label(Giris,text="Login",bg="red")
lable_login.place(x=10,y=220)

entry_login1 = Entry(Giris)
entry_login1.place(x=70,y=220)

lable_paasword = Label(Giris,text="Password",bg="red")
lable_paasword.place(x=10,y=260)

entry_password1 = Entry(Giris)
entry_password1.place(x=100,y=260)

button_qeydiyyat = Button(Giris,text="Qeydiyyat",command=Genel)
button_qeydiyyat.place(x=250,y=300)

#Genel Hissei------------------------------------------

label_loginfarme = Label(genel,text="Girsi Bolmesi",width=30,height=2,
            background="Black",fg="white",font=(2))

lable_genel = Label(genel,text="Qeyydiyat",height=2,width=15,
            background="green",fg="white",font=(2))
lable_genel.place(x=170,y=80)


lable_login1 = Label(genel,text="Login: ",
            background="black",fg="white")
lable_login1.place(x=0,y=187)

entry_giris = Entry(genel)
entry_giris.place(x=70,y=187)

button_anbar = Button(genel,text="Anbar")
button_anbar.place(x=125,y=500)


Window1.mainloop()
