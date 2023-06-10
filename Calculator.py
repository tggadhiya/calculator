from tkinter import*

def click(event):
    global scvalue
    text= event.widget.cget("text")
    print(text)
    if text=="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            try:
                value=eval(v1.get())
            except Exception as e:
                print(e)
                value = "Error"

        scvalue.set(value)
        v1.update()

    elif text=="C":
        scvalue.set("")
        v1.update()
    else:
        scvalue.set(scvalue.get() + text)
        v1.update()



root=Tk()
root.geometry("390x570")

scvalue=StringVar()
scvalue.set("")

v1=Entry(root,textvariable=scvalue,font="lucida 45 bold",bg="black",fg="white",relief=SUNKEN)
v1.pack(fill=X,ipadx=8,padx=10,pady=12)

b1=Button(root,text="C",font="lucida 25 bold",padx=20,pady=15,bg="black",fg="red")
b1.place(x=0,y=95)
b1.bind("<Button-1>",click)

b1=Button(root,text="<>",font="lucida 25 bold",padx=12,pady=15,bg="black",fg="green")
b1.place(x=100,y=95)
b1.bind("<Button-1>",click)

b1=Button(root,text="%",font="lucida 25 bold",padx=18,pady=15,bg="black",fg="green")
b1.place(x=200,y=95)
b1.bind("<Button-1>",click)

b1=Button(root,text="/",font="lucida 25 bold",padx=27,pady=15,bg="black",fg="green")
b1.place(x=300,y=95)
b1.bind("<Button-1>",click)

##### 2


b2=Button(root,text="7",font="lucida 25 bold",padx=23,pady=15,bg="black",fg="white")
b2.place(x=0,y=190)
b2.bind("<Button-1>",click)

b2=Button(root,text="8",font="lucida 25 bold",padx=22,pady=15,bg="black",fg="white")
b2.place(x=100,y=190)
b2.bind("<Button-1>",click)

b2=Button(root,text="9",font="lucida 25 bold",padx=22,pady=15,bg="black",fg="white")
b2.place(x=200,y=190)
b2.bind("<Button-1>",click)

b2=Button(root,text="*",font="lucida 25 bold",padx=25,pady=15,bg="black",fg="green")
b2.place(x=300,y=190)
b2.bind("<Button-1>",click)


###3
b3=Button(root,text="4",font="lucida 25 bold",padx=23,pady=15,bg="black",fg="white")
b3.place(x=0,y=285)
b3.bind("<Button-1>",click)

b3=Button(root,text="5",font="lucida 25 bold",padx=22,pady=15,bg="black",fg="white")
b3.place(x=100,y=285)
b3.bind("<Button-1>",click)

b3=Button(root,text="6",font="lucida 25 bold",padx=22,pady=15,bg="black",fg="white")
b3.place(x=200,y=285)
b3.bind("<Button-1>",click)

b3=Button(root,text="-",font="lucida 25 bold",padx=26,pady=15,bg="black",fg="green")
b3.place(x=300,y=285)
b3.bind("<Button-1>",click)

####4

b4=Button(root,text="1",font="lucida 25 bold",padx=23,pady=15,bg="black",fg="white")
b4.place(x=0,y=380)
b4.bind("<Button-1>",click)

b4=Button(root,text="2",font="lucida 25 bold",padx=22,pady=15,bg="black",fg="white")
b4.place(x=100,y=380)
b4.bind("<Button-1>",click)

b4=Button(root,text="3",font="lucida 25 bold",padx=22,pady=15,bg="black",fg="white")
b4.place(x=200,y=380)
b4.bind("<Button-1>",click)

b4=Button(root,text="+",font="lucida 25 bold",padx=22,pady=15,bg="black",fg="green")
b4.place(x=300,y=380)
b4.bind("<Button-1>",click)

##5

b5=Button(root,text=",",font="lucida 25 bold",padx=27,pady=15,bg="black",fg="white")
b5.place(x=0,y=475)
b5.bind("<Button-1>",click)
b5=Button(root,text="0",font="lucida 25 bold",padx=22,pady=15,bg="black",fg="white")
b5.place(x=100,y=475)
b5.bind("<Button-1>",click)
b5=Button(root,text=".",font="lucida 25 bold",padx=26,pady=15,bg="black",fg="white")
b5.place(x=200,y=475)
b5.bind("<Button-1>",click)
b5=Button(root,text="=",font="lucida 25 bold",padx=26,pady=15,bg="black",fg="green")
b5.place(x=300,y=475)
b5.bind("<Button-1>",click)

root.mainloop()
