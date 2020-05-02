from socket import *
import random
import datetime
import sys
import threading
import cmath
import webbrowser

print('_____________________________________________________________________________________________________________')
print('-----------------------------------Ky eshte programi per TCP-Server--------------------------------------------')
print('_____________________________________________________________________________________________________________')


serverPort = 13000


serverSocket = socket(AF_INET, SOCK_STREAM)


serverSocket.bind(('', serverPort))

print('Serveri startoi ne localhost me IP adrese: ' + str(gethostbyname(gethostname())) + " ne portin: " + str(
    serverPort))


serverSocket.listen(5)

print('Serveri eshte i gatshem te pranoj kerkesa...')


# --------------------------------------------------------METODAT: -------------------------------------------------------
def IPADDRESS(address):
    return str(address[0])
#-------------------------------------------------------------------------------------------------------------------------

def PORT(address):
    return str(address[1])
#-------------------------------------------------------------------------------------------------------------------------

def COUNT(str):
    vcount = 0
    ccount = 0
    str = str.lower()
    for i in range(0, len(str)):
        if str[i] in ('a', "e", "i", "o", "u"):
            vcount = vcount + 1;
        elif (str[i] >= 'a' and str[i] <= 'z'):
            ccount = ccount + 1;
    return vcount, ccount
#-------------------------------------------------------------------------------------------------------------------------

def REVERSE(s):
    return s[::-1]
#-------------------------------------------------------------------------------------------------------------------------

def PALINDROME(s):
    s = s.replace(" ", "")
    rev = REVERSE(s)
    if (s == rev):
        return str('Eshte Palindrom')
    return str('Nuk eshte Palindrom')
#-------------------------------------------------------------------------------------------------------------------------

def GCF(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    if num1 > num2:
        num1, num2 = num2, num1
    for x in range(num1, 0, -1):
        if num1 % x == 0 and num2 % x == 0:
            return str(x)
#-------------------------------------------------------------------------------------------------------------------------

def TIME():
    return str(datetime.datetime.now())
#-------------------------------------------------------------------------------------------------------------------------

def GAME():
    listaNumrave = []
    for i in range(5):
        listaNumrave.append(random.randint(1, 35))
    listaNumrave.sort()
    return str(listaNumrave)
#-------------------------------------------------------------------------------------------------------------------------

def CONVERT(tipi, vlera):
    vleraKonvertuar = 0
    vlera = float(vlera)

    if tipi == "CmToFeet":
        return str(vlera / 30.49)
        return str(vlera * 30.48)
    elif tipi == "KmToMiles":
        return str(vlera / 1.609)
    elif tipi == "MilesToKm":
        return str(vlera * 1.609)
    else:
        return "Error - Keni bere ndonje gabim gjate shenimit!"

#-------------------------------------------------------------------------------------------------------------------------
# metodat shtese

def UP_LOW(s):
    d = {"upper": 0, "lower": 0}
    for c in s:
        if c.isupper():
            d["upper"] += 1
        elif c.islower():
            d["lower"] += 1
    return str(d["upper"]),str(d["lower"])

#-------------------------------------------------------------------------------------------------------------------------

def OPENLINK(url):
    return webbrowser.open(url)
#-------------------------------------------------------------------------------------------------------------------------


def ShtypTeDhenat(teDhenat):
    print("\n----------------------------------------------------------------------------------------------")
    print("Te dhenat e derguara te klienti =>  ", teDhenat)
    return


def klienti_i_ri(connectionSocket, addr):
    kerkesa = (bytes)("empty".encode())
    try:
        while str(kerkesa.decode()).upper() != "EXIT" and str(kerkesa.decode()) != "":
            
            kerkesa = connectionSocket.recv(128)

            
            kerkesaStr = str(kerkesa.decode()).strip()

            
            kerkesaArray = kerkesaStr.split(' ')


            kerkesaArray[0] = kerkesaArray[0].upper()
# -------------------------------------------------------------------------------------------------------------------------

            # metoda IPADDRESS
            if kerkesaArray[0] == "IPADDRESS":
                if len(kerkesaArray) == 1:
                    connectionSocket.send(("IP adresa juaj eshte: " + IPADDRESS(addr)).encode())
                    ShtypTeDhenat(("IP adresa e klientit: " + IPADDRESS(addr)))
                else:
                    connectionSocket.send("Kerkesa juaj eshte gabim apo nuk ekziston, ju lutem provoni perseri!".encode())
                    ShtypTeDhenat("GABIM / ERROR")
#-------------------------------------------------------------------------------------------------------------------------
            # metoda PORT
            elif kerkesaArray[0] == "PORT":
                if len(kerkesaArray) == 1:
                    connectionSocket.send(("Numri i portit tuaj eshte: " + PORT(addr)).encode())
                    ShtypTeDhenat(("Numri i portit te klientit eshte: " + PORT(addr)))
                else:
                    connectionSocket.send("Kerkesa juaj eshte gabim apo nuk ekziston, ju lutem provoni perseri!".encode())
                    ShtypTeDhenat("GABIM / ERROR")
#-------------------------------------------------------------------------------------------------------------------------
            # metoda TIME
            elif kerkesaArray[0] == "TIME":
                if len(kerkesaArray) == 1:
                    connectionSocket.send(("Koha e tanishme eshte: " + TIME()).encode())
                    ShtypTeDhenat(("Koha e tanishme eshte: " + TIME()))
                else:
                    connectionSocket.send("Kerkesa juaj eshte gabim apo nuk ekziston, ju lutem provoni perseri!".encode())
                    ShtypTeDhenat("GABIM / ERROR")
#-------------------------------------------------------------------------------------------------------------------------
            # metoda GAME
            elif kerkesaArray[0] == "GAME":
                if len(kerkesaArray) == 1:
                    connectionSocket.send(("Rezultati nga loja: " + GAME()).encode())
                    ShtypTeDhenat(("Rezultati nga loja: " + GAME()))
                else:
                    connectionSocket.send("Kerkesa juaj eshte gabim apo nuk ekziston, ju lutem provoni perseri!".encode())
                    ShtypTeDhenat("GABIM / ERROR")
#-------------------------------------------------------------------------------------------------------------------------
            # metoda CONVERT
            elif kerkesaArray[0] == "CONVERT":
                for i in range(len(kerkesaArray)):
                    if "" in kerkesaArray:
                        kerkesaArray.remove("")
                if len(kerkesaArray) > 3 or len(kerkesaArray) < 3:
                    connectionSocket.send( ("Kerkesa juaj eshte gabim apo nuk ekziston, ju lutem provoni perseri!").encode())
                    ShtypTeDhenat("GABIM / ERROR")
                else:
                    Konvertimi = str(kerkesaArray[1]).lower().split("to")
                    pergjigja = kerkesaArray[2] + " " + str(Konvertimi[0]) + " jane te barabarte me " + CONVERT(
                        str(kerkesaArray[1]), kerkesaArray[2]) + " " + str(Konvertimi[1])
                    connectionSocket.send(str(pergjigja).encode())
                    ShtypTeDhenat(pergjigja)
#-------------------------------------------------------------------------------------------------------------------------
            # metoda GCF
            elif kerkesaArray[0] == "GCF":
                if len(kerkesaArray) == 3:
                    connectionSocket.send(("GCF eshte : " + GCF(kerkesaArray[1], kerkesaArray[2])).encode())
                    ShtypTeDhenat(("GCF eshte : " + GCF(kerkesaArray[1], kerkesaArray[2])))
                else:
                    connectionSocket.send("Kerkesa juaj eshte gabim apo nuk ekziston, ju lutem provoni perseri!".encode(clientAddress),
                        clientAddress)
                    ShtypTeDhenat("GABIM / ERROR")
#-------------------------------------------------------------------------------------------------------------------------
            # metoda PALINDROME
            elif kerkesaArray[0] == "PALINDROME":
                if len(kerkesaArray) == 2:
                    connectionSocket.send(("Fjala e dhene eshte : " + PALINDROME(kerkesaArray[1])).encode())
                    ShtypTeDhenat(("Fjala e dhene eshte : " + PALINDROME(kerkesaArray[1])))
                else:
                    connectionSocket.send("Kerkesa juaj eshte gabim apo nuk ekziston, ju lutem provoni perseri!".encode())
                    ShtypTeDhenat("GABIM / ERROR")
#-------------------------------------------------------------------------------------------------------------------------
            # metoda REVERSE
            elif kerkesaArray[0] == "REVERSE":
                if len(kerkesaArray) == 2:
                    connectionSocket.send(("Fjala reverse eshte : " + REVERSE(kerkesaArray[1])).encode())
                    ShtypTeDhenat(("Fjala reverse eshte : " + REVERSE(kerkesaArray[1])))
                else:
                    connectionSocket.send("Kerkesa juaj eshte gabim apo nuk ekziston, ju lutem provoni perseri!".encode())
                    ShtypTeDhenat("GABIM / ERROR")
#-------------------------------------------------------------------------------------------------------------------------
            # metoda COUNT
            elif kerkesaArray[0] == "COUNT":
                if len(kerkesaArray) == 2:
                    var1, var2 = COUNT(kerkesaArray[1])
                    var1 = str(var1)
                    var2 = str(var2)
                    connectionSocket.send(
                        ("Numri i zanoreve eshte : " + var1 + " Numri i bashtinglloreve " + var2).encode())
                    ShtypTeDhenat(("Numri i zanoreve dhe i bashtinglloreve eshte : " + var1 + " " + var2))
                else:
                    connectionSocket.send("Kerkesa juaj eshte gabim apo nuk ekziston, ju lutem provoni perseri!".encode())
                    ShtypTeDhenat("GABIM / ERROR")
#-------------------------------------------------------------------------------------------------------------------------
            # metodat shtese
            # metoda UP_LOW
            elif kerkesaArray[0] == "UP_LOW":
                if len(kerkesaArray) == 2:
                    var1,var2 = UP_LOW(kerkesaArray[1])
                    var1 = str(var1)
                    var2 = str(var2)
                    connectionSocket.send(("Jane "+ var1 +" shkronja te medha dhe "+ var2 +" shkronja te vogla").encode())
                    ShtypTeDhenat(("Numri i shkronjave te medha dhe i shkronjave te vogla eshte : " + var1 + " " + var2))
                else:
                    connectionSocket.send("Kerkesa juaj eshte gabim apo nuk ekziston, ju lutem provoni perseri!".encode())
                    ShtypTeDhenat("GABIM / ERROR!")
#-------------------------------------------------------------------------------------------------------------------------
            #metoda OPENLINK
            elif kerkesaArray[0] == "OPENLINK":
                if len(kerkesaArray) == 2:
                    connectionSocket.send(("Duke u hapur..." + OPENLINK(kerkesaArray[1])).encode())
                    ShtypTeDhenat(("Duke u hapur..." + OPENLINK(kerkesaArray[1])))
                else:
                    connectionSocket.send("Kerkesa juaj eshte gabim apo nuk ekziston, ju lutem provoni perseri!".encode())
                    ShtypTeDhenat("GABIM / ERROR!")
            
            else:
                connectionSocket.send("Kerkesa juaj eshte gabim apo nuk ekziston, ju lutem provoni perseri!".encode())
                ShtypTeDhenat("GABIM / ERROR!")
#-------------------------------------------------------------------------------------------------------------------------

        
        connectionSocket.close()
    except Exception as msg:
        print("\n GABIM / ERROR: ")
        print(str(msg))
        connectionSocket.close()



while 1:
    
    connectionSocket, addr = serverSocket.accept()
    print('Klienti me IP adrese %s dhe me numrin e portit %s eshte lidhur me server' % (addr))

    threading._start_new_thread(klienti_i_ri, (connectionSocket, addr))
