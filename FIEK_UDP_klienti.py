from socket import *

print('______________________________________________________________________________________________________________________')
print('-------------------------------------------Ky eshte programi per UDP-Klient-------------------------------------------')
print('______________________________________________________________________________________________________________________')

serverName = '127.0.0.1'  #127.0.0.1 ose localhost
serverPort = 13000


s = socket(AF_INET, SOCK_DGRAM)

print("Jeni lidhur ne serverin ",serverName," ne portin ",serverPort)
print("====================================================================================================================\n")

# MENYJA e programit 
print ("""
*************************************************************MIRSEVINI************************************************
-----------------------------------------------------Universiteti i Prishtinës ---------------------------------------
-----------------------------------------Fakulteti i inxhinierise elektrike dhe kompjuterike--------------------------
-------------------------------------------------Departamenti  i kompjuterikes----------------------------------------
---------------------------------------------------Lenda: Rrjeta kompjuterike-----------------------------------------
--------------------------------------------------------Programi UDP-Klient-------------------------------------------
------------------------------------------------------Studenti:Teuta Ukshini------------------------------------------

\nShtypni njërën nga kërkesat e dhëna më poshtë: 
======================================================================================================================\n
-IPADDRESS\n-PORT\n-COUNT [COUNT {hapsire} text]\n-REVERSE [REVERSE {hapsire} text]\n-PALINDROME [PALINDROME {hapsire} text]\n-TIME\n-GAME\n-CONVERT [CONVERT {Hapësire} Opcioni {Hapësire} Numër] {opcioni CmToFeet,FeetToCm,KmToMiles,MilesToKm}\n-GCF [GCF {hapsire} Number1 {hapsire} Number2]\n-UP_LOW [UP_LOW {hapesire} tekst]\n-OPENLINK [OPENLINK {hapesire} link]\n

-------------------------------------------------------Shtyp exit per te ndal lidhjen.--------------------------------
______________________________________________________________________________________________________________________\n """) 

while 1:
    try:
        kerkesa = input('Shkruaj metoden adekuate dhe opcionin (nese ka): ')
        if kerkesa!="" and kerkesa.upper()!="EXIT":
            
            s.sendto(str(kerkesa).encode(), (serverName, serverPort))
        else:
            break
        
        data, serverAddress = s.recvfrom(128)
        print('Te dhenat e pranuara nga serveri: ')
        print(str(data.decode()).strip())
        print("----------------------------------------------------------------------------------------\n")
    except Exception as msg:
        print(str(msg))
        break

s.close()   




