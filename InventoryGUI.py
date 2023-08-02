import pickle
import threading
import csv
# import pandas as pd
from tkinter import *
from tkinter import Tk, font
import tkinter as tk
import tkinter as ttk
from random import randint
from tkinter import messagebox

global partsOn1st
global parts2ndBack
global parts2ndOff
global partsDict
global userPartCheck
global options
global places
global stop
stop: bool = True

#partsDict = {}
#partsOn1st = {}
#parts2ndOff = {}
#parts2ndBack = {}
#userPartCheck = {}


options = ['Han', 'AWS', 'Random']
places = ['2nd Floor Office', '1st Floor', '2nd Floor Backroom']


def saveAwayMain():
    global data1
    data1 = open(r'S:\Product_Developement\Inventory Files\Inventory Data\Data1.csv', 'wb')
    pickle.dump(partsDict, data1)
    pickle.dump(partsOn1st, data1)
    pickle.dump(parts2ndBack, data1)
    pickle.dump(parts2ndOff, data1)
    pickle.dump(userPartCheck, data1)
    pickle.dump(options, data1)
    data1.close()


def saveAwayBackup():
    global data2
    data2 = open(r'S:\Product_Developement\Inventory Files\Inventory Data\BkUpData.csv', 'wb')
    pickle.dump(partsDict, data2)
    pickle.dump(partsOn1st, data2)
    pickle.dump(parts2ndBack, data2)
    pickle.dump(parts2ndOff, data2)
    pickle.dump(userPartCheck, data2)
    pickle.dump(options, data2)
    data2.close()

def saveAwayFinalBackup():
    global data3
    data3 = open(r'S:\Product_Developement\Inventory Files\Inventory Data\FinalBackup.csv', 'wb')
    pickle.dump(partsDict, data3)
    pickle.dump(partsOn1st, data3)
    pickle.dump(parts2ndBack, data3)
    pickle.dump(parts2ndOff, data3)
    pickle.dump(userPartCheck, data3)
    pickle.dump(options, data3)
    data3.close()



def showError(msg):
    messagebox.showerror('Entry Error', msg)


class GUI:
    bigString = ""
    dataList = []
    quan = 0
    data = ""
    num = ''
    pjm = ''
    desc = ""
    proj = ''
    place = ''
    key1 = ""

    # CONSTRUCTOR

    def __init__(self, ent):
        self.data = ent

    # WINDOW OPERATIONS & VARIABLES

    # ==========> Functions

    def face(self):

        def click2():
            entdelWindow()
            print("click")
            badLabel.place_forget()
            yesButton.place_forget()
            noButton.place_forget()
            entry1.place(width=250, height=20, relx=0.32, y=77)
            clearRoot()
            resetRoot()

        def click3():
            resetRoot()

        # TOPLEVELBlOCK

        def entdelWindow():

            def refresh():
                # Reset var and delete all old options
                clicked.set('')
                projselect['menu'].delete(0, 'end')

                # Insert list of new options (tk._setit hooks them up to var)

                for choice in options:
                    projselect['menu'].add_command(label=choice, command=tk._setit(clicked, choice))

            def projectAdded():
                if Addprojname.get() == '':
                    showError("Empty Field")

                else:
                    options.append(Addprojname.get())
                    saveAwayMain()
                    saveAwayBackup()
                    Addprojnamelabel.place_forget()
                    Addprojname.place_forget()
                    Addprojbutton.place_forget()
                    refresh()
                    fillTopLevel()

            def addProject1():
                clearTopWindow()
                Addprojnamelabel.place(relx=0.34, rely=0.29)
                Addprojname.place(relx=0.27, rely=0.39)
                Addprojbutton.place(relx=0.42, rely=0.49)

            def AddParts():

                haveAdded.place(relx=0.36, rely=0.37)
                haveAddedButton.place(relx=0.40, rely=0.48)
                partsDict[Addptnumentry.get()].quantity += int(Addptquantity.get())
                if ((clicked2.get() == '1st Floor')):
                    partsOn1st[Addptnumentry.get()].quantity += int(Addptquantity.get())
                elif (clicked2.get() == '2nd Floor Office'):
                    parts2ndOff[Addptnumentry.get()].quantity += int(Addptquantity.get())
                elif (clicked2.get() == '2nd Floor Backroom'):
                    parts2ndBack[Addptnumentry.get()].quantity += int(Addptquantity.get())

                saveAwayMain()
                saveAwayBackup()

                partInfoLabel.place_forget()
                numLabel.place_forget()
                projLabel.place_forget()
                desLabel.place_forget()
                quanLabel.place_forget()
                tryAgain.place_forget()
                addParts1.place_forget()
                takeMeBackBut.place_forget()

                print(partsDict[Addptnumentry.get()].quantity)

            def makeLabels():
                quanLabel.config(text="Current Quantity:  " + str(partInfo[3]))
                numLabel.config(text="Part Number:  " + partInfo[0])
                projLabel.config(text="Project:  " + partInfo[1])
                desLabel.config(text="Description:  " + partInfo[2])

            def closeTopLevel():
                newWindow.destroy()
                resetRoot()

            def resetTopLevel():
                takeMeBackBut.place_forget()
                tryAgain.place_forget()
                addParts1.place_forget()
                partInfoLabel.place_forget()
                numLabel.place_forget()
                projLabel.place_forget()
                desLabel.place_forget()
                quanLabel.place_forget()

                fillTopLevel()

            def fillTopLevel():
                AddpartLabel.place(relx=0.18, rely=0.03)
                Addptnumentry.place(width=200, relx=0.35, rely=0.18)
                ptnumLabel.place(relx=0.34, rely=0.12)
                projselectlabel.place(relx=0.36, rely=0.24)
                projselect.place(relx=0.35, rely=0.30, width=205)

                Addptprojmentry.place(width=200, relx=0.35, rely=0.44)
                Addptprojmentrylabel.place(relx=0.36, rely=0.38)
                Addptdescentry.place(width=200, relx=0.35, rely=0.55)
                Addptdescentrylabel.place(relx=0.36, rely=0.49)
                enterpartButton.place(relx=0.285, rely=0.89)
                Addptquantitylabel.place(relx=0.37, rely=0.61)
                Addptquantity.place(relx=0.35, rely=0.67, width=200)
                Addprojectbut1.place(relx=0.72, rely=0.305)
                ptLocationLabel.place(relx=0.35, rely=0.73)
                ptLocationMenu.place(relx=0.35, rely=0.79, width=205)
                Addptnumentry.insert(0, entry1.get())

            def clearTopWindow():
                AddpartLabel.place_forget()
                Addptnumentry.place_forget()
                ptnumLabel.place_forget()
                projselectlabel.place_forget()
                projselect.place_forget()
                Addptprojmentry.place_forget()
                Addptprojmentrylabel.place_forget()
                Addptdescentry.place_forget()
                Addptdescentrylabel.place_forget()
                enterpartButton.place_forget()
                Addptquantitylabel.place_forget()
                Addptquantity.place_forget()
                Addprojectbut1.place_forget()
                ptLocationLabel.place_forget()
                ptLocationMenu.place_forget()

            def partEntered():
                if (Addptquantity.get()) == '' or Addptnumentry.get() == '' or clicked2.get() == '' \
                        or clicked.get() == '' or Addptdescentry.get() == '' or Addptprojmentry.get() == '':
                    showError("Empty Field(s), Try Again")




                elif Addptnumentry.get() in partsDict.keys():
                    clearTopWindow()
                    global partInfo
                    partInfo = [partsDict[Addptnumentry.get()].number, partsDict[Addptnumentry.get()].project,
                                partsDict[Addptnumentry.get()].descrip, (partsDict[Addptnumentry.get()].quantity),
                                clicked2.get()]
                    makeLabels()

                    quanLabel.place(relx=0.42, rely=0.55)
                    tryAgain.place(relx=0.23, rely=0.7)
                    addParts1.place(relx=0.40, rely=0.7)
                    takeMeBackBut.place(relx=0.62, rely=0.7)
                    partInfoLabel.place(relx=0.10, rely=0.30)
                    numLabel.place(relx=0.42, rely=0.4)
                    projLabel.place(relx=0.42, rely=0.45)
                    desLabel.place(relx=0.42, rely=0.5)


                else:
                    self.dataList = [clicked.get(), Addptnumentry.get(), Addptdescentry.get(), Addptprojmentry.get(),
                                     Addptquantity.get(), clicked2.get()]
                    dataProc(self)
                    badLabel.place_forget()
                    closeTopLevel()
                    clearRoot()
                    OKresetbutton.place(relx=0.44, y=180)
                    partenteredlabel.place(relx=0.34, y=144)

            newWindow = Toplevel(root)
            newWindow.config(bg='gray82')
            newWindow.geometry("%dx%d%+d%+d" % (640, 480, 250, 125))

            # Toplevel Core Widgets
            AddpartLabel = Label(newWindow, text="Enter New Part Information", bg='White', font=font2, padx=150, pady=8)
            Addptnumentry = Entry(newWindow)
            ptnumLabel = Label(newWindow, text="Type Part Number or Scan Barcode", bg='gray82', font=font2)
            projselectlabel = Label(newWindow, text="Select project from drop-down", font=font2, bg='gray82')
            clicked = StringVar()
            clicked.set(options[0])
            projselect = OptionMenu(newWindow, clicked, *options)
            Addptprojmentry = Entry(newWindow)
            Addptprojmentrylabel = Label(newWindow, text="Who's adding this part?", bg='gray82', font=font2)
            Addptdescentry = Entry(newWindow)
            Addptdescentrylabel = Label(newWindow, text="Enter part description", bg='gray82', font=font2)
            enterpartButton = Button(newWindow, text="Enter new part into system", bg='lime green', padx=60, pady=1.25,
                                     font=font2, command=partEntered)
            Addptquantitylabel = Label(newWindow, text="Enter quantity", bg='gray82', font=font2)
            Addptquantity = Entry(newWindow)
            Addprojectbut1 = Button(newWindow, text="Add project?", padx=20, bg='White', command=addProject1)
            ptLocationLabel = Label(newWindow, text="Where is this part being entered?", bg='gray82', font=font2)
            clicked2 = StringVar()
            clicked2.set(places[0])
            ptLocationMenu = OptionMenu(newWindow, clicked2, *places)

            # Second Level Widgets TopLevel (Part exists, add or go back, addproj)

            failLabel = Label(newWindow,
                              text="Part already in system, try again or add quantity to existing inventory?")
            partInfoLabel = Label(newWindow,
                                  text="Is this the part you're trying to enter? If so, already in system. If not, maybe try part number again")
            haveAdded = Label(newWindow, text="Part(s) added to system", font=font2, bg='grey82')

            addParts1 = Button(newWindow, text="Add to existing", font=font2, padx=18, bg='White', command=AddParts)
            tryAgain = Button(newWindow, text="Try Again", font=font2, padx=20, bg='White', command=resetTopLevel)
            haveAddedButton = Button(newWindow, text="OK", padx=18, bg='White', command=closeTopLevel)
            takeMeBackBut = Button(newWindow, text="Take me back", font=font2, bg='White', command=closeTopLevel,
                                   padx=20)

            Addprojnamelabel = Label(newWindow, text="Enter Official Project Name, i.e. HAN Protect", bg='gray82',
                                     font=font2)
            Addprojname = Entry(newWindow, width=50, font=font2)
            Addprojbutton = Button(newWindow, text="All Set!", padx=25, bg='White', command=projectAdded)

            # intermediate variables

            numLabel = Label(newWindow, text='', font=font2, bg='White')
            projLabel = Label(newWindow, text='', font=font2, bg='White')
            desLabel = Label(newWindow, text='', font=font2, bg='White')
            quanLabel = Label(newWindow, text='why', font=font2, bg='White')

            fillTopLevel()

        # OtherFunctions
        def editPartsOutSubtractWork():
            userPartCheck[tempText][0][1][0] -= int(editNumberEntry.get())
            if userPartCheck[tempText][0][1][0] == 0:
                userPartCheck[tempText].remove(userPartCheck[tempText][0])

            saveAwayMain()
            saveAwayBackup()

            clearRoot()
            actionCompletedLabel.place(relx=0.42, rely=0.37)
            OKresetbutton.place(relx=0.435, rely=0.43)

        def editPartsOutAddWork():
            userPartCheck[tempText][0][1][0] += int(editNumberEntry.get())
            if userPartCheck[tempText][0][1][0] == 0:
                userPartCheck[tempText].remove(userPartCheck[tempText][0])

            saveAwayMain()
            saveAwayBackup()

            clearRoot()
            actionCompletedLabel.place(relx=0.42, rely=0.37)
            OKresetbutton.place(relx=0.435, rely=0.43)

        def editPartsOut(o):
            select1 = partScrollEntry.curselection()
            global tempText1

            tempText1 = partScrollEntry.get(select1).strip()

            clearRoot()
            editNumberEntry.place(relx=0.39, rely=0.37)
            addButton2.place(relx=0.295, rely=0.45)
            subtractButton.place(relx=0.495, rely=0.45)
            decorLabel1.place(relx=0.2, rely=0.11)
            columnLabel3.place(relx=0.384, rely=0.136)
            partInfoLabel1.place(relx=0.27, rely=0.20)

            exPartLabel0.config(text="Part Description:  " + tempText1)

            exPartLabel0.place(relx=0.37, rely=0.29)

        def userPartCheckLog(o):
            global select
            global tempText
            select = userEntry.curselection()

            tempText = userEntry.get(select).strip()

            partScrollEntry.delete(0, END)
            clearRoot()
            columnLabel2.place(relx=0.24, rely=0.136)
            partScrollEntry.place(relx=0.38, rely=0.4)

            browseList2 = []
            decorLabel1.place(relx=0.2, rely=0.11)
            OKresetbutton.place(relx=0.69, rely=0.135)
            for item in userPartCheck[tempText]:
                tempString1 = userPartCheck[tempText][0][0][0] + " :" + str(userPartCheck[tempText][0][1][0])
                browseList2.append(tempString1)
            for item in browseList2:
                partScrollEntry.insert(END, item)

            scroll1.pack(side=RIGHT, fill=Y)
            partScrollEntry.pack()
            partFrame.place(relx=0.2104, rely=0.208)

        def userCheckLog():
            userEntry.delete(0, END)
            clearRoot()
            columnLabel1.place(relx=0.24, rely=0.136)
            userEntry.place(relx=0.38, rely=0.4)

            browseList1 = []
            decorLabel1.place(relx=0.2, rely=0.11)
            OKresetbutton.place(relx=0.69, rely=0.135)

            for key in userPartCheck.keys():
                tempString = " " + key + " "
                browseList1.append(tempString)
            print(browseList1)
            for item in browseList1:
                userEntry.insert(END, item)

            scroll1.pack(side=RIGHT, fill=Y)
            userEntry.pack()
            userFrame.place(relx=0.2104, rely=0.208)

        def Browse():

            browseEntry.delete(0, END)
            clearRoot()
            columnLabel.place(relx=0.24, rely=0.136)
            browseEntry.place(relx=0.38, rely=0.4)
            objectsList = list(partsDict.values())
            browseList = []
            decorLabel1.place(relx=0.2, rely=0.11)
            OKresetbutton.place(relx=0.69, rely=0.135)

            for item in objectsList:
                tempString = " " + item.number + "   :       " + item.descrip
                browseList.append(tempString)
                spaceString = " "
                browseList.append(spaceString)
            for item in browseList:
                browseEntry.insert(END, item)

            scroll.pack(side=RIGHT, fill=Y)
            browseEntry.pack()
            browseFrame.place(relx=0.2104, rely=0.208)

        def removePartsWork():
            if Addrandptquantity0.get() == '' or clicked4.get() == '':
                showError("Empty Field")
            else:
                if (partsDict[entry1.get()].quantity >= int(Addrandptquantity0.get())):
                    if ((clicked4.get() == '1st Floor')):
                        if ((int(Addrandptquantity0.get())) > (partsOn1st[entry1.get()].quantity)):
                            showError(
                                "There aren't that many parts logged at this location, readjust stock to remove this quantity.")
                        else:
                            partsOn1st[entry1.get()].quantity -= int(Addrandptquantity0.get())
                            util1()
                    elif (clicked4.get() == '2nd Floor Office'):
                        if ((int(Addrandptquantity0.get())) > (parts2ndOff[entry1.get()].quantity)):
                            showError(
                                "There aren't that many parts logged at this location, readjust stock to remove this quantity.")
                        else:
                            parts2ndOff[entry1.get()].quantity -= int(Addrandptquantity0.get())
                            util1()
                    elif (clicked4.get() == '2nd Floor Backroom'):
                        if ((int(Addrandptquantity0.get())) > (parts2ndBack[entry1.get()].quantity)):
                            showError(
                                "There aren't that many parts logged at this location, readjust stock to remove this quantity.")
                        else:
                            parts2ndBack[entry1.get()].quantity -= int(Addrandptquantity0.get())
                            util1()
                else:
                    showError(
                        "There aren't that many parts logged in the system, readjust stock to remove this quantity.")

        def util1():
            partsDict[entry1.get()].quantity -= int(Addrandptquantity0.get())

            saveAwayMain()
            saveAwayBackup()

            clearRoot()
            partsRemovedLabel.place(relx=0.41, rely=0.36)
            OKresetbutton.place(relx=0.435, rely=0.43)

        def util2():
            if (enterName.get().lower() not in userPartCheck.keys()) or len(
                    userPartCheck[enterName.get().lower()]) == 0:
                userPartCheck[enterName.get().lower()] = (
                [[[partsDict[entry1.get()].descrip], [int(Addrandptquantity0.get())]]])
            else:
                for pair in userPartCheck[enterName.get().lower()]:

                    if pair[0][0] == partsDict[entry1.get()].descrip:
                        pair[1][0] += int(Addrandptquantity0.get())

                    else:
                        userPartCheck[enterName.get().lower()].append(
                            [[partsDict[entry1.get()].descrip], [int(Addrandptquantity0.get())]])
                        break

            saveAwayMain()
            saveAwayBackup()

            clearRoot()
            partsCheckedOutLabel.place(relx=0.41, rely=0.36)
            OKresetbutton.place(relx=0.435, rely=0.43)

        def removePartFromSystemWork():
            if entry1.get() in partsDict.keys():
                del partsDict[entry1.get()]
            if entry1.get() in partsOn1st.keys():
                del partsOn1st[entry1.get()]
            if entry1.get() in parts2ndOff.keys():
                del parts2ndOff[entry1.get()]
            if entry1.get() in parts2ndBack.keys():
                del parts2ndBack[entry1.get()]
            clearRoot()
            actionCompletedLabel.place(relx=0.42, rely=0.37)
            OKresetbutton.place(relx=0.425, rely=0.44)
            saveAwayMain()
            saveAwayBackup()

        def checkOutWork():
            if Addrandptquantity0.get() == '' or clicked4.get() == '' or enterName.get() == '':
                showError("Empty Field")
            else:
                if (partsDict[entry1.get()].quantity >= int(Addrandptquantity0.get())):
                    if ((clicked4.get() == '1st Floor')):
                        if ((int(Addrandptquantity0.get())) > (partsOn1st[entry1.get()].quantity)):
                            showError(
                                "There aren't that many parts logged at this location, readjust stock to check-out this quantity.")
                        else:
                            partsOn1st[entry1.get()].quantity -= int(Addrandptquantity0.get())
                            util2()
                    elif (clicked4.get() == '2nd Floor Office'):
                        if ((int(Addrandptquantity0.get())) > (parts2ndOff[entry1.get()].quantity)):
                            showError(
                                "There aren't that many parts logged at this location, readjust stock to check-out this quantity.")
                        else:
                            parts2ndOff[entry1.get()].quantity -= int(Addrandptquantity0.get())
                            util2()
                    elif (clicked4.get() == '2nd Floor Backroom'):
                        if ((int(Addrandptquantity0.get())) > (parts2ndBack[entry1.get()].quantity)):
                            showError(
                                "There aren't that many parts logged at this location, readjust stock to check-out this quantity.")
                        else:
                            parts2ndBack[entry1.get()].quantity -= int(Addrandptquantity0.get())
                            util2()
                else:
                    showError(
                        "There aren't that many parts logged in the system, readjust stock to check-out this quantity.")

        def checkInWork():
            if Addrandptquantity0.get() == '' or clicked4.get() == '' or enterName.get() == '':
                showError("Empty Field")
            else:

                if ((clicked4.get() == '1st Floor')):
                    partsOn1st[entry1.get()].quantity += int(Addrandptquantity0.get())
                elif (clicked4.get() == '2nd Floor Office'):
                    parts2ndOff[entry1.get()].quantity += int(Addrandptquantity0.get())
                elif (clicked4.get() == '2nd Floor Backroom'):
                    parts2ndBack[entry1.get()].quantity += int(Addrandptquantity0.get())

                if (enterName.get().lower() not in userPartCheck.keys()) or len(
                        userPartCheck[enterName.get().lower()]) == 0:
                    print('hmmm')
                else:
                    for pair in userPartCheck[enterName.get().lower()]:

                        if pair[0][0] == partsDict[entry1.get()].descrip:
                            pair[1][0] -= int(Addrandptquantity0.get())
                            if pair[1][0] < 1:
                                userPartCheck[enterName.get().lower()].remove(pair)
                            break
                saveAwayMain()
                saveAwayBackup()

                clearRoot()
                partsEnteredLabel.place(relx=0.40, rely=0.36)
                OKresetbutton.place(relx=0.435, rely=0.43)

        def checkIn():

            clearRoot()
            partCheckInLabel.place(relx=0.278, rely=0.03)
            partInfoLabel1.place(relx=0.275, rely=0.17)
            partInfoLabel2.place(relx=0.275, rely=0.42)
            decorLabel1.place(relx=0.2, rely=0.16)
            exPartLabel0.config(text="Part Number:  " + partsDict[entry1.get()].number, font=font2)
            exPartLabel1.config(text="Description:  " + partsDict[entry1.get()].descrip, font=font2)
            exPartLabel2.config(text="Quantity:  " + str(partsDict[entry1.get()].quantity) + " (across all inventory)",
                                font=font2)
            exPartLabel0.place(relx=0.39, rely=0.25)
            exPartLabel1.place(relx=0.39, rely=0.31)
            exPartLabel2.place(relx=0.39, rely=0.37)
            ptLocationLabel2.place(relx=0.405, rely=0.51)
            Addrandptquantitylabel0.place(relx=0.435, rely=0.635)
            Addrandptquantity0.place(relx=0.4105, rely=0.687)
            ptLocationMenu2.place(relx=0.415, rely=0.57)
            enterNameLabel.place(relx=0.412, rely=0.742)
            enterName.place(relx=0.4105, rely=0.80)
            enterPartsButton.place(relx=0.425, rely=0.860)

        def checkOut():
            clearRoot()
            partCheckOutLabel.place(relx=0.278, rely=0.03)
            partInfoLabel1.place(relx=0.275, rely=0.17)
            partInfoLabel2.place(relx=0.275, rely=0.42)
            decorLabel1.place(relx=0.2, rely=0.16)
            exPartLabel0.config(text="Part Number:  " + partsDict[entry1.get()].number, font=font2)
            exPartLabel1.config(text="Description:  " + partsDict[entry1.get()].descrip, font=font2)
            exPartLabel2.config(text="Quantity:  " + str(partsDict[entry1.get()].quantity) + " (across all inventory)",
                                font=font2)
            exPartLabel0.place(relx=0.39, rely=0.25)
            exPartLabel1.place(relx=0.39, rely=0.31)
            exPartLabel2.place(relx=0.39, rely=0.37)
            ptLocationLabel3.place(relx=0.405, rely=0.51)
            Addrandptquantitylabel0.place(relx=0.435, rely=0.635)
            Addrandptquantity0.place(relx=0.4105, rely=0.687)
            ptLocationMenu2.place(relx=0.415, rely=0.57)
            enterNameLabel.place(relx=0.412, rely=0.742)
            enterName.place(relx=0.4105, rely=0.80)
            checkOutButton.place(relx=0.412, rely=0.860)

        def removePart():
            clearRoot()
            partsRemoveLabel.place(relx=0.278, rely=0.03)
            decorLabel1.place(relx=0.2, rely=0.19)
            removePartsFromStockButton.place(relx=0.21, rely=0.20)
            removePartsFromSystemButton.place(relx=0.5075, rely=0.20)

        def removeParts():
            clearRoot()
            partsRemoveLabel.place(relx=0.278, rely=0.03)
            partInfoLabel1.place(relx=0.275, rely=0.20)
            partInfoLabel2.place(relx=0.275, rely=0.47)
            decorLabel1.place(relx=0.2, rely=0.19)
            exPartLabel0.config(text="Part Number:  " + partsDict[entry1.get()].number, font=font2)
            exPartLabel1.config(text="Description:  " + partsDict[entry1.get()].descrip, font=font2)
            exPartLabel2.config(text="Quantity:  " + str(partsDict[entry1.get()].quantity) + " (across all inventory)",
                                font=font2)
            exPartLabel0.place(relx=0.39, rely=0.29)
            exPartLabel1.place(relx=0.39, rely=0.35)
            exPartLabel2.place(relx=0.39, rely=0.41)
            ptLocationLabel3.place(relx=0.405, rely=0.565)
            Addrandptquantitylabel0.place(relx=0.435, rely=0.703)
            Addrandptquantity0.place(relx=0.4105, rely=0.755)
            ptLocationMenu2.place(relx=0.42, rely=0.625)
            removePartsButton.place(relx=0.412, rely=0.82)

        def removePartFromSystem():
            clearRoot()
            partsRemoveLabel.place(relx=0.278, rely=0.03)
            partInfoLabel1.place(relx=0.275, rely=0.20)
            partInfoLabel3.place(relx=0.22, rely=0.53)
            decorLabel1.place(relx=0.2, rely=0.19)
            exPartLabel0.config(text="Part Number:  " + partsDict[entry1.get()].number, font=font2)
            exPartLabel1.config(text="Description:  " + partsDict[entry1.get()].descrip, font=font2)
            exPartLabel2.config(text="Quantity:  " + str(partsDict[entry1.get()].quantity) + " (across all inventory)",
                                font=font2)
            exPartLabel0.place(relx=0.39, rely=0.29)
            exPartLabel1.place(relx=0.39, rely=0.35)
            exPartLabel2.place(relx=0.39, rely=0.41)
            yesRemoveButton.place(relx=0.36, rely=0.61)
            noRemoveButton.place(relx=0.56, rely=0.61)

        def takeMeBack1():
            resetRoot()

        def displayPic():
            clearRoot()
            extraLabel.place(relx = 0.20, rely = 0.02)
            wowButton.place(relx = 0.43, rely = 0.78)

        # Also add location variable to part objects for real-life organization, organize code with comment structuring
        def placeLabelProcessing():

            num1 = 0
            num2 = 0
            num3 = 0
            if entry1.get() in partsOn1st.keys():
                num1 = partsOn1st[entry1.get()].quantity
            if entry1.get() in parts2ndBack.keys():
                num2 = parts2ndBack[entry1.get()].quantity
            if entry1.get() in parts2ndOff.keys():
                num3 = parts2ndOff[entry1.get()].quantity

            exPartLabel4.config(text="Units at:  " + "1st floor: " + str(num1) + "  |  2nd floor office: " + str(
                num3) + "  |  2nd floor backroom: " + str(num2))

        def Lookup():

            clearRoot()

            placeLabelProcessing()
            partLookupLabel.place(relx=0.139, rely=0.125)
            OKresetbutton.place(relx=0.45, rely=0.66)
            decorLabel.place(relx=0.2, rely=0.19)
            partInfoLabel1.place(relx=0.275, rely=0.20)
            exPartLabel0.place(relx=0.21, rely=0.28)
            exPartLabel1.place(relx=0.21, rely=0.34)
            exPartLabel2.place(relx=0.21, rely=0.4)
            exPartLabel3.place(relx=0.21, rely=0.46)
            exPartLabel4.place(relx=0.21, rely=0.52)

            exPartLabel0.config(text="Part Number:  " + partsDict[entry1.get()].number, font=font2)
            exPartLabel1.config(text="Description:  " + partsDict[entry1.get()].descrip, font=font2)
            exPartLabel2.config(
                text="Quantity:  " + "Quantity:  " + str(partsDict[entry1.get()].quantity) + " (across all inventory)",
                font=font2)
            exPartLabel3.config(text="Project:  " + partsDict[entry1.get()].project, font=font2)

        def clearRoot():
            entry1.place_forget()
            nameLabel.place_forget()
            enterButton.place_forget()
            noButton.place_forget()
            yesButton.place_forget()
            topLabel.place_forget()
            AddrandpartButton.place_forget()
            dashBoardLabel.place_forget()
            modButton1.place_forget()
            modButton2.place_forget()
            modButton3.place_forget()
            modButton4.place_forget()
            partLookupLabel.place_forget()
            decorLabel.place_forget()
            partInfoLabel1.place_forget()
            OKresetbutton.place_forget()
            exPartLabel0.place_forget()
            exPartLabel1.place_forget()
            exPartLabel2.place_forget()
            exPartLabel3.place_forget()
            exPartLabel4.place_forget()
            ptLocationLabel2.place_forget()
            Addrandptquantitylabel0.place_forget()
            Addrandptquantity0.place_forget()
            ptLocationMenu2.place_forget()
            enterPartsButton.place_forget()
            partCheckInLabel.place_forget()
            partInfoLabel1.place_forget()
            partInfoLabel2.place_forget()
            decorLabel1.place_forget()
            partsEnteredLabel.place_forget()
            partsRemovedLabel.place_forget()
            ptLocationLabel3.place_forget()
            checkOutButton.place_forget()
            partCheckOutLabel.place_forget()
            partsCheckedOutLabel.place_forget()
            partsRemoveLabel.place_forget()
            removePartsButton.place_forget()
            removePartsFromSystemButton.place_forget()
            removePartsFromStockButton.place_forget()
            yesRemoveButton.place_forget()
            noRemoveButton.place_forget()
            ptLocationLabel3.place_forget()
            partInfoLabel3.place_forget()
            actionCompletedLabel.place_forget()
            modButton5.place_forget()
            enterNameLabel.place_forget()
            enterName.place_forget()
            browsePartsButton.place_forget()
            columnLabel.place_forget()
            browseFrame.place_forget()
            userEntry.forget()
            browseEntry.forget()
            checkOutLogButton.place_forget()
            columnLabel1.place_forget()
            partScrollEntry.forget()
            columnLabel2.place_forget()
            partFrame.place_forget()
            scroll1.forget()
            editNumberEntry.place_forget()
            addButton2.place_forget()
            subtractButton.place_forget()
            decorLabel1.place_forget()
            columnLabel3.place_forget()
            scroll.forget()
            easterEggButton.place_forget()
            extraLabel.place_forget()
            wowButton.place_forget()

        def resetRoot():
            easterEggButton.place(relx = 0.00, rely = 0.94)
            entry1.place(width=250, relx=0.32, y=77)
            root.bind('<Return>', entering1)
            noButton.place_forget()
            yesButton.place_forget()
            badLabel.place_forget()
            enterButton.place(relx=0.3525, y=115)
            enterButton["state"] = NORMAL
            OKresetbutton.place_forget()
            partenteredlabel.place_forget()
            nameLabel.place(relx=0.305, y=47)
            topLabel.place(relx=0.235, y=10)
            checkOutLogButton.place(relx=0.756, rely=0.69)
            entry1.delete(0, tk.END)
            AddrandpartButton.place(relx=0.756, rely=0.87)
            dashBoardLabel.place_forget()
            modButton1.place_forget()
            modButton2.place_forget()
            modButton3.place_forget()
            modButton4.place_forget()
            partLookupLabel.place_forget()
            decorLabel.place_forget()
            partInfoLabel1.place_forget()
            OKresetbutton.place_forget()
            exPartLabel0.place_forget()
            exPartLabel1.place_forget()
            exPartLabel2.place_forget()
            exPartLabel3.place_forget()
            exPartLabel4.place_forget()
            ptLocationLabel2.place_forget()
            Addrandptquantitylabel0.place_forget()
            Addrandptquantity0.place_forget()
            ptLocationMenu2.place_forget()
            enterPartsButton.place_forget()
            partCheckInLabel.place_forget()
            partInfoLabel1.place_forget()
            partInfoLabel2.place_forget()
            decorLabel1.place_forget()
            partsEnteredLabel.place_forget()
            ptLocationLabel3.place_forget()
            checkOutButton.place_forget()
            partsRemovedLabel.place_forget()
            partCheckOutLabel.place_forget()
            partsCheckedOutLabel.place_forget()
            partsRemoveLabel.place_forget()
            removePartsButton.place_forget()
            removePartsFromSystemButton.place_forget()
            removePartsFromStockButton.place_forget()
            yesRemoveButton.place_forget()
            noRemoveButton.place_forget()
            ptLocationLabel3.place_forget()
            partInfoLabel3.place_forget()
            actionCompletedLabel.place_forget()
            modButton5.place_forget()
            browsePartsButton.place(relx=0.756, rely=0.78)
            columnLabel.place_forget()
            browseFrame.place_forget()
            userFrame.place_forget()
            userEntry.forget()
            browseEntry.forget()

            columnLabel1.place_forget()
            partScrollEntry.forget()
            columnLabel2.place_forget()
            partFrame.place_forget()
            scroll1.forget()
            editNumberEntry.place_forget()
            addButton2.place_forget()
            subtractButton.place_forget()
            decorLabel1.place_forget()
            columnLabel3.place_forget()
            scroll.forget()
            extraLabel.place_forget()
            wowButton.place_forget()

        # first entering function on root

        def entering1(e):
            if entry1.get() == '':

                showError("Empty Field")
            else:
                # Part is in Inventory
                enterButton.place_forget()
                root.unbind('<Return>')

                enterButton['state'] = tk.DISABLED

                self.data = entry1.get()

                if entry1.get() in partsDict.keys():
                    dashBoardLabel.place(relx=0.26, rely=0.31)
                    modButton1.place(relx=0.27, rely=0.32)
                    modButton2.place(relx=0.4115, rely=0.32)
                    modButton3.place(relx=0.55, rely=0.3190)
                    modButton4.place(relx=0.27, rely=0.4694)
                    modButton5.place(relx=0.55, rely=0.4694)
                # Part number not found in inventory

                else:

                    badLabel.place(relx=0.25, y=168)
                    yesButton.place(relx=0.37, y=205)
                    noButton.place(relx=0.5, y=205)
                    AddrandpartButton.place_forget()

        # Same as entering but for mouse-click

        def click1():
            if entry1.get() == '':

                showError("Empty Field")
            else:
                # Part is in Inventory
                enterButton.place_forget()
                root.unbind('<Return>')

                enterButton['state'] = tk.DISABLED

                self.data = entry1.get()

                if entry1.get() in partsDict.keys():
                    dashBoardLabel.place(relx=0.26, rely=0.31)
                    modButton1.place(relx=0.27, rely=0.32)
                    modButton2.place(relx=0.4115, rely=0.32)
                    modButton3.place(relx=0.55, rely=0.3190)
                    modButton4.place(relx=0.27, rely=0.4694)
                    modButton5.place(relx=0.55, rely=0.4694)
                # Part number not found in inventory

                else:

                    badLabel.place(relx=0.25, y=168)
                    yesButton.place(relx=0.37, y=205)
                    noButton.place(relx=0.5, y=205)
                    AddrandpartButton.place_forget()

        # Add random item thread: poorly designed, basically the same as the newWindow thread above

        def addRandPart():
            addRandWindow = Toplevel(root)
            addRandWindow.config(bg='gray82')
            addRandWindow.geometry("%dx%d%+d%+d" % (640, 480, 250, 125))

            def resetRandLevel():
                BackBut.place_forget()
                tryAgain1.place_forget()
                addRandPartsB.place_forget()
                randPartInfoLabel.place_forget()
                randNumLabel.place_forget()
                randProjLabel.place_forget()
                randDesLabel.place_forget()
                randQuanLabel.place_forget()

                fillRandLevel()

            def refresh1():
                # Reset var and delete all old options
                clicked1.set('')
                projselect1['menu'].delete(0, 'end')

                # Insert list of new options (tk._setit hooks them up to var)

                for choice in options:
                    projselect1['menu'].add_command(label=choice, command=tk._setit(clicked1, choice))

            def projectAdded1():
                if Addprojname1.get() == '':
                    showError("Empty Field")
                else:
                    options.append(Addprojname1.get())
                    saveAwayMain()
                    saveAwayBackup()
                    Addprojnamelabel2.place_forget()
                    Addprojname1.place_forget()
                    Addprojbutton1.place_forget()
                    refresh1()
                    fillRandLevel()

            def addProject2():
                clearRandLevel()
                Addprojnamelabel2.place(relx=0.34, rely=0.29)
                Addprojname1.place(relx=0.27, rely=0.39)
                Addprojbutton1.place(relx=0.42, rely=0.49)

            def addRandParts():

                haveAddedRand.place(relx=0.36, rely=0.37)
                haveAddedRandButton.place(relx=0.40, rely=0.48)
                partsDict[self.key1].quantity += int(Addrandptquantity.get())

                if ((clicked3.get() == '1st Floor')):
                    partsOn1st[self.key1].quantity += int(Addrandptquantity.get())
                elif (clicked3.get() == '2nd Floor Office'):
                    parts2ndOff[self.key1].quantity += int(Addrandptquantity.get())
                elif (clicked3.get() == '2nd Floor Backroom'):
                    parts2ndBack[self.key1].quantity += int(Addrandptquantity.get())

                saveAwayMain()
                saveAwayBackup()

                randPartInfoLabel.place_forget()
                randNumLabel.place_forget()
                randProjLabel.place_forget()
                randDesLabel.place_forget()
                randQuanLabel.place_forget()
                tryAgain1.place_forget()
                addRandPartsB.place_forget()
                BackBut.place_forget()

            def randPartEntered():
                if clicked1.get() == '' or Addrandptnumentry.get() == '' or Addrandptdescentry.get() == '' \
                        or Addrandptprojmentry.get() == '' or clicked3.get() == '' or Addrandptquantity.get() == '':
                    showError('Empty Field(s), try again. (Entry Window Did Not Close, Its Behind Main Window')
                else:
                    boolean = True
                    if Addrandptnumentry.get() in partsDict.keys():
                        tempVar = partsDict[Addrandptnumentry.get()].number
                        self.key1 = partsDict[Addrandptnumentry.get()].number
                        global randnum
                        clearRandLevel()
                        global randPartInfo
                        randPartInfo = [partsDict[tempVar].number, partsDict[tempVar].project,
                                        partsDict[tempVar].descrip,
                                        (partsDict[tempVar].quantity)]
                        makeRandLabels()
                        boolean = False

                        randQuanLabel.place(relx=0.42, rely=0.55)
                        tryAgain1.place(relx=0.23, rely=0.7)
                        addRandPartsB.place(relx=0.40, rely=0.7)
                        BackBut.place(relx=0.62, rely=0.7)
                        randPartInfoLabel.place(relx=0.10, rely=0.30)
                        randNumLabel.place(relx=0.42, rely=0.4)
                        randProjLabel.place(relx=0.42, rely=0.45)
                        randDesLabel.place(relx=0.42, rely=0.5)



                    else:
                        for key in partsDict.keys():
                            if (partsDict[key].descrip.lower() == Addrandptdescentry.get().lower()):
                                self.key1 = key

                                clearRandLevel()

                                randPartInfo = [partsDict[key].number, partsDict[key].project, partsDict[key].descrip,
                                                (partsDict[key].quantity)]
                                makeRandLabels()
                                boolean = False

                                randQuanLabel.place(relx=0.42, rely=0.55)
                                tryAgain1.place(relx=0.23, rely=0.7)
                                addRandPartsB.place(relx=0.40, rely=0.7)
                                BackBut.place(relx=0.62, rely=0.7)
                                randPartInfoLabel.place(relx=0.10, rely=0.30)
                                randNumLabel.place(relx=0.42, rely=0.4)
                                randProjLabel.place(relx=0.42, rely=0.45)
                                randDesLabel.place(relx=0.42, rely=0.5)

                    if (boolean):
                        self.dataList = [clicked1.get(), Addrandptnumentry.get(), Addrandptdescentry.get(),
                                         Addrandptprojmentry.get(), Addrandptquantity.get(), clicked3.get()]
                        dataProc(self)
                        closeRandLevel()
                        clearRoot()
                        OKresetbutton.place(relx=0.44, y=180)
                        partenteredlabel.place(relx=0.34, y=144)

            def clearRandLevel():
                AddrandpartLabel.place_forget()
                Addrandptnumentry.place_forget()
                randButton.place_forget()
                randprojselectlabel.place_forget()
                projselect1.place_forget()
                Addrandptprojmentry.place_forget()
                Addrandptprojmentrylabel.place_forget()
                Addrandptdescentry.place_forget()
                Addrandptdescentrylabel.place_forget()
                enterrandpartButton.place_forget()
                Addrandptquantitylabel.place_forget()
                Addrandptquantity.place_forget()
                ptLocationLabel.place_forget()
                ptLocationMenu.place_forget()
                Addprojectbut2.place_forget()
                AddrandptnumEntryLabel.place_forget()

            def genRandNum():
                inString = createRandNum()
                Addrandptnumentry.delete(0, END)
                Addrandptnumentry.insert(0, inString)

            def createRandNum():
                randNum = str(randint(10000000000, 99999999999))
                if randNum in partsDict.keys():
                    createRandNum()

                else:
                    return randNum

            def closeRandLevel():
                addRandWindow.destroy()

            def fillRandLevel():
                AddrandptnumEntryLabel.place(relx=0.35, rely=0.13)
                AddrandpartLabel.place(relx=0.18, rely=0.02)
                Addrandptnumentry.place(width=200, relx=0.35, rely=0.19)
                randButton.place(relx=0.70, rely=0.135)
                randprojselectlabel.place(relx=0.35, rely=0.25)
                projselect1.place(relx=0.35, rely=0.31, width=205)

                Addrandptprojmentry.place(width=200, relx=0.35, rely=0.45)
                Addrandptprojmentrylabel.place(relx=0.36, rely=0.39)
                Addrandptdescentry.place(width=200, relx=0.35, rely=0.57)
                Addrandptdescentrylabel.place(relx=0.36, rely=0.51)
                enterrandpartButton.place(relx=0.28, rely=0.91)
                Addrandptquantitylabel.place(relx=0.37, rely=0.63)
                Addrandptquantity.place(relx=0.35, rely=0.69, width=200)
                ptLocationLabel.place(relx=0.36, rely=0.75)
                ptLocationMenu.place(relx=0.345, rely=0.82, width=205)
                Addprojectbut2.place(relx=0.72, rely=0.305)

            def makeRandLabels():
                randQuanLabel.config(text="Current Quantity:  " + str(randPartInfo[3]))
                randNumLabel.config(text="Part Number:  " + randPartInfo[0])
                randProjLabel.config(text="Project:  " + randPartInfo[1])
                randDesLabel.config(text="Description:  " + randPartInfo[2])

            tryAgain1 = Button(addRandWindow, text="Try Again", font=font2, padx=20, bg='White', command=resetRandLevel)
            haveAddedRandButton = Button(addRandWindow, text="OK", padx=18, bg='White', command=closeRandLevel)
            haveAddedRand = Label(addRandWindow, text="Part(s) added to system", font=font2, bg='gray82')
            randPartInfoLabel = Label(addRandWindow,
                                      text="Is this the part you're trying to enter? If so, already in system. If not, maybe try part number again")
            Addrandptnumentry = Entry(addRandWindow)
            Addrandptprojmentry = Entry(addRandWindow)
            Addrandptdescentry = Entry(addRandWindow)
            Addrandptquantity = Entry(addRandWindow)
            enterrandpartButton = Button(addRandWindow, text="Enter new part into system", bg='lime green', padx=60,
                                         pady=1.25, font=font2, command=randPartEntered)
            randButton = Button(addRandWindow, wraplength=140,
                                text="Click to generate part number (if part doesn't have one)", bg='White', font=font2,
                                command=genRandNum)
            BackBut = Button(addRandWindow, text="Take me back", font=font2, bg='White', command=closeRandLevel,
                             padx=20)
            addRandPartsB = Button(addRandWindow, text="Add to existing", font=font2, padx=18, bg='White',
                                   command=addRandParts)
            randNumLabel = Label(addRandWindow, text='', font=font2, bg='White')
            randProjLabel = Label(addRandWindow, text='', font=font2, bg='White')
            randDesLabel = Label(addRandWindow, text='', font=font2, bg='White')
            randQuanLabel = Label(addRandWindow, text='why', font=font2, bg='White')
            Addrandptquantitylabel = Label(addRandWindow, text="Enter quantity", bg='gray82', font=font2)
            Addrandptquantity = Entry(addRandWindow)
            AddrandpartLabel = Label(addRandWindow, text="Enter New Part Information", bg='White', font=font2, padx=150,
                                     pady=8)
            Addrandptnumentry = Entry(addRandWindow)
            AddrandptnumEntryLabel = Label(addRandWindow, text="Type Part Number or Scan Barcode", bg='gray82',
                                           font=font2)
            randprojselectlabel = Label(addRandWindow, text="Select project from drop-down", font=font2, bg='gray82')
            clicked1 = StringVar()
            clicked1.set(options[0])
            projselect1 = OptionMenu(addRandWindow, clicked1, *options)
            Addrandptprojmentry = Entry(addRandWindow)
            Addrandptprojmentrylabel = Label(addRandWindow, text="Who's adding this part?", bg='gray82', font=font2)
            Addrandptdescentry = Entry(addRandWindow)
            Addrandptdescentrylabel = Label(addRandWindow, text="Enter part description", bg='gray82', font=font2)
            clicked3 = StringVar()
            clicked3.set(places[0])
            ptLocationMenu = OptionMenu(addRandWindow, clicked3, *places)
            ptLocationLabel = Label(addRandWindow, text="Where is this item going?", bg='gray82', font=font2)
            Addprojnamelabel2 = Label(addRandWindow, text="Enter Official Project Name, i.e. HAN Protect", bg='gray82',
                                      font=font2)
            Addprojname1 = Entry(addRandWindow, width=50, font=font2)
            Addprojbutton1 = Button(addRandWindow, text="All Set!", padx=25, bg='White', command=projectAdded1)
            Addprojectbut2 = Button(addRandWindow, text="Add project?", padx=20, bg='White', command=addProject2)
            fillRandLevel()

        # VARIABLES

        # root window config

        root = Tk()
        root.config(bg='Black')
        root.geometry('820x620')

        # Photos

        bigSearch = PhotoImage(file=r"S:\Product_Developement\Inventory Files\searchIcon.png")
        searchIcon = bigSearch.subsample(20, 20)
        bigUp = PhotoImage(file=r"S:\Product_Developement\Inventory Files\inArrow.png")
        inArrow = bigUp.subsample(26, 28)
        bigDown = PhotoImage(file=r"S:\Product_Developement\Inventory Files\outArrow.png")
        outArrow = bigDown.subsample(26, 27)
        bigX = PhotoImage(file=r"S:\Product_Developement\Inventory Files\xOut.png")
        xOut = bigX.subsample(9, 8)
        bigBack = PhotoImage(file=r"S:\Product_Developement\Inventory Files\backArrow.png")
        backArrow = bigBack.subsample(60, 50)
        bigLogo = PhotoImage(file=r"S:\Product_Developement\Inventory Files\HartingLogoYellow.png")
        logo = bigLogo.subsample(20, 20)
        randPic = PhotoImage(file=r"S:\Product_Developement\Inventory Files\randPic.png")
        extra1 = randPic.subsample(1, 1)
        # fonts

        font1 = font.Font(family='Georgia', size=7)
        font2 = font.Font(family='Helvetica', size=10)

        # Labels
        logoLabel = Label(root, bg='Black', image=logo)
        nameLabel = Label(root, text="Enter Part Number or Scan Barcode", font=font2, padx=40, bg='Black', fg='yellow')
        badLabel = Label(root, text="Part number not in inventory, logging new part into system?", font=font2, padx=40,
                         bg='Black', fg='Red')
        partenteredlabel = Label(root, text="You have successfully entered a new part", font=font2, bg='Black',
                                 fg='yellow',
                                 )
        topLabel = Label(root, text="Part Entry, Return or Lookup", bg='White', font=font2, padx=120)
        dashBoardLabel = Label(root, padx=175, pady=90, bg='White', relief='groove')
        partLookupLabel = Label(root, padx=300, pady=205, bg='White', relief='groove')
        decorLabel = Label(root, padx=250, pady=120, bg='White', relief='solid', borderwidth=0.5)

        partCheckInLabel = Label(root, padx=100, pady=20, bg='White', relief='groove',
                                 text="-------- Part Check-In ---------")

        decorLabel1 = Label(root, padx=250, pady=230, bg='White', relief='solid', borderwidth=0.5)
        partInfoLabel2 = Label(root, padx=100, pady=20, bg='White', text="------- Enter Information ------", font=font2)
        partInfoLabel1 = Label(root, padx=100, pady=20, bg='White', text="------- Part Information ------", font=font2)
        partInfoLabel3 = Label(root, padx=100, bg='White', text="------- Permanently Remove From System? ------")
        exPartLabel0 = Label(root, padx=25, pady=6, bg='White')
        exPartLabel1 = Label(root, padx=25, pady=6, bg='White')
        exPartLabel2 = Label(root, padx=25, pady=6, bg='White')
        exPartLabel3 = Label(root, padx=25, pady=6, bg='White')
        exPartLabel4 = Label(root, padx=25, pady=6, bg='White')

        ptLocationLabel2 = Label(root, text="Where is this item going?", bg='White', font=font2)
        ptLocationLabel3 = Label(root, text="Where is this part coming from?", bg='White', font=font2)
        enterNameLabel = Label(root, text="Who's Checking Out/In?", bg='White', font=font2)
        Addrandptquantitylabel0 = Label(root, text="Enter quantity", bg='White', font=font2)

        partsEnteredLabel = Label(root, text='Parts Have Been Entered', font=font2, bg='Black', fg='yellow')
        partCheckOutLabel = Label(root, padx=100, pady=20, bg='White', relief='groove',
                                  text="-------- Part Check-Out ---------")
        partsCheckedOutLabel = Label(root, text='Parts Checked Out', font=font2, bg='Black', fg="yellow")
        partsRemoveLabel = Label(root, padx=100, pady=20, bg='White', relief='groove',
                                 text="-------- Remove Parts ---------")
        partsRemovedLabel = Label(root, text='Parts Have Been Removed', font=font2, bg='White')
        actionCompletedLabel = Label(root, text='Action Completed', font=font2, bg='Black', fg='yellow')
        columnLabel = Label(root, text="Browse Parts In System   ~   (Part Number    :    Description )", bg='White')
        columnLabel1 = Label(root, text="Users ----- Double Click to View Parts Out)", bg='White')
        columnLabel2 = Label(root, text=" Parts Out  :         (double click part to make edit)", bg='White')
        columnLabel3 = Label(root, text=" Edit Number of Parts Out", bg='White')
        extraLabel = Label(root, image = extra1, bg = 'Black')
        # buttons

        AddrandpartButton = Button(root, text="Add New Parts to System", font=font2, width=23, bg='White',
                                   height=2, command=addRandPart)
        removePartFromSystemButton = Button(root, text="Remove Part(s) from System", font=font2, width=23,
                                            bg='White',
                                            height=2, command=addRandPart)

        yesButton = Button(root, text="Yes", font=font2, padx=20, bg='White', command=click2)
        noButton = Button(root, text="No", font=font2, padx=23, bg='White', command=click3)
        enterButton = Button(root, text="Enter", font=(font2), command=click1 or entering1, padx=75, pady=1.75,
                             bg='White')
        OKresetbutton = Button(root, text="OK", font=font2, command=resetRoot, padx=22, bg='White')
        modButton1 = Button(root, text="Lookup", bg='grey99', font=font2, command=Lookup, padx=30, pady=17,
                            image=searchIcon, compound=BOTTOM)
        modButton2 = Button(root, text="Check In", bg='dark sea green', font=font2, padx=24, pady=14, image=inArrow,
                            compound=BOTTOM, command=checkIn)
        modButton3 = Button(root, text="Check Out", bg='light goldenrod', command=checkOut, font=font2, padx=19,
                            pady=14, image=outArrow, compound=BOTTOM)

        modButton4 = Button(root, text="Remove Parts From System", bg='IndianRed3', font=font2, padx=25, pady=14,
                            image=xOut,
                            compound=BOTTOM, command=removePart)
        modButton5 = Button(root, text="Back", bg='grey88', fg='Black', font=font2, padx=34, pady=17,
                            command=takeMeBack1, image=backArrow, compound=BOTTOM)
        enterPartsButton = Button(root, text="Enter", bg='lime green', padx=30, command=checkInWork)
        checkOutButton = Button(root, text="Check Out", bg='lime green', padx=30, command=checkOutWork)
        removePartsButton = Button(root, text="Done", bg='lime green', padx=30, command=removePartsWork)
        removePartsFromSystemButton = Button(root, wraplength=180, text="Remove Parts Permanently From System", pady=40,
                                             padx=30, command=removePartFromSystem)
        removePartsFromStockButton = Button(root, wraplength=180, text="Remove Parts From Stock", pady=47, padx=45,
                                            command=removeParts)
        yesRemoveButton = Button(root, text="Yes", padx=20, pady=7, command=removePartFromSystemWork)
        noRemoveButton = Button(root, text="No", padx=20, pady=7, command=resetRoot)
        browsePartsButton = Button(root, text="Browse Parts In System", font=font2, width=23, bg='White',
                                   height=2, command=Browse)
        checkOutLogButton = Button(root, text='Check Out Log', font=font2, width=23, bg='White',
                                   height=2, command=userCheckLog)
        addButton2 = Button(root, text="Add number of parts to user's record", padx=20, pady=15,
                            command=editPartsOutAddWork, wraplength=80)
        subtractButton = Button(root, text="Remove number of parts from user's record", padx=20, pady=7,
                                command=editPartsOutSubtractWork, wraplength=80)
        easterEggButton = Button(root, bg = 'Black', command = displayPic, padx = 14, pady = 6)
        wowButton = Button(root, bg = 'White', text = 'WOW!', command = resetRoot, padx = 14, pady = 6)


        # entryBoxes
        entry1 = Entry(root)
        Addrandptquantity0 = Entry(root, relief='groove', highlightbackground="Black", highlightthickness=0.5)
        clicked4 = StringVar()
        clicked4.set(places[0])
        ptLocationMenu2 = OptionMenu(root, clicked4, *places)
        enterName = Entry(root, relief='groove', highlightbackground="Black", highlightthickness=0.5)
        editNumberEntry = Entry(root, relief='groove', highlightbackground="Black", highlightthickness=0.5)

        # bindings

        root.bind('<Return>', entering1)

        # root window default
        topLabel.place(relx=0.235, y=10)
        entry1.place(width=250, height=20, relx=0.32, y=77)
        logoLabel.place(relx=0.03, rely=0.75)
        enterButton.place(relx=0.3525, y=115)

        nameLabel.place(relx=0.295, y=47)
        easterEggButton.place(relx = 0.00, rely = 0.94)
        AddrandpartButton.place(relx=0.756, rely=0.87)
        browsePartsButton.place(relx=0.756, rely=0.78)
        checkOutLogButton.place(relx=0.756, rely=0.69)

        # Frame Pieces

        browseFrame = Frame(root)
        scroll = Scrollbar(browseFrame, orient=VERTICAL)
        browseEntry = Listbox(browseFrame, width=77, height=25, relief='groove', highlightbackground="White",
                              highlightthickness=0.8, yscrollcommand=scroll)
        scroll.config(command=browseEntry.yview)

        userFrame = Frame(root)
        scroll1 = Scrollbar(userFrame, orient=VERTICAL)
        userEntry = Listbox(userFrame, width=77, height=25, relief='groove', highlightbackground="White",
                            highlightthickness=0.8, yscrollcommand=scroll1)
        scroll1.config(command=userEntry.yview)

        partFrame = Frame(root)
        scroll2 = Scrollbar(partFrame, orient=VERTICAL)
        partScrollEntry = Listbox(partFrame, width=77, height=25, relief='groove', highlightbackground="White",
                                  highlightthickness=0.8, yscrollcommand=scroll2)
        scroll2.config(command=partScrollEntry.yview)
        userEntry.bind('<Double-1>', userPartCheckLog)
        partScrollEntry.bind('<Double-1>', editPartsOut)

        def dataProc(self):
            self.proj = self.dataList[0]
            self.num = self.dataList[1]
            self.desc = self.dataList[2]
            self.pjm = self.dataList[3]
            self.quan = int(self.dataList[4])
            self.place = self.dataList[5]
            print(self.dataList[5])
            temp = part(self.quan, self.num, self.desc, self.proj, self.pjm)
            temp.check(self.place)
            print(partsDict)

        root.mainloop()


class part(GUI):
    quantity = 0
    number = ""
    descrip = ""
    project = ""
    pm = ""

    def __init__(self, quan, num, desc, proj, pjm):
        self.quantity = int(quan)
        self.number = num
        self.descrip = desc
        self.project = proj
        self.pm = pjm

    def check(self, place):
        print(place)
        if self.number in partsDict.keys():
            print('Something went wrong, check partEntered')
        else:
            partsDict[self.number] = self
            partsOn1st[self.number] = part(0, self.number, self.desc, self.proj, self.pjm)
            parts2ndOff[self.number] = part(0, self.number, self.desc, self.proj, self.pjm)
            parts2ndBack[self.number] = part(0, self.number, self.desc, self.proj, self.pjm)

            if (place == '1st Floor'):
                partsOn1st[self.number].quantity += self.quantity
            elif (place == '2nd Floor Office'):
                parts2ndOff[self.number].quantity += self.quantity
            elif (place == '2nd Floor Backroom'):
                parts2ndBack[self.number].quantity += self.quantity

            saveAwayMain()
            saveAwayBackup()

            print("part added to dic")

    def printer(self):
        print(self.quantity)
        print(self.number)
        print(partsDict)


def initialize():
    data3 = open(r'S:\Product_Developement\Inventory Files\Inventory Data\Data1.csv', 'rb')
    global partsOn1st
    global parts2ndBack
    global parts2ndOff
    global userPartCheck
    global partsDict
    global options
    partsDict = pickle.load(data3)
    partsOn1st = pickle.load(data3)
    parts2ndBack = pickle.load(data3)
    parts2ndOff = pickle.load(data3)
    userPartCheck = pickle.load(data3)
    options = pickle.load(data3)
    data3.close()
    print('running')


class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer = None
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = threading.Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False


rt = RepeatedTimer(2, initialize)

gui = GUI(" ")
gui.face()
print("Program Closed Successfully")
rt.stop()

saveAwayMain()