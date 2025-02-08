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
    import ctypes


    def Mbox(title, text, style):
        return ctypes.windll.user32.MessageBoxW(0, text, title, style)


    Mbox(titulo.upper(), msg, 0)
