#!/usr/bin/python
#import rijeci
from selenium import webdriver
import time
from colorama import Fore, Back, Style
import sys
import os
from console_progressbar import ProgressBar
import datetime
import string
import smtplib
import random





od = 0

while(od!=100):

    os.system('cls||clear')
    print(Fore.BLUE + Style.BRIGHT + """
      /$$$$$$                                /$$               /$$           /$$
     /$$__  $$                              |__/              | $$          |__/
    | $$  \__/  /$$$$$$   /$$$$$$   /$$$$$$$ /$$ /$$  /$$$$$$ | $$  /$$$$$$$ /$$
    |  $$$$$$  /$$__  $$ /$$__  $$ /$$_____/| $$|__/ |____  $$| $$ /$$_____/| $$
     \____  $$| $$  \ $$| $$$$$$$$| $$      | $$ /$$  /$$$$$$$| $$| $$      | $$
     /$$  \ $$| $$  | $$| $$_____/| $$      | $$| $$ /$$__  $$| $$| $$      | $$
    |  $$$$$$/| $$$$$$$/|  $$$$$$$|  $$$$$$$| $$| $$|  $$$$$$$| $$|  $$$$$$$| $$
     \______/ | $$____/  \_______/ \_______/|__/| $$ \_______/|__/ \_______/|__/
              | $$                         /$$  | $$
              | $$                        |  $$$$$$/
              |__/                         \______/
    """)

    print(Fore.YELLOW + Style.BRIGHT + '!!!!DOBRODOŠLI!!!!' + Style.RESET_ALL)
    print(Fore.YELLOW + Style.BRIGHT + '!!!!SPECIJALCI!!!!' + Style.RESET_ALL)
    print()
    print(Fore.YELLOW + Style.BRIGHT +'1. WHATSAPP' + Style.RESET_ALL)
    print(Fore.YELLOW + Style.BRIGHT +'1)' + Style.RESET_ALL + 'jednostavno tekst')
    print(Fore.YELLOW + Style.BRIGHT +'2)' + Style.RESET_ALL + 'riječ po riječ')
    print(Fore.YELLOW + Style.BRIGHT +'3)' + Style.RESET_ALL + 'slovo po slovo')
    print(Fore.YELLOW + Style.BRIGHT +'4)' + Style.RESET_ALL + 'izmjene')
    print(Fore.YELLOW + Style.BRIGHT +'5)' + Style.RESET_ALL + 'raspored')
    print(Fore.YELLOW + Style.BRIGHT +'6)' + Style.RESET_ALL + 'dnevni info')
    print()
    print(Fore.YELLOW + Style.BRIGHT +'2. GOOGLE KALENDAR' + Style.RESET_ALL)
    print(Fore.YELLOW + Style.BRIGHT +'7)' + Style.RESET_ALL + 'izmjene - auto')
    print()
    print(Fore.YELLOW + Style.BRIGHT +'3. INSTAGRAM' + Style.RESET_ALL)
    print(Fore.YELLOW + Style.BRIGHT +'8)' + Style.RESET_ALL + 'auto - like')
    print()
    print(Fore.YELLOW + Style.BRIGHT +'4. WIKI' + Style.RESET_ALL)
    print(Fore.YELLOW + Style.BRIGHT +'9)' + Style.RESET_ALL + 'wordlist')
    print()


    od = int(input())

    if(od==1):
        driver = webdriver.Chrome('/home/jakov/Desktop/tsrb/izmjene/drivers/chromedriver')
        driver.get('https://web.whatsapp.com/')
        print(Fore.GREEN + Style.BRIGHT)
        li = str(input("PORUKA: "))
        n = int(input("BROJ PONAVLJANJA: "))
        print(Style.RESET_ALL)
        print(Fore.YELLOW + Style.BRIGHT + 'Jeste li spremni? (y/n)')
        p = str(input())
        if(p=='n'):
            sys.exit()
        else:
            pb = ProgressBar(total=100,prefix='Početak', suffix='Kraj', decimals=0, length=50, fill='X', zfill='-')
            for i in range(n):
                pb.print_progress_bar(((i+1)/float(n))*100)
                sr = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
                sr.click
                sr.send_keys(li)
                sr.send_keys(u'\ue007')
    elif(od==2):
        driver = webdriver.Chrome('/home/jakov/Desktop/tsrb/izmjene/drivers/chromedriver')
        driver.get('https://web.whatsapp.com/')
        print(Fore.GREEN + Style.BRIGHT)
        li = list(input("TEXT: ").split())
        print(Style.RESET_ALL)
        print(Fore.YELLOW + Style.BRIGHT + 'Jeste li spremni? (y/n)')
        p = str(input())
        if(p=='n'):
            sys.exit()
        else:
            pb = ProgressBar(total=100,prefix='Početak', suffix='Kraj', decimals=0, length=50, fill='X', zfill='-')
            for i in range(len(li)):
                pb.print_progress_bar(((i+1)/float(len(li)))*100)
                sr = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
                sr.click
                sr.send_keys(li[i])
                sr.send_keys(u'\ue007')
    elif(od==3):
        #print(Fore.RED + Style.BRIGHT + "@pekas"+ Style.RESET_ALL)
        driver = webdriver.Chrome('/home/jakov/Desktop/tsrb/izmjene/drivers/chromedriver')
        driver.get('https://web.whatsapp.com/')
        print(Fore.GREEN + Style.BRIGHT)
        li = input("TEXT: ").split()
        n = int(input("BROJ PONAVLJANJA: "))
        d = int(input("ODGODA(s): "))
        print(Style.RESET_ALL)
        print(Fore.YELLOW + Style.BRIGHT + 'Jeste li spremni? (y/n)')
        p = str(input())
        if(p=='n'):
            sys.exit()
        else:
            pb = ProgressBar(total=100,prefix='Početak', suffix='Kraj', decimals=0, length=50, fill='X', zfill='-')
            for ii in range(n):

                for i in range(len(li)):
                    for x in range(len(li[i])):
                        zn = list(str(li[i]))
                        sr = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
                        sr.click
                        sr.send_keys(zn[x])
                        sr.send_keys(u'\ue007')
                        time.sleep(d)
                        pb.print_progress_bar(((ii+1)/float(n))*100)
    elif(od==4):
        r = str(input("RAZRED: "))
        driver = webdriver.PhantomJS('/home/jakov/Desktop/tsrb/izmjene/drivers/phantomjs')
        driver.get('https://docs.google.com/document/d/e/2PACX-1vSSFLOpcnjyfI3tIWSpyWYBDrYvj0Y_VQmJT86GRCCsIiOZxAq6FNgxUhP4_lVj6omOyhMn-QKy6ZmR/pub?embedded=true')
        d = datetime.datetime.today()
        locator = driver.find_element_by_xpath('/html/body/p[1]/span').text
        Ltitle = locator
        locator = locator[:-5]
        tableElement = driver.find_element_by_xpath('/html/body/table[1]')
        if str(d.day) not in locator:
        	locator = driver.find_element_by_xpath('/html/body/p[4]/span[2]').text
        	Ltitle = locator
        	locator = locator[:-5]
        	tableElement = driver.find_element_by_xpath('/html/body/table[2]')
        	if str(d.day) not in locator:
        		locator = driver.find_element_by_xpath('/html/body/p[8]/span').text
        		Ltitle = locator
        		locator = locator[:-5]
        		tableElement = driver.find_element_by_xpath('/html/body/table[3]')
        		if str(d.day) not in locator:
        			locator = driver.find_element_by_xpath('/html/body/p[12]/span[2]').text
        			Ltitle = locator
        			locator = locator[:-5]
        			tableElement = driver.find_element_by_xpath('/html/body/table[4]')
        t = list()
        for i in range(1,10):
            print('.//tbody/tr[4]/td['+str(i)+']')
            t.append(str(tableElement.find_element_by_xpath('.//tbody/tr[4]/td['+str(i)+']').text))
        q = list()
        for i in range(1,10):
            print('.//tbody/tr[1]/td['+str(i)+']')
            q.append(tableElement.find_element_by_xpath('.//tbody/tr[1]/td['+str(i)+']').text)

        driver = webdriver.Chrome('/home/jakov/Desktop/tsrb/izmjene/drivers/chromedriver')
        driver.get('https://web.whatsapp.com/')
        print(Fore.YELLOW + Style.BRIGHT + 'Jeste li spremni? (y/n)')
        p = str(input())
        if(p=='n'):
            sys.exit()
        else:
            sr = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
            sr.click
            print(t,q)
            sr.send_keys('IZMJENE ZA ' + str(r))
            sr.send_keys(u'\ue007')
            for i in range(len(q)):
                sr.send_keys(q[i]+" "+t[i])
                #sr.send_keys(t[i]+" "+str(q[i]))
                print(t[i],q[i])
                sr.send_keys(u'\ue007')
    elif(od==5):
        zp = ['7:30','8:20','9:10','10:15','11:05','11:55','12:45','13:35','14:25','15:15','16:20','17:10','18:00','18:50']
        zk = ['8:15','9:05','9:55','11:00','11:50','12:40','13:30','14:20','15:10','16:00','17:05','17:55','18:45','19:35']
        dani = ['Ponedjeljak','Utorak','Srijedu','Četvrtak','Petak']
        ras = [[['HRV','OE','AIP','AIP','UITTUP','UITTUP','MAT-DOP',''],['TD','TD','GEO','MAT','KEM','FIZ','FIZ',''],['MAT','ENJ','OE','OE','GEO','SR','KEM',''],['MAT','FIZ','OE','POV','HRV','TZK','TZK','E/V'],['MAT','BIO','HRV','AIP','OE','POV','ENJ','']],[['V/E','SR','UITTUP','UITTUP','HRV','MAT','AIP',''],['MAT-DOP','KEM','KEM','OE','FIZ','OE','ENJ',''],['','','GEO','MAT','OE','POV','FIZ',''],['OE','ENJ','HRV','TZK','TZK','POV','MAT','GEO'],['TD','TD','MAT','OE','BIO','HRV','AIP','AIP']]]
        d = int(input("DAN U TJEDNU(1-7): "))
        d = d -1
        s = str(input("SMJENA(A,B): "))
        a = input("AUTOMATSKO SLANJE(y/n): ")
        if(a=='y'):
            driver = webdriver.Chrome('/home/jakov/Desktop/tsrb/izmjene/drivers/chromedriver')
            driver.get('https://web.whatsapp.com/')
            print(Fore.YELLOW + Style.BRIGHT + 'Jeste li spremni? (y/n)')
            p = str(input())
            if(p=='n'):
                sys.exit()
            else:
                if(s == 'A'):
                    i = 0
                else:
                    i = 1

            #z = d
            while(True):
                sr = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
                sr.click

                if(d==5):
                    print(d)
                    d = 0
                    print(d)
                    i = i + 1
                    if(i>=2):
                        i = 0
                sr.send_keys('Raspored za ' + str(dani[d]))
                sr.send_keys(u'\ue007')
                bc = 0
                for l in range(len(ras[i][d])):
                    if(ras[i][d][l]==''):
                        bc = bc + 1

                if(i==0):
                    sr.send_keys("Škola počinje u *" + str(zp[0]) + "* i završava u *" + str(zp[len(ras[i][d])-bc])+"*")
                    #print("Škola počinje u *" + str(zp[bc]) + "* i završava u *" + str(zp[len(ras[i][d])+bc])+"*")
                    sr.send_keys(u'\ue007')
                else:
                    bc = 0
                    br = 0
                    for q in range(4):
                        if(ras[i][d][q]==''):
                            bc = bc + 1
                    for q in range(7,7//2,-1):
                        if(ras[i][d][q]==''):
                            br = br + 1
                    print(len(ras[i][d])+bc+6-1,bc,len(zk))
                    sr.send_keys("Škola počinje u *" + str(zp[6+bc]) + "* i završava u *" + str(zk[-(br+1)])+"*")
                    sr.send_keys(u'\ue007')




                for iii in range(len(ras[i][d])):
                    if(i==0):
                        print(str(iii+1)+'.',ras[i][d][iii])
                        sr.send_keys('*'+str(iii+1)+'.* '+str(ras[i][d][iii]))
                        sr.send_keys(u'\ue007')
                    else:
                        print(str(iii)+'.',ras[i][d][iii])
                        sr.send_keys('*'+str(iii)+'.* '+str(ras[i][d][iii]))
                        sr.send_keys(u'\ue007')

                time.sleep(24*60*60)
                d = d + 1
                print(d)
    elif(od==6):
        def izmjene():
            driver = webdriver.PhantomJS('/home/jakov/Desktop/tsrb/izmjene/drivers/phantomjs')
            driver.get('https://docs.google.com/document/d/e/2PACX-1vSSFLOpcnjyfI3tIWSpyWYBDrYvj0Y_VQmJT86GRCCsIiOZxAq6FNgxUhP4_lVj6omOyhMn-QKy6ZmR/pub?embedded=true')
            d = datetime.datetime.today()
            locator = driver.find_element_by_xpath('/html/body/p[1]/span').text
            Ltitle = locator
            locator = locator[:-5]
            tableElement = driver.find_element_by_xpath('/html/body/table[1]')
            if str(d.day) not in locator:
            	locator = driver.find_element_by_xpath('/html/body/p[4]/span[2]').text
            	Ltitle = locator
            	locator = locator[:-5]
            	tableElement = driver.find_element_by_xpath('/html/body/table[2]')
            	if str(d.day) not in locator:
            		locator = driver.find_element_by_xpath('/html/body/p[8]/span').text
            		Ltitle = locator
            		locator = locator[:-5]
            		tableElement = driver.find_element_by_xpath('/html/body/table[3]')
            		if str(d.day) not in locator:
            			locator = driver.find_element_by_xpath('/html/body/p[12]/span[2]').text
            			Ltitle = locator
            			locator = locator[:-5]
            			tableElement = driver.find_element_by_xpath('/html/body/table[4]')
            t = list()
            for i in range(2,10):
                print('.//tbody/tr[4]/td['+str(i)+']')
                t.append(str(tableElement.find_element_by_xpath('.//tbody/tr[4]/td['+str(i)+']').text))
            q = list()
            for i in range(2,10):
                print('.//tbody/tr[1]/td['+str(i)+']')
                q.append(tableElement.find_element_by_xpath('.//tbody/tr[1]/td['+str(i)+']').text)
            return [t,q]
        zp = ['7:30','8:20','9:10','10:15','11:05','11:55','12:45','13:35','14:25','15:15','16:20','17:10','18:00','18:50']
        zk = ['8:15','9:05','9:55','11:00','11:50','12:40','13:30','14:20','15:10','16:00','17:05','17:55','18:45','19:35']
        dani = ['Ponedjeljak','Utorak','Srijedu','Četvrtak','Petak']
        uc = [['Babić','Petar'],['Bekavac','Roko'],['Cetina','Marko'],['Cigula','Leonardo'],['Čučdković','Luka'],['Domitrović','Tin'],['Glavač','Jakov'],['Grdinić','Leon'],['Ivezić','Marko'],['Jaranović','Zlatko'],['Karolj','Patrik'],['Kordić','Luka'],['Krehula','Filip'],['Lacko','Ines'],['Malbaša','Petra'],['Maskalan','Gvido'],['Pekas','Marko'],['Petković','Ana'],['Rodeš','Klara'],['Roachbacher','Dora'],['Sadović','Din'],['Sić','Hrvoje'],['Solomun','Franko'],['Vodstričil','Matejo']]
        ras = [[['HRV','OE','AIP','AIP','UITTUP','UITTUP','MAT-DOP',''],['TD','TD','GEO','MAT','KEM','FIZ','FIZ',''],['MAT','ENJ','OE','OE','GEO','SR','KEM',''],['MAT','FIZ','OE','POV','HRV','TZK','TZK','E/V'],['MAT','BIO','HRV','AIP','OE','POV','ENJ','']],[['V/E','SR','UITTUP','UITTUP','HRV','MAT','AIP',''],['MAT-DOP','KEM','KEM','OE','FIZ','OE','ENJ',''],['','','GEO','MAT','OE','POV','FIZ',''],['OE','ENJ','HRV','TZK','TZK','POV','MAT','GEO'],['TD','TD','MAT','OE','BIO','HRV','AIP','AIP']]]
        print(izmjene())
        d = int(input("DAN U TJEDNU(1-7): "))
        d = d -1
        s = str(input("SMJENA(A,B): "))
        ini = str(input("KO JE BIO PROŠLI TJ REDDAR KASNIJE PO ABECEDI?(Inicijali(prezime-ime)): "))
        for o in range(len(uc)):
            if(ini==str(list(uc[o][0])[0])+str(list(uc[o][1])[0])):
                red = o
                print(uc[o])
                o = o + 2
                break

        a = input("AUTOMATSKO SLANJE(y/n): ")
        if(a=='y'):
            driver = webdriver.Chrome('/home/jakov/Desktop/tsrb/izmjene/drivers/chromedriver')
            driver.get('https://web.whatsapp.com/')
            print(Fore.YELLOW + Style.BRIGHT + 'Jeste li spremni? (y/n)')
            p = str(input())
            if(p=='n'):
                sys.exit()
            else:
                if(s == 'A'):
                    i = 0
                else:
                    i = 1

            #z = d
            while(True):
                sr = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
                sr.click

                if(d==5):
                    print(d)
                    d = 0
                    o = o + 2
                    if(o>=len(uc)):
                        o = (o-len(uc))
                    print(d)
                    i = i + 1
                    if(i>=2):
                        i = 0
                if(d==0):
                    sr.send_keys('Redari ovaj tjedan su *' + str(uc[o-1][0]) +' '+ str(uc[o-1][1])+'* i *' + str(uc[o][0]) +' '+ str(uc[o][1]) +'*')
                    sr.send_keys(u'\ue007')
                sr.send_keys('Raspored za ' + str(dani[d]))
                sr.send_keys(u'\ue007')
                bc = 0
                for l in range(len(ras[i][d])):
                    if(ras[i][d][l]==''):
                        bc = bc + 1

                if(i==0):
                    sr.send_keys("Škola počinje u *" + str(zp[0]) + "* i završava u *" + str(zp[len(ras[i][d])-bc])+"*")
                    #print("Škola počinje u *" + str(zp[bc]) + "* i završava u *" + str(zp[len(ras[i][d])+bc])+"*")
                    sr.send_keys(u'\ue007')
                else:
                    bc = 0
                    br = 0
                    for q in range(4):
                        if(ras[i][d][q]==''):
                            bc = bc + 1
                    for q in range(7,7//2,-1):
                        if(ras[i][d][q]==''):
                            br = br + 1
                    print(len(ras[i][d])+bc+6-1,bc,len(zk))
                    sr.send_keys("Škola počinje u *" + str(zp[6+bc]) + "* i završava u *" + str(zk[-(br+1)])+"*")
                    sr.send_keys(u'\ue007')


                iz = izmjene()
                print(iz)

                for iii in range(len(ras[i][d])):
                    if(i==0):
                        if(iz[0][iii]=='X'):
                            sr.send_keys('*'+str(iii+1)+'.* ~*'+str(ras[i][d][iii])+'*~ _(slobodan sat)_')
                            sr.send_keys(u'\ue007')
                        elif(iz[0][iii]!='X' and iz[0][iii]!=''):
                            sr.send_keys('*'+str(iii+1)+'.* ~*'+str(ras[i][d][iii])+'*~ ' +str(iz[0][iii]))
                            sr.send_keys(u'\ue007')
                        else:
                            #print(str(iii+1)+'.',ras[i][d][iii])
                            sr.send_keys('*'+str(iii+1)+'.* '+str(ras[i][d][iii]))
                            sr.send_keys(u'\ue007')
                    else:
                        if(iz[0][iii]=='X'):
                            sr.send_keys('*'+str(iii)+'.* ~*'+str(ras[i][d][iii])+'*~ _(slobodan sat)_')
                            sr.send_keys(u'\ue007')
                        elif(iz[0][iii]!='X' and iz[0][iii]!=''):
                            sr.send_keys('*'+str(iii)+'.* ~*'+str(ras[i][d][iii])+'*~ ' +str(iz[0][iii]))
                            sr.send_keys(u'\ue007')
                        else:
                        #print(str(iii)+'.',ras[i][d][iii])
                            sr.send_keys('*'+str(iii)+'.* '+str(ras[i][d][iii]))
                            sr.send_keys(u'\ue007')

                time.sleep(24*60*60)
                d = d + 1
                print(d)



    print(Fore.RED + Style.BRIGHT)
    print("""
     ██████╗  ██████╗
    ██╔════╝ ██╔════╝
    ██║  ███╗██║  ███╗
    ██║   ██║██║   ██║
    ╚██████╔╝╚██████╔╝
     ╚═════╝  ╚═════╝ """)
