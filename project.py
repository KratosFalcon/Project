from asyncore import read
import csv
from re import T
import random
import string

'''
PROJECT FOR TERM 1 | AIRPLANE PASSANGER MANAGEMENT SYSTEM IN CSV
'''


#PLANES ENTRY LIST
def planes():
    f = open("planes.csv","a",newline="")
    w = csv.writer(f)
    ch='y'
    while ch in 'Yy':
        Plane = input("Plane name: ").upper()
        From = input("From: ").upper()
        To = input("To: ").upper()
        ch = input("want to enter more flight paths: ")
        l = [Plane,From,To]
        w.writerow(l)
    f.close()
#planes()

#INFO PLANES
def readplanes():
    f = open("planes.csv","r")
    stud= csv.reader(f)
    for i in stud:
        print(i)
    f.close()

# MAIN WORKING FUNCTION
def main():
    print()
    print("****WELCOME TO AIRPLANEGO****")
    print("****Select your flight path****")

    q = input ("date(dd/mm/yy): ")
    m = input("From:").upper()
    n= input("To: ").upper()
    f = open("planes.csv","r")
    
    w = csv.reader(f)
    for i in w:
        if i[1]==m and i[2]==n:

            #OTP GENERATOR
            def otp():
                m = string.digits
                g= list(m)
                cptcha = random.choices(g,k=6)
                s = ''.join(str(x) for x in cptcha)
                print("*********************")
                print("OTP IN YOUR EMAIL: ",s)
                print("*********************")
                print()
                p = input("Enter otp:")
                if p == s:
                    print("tick!!")
                    print()
                    pass
                else:
                    print("WRONG OTP !")
                    otp()

            #LOG IN 
            print()
            print("***************************************")
            print("WELCOME TO AIRPLANE GO PLS LOG IN")
            print()
            def login():
                r = input("Enter email id: ")
                c = input("Create a password: ")
                d = input("Reenter password: ")
                if c == d:
                    otp()
                else:
                    print("wrong password enter carefully!")
                    print()
                    login()

            login()

            print(f"****FLIGHTS ARE AVAILABLE FROM:{m}|TO:{n}|ON:{q}****")
            print("****Input your credentials****")
            
            def detailsde():
                gocsv = open("details.csv","a",newline="")
                w = csv.writer(gocsv)
                
                Name = input("Name of passanger: ")
                Age = input("Age: ")
                Gender = input("Gender: ")
                Meal = input("Meal prefernces(veg/non-veg): ")
                newlist1 = [Name,Age,Gender,Meal]
                w.writerow(newlist1)
                gocsv.close()
                mor = input("Do you want to book another ticket(y/n): ")
                if mor in "yY":
                    detailsde()
                else: 
                    pass
            detailsde()
            

            # READ DETAILS 
            
            def readdetailsde():
                a = open("details.csv","r")
                de = csv.reader(a)
                for i in de:
                    print(i)
                a.close()
                

            #CHANGE DETAILS

            #NAME UPDATER FUNCTION
            def nameupdater():
                file = open('details.csv','r')
                reader = csv.reader(file)
                l=[]
                uname = input("Enter your previous name data: ")
                Found= False
                for row in reader:
                    if row[0]==uname:
                        Found = True
                        newname = input("Enter name to be updated: ")
                        row[0]=newname
                    l.append(row)
                file.close()
                if Found == False:
                    print('Data with the given name not found')
                else:
                    file = open('details.csv','w+',newline="")
                    writer = csv.writer(file)
                    writer.writerows(l)
                    file.seek(0)
                    Reader = csv.reader(file)
                    for row in Reader:
                        print("New Data:",row)
                    file.close()

            #AGE CHANGE FUNCTION
            def ageupdater():
                file = open('details.csv','r')
                reader = csv.reader(file)
                l=[]
                uname = input("Enter your name to fetch data: ")
                Found= False
                for row in reader:
                    if row[0]==uname:
                        Found = True
                        age = input("Enter age to be updated: ")
                        row[1]=age
                    l.append(row)
                file.close()
                if Found == False:
                    print('Data with the given name not found')
                else:
                    file = open('details.csv','w+',newline="")
                    writer = csv.writer(file)
                    writer.writerows(l)
                    file.seek(0)
                    Reader = csv.reader(file)
                    for row in Reader:
                        print("New Data:",row)
                    file.close()

            #GENDER UPDATER
            def genderupdater():
                file = open('details.csv','r')
                reader = csv.reader(file)
                l=[]
                uname = input("Enter your name to fetch data: ")
                Found= False
                for row in reader:
                    if row[0]==uname:
                        Found = True
                        genderz = input("Enter gender to be updated: ")
                        row[2]=genderz
                    l.append(row)
                file.close()
                if Found == False:
                    print('Data with the given name not found')
                else:
                    file = open('details.csv','w+',newline="")
                    writer = csv.writer(file)
                    writer.writerows(l)
                    file.seek(0)
                    Reader = csv.reader(file)
                    for row in Reader:
                        print("New Data:",row)
                    file.close()

            #MEAL UPDATER
            def mealupdater():
                file = open('details.csv','r')
                reader = csv.reader(file)
                l=[]
                uname = input("Enter your name to fetch data: ")
                Found= False
                for row in reader:
                    if row[0]==uname:
                        Found = True
                        mealz = input("Enter meal to be updated: ")
                        row[3]=mealz
                    l.append(row)
                file.close()
                if Found == False:
                    print('Data with the given name not found')
                else:
                    file = open('details.csv','w+',newline="")
                    writer = csv.writer(file)
                    writer.writerows(l)
                    file.seek(0)
                    Reader = csv.reader(file)
                    for row in Reader:
                        print("New Data:",row)
                    file.close()


            print()
            print("*****************************************")
            print("NOTE : Do you want to change any credentials you can do it here before payment ")
            chois=input("Anything to change(y/n): ")

            #DETAIL CHANGE MENU
            chois = "y"
            while chois in "yY":
                print("****HERE IS THE DETAIL CHANGE MENU****")
                print("(1)Name\n(2)Age\n(3)Gender\n(4)Meal\n(5)Continue with next step")
                ger = int(input("Enter your choice: "))
                if ger == 1:
                    nameupdater()
                elif ger == 2:
                    ageupdater()
                elif ger ==3:
                    genderupdater()
                elif ger == 4:
                    mealupdater()
                elif ger ==5:
                    pass
                chois = input("Update anymore details(y/n): ")

            
            #TICKET SEARCH
            def ser():
                rd = open("details.csv","r")
                f=0
                rdl = csv.reader(rd)
                n = input("Enter your name to search info about your ticket: ")
                for i in rdl:
                    if i[0]==n:
                        print(i,end="")
                        f = f+1
                if f==0:
                    print("Wrong name entered!")
                    ser()      
                    
                rd.close()
                cfa = input("\ndo you want to view your ticket again (y/n): ")
                if cfa in "yY":
                    ser()
            
            print()
            print("*****************************************")
            print("YOU CAN VIEW YOUR FINAL TICKET HERE: ")

            #TICKET SEARCH MENU
            def ticketsearch():
                    rr = input("do you want to view your ticket(y/n): ")
                    if rr in "yY":
                        ser()
                    elif rr in "nN":
                        pass
                    else:
                        print("Wrong option selection!")
                        print()
                        ticketsearch()
                    
            ticketsearch()
            
            #DUMMY PAYMENT FUNCTION
            def dumpay():   
                i = random.randrange(2500,5400)
                m= (0.05*i)+i

                print()
                print("*****************************************")
                print(f"TOTAL FARE (including GST):{m}")
                print()
                print("SELECT PAYMENT MODE")
                print("(1)Bhim UPI\n(2)Debit card\n(3)Credit card\n")

                #CAPTCHA FOR PAYMENT
                def captcha()   :
                    i = string.ascii_lowercase
                    m = string.ascii_uppercase
                    n = string.digits
                    g= list(i+n+m)
                    cptcha = random.choices(g,k=6)
                    s = ''.join(str(x) for x in cptcha)
                    print(s)
                    print()
                    p = input("Enter above captcha: ")
                    if p==s:
                        pass
                    else:
                        print("Wrong captcha!")
                        print()
                        captcha()

                dhh= int(input("Enter choice: "))
                if dhh == 1:
                    gr = input("Enter upi id: ")
                    print()
                    captcha()

                    d = input("\nProceed(y): ")
                    if d in "yY":
                        print()
                        print("Intiating transaction")
                        print(".......")
                        print("Transcation Sucessfull!")
                        print()
                        #read details
                        print("[Name, Age, Gender,Meal]")
                        readdetailsde()
                        print()
                        print("!!FLIGHT SEATS ARE BOOKED SUCCESSFULLY!!")
        
                    else:
                        print("Kindly Cancel your ticket to remove filled crendentials!")
    

                if dhh == 2:
                    gr = input("Enter naame on card: ")
                    nu = int(input("Enter card number: "))
                    dr = int(input("Enter expiry: "))
                    dat = int(input("Enter cvv: "))
                    print()
                    captcha()

                    d = input("\nProceed(y): ")
                    if d in "yY":
                        print()
                        print("Intiating transaction")
                        print(".......")
                        print("Transcation Sucessfull!")
                        print()
                        #read details
                        print("[Name, Age, Gender,Meal]")
                        readdetailsde()
                        print()
                        print("!!FLIGHT SEATS ARE BOOKED SUCCESSFULLY!!")
        
                    else:
                        print("Kindly Cancel your ticket to remove filled credentials!")

                if dhh == 3:
                    gr = input("Enter name on card: ")
                    nu = int(input("Enter card number: "))
                    dr = int(input("Enter expiry: "))
                    dat = int(input("Enter cvv: "))
                    print()
                    captcha()

                    d = input("\nProceed(y): ")
                    if d in "yY":
                        print()
                        print("Intiating transaction")
                        print(".......")
                        print("Transcation Sucessfull!")
                        print()
                        #read details
                        print("[Name, Age, Gender,Meal]")
                        readdetailsde()
                        print()
                        print("!!FLIGHT SEATS ARE BOOKED SUCCESSFULLY!!")
        
                    else:
                        print("Kindly Cancel your ticket to remove filled credentials!")

            print()
            print("*****************************************")
            kir = input("Get redirected to the payments gateway(y/n): ")
            if kir in "yY":
                dumpay()
            else:
                pass

            #TICKET DELETE
            def ticketdelete():
                f= open("details.csv","r")
                csrv = csv.reader(f)
                found = 0
                ml = []
                namef =input("input name to cancel your ticket: ")
                for r in csrv:
                    if (r[0]!=namef):
                        ml.append(r)
                    else: 
                        found = 1
                f.close()
                if found == 0:
                    print("wrong input data")
                else:
                    f= open("details.csv","w",newline= "")
                    csvr = csv.writer(f)
                    csvr.writerows(ml)
                    print("\nTicket cancelled sucessfully")
                    print("!! Refund will be intiated in 24 working hours !!")
                    f.close()
            def ticketcanceloption():
                print()
                print("*****************************************")
                print("CANCELLATION OF THE TICKET IF NEEDED : ")
                fg = input("Cancel ticket (y/n): ")
                if fg in "yY":
                    ticketdelete()

                else:
                    print()
                    print("**********************")
                    print("ThankYou For Booking Airplanes Tickets With Us!")
                    print("**********************")
                    print()
                    break
                    
            ticketcanceloption()
            

    else:
        print("No flights available for this path")

main()

