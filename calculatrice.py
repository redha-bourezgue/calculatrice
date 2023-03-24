import tkinter as tk

calculation=""

def ajouter_au_calcul(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0,"end")
    text_result.insert(1.0,calculation)

def evaluer_lecalcul():
    global calculation
    try:
        calculation=str(eval(calculation))
        text_result.delete(1.0,"end")
        text_result.insert(1.0,calculation)
    except:
        effacer_calcul()
        text_result.insert(1.0,"Error")

def effacer_calcul():
    global calculation
    calculation = ""
    text_result.delete(1.0,"end")

root=tk.Tk()
root.geometry("400x300")

text_result=tk.Text(root,height=2,width=16,font=('asia',24))
text_result.grid(columnspan=5)

btn_1=tk.Button(root,text="1",command=lambda:ajouter_au_calcul(1),width=5,font=('asia',14))
btn_1.grid(row=2,column=1)

btn_2=tk.Button(root,text="2",command=lambda:ajouter_au_calcul(2),width=5,font=('asia',14))
btn_2.grid(row=2,column=2)

btn_3=tk.Button(root,text="3",command=lambda:ajouter_au_calcul(3),width=5,font=('asia',14))
btn_3.grid(row=2,column=3)

btn_4=tk.Button(root,text="4",command=lambda:ajouter_au_calcul(4),width=5,font=('asia',14))
btn_4.grid(row=3,column=1)

btn_5=tk.Button(root,text="5",command=lambda:ajouter_au_calcul(5),width=5,font=('asia',14))
btn_5.grid(row=3,column=2)

btn_6=tk.Button(root,text="6",command=lambda:ajouter_au_calcul(6),width=5,font=('asia',14))
btn_6.grid(row=3,column=3)

btn_7=tk.Button(root,text="7",command=lambda:ajouter_au_calcul(7),width=5,font=('asia',14))
btn_7.grid(row=4,column=1)

btn_8=tk.Button(root,text="8",command=lambda:ajouter_au_calcul(8),width=5,font=('asia',14))
btn_8.grid(row=4,column=2)

btn_9=tk.Button(root,text="9",command=lambda:ajouter_au_calcul(9),width=5,font=('asia',14))
btn_9.grid(row=4,column=3)

btn_0=tk.Button(root,text="0",command=lambda:ajouter_au_calcul(0),width=5,font=('asia',14))
btn_0.grid(row=5,column=2)

btn_plus=tk.Button(root,text="+",command=lambda:ajouter_au_calcul("+"),width=5,font=('asia',14))
btn_plus.grid(row=2,column=5)

btn_sous=tk.Button(root,text="-",command=lambda:ajouter_au_calcul("-"),width=5,font=('asia',14))
btn_sous.grid(row=3,column=5)

btn_div=tk.Button(root,text="/",command=lambda:ajouter_au_calcul("/"),width=5,font=('asia',14))
btn_div.grid(row=4,column=5)

btn_mul=tk.Button(root,text="x",command=lambda:ajouter_au_calcul("*"),width=5,font=('asia',14))
btn_mul.grid(row=5,column=5)

btn_open=tk.Button(root,text="(",command=lambda:ajouter_au_calcul("("),width=5,font=('asia',14))
btn_open.grid(row=5,column=1)

btn_clos=tk.Button(root,text=")",command=lambda:ajouter_au_calcul(")"),width=5,font=('asia',14))
btn_clos.grid(row=5,column=3)

btn_equal=tk.Button(root,text="=",command=evaluer_lecalcul,width=10,font=('asia',14))
btn_equal.grid(row=6,column=3,columnspan=2)

btn_clear=tk.Button(root,text="C",command=effacer_calcul,width=10,font=('asia',14))
btn_clear.grid(row=6,column=1,columnspan=2)

root.mainloop()