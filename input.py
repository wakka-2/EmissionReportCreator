import tkinter as tk
import tkinter.simpledialog as simpledialog
import pandas as pd
from tkinter import messagebox
import matplotlib.pyplot as plt

from pie import show_plot


root = tk.Tk()

def validate_input(sp):
    try:
            try:
                int(sp)
            except ValueError:
                messagebox.showwarning("Illegal Value", "Not an integer.\nPlease try again.")
            assert int(sp) > 0
    except AssertionError:
            messagebox.showwarning("Illegal Value", "Only positive numbers.\nPlease try again.")

def get_emissions_input():
    avgElectercityBill = simpledialog.askstring("Data input window" , "What is your avg monthly electrcity bill in euros?" )
    validate_input(avgElectercityBill)
    avgNaturalBill = simpledialog.askstring("Data input window" , "What is your avg monthly natural gas bill in euros?" )
    validate_input(avgNaturalBill)
    avgFuelBill = simpledialog.askstring("Data input window" , "What is your avg monthly fuel bill for transportation in euros?" )
    validate_input(avgFuelBill)
    
    wasteInKG = simpledialog.askstring("Data input window" , "How much waste do you generate per month in kilograms?" )
    validate_input(wasteInKG)
    wasteRecycled = simpledialog.askstring("Data input window" , "How much of that waste is recycled or composted (in percentagre)?" )
    validate_input(wasteRecycled)

    kilometersTraveled = simpledialog.askstring("Data input window" , "How many kilometers do your employees travel per year for business purpose?" )
    avgFuelEffecincy = simpledialog.askstring("Data input window" , "What is the avg feul effecincy of the veichles used for business travel in liters per 100 kilometers?" )
    validate_input(avgFuelEffecincy)


    energyKGCO2 = (int(avgElectercityBill) * 12 * 0.0005) + (int(avgNaturalBill) * 12 + 0.00553) + (int(avgFuelBill) * 12 *2.32)
    wasteKGCO2 = (int(wasteInKG) * 12 * (0.57 - int(wasteRecycled)/100))
    businessTravelKGCO2 = int(kilometersTraveled) * (1/(int(avgFuelEffecincy) * 2.31))

    x = [energyKGCO2, wasteKGCO2, businessTravelKGCO2*100]
    labels = ['Energy KGCO2', 'Waste KGCO2', 'Business Travel KGCO2']

    fig, ax = plt.subplots()
    ax.pie(x, labels=labels, autopct='%.1f%%')
    ax.set_title('CO2 emission in KG')
    plt.tight_layout()

    # showing the plot
    plt.show()

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