import tkinter as tk
import tkinter.simpledialog as simpledialog
import pandas as pd
from tkinter import messagebox

from pie import show_plot


root = tk.Tk()

def get_emissions_input():
    df = pd.DataFrame()
    try:
        try:
                int(parts.get())
        except ValueError:
                messagebox.showwarning("Illegal Value", "Not an integer.\nPlease try again.")
        assert int(parts.get()) > 0
    except AssertionError:
            messagebox.showwarning("Illegal Value", "Only positive numbers.\nPlease try again.")
            
    for _ in range(int(parts.get())):
        dp = simpledialog.askstring("Data input window" , "Enter Type of CO2 emmision " )
        #Validation of type of emission
        try:
            assert dp.isalpha()
        except AssertionError:
            messagebox.showwarning("Illegal Value", "Not a String.\nPlease try again.")
            break
        st = simpledialog.askstring("Data input window" , f"Enter number of emission {dp} ")
        #Validation of type of emission
        try:
            try:
                int(st)
            except ValueError:
                messagebox.showwarning("Illegal Value", "Not an integer.\nPlease try again.")
            assert int(st) > 0
            #assert int(st) > 0
        except AssertionError:
            messagebox.showwarning("Illegal Value", "Only positive numbers.\nPlease try again.")
            break
        df1 = pd.DataFrame(data=[[dp,st]],columns=["Type", "Emission"])
        df = pd.concat([df,df1], axis=0)

    df.index = range(len(df.index))
    df.index.name = 'index'
    mylist = df['Type'].tolist()
    slices = df['Emission'].tolist()

    show_plot(mylist, slices)

    lbl_df.config(text=df)
    # lbl_ml.config(text=mylist)

tk.Label(root, text="Enter the number of CO2 emissions : ").grid(row=0, column=0)

parts = tk.Entry(root)
parts.grid(row=1, column=0)

tk.Button(root, text="Submit", command=get_emissions_input).grid(row=2, column=0)

lbl_df = tk.Label(root, text="")
lbl_df.grid(row=3, column=0)
# lbl_ml = tk.Label(root, text="")
# lbl_ml.grid(row=4, column=0)

root.mainloop()