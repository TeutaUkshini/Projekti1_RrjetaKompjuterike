from socket import *
import sys

print('______________________________________________________________________________________________________________________')
print('-------------------------------------------Ky eshte programi per TCP-Klient-------------------------------------------')
print('______________________________________________________________________________________________________________________')


serverName = '127.0.0.1'  #127.0.0.1 ose localhost
serverPort = 13000


s = socket(AF_INET, SOCK_STREAM)

s.connect((serverName,serverPort))

kerkesa = ""

print("Jeni lidhur ne serverin ",serverName," ne portin ",serverPort)
print("______________________________________________________________________________________________________________________\n")

# MENYJA e programit 

width = 50
print("*************************************************************MIRSEVINI************************************************".center(width, '*'))
print("-----------------------------------------------------Universiteti i Prishtines ---------------------------------------".center(width, '-'))
print("-----------------------------------------Fakulteti i inxhinierise elektrike dhe kompjuterike--------------------------".center(width, '-'))
print("-------------------------------------------------Departamenti  i kompjuterikes----------------------------------------".center(width, '-'))
print("---------------------------------------------------Lenda: Rrjeta kompjuterike-----------------------------------------".center(width, '-'))
print("--------------------------------------------------------Programi TCP-Klient-------------------------------------------".center(width, '-'))
print("-------------------------------------------------------Studenti:Teuta Ukshini-----------------------------------------".center(width, '-'))

print("\nShtypni njërën nga kërkesat e dhëna më poshtë: ")
print("======================================================================================================================\n")
print("-IPADRESS\n-PORT\n-COUNT [COUNT {hapsire} text]\n-REVERSE [REVERSE {hapsire} text]\n-PALINDROME [PALINDROME {hapsire} text]\n-TIME\n-GAME\n-CONVERT [CONVERT {Hapësire} Opcioni {Hapësire} Numër]{Opcioni:CmtoFeet,FeetToCm,KmToMiles,MilesToKm}\n-GCF [GCF {hapsire} Number1 {hapsire} Number2]\n-UP_LOW[UP_LOW {hapesire} tekst]\n-OPENLINK [OPENLINK {hapesire} link]\n")

print("------------------------------------------------Shtyp exit per te ndal lidhjen.---------------------------------------")
print("______________________________________________________________________________________________________________________\n")

while 1:
    try:
        kerkesa = input('Shkruaj metoden adekuate si dhe opsionin(nese ka): ')
        if kerkesa!="" and kerkesa.upper()!="EXIT":
        
            s.sendall(str(kerkesa).encode())
        else:
            break
        
        data = s.recv(128)
        print('Te dhenat e pranuara nga serveri: ')
        print(str(data.decode()).strip())
        print("----------------------------------------------------------------------------------\n")
    except Exception as msg:
        print(str(msg))
        break
    
s.close()   
