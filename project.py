from asyncore import read
import csv
from re import T

'''
PROJECT FOR TERM 1 | AIRPLANCE PASSANGER MANAGEMENT SYSTEM IN CSV
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

#INFO PLANES
def readplanes():
    f = open("planes.csv","r")
    stud= csv.reader(f)
    for i in stud:
        print(i)
    f.close()

#
def main():
    print("****WELCOME TO AIRPLANEGO****")
    print("****Select your flight path****")

    q = input ("date(dd/mm/yy): ")
    m = input("From:").upper()
    n= input("To: ").upper()
    f = open("planes.csv","r")
    
    w = csv.reader(f)
    for i in w:
        if i[1]==m and i[2]==n:

            print(f"****FLIGHTS ARE AVAILABLE FROM:{m}|TO:{n}|ON:{q}")
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
            detailsde()
            print("flight ticket sucessfully booked.")

            # READ DETAILS 
            
            def readdetailsde():
                a = open("details.csv","r")
                de = csv.reader(a)
                for i in de:
                    print(i)
                a.close()
            lookz = input("Do you want to view your ticket info(y/n): ")
            for lookz in"yY":
                print("[Name, Age, Gender,Meal]")
                readdetailsde()

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

            #AGE CHANGE FUCTION
            def ageupdater():
                file = open('details.csv','r')
                reader = csv.reader(file)
                l=[]
                uname = input("Enter your name to fetch data: ")
                Found= False
                for row in reader:
                    if row[0]==uname:
                        Found = True
                        age = input("Enter age to be updaated: ")
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
                        genderz = input("Enter gender to be updaated: ")
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
                        mealz = input("Enter gender to be updaated: ")
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
            if chois in "yY":
                print("****HERE IS THE DETAIL CHANGE MENU****")
                print("(1)Name\n(2)Age\n(3)Gender\n(4)Meal")
                ger = int(input("Enter your choice: "))
                if ger == 1:
                    nameupdater()
                elif ger == 2:
                    ageupdater()
                elif ger ==3:
                    genderupdater()
                elif ger == 4:
                    pass

            
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
                    
                rd.close()

            def ticketsearch():
                cfa="y"
                while cfa in "yY":
                    rr = input("do you want to view your ticket(y/n): ")
                    if rr in "yY":
                        ser()
                    cfa = input("\ndo you want to view your ticket again (y/n): ")
            ticketsearch()
            

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
                    print("Ticket cancelled sucessfully")
                    f.close()
            def ticketcanceloption():
                fg = input("Cancel ticket (y/n): ")
                if fg in "yY":
                    ticketdelete()
                else:
                    pass
            ticketcanceloption()
            

    else:
        print("No flights available for this path")

main()



















































