import tkinter
 
 
window = Tk()
window.title("Python Tkinter")
window.minsize(width=450, height=300)

def click_button():
    print("button clicked")

#Label
my_label = tkinter.Label(text="This is a Label", font=('Arial', 20, "italic"))
#my_label.config(bg="black", fg="white")
my_label.pack()

my_button = tkinter.Button(text="this is a Button", command=click_button)
my_button.pack()

my_entry = tkinter.Entry(width=20)
my_entry.pack()

window.mainloop()