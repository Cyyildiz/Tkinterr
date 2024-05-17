from tkinter import *
window = Tk()
window.title("Tkinter Python")
window.minsize(width=600, height=600)

Label = Label(text="my label")
Label.config(bg="black")
Label.config(fg="white")

#button
def button_clicked():
    print("button_clicked")
    print(my_entry.get("1.0", END)) # buraya 2 deseydik eğer o zaman text'in içinde ki ilk satırı almazdı ama 1.3 deseydik eğer o zaman text'in içinde ki ilk satırın ilk 3 karakterini almazdı

my_button = Button(text="button", command=button_clicked)
my_button.configure(padx=10, pady=10)
my_button.pack()

#entry
my_entry = Entry(width=20)
my_entry.pack()


#multiline
#text
my_text = Text(width=30, height=5)
my_text.pack()

#scale
my_scale = Scale(from_=0, to_=50)
my_scale.pack()

#spinbox
my_spinbox = Spinbox(from_=0, to_=50)
my_spinbox.pack()

#checkbutton
def checkbutton_selected():
    print(check_stated.get())

check_stated = IntVar()
my_checkbutton = Checkbutton(text="Check", variable=check_stated, command=checkbutton_selected)
my_checkbutton.pack()

#radio button

def radio_selected():
    print(radio_checked_stated.get())

radio_checked_stated = IntVar()
my_radiobutton = Radiobutton(text="1. Option", value=10, variable=radio_checked_stated, command=radio_selected)
my_radiobutton_2 = Radiobutton(text="1. Option", value=20, variable=radio_checked_stated, command=radio_selected)
my_radiobutton.pack()
my_radiobutton_2.pack()

#listbox

my_listbox = Listbox()
my_list = ["Atil", "Cem", "Ali", "Veli", "Erdal"]
for i in range(len(my_list)):
    my_listbox.insert(i, my_list[i])

my_listbox.pack()

window.mainloop()