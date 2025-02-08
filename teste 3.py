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


    class Janela:
        def __init__(self):
            # ----------------------------------------
            self.msgLabel = Label(root,
                                  text=f'{msg}',
                                  font=("Franklin Gothic Medium", "10"))
            self.msgLabel.grid(row=1,
                               column=0,
                               sticky='we',
                               pady=5)
            self.msgLabel["anchor"] = 'w'
            # -----------------------------------------
            self.botao = Button(root,
                                relief="solid",
                                borderwidth=0.5)
            self.botao['text'] = 'OK'
            self.botao['font'] = ("Franklin Gothic Medium", "15")
            self.botao['width'] = 10
            self.botao['command'] = root.destroy
            self.botao.grid(row=15,
                            column=0,
                            rowspan=2,
                            pady=5)


    root = Tk()
    root.title(f'{titulo}')
    Janela()
    root.mainloop()
