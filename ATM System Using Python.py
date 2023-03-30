from tkinter import *
root=Tk()
root.geometry("900x850")
root.title("ATM MACHINE")
root.configure(bg="black")

Tops=Frame(root,bg="white",width=500,height=50)
Tops.pack(side=TOP)

f1=Frame(root,bg="black",width=300,height=700)
f1.pack(side=LEFT)

f2=Frame(root,bg="black",width=400,height=700)
f2.pack(side=RIGHT)


lblinfo=Label(Tops,font=('aria',30,'bold'),text="ATM MACHINE",fg="powder blue",bg="black",bd=10,anchor='w')
lblinfo.grid(row=0,column=0)

number=StringVar()
amount=StringVar()
withd=StringVar()
acca= " "

def bank():
    global acca
    accno=["00092","67898","078365"]      #list of account no
    account=number.get()
    if account in accno:
        label.config(text="Registered User")
        bank={"00092":10000,"67898":20000,"078365":30000} #Dictionary to store balances
        balance=bank[account]
        acca=balance
    else:
        label.config(text="Non Registered User")

def deposit():
    global acca
    amo=float(amount.get())
    acca=acca+amo
    label3.config(text="Deposit Successful!!")

def withdrawn():
    global acca
    wd=float(withd.get())
    if acca >= wd:
        acca=acca-wd
        label4.config(text="Withdrawl Successful!")
    else:
        label4.config(text=("Insufficient Balance"))

def reset():
    number.set("")
    amount.set("")
    withd.set("")
    label.config(text="")
    label4.config(text="")
    label3.config(text="")
    label5.config(text="")
    

def bal():
    global acca
    label5.config(text=("Net Balance:",str(acca)))
    

lbl=Label(f1,font=('aria',16,'bold'),text="Enter the account number:      ",fg="powder blue",bg="black",bd=10,anchor='w')
lbl.grid(row=0,column=3)
txt=Entry(f1,textvariable=number,font=('ariel',16,'bold'),bg="powder blue",bd=6,insertwidth=4,justify='right')
txt.grid(row=0,column=4)
label=Label(f1,font=('aria',16,'bold'),fg="white",bg="black")
label.grid(row=1,column=4)
btnsubmit=Button(f2,padx=16,pady=4,bd=10,font=('ariel',16,'bold'),bg="powder blue",fg="black",width=7,text="SUBMIT",command=bank)
btnsubmit.grid(row=0,column=4)

lblTotal=Label(f1,text="               ",fg="white",bg="black")
lblTotal.grid(row=3,columnspan=10)

lbl=Label(f1,font=('aria',16,'bold'),text="Enter ammount to be deposited:      ",fg="powder blue",bg="black",bd=10,anchor='w')
lbl.grid(row=4,column=3)
txt=Entry(f1,textvariable=amount,font=('ariel',16,'bold'),bg="powder blue",bd=6,insertwidth=4,justify='right')
txt.grid(row=4,column=4)
label3=Label(f1,font=('aria',16,'bold'),fg="white",bg="black")
label3.grid(row=5,column=4)
btndeposit=Button(f2,padx=16,pady=4,bd=10,font=('ariel',16,'bold'),bg="powder blue",fg="black",width=7,text="DEPOSIT",command=deposit)
btndeposit.grid(row=4,column=4)

lblTotal=Label(f1,text="               ",fg="white",bg="black")
lblTotal.grid(row=7,columnspan=10)

lbl=Label(f1,font=('aria',16,'bold'),text="Enter ammount to be withdrawn:      ",fg="powder blue",bg="black",bd=10,anchor='w')
lbl.grid(row=8,column=3)
txt=Entry(f1,textvariable=withd,font=('ariel',16,'bold'),bg="powder blue",bd=6,insertwidth=4,justify='right')
txt.grid(row=8,column=4)
label4=Label(f1,font=('aria',16,'bold'),fg="white",bg="black")
label4.grid(row=9,column=4)
label5=Label(f1,font=('aria',16,'bold'),fg="white",bg="black")
label5.grid(row=10,column=4)

btnwithdraw=Button(f2,padx=16,pady=4,bd=10,font=('ariel',16,'bold'),bg="powder blue",fg="black",width=7,text="WITHDRAW",command=withdrawn)
btnwithdraw.grid(row=8,column=4)

btnbal=Button(f2,padx=16,pady=4,bd=10,font=('ariel',16,'bold'),bg="powder blue",fg="black",width=7,text="BALANCE",command=bal)
btnbal.grid(row=10,column=4)
btnreset=Button(f2,padx=16,pady=4,bd=10,font=('ariel',16,'bold'),bg="powder blue",fg="black",width=7,text="RESET",command=reset)
btnreset.grid(row=11,column=4)
btnexit=Button(f2,padx=16,pady=4,bd=10,font=('ariel',16,'bold'),bg="powder blue",fg="black",width=7,text="EXIT",command=root.destroy)
btnexit.grid(row=12,column=4)

root.mainloop()
