import tkinter as tk

def str_to_list (exp):
    temp_elements = []
    digits = ["0","1","2","3","4","5","6","7","8","9"]
    operators = ["+", "-", "/", "*"]
    temp_number = ""
    for each_symbol in exp:
        if each_symbol != " ":
            if each_symbol in digits:
                temp_number = temp_number + str(each_symbol)
            elif each_symbol in operators:
                temp_elements.append(temp_number)
                temp_number = ""
                temp_elements.append(each_symbol)
    temp_elements.append(temp_number)
    return temp_elements

def add (a, b):
    return int(a)+int(b)

def sub (a, b):
    return int(a)-int(b)

def div (a, b):
    return int(a)/int(b)

def mul (a, b):
    return int(a)*int(b)

def calculation():

    global resultLabel
    elements = str_to_list(expression.get())

    result = 0

    if len(elements) >= 3:
        
        i = 0

        while i < (len(elements) - 2):
            
            # print("value = " + str(elements[i]) + ". i = " + str(i) + ". Lists' length = " + str (len(elements)))

            if elements[i+1] == "*":
                element_to_add = mul(elements [i], elements[i+2])
                elements.pop(i)
                elements.pop(i)
                elements.pop(i)
                elements.insert(i, element_to_add)
            
            elif elements[i+1] == "/":
                element_to_add = div(elements [i], elements[i+2])
                elements.pop(i)
                elements.pop(i)
                elements.pop(i)
                elements.insert(i, element_to_add)

            else:
                i = i + 1

            if len(elements) == 1:
                result = elements[0]
                break

    if len(elements) >= 3:
        
        i = 0

        while i < (len(elements) - 2):
            
            if elements[i+1] == "+":
                element_to_add = add(elements [i], elements[i+2])
                elements.pop(i)
                elements.pop(i)
                elements.pop(i)
                elements.insert(i, element_to_add)
            
            elif elements[i+1] == "-":
                element_to_add = sub(elements [i], elements[i+2])
                elements.pop(i)
                elements.pop(i)
                elements.pop(i)
                elements.insert(i, element_to_add)

            else:
                i = i + 1

            if len(elements) == 1:
                result = elements[0]
                break

    resultValue.config(text = expression.get().replace(" ", "") + " = " + str(result))
    expression.delete(0, tk.END)

window = tk.Tk()
window.configure(background="light blue")
window.title("Calculator")
window.geometry("265x100")

frameBorderWidth = 1
padx = 5
pady = 5

Frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=frameBorderWidth)
Frame.grid(row=0, column=0, padx=padx, pady=pady)

expressionLabel = tk.Label(master=Frame, text="Expression:", width = 9)
expressionLabel.grid(row=0, column=0)

expression = tk.Entry(master=Frame, width=30)
expression.grid(row=0, column=1)

resultLabel = tk.Label(master=Frame, text="Result:", width = 9)
resultLabel.grid(row=1, column=0)

resultValue = tk.Label(master=Frame)
resultValue.grid(row=1, column=1, sticky="w")

button_calculate = tk.Button(master=window, text="Calculate", command=calculation)
button_calculate.grid(row=3, column=0)

window.bind('<Return>', lambda event: calculation())

window.mainloop()