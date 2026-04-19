from tkinter import *
from tkinter import ttk

def is_float(val):
    try:
        float(val)
        return True
    except: 
        return False
    
def validate_entry_temp(newval):
    scl = scale_combobox.get()
    scls = {'K':0.0, 'F': -459.67, 'C': -273.15}
  
    if(newval == "" or newval == "-" and scl != 'K'):
        return True
  
    if(is_float(newval)):
        if(float(newval) >= scls[scl]):
            return True
    
    return False


def calculate(*args):
    
    scl = scale_combobox.get()
    e_temp = entry_temp.get()
    if(e_temp == "" or e_temp == "-"): 
        e_temp = '0'
        entry_temp.set('0')
    match scl:
        case 'K':
            convert_temp1.set(f"{(float(e_temp) - 273.15) *1.8 + 32: .2f}")
            convert_temp2.set(f"{float(e_temp) - 273.15: .2f}")
        case 'F':
            convert_temp1.set(f"{(float(e_temp) - 32)/1.8: .2f}")
            convert_temp2.set(f"{(float(e_temp) - 32)/1.8 + 273.15: .2f}")
        case 'C':
            convert_temp1.set(f"{float(e_temp) + 273.15: .2f}")
            convert_temp2.set(f"{float(e_temp) * 1.8 + 32: .2f}")


def scale_changed(*args):
    scl = scale_combobox.get()
    match scl:
        case 'K':
            converted_scale1.set('F')
            converted_scale2.set('C')
        case 'F':
            converted_scale1.set('C')
            converted_scale2.set('K')
        case 'C':
            converted_scale1.set('K')
            converted_scale2.set('F')


root = Tk()
root.title("Temperature Converter")
root.resizable(False, False)
mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))


validate_entry = (root.register(validate_entry_temp), '%P')
entry_temp = StringVar()
ttk.Entry(mainframe, textvariable=entry_temp, validate='key' , validatecommand=validate_entry, justify="right").grid(column=1, row=1, sticky=(E, W))

scale_combobox = ttk.Combobox(mainframe, state='readonly', values=('K', 'F', 'C'), width=1)
scale_combobox.grid(column=2, row=1, sticky=(N, E, W))
scale_combobox.current(0)

convert_temp1 = StringVar(value='0.00')
convert_temp2 = StringVar(value='0.00')
ttk.Label(mainframe, textvariable=(convert_temp1)).grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, textvariable=(convert_temp2)).grid(column=1, row=3, sticky=E)

converted_scale1 = StringVar(value='F')
converted_scale2 = StringVar(value='C')
ttk.Label(mainframe, textvariable=(converted_scale1)).grid(column=2, row=2, sticky=W)
ttk.Label(mainframe, textvariable=(converted_scale2)).grid(column=2, row=3, sticky=W)

ttk.Button(mainframe, text='convert', command=calculate).grid(column=1, row=4, columnspan=2, sticky=E)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.bind("<<ComboboxSelected>>", scale_changed)
root.bind("<Return>", calculate)



root.mainloop()