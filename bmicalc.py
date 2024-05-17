from tkinter import *

w = Tk()
w.title("BMI Calculator")
w.minsize(width=200, height=150)
w.config(padx=30, pady=30)


# def calc_bmi():
#     if input_entry_kg and input_entry_hi is int:
#         if input_entry_kg and input_entry_hi > 0:
#            sonuc = input_entry_hi / input_entry_kg * input_entry_kg
#         if sonuc <= 18.5:
#             print("Zayıfsın")
#         elif sonuc > 18.5 and sonuc <= 29.9:
#             print("Normal Ağırlıktasın") 
#         elif sonuc > 29.9 and sonuc <= 34.9:
#             print("Kilolu")
#         elif sonuc > 34.9 and sonuc <= 39.9:
#             print("I. Derece Obezite")
#         elif sonuc > 39.9 and sonuc <= 49.9:
#             print("II. Derece Obezite")
#         elif sonuc > 49.9 and sonuc <= 59.9:
#             print("III. Derece Obezite")

def calculate_bmi():
    height = input_entry_hi.get()
    weight = input_entry_we.get()
    if weight == "" or height == "":
        result_label.config(text="Enter both weight and height")
        
    else:
        try:
            bmi = float(weight) / ((float(height) /100) ** 2)
            result_string = Write_result(bmi)
            result_label.config(text=result_string)

        except:
            result_label.config(text="Enter a valid number")

label_kg = Label(text="Enter Your Weight (kg)")
label_kg.pack()


input_entry_we = Entry(width=20)
input_entry_we.pack()

label_height = Label(text="Enter Your Height (cm)")
label_height.pack()

input_entry_hi = Entry(width=20)
input_entry_hi.pack()

calc_button = Button(text= "Calculate", command=calculate_bmi)
calc_button.pack()

result_label = Label()
result_label.pack()

def Write_result(bmi):
    result_string = f"Your BMI is: {round(bmi, 2)}. You are "
    if bmi <= 18.5:
        result_string += "Your bmi: Severely Thin!"
    elif 18.5 < bmi <= 24.9:
        result_string += "Your bmi: Normal!"
    elif 24.9 < bmi <= 29.9:
        result_string += "Your bmi: Fat!"
    elif 29.9 < bmi <= 34.9:
        result_string += "Your bmi: I. Level Obese!"
    elif 34.9 < bmi <= 39.9:
        result_string += "Your bmi: II. Level Obese!"
    else:
        result_string += "Your bmi: III. Level Obese!!"
    return result_string


w.mainloop()