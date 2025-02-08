from tkinter import *

bg = '#c7d3dc'
top = Tk()
top.title('Teste')
top.geometry('500x300')
top.resizable(width=0, height=0)
top.config(background=bg)
filename = PhotoImage(file="MasterTech-img-removebg 225x149.png")
background_label = Label(top, image=filename, bg=bg, width=300, height=200)
background_label.grid(row=0,
                      column=0,
                      columnspan=2)

msg = Label(top,
            text='O prazo da sua manutenção foi vencida.\n'
                 'Entre em contato com MasterTech Soluções em Informática para a\n'
                 'manutenção de seu computador.\n'
                 '-(99) 99999-9999',
            bg=bg,
            justify=LEFT,
            font=("Franklin Gothic Medium", "10"),
            foreground='#454545')

msg.grid(sticky='w',
         padx=10,
         row=1,
         column=0)

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
