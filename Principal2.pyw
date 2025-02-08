from datetime import datetime

hojeD = int(datetime.now().strftime('%d'))
hojeM = int(datetime.now().strftime('%m'))
hojeY = int(datetime.now().strftime('%Y'))
Hoje = (hojeD * 24) + (hojeM * 730) + (hojeY * 8760)

limiteD = 9
limiteM = 12
limiteY = 2021
limite = (limiteD * 24) + (limiteM * 730) + (limiteY * 8760)

if Hoje >= limite:
    import pyautogui
    pyautogui.alert(text="O prazo da sua manutenção foi vencida,\n"
                    "Entre em contato com MasterTech Soluções em Informática para a "
                    "manutenção de seu computador.\n"
                    "-(99) 99999-9999",
                    title='Data de manutenção vencida'.upper())
