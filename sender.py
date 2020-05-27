import csv,re,time,keyboard, webbrowser, datetime, os, subprocess
from tkinter import scrolledtext,LabelFrame,Entry,ttk, messagebox,Tk,PhotoImage,Button,LEFT,N,S,W,E,Label,Menu,IntVar,Spinbox,StringVar
from tkinter import filedialog as fd
from threading import Thread
#creating window
window = Tk()
window.title("WhatsApp sender per Studio Medico")
window.geometry('520x450')
window.iconbitmap('./ico/wa32x32.ico')
tab_control = ttk.Notebook(window)

#variables
message_p=StringVar()
message_p.set("Default Message")
message_pa=StringVar()
message_pa.set("Default Message")
message_ivs="Default Message"
ivstxt="Default Message"
promapp="Default Message"
second=IntVar(value=10)
edit=PhotoImage(file='./ico/edit16x16.png')
file_name=StringVar()
file_name2=StringVar()
file_name2.set("File Not Selected")
phone_number=StringVar()
pz_list = []
oggi0 = datetime.datetime.today()
domani0 = oggi0+datetime.timedelta(days=1)
tregiorni0 = oggi0+datetime.timedelta(days=3)
oggi = datetime.datetime.today().strftime("%d %m %y")
domani=domani0.strftime("%d %m %y")
tregiorni = tregiorni0.strftime("%d %m %y")

f=open("./testi/primavs.txt", "r", encoding="utf-8")
if f.mode == 'r':
    contents=f.read()
    ivstxt=contents

f1=open("./testi/promemoriaappto.txt", "r", encoding="utf-8")
if f1.mode == 'r':
    contents=f1.read()
    promapp=contents

#functions
def upload():
    global file_name
    file_name = fd.askopenfilename()
    file_name2.set(file_name)

def msg_personal():
    global message_p
    with open(file_name) as csvfile:
        numreader=csv.reader(csvfile, delimiter=';')
        message_p=txt.get("1.0",'end-1c')
        for row in numreader:
            phonenumber=re.sub(r'\D', '',row[0]).split()
            for i in phonenumber:
                webbrowser.open("https://web.whatsapp.com/send?phone=39"+i+"&text="+message_p)
                time.sleep(second.get())
                keyboard.press_and_release("enter")
                time.sleep(second.get())
                keyboard.press_and_release("ctrl+w")
                time.sleep(1)
                keyboard.press_and_release("enter")

def promemoria_app_1():
    with open(file_name) as csvfile:
        numreader=csv.DictReader(csvfile, delimiter=';')
        for patient in numreader:
            pz_list.append(dict(patient))
            if patient["data"]==domani:
                phonenumber=re.sub(r'\D', '',patient["numero"]).split()
                name=patient["nome"]
                date=patient["data"]
                orario=patient["orario"]
                message_pa="Gentile "+name+", le vogliamo ricordare il suo appuntamento del "+date+" alle "+orario+". "
                for i in phonenumber:
                    webbrowser.open("https://web.whatsapp.com/send?phone=39"+i+"&text="+message_pa+promapp)
                    time.sleep(second.get())
                    keyboard.press_and_release("enter")
                    time.sleep(second.get())
                    keyboard.press_and_release("ctrl+w")
                    time.sleep(1)
                    keyboard.press_and_release("enter")

def promemoria_app_3():
    with open(file_name) as csvfile:
        numreader=csv.DictReader(csvfile, delimiter=';')
        for patient in numreader:
            pz_list.append(dict(patient))
            if patient["data"]==tregiorni:
                phonenumber=re.sub(r'\D', '',patient["numero"]).split()
                name=patient["nome"]
                date=patient["data"]
                orario=patient["orario"]
                message_pa="Gentile "+name+", le vogliamo ricordare il suo appuntamento del "+date+" alle "+orario+". "
                for i in phonenumber:
                    webbrowser.open("https://web.whatsapp.com/send?phone=39"+i+"&text="+message_pa+promapp)
                    time.sleep(second.get())
                    keyboard.press_and_release("enter")
                    time.sleep(second.get())
                    keyboard.press_and_release("ctrl+w")
                    time.sleep(1)
                    keyboard.press_and_release("enter")

def prima_vs_1():
    with open(file_name) as csvfile:
        numreader=csv.DictReader(csvfile, delimiter=';')
        for patient in numreader:
            pz_list.append(dict(patient))
            if patient["data"]==domani:
                phonenumber=re.sub(r'\D', '',patient["numero"]).split()
                name=patient["nome"]
                date=patient["data"]
                orario=patient["orario"]
                message_ivs="Gentile "+name+", le vogliamo ricordare il suo appuntamento del "+date+" alle "+orario+". "
                for i in phonenumber:
                    webbrowser.open("https://web.whatsapp.com/send?phone=39"+i+"&text="+message_ivs+ivstxt)
                    time.sleep(second.get())
                    keyboard.press_and_release("enter")
                    time.sleep(second.get())
                    keyboard.press_and_release("ctrl+w")
                    time.sleep(1)
                    keyboard.press_and_release("enter")

def prima_vs_3():
    with open(file_name) as csvfile:
        numreader=csv.DictReader(csvfile, delimiter=';')
        for patient in numreader:
            pz_list.append(dict(patient))
            if patient["data"]==tregiorni:
                phonenumber=re.sub(r'\D', '',patient["numero"]).split()
                name=patient["nome"]
                date=patient["data"]
                orario=patient["orario"]
                message_ivs="Gentile "+name+", le vogliamo ricordare il suo appuntamento del "+date+" alle "+orario+". "
                for i in phonenumber:
                    webbrowser.open("https://web.whatsapp.com/send?phone=39"+i+"&text="+message_ivs+ivstxt)
                    time.sleep(second.get())
                    keyboard.press_and_release("enter")
                    time.sleep(second.get())
                    keyboard.press_and_release("ctrl+w")
                    time.sleep(1)
                    keyboard.press_and_release("enter")

def editvs():
    current_dir = os.getcwd()
    os.startfile(current_dir+"/testi/primavs.txt")

def promemoriaappto():
    current_dir = os.getcwd()
    os.startfile(current_dir+"/testi/promemoriaappto.txt")

def about():
    messagebox.showinfo("Version 240520", 'WhatsApp message sender per Studio Medico\n \n Change log: \n *Threading enabled \n *path fixed \n *edit messages in templates \n *date reminder')    

def clicked():
    messagebox.showinfo("Avviso!", 'Questa pulsanta non funziona ancora :(')

#thread for personal message
def th1():
    thread3=Thread(target=prima_vs_1, daemon=True)
    thread3.start()
def th2():
    thread4=Thread(target=prima_vs_3, daemon=True)
    thread4.start()
def th3():
    thread3=Thread(target=promemoria_app_3, daemon=True)
    thread3.start()
def th4():
    thread4=Thread(target=promemoria_app_1, daemon=True)
    thread4.start()
def th5():
    thread5=Thread(target=msg_personal, daemon=True)
    thread5.start()
#create menu
selected = IntVar() 
menu = Menu(window)  
new_item = Menu(menu,tearoff=0)  
new_item.add_command(label='About', command=about)  
menu.add_cascade(label='Menu', menu=new_item)  
window.config(menu=menu)
#create TABs
tab0 = ttk.Frame(tab_control)
tab_control.add(tab0, text='Personalizzato')
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Templates')
#Label frame in the 0 tab
checkGroup2 = LabelFrame(tab0, text = "Messaggio personalizzato", padx=10, pady=10)
checkGroup2.place(x=5,y=100)
txt = scrolledtext.ScrolledText(checkGroup2, width=57, height=10)  
txt.grid(column=1, row=1)

checkGroup3 = LabelFrame(tab0, text = "Impostazioni:", padx=6, pady=5)
checkGroup3.place(x=5,y=5)
lbl = Label(checkGroup3, text="Elenco numeri:" , compound=LEFT, anchor="w")
lbl.grid(sticky=N+S+W+E, column=0, row=0)
btn = Button(checkGroup3, text="Select file", command=upload)
btn.grid(sticky=N+S+W+E, column=2, row=0)

lbl = Label(tab0, text="Hai selezionato: ", compound=LEFT, anchor="w")
lbl.grid(sticky=N+S+W+E, column=0, row=10)
lbl.place(x=5,y=70)
lbl = Label(tab0, textvariable=file_name2, compound=LEFT, anchor="w")
lbl.grid(sticky=N+S+W+E, column=1, row=10)
lbl.place(x=95,y=70)

lbl = Label(checkGroup3, text="Mandare messaggio ogni")  
lbl.grid(column=3, row=0)  
spin = Spinbox(checkGroup3, from_=10, to=60, width=3, textvariable=second)
spin.grid(column=4, row=0)
lbl = Label(checkGroup3, text="secondi.")
lbl.grid(column=5, row=0)

#tab 1###############
checkGroup4 = LabelFrame(tab1, text = "Impostazioni:", padx=6, pady=5)
checkGroup4.place(x=5,y=5)
lbl = Label(checkGroup4, text="Elenco numeri:" , compound=LEFT, anchor="w")
lbl.grid(sticky=N+S+W+E, column=0, row=0)
btn = Button(checkGroup4, text="Select file", command=upload)
btn.grid(sticky=N+S+W+E, column=2, row=0)

lbl = Label(tab1, text="Hai selezionato: ", compound=LEFT, anchor="w")
lbl.grid(sticky=N+S+W+E, column=0, row=10)
lbl.place(x=5,y=70)
lbl = Label(tab1, textvariable=file_name2, compound=LEFT, anchor="w")
lbl.grid(sticky=N+S+W+E, column=1, row=10)
lbl.place(x=95,y=70)

lbl = Label(checkGroup4, text="Mandare messaggio ogni")  
lbl.grid(column=3, row=0)  
spin = Spinbox(checkGroup4, from_=10, to=60, width=3, textvariable=second)
spin.grid(column=4, row=0)
lbl = Label(checkGroup4, text="secondi.")
lbl.grid(column=5, row=0)

#templates in tab 1
checkGroup = LabelFrame(tab1, text = "Templates", padx=10, pady=10)
checkGroup.place(x=10,y=100)
lbl1 = Label(checkGroup, text="Promemoria appuntamento:", compound=LEFT, anchor="w")
lbl1.grid(sticky=N+S+W+E, column=0, row=1)
button = Button(checkGroup, text="1 Giorno", bg="green3", anchor="w", command=th4)
button.grid(sticky=N+S+W+E, column=1, row=1)
button = Button(checkGroup, text="3 Giorni", bg="gold2", anchor="w", command=th3)
button.grid(sticky=N+S+W+E, column=2, row=1)
button = Button(checkGroup, text="Edit",image=edit, anchor="w", command=promemoriaappto)
button.grid(sticky=N+S+W+E, column=3, row=1)
lbl2 = Label(checkGroup, text="Messaggio Prima Visita:", compound=LEFT, anchor="w")
lbl2.grid(sticky=N+S+W+E, column=0, row=2)
button = Button(checkGroup, text="1 Giorno", anchor="w", bg="green3", command=th1)
button.grid(sticky=N+S+W+E, column=1, row=2)
button = Button(checkGroup, text="3 Giorni", anchor="w", bg="gold2", command=th2)
button.grid(sticky=N+S+W+E, column=2, row=2)
button = Button(checkGroup, text="Edit",image=edit, anchor="w", command=editvs)
button.grid(sticky=N+S+W+E, column=3, row=2)
#send button
btn = Button(tab0, text="MANDARE MESSAGGIO", font=("Arial Bold", 20), bg="DarkOliveGreen2", fg="gray17", command=th5)
btn.grid(sticky=N+S+W+E, column=1, row=10)
btn.place(x=95,y=310)
#
tab_control.pack(expand=1, fill='both')
window.mainloop()