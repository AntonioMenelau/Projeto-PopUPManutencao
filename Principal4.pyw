from datetime import datetime

hojeD = int(datetime.now().strftime('%d'))
hojeM = int(datetime.now().strftime('%m'))
hojeY = int(datetime.now().strftime('%Y'))
Hoje = (hojeD * 24) + (hojeM * 730) + (hojeY * 8760)

with open('data.txt', 'r', encoding='utf-8') as datalimit:
    d = str(datalimit.read())
limiteD = int(d[0] + d[1])
limiteM = int(d[3] + d[4])
limiteY = int(d[6] + d[7] + d[8] + d[9])
limite = (limiteD * 24) + (limiteM * 730) + (limiteY * 8760)

with open('msg.txt', 'r', encoding='utf-8') as mensagem:
    msg = mensagem.read()

with open('titulo.txt', 'r', encoding='utf-8') as titu:
    titulo = titu.read()

if Hoje >= limite:
    from tkinter import *

    bg = '#c7d3dc'
    top = Tk()
    top.title(titulo.upper())
    top.geometry('650x200')
    top.resizable(width=0, height=0)
    top.config(background=bg)
    filename = PhotoImage(file="MasterTech-img-removebg 225x149.png")
    background_label = Label(top, image=filename, bg=bg, width=250, height=175)
    background_label.grid(row=0,
                          column=0,
                          rowspan=2)

    msgLabel = Label(top,
                     text=msg,
                     bg=bg,
                     justify=LEFT,
                     font=("Franklin Gothic Medium", "10"),
                     foreground='#454545')

    msgLabel.grid(sticky='w',
                  padx=10,
                  row=0,
                  column=1)

    botao = Button(top,
                   relief="solid",
                   borderwidth=0.5,
                   foreground='#454545',
                   bg=bg)
    botao['text'] = 'OK'
    botao['font'] = ("Franklin Gothic Medium", "15")
    botao['width'] = 7
    botao['command'] = top.destroy
    botao.grid(row=1,
               column=1,
               pady=5)

    top.mainloop()
