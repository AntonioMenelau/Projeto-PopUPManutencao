with open('data.txt', 'r') as datalimit:
    d = str(datalimit.read())
limiteD = int(d[0] + d[1])
limiteM = int(d[3] + d[4])
limiteY = int(d[6] + d[7] + d[8] + d[9])
limite = (limiteD * 24) + (limiteM * 730) + (limiteY * 8760)
