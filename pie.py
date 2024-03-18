# Use this libaray to implement Pie chart/graphs
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import random
import numpy as np
import sqlite3

# Python program to create
# a pdf file
from fpdf import FPDF

import Emission as Emission


#TODO : 1) Protect the input of numbers 
#       2) protect the input from accepting negative numbers
#       3) Concatnate text in python
#       4) Write the report of the final project
#       5) finish 5-10 types of CO2 emissions
#       6) Try to seperate text report
#       7) Make readme file for Github

def zerolistmaker(n):
    listofzeros = [0] * n
    return listofzeros

# This function is to create a random color hex code
def random_color():
    return "#{}{}{}{}{}{}".format(*(random.choice("0123456789abcdef") for _ in range(6)))

def show_plot(activities,slices):
     # color for each label
     colors = [random_color() for _ in range(len(activities))]
     # colors = ['r', 'y','g', 'b'] #todo: add random colors to match actvities list

     explode = zerolistmaker(len(activities))
     
     # plotting the pie chart
     plt.pie(slices, labels = activities, colors=colors, 
          startangle=90, shadow = True, explode = explode,
          radius = 1.2,pctdistance=0.85, autopct = '%1.0f%%')
               # radius = 1.2,pctdistance=0.85, autopct = '%1.1f%%')

     
     # plotting legend
     plt.legend()
     
     #draw circle
     centre_circle = plt.Circle((0,0),0.90,fc='white')
     fig = plt.gcf()
     fig.gca().add_artist(centre_circle)
     #fig.suptitle = "Emission Report Graph"

     # Equal aspect ratio ensures that pie is drawn as a circle
     plt.axis('equal')  
     plt.tight_layout()

     axes = plt.axes([0.81, 0.000001, 0.1, 0.075])
     bnext = Button(axes, 'Create',color="grey")
     bnext.on_clicked(show_report(activities))

     # showing the plot
     plt.show()
 
def show_report(activties, **kwargs):
    # save FPDF() class into a 
    # variable pdf
    pdf = FPDF()
 
    # Add a page
    pdf.add_page()
 
    # set style and size of font 
    # that you want in the pdf
    pdf.set_font("Arial", size = 15)
 
    # create a cell
    pdf.cell(200, 10, txt = "Emission Report", 
         ln = 1, align = 'C')
 
    #Get Emission Data from DB
    connection = sqlite3.connect('emissions.db')
    cursor = connection.cursor()

    all_emissions = cursor.execute('Select * from emission')
    data = all_emissions.fetchall()
    print(data)
    emission_list = []
    for e in data:
     print(e)
     emission_list.append(Emission.Emission(*e))
       
    # add another cell
     print("sdyufigdfods",emission_list)
    text = ""
    for activity in activties:
     print(activity)
     for emiss in emission_list:
            print(f"fdgfdgdf {emiss.name.lower()} ksdyhfuisd564675 {activity.lower()}")
            if(emiss.name.lower() == activity.lower()):
                text = "\n \n"
                text += emiss.emission_reduction_tips
                
     #continue
#     if any("car" in s for s in activties):
#         text = " This comprehensive report examines the critical issue of CO2 emissions from automobiles, a significant contributor to global greenhouse gas emissions. With transportation being a major source of CO2 emissions worldwide, understanding the environmental impact of different types of vehicles is crucial for developing effective strategies to mitigate climate change.\
#         \n\n- Recommendations: \n \
#         Encourage the adoption of EVs through incentives and infrastructure development.\
#         \n- Promote hybrid vehicles as a transitional solution for those unable to switch to EVs immediately.\
#         \n- Implement stricter emissions standards and promote fuel-efficient technologies to reduce CO2 emissions from gasoline vehicles.\
#         \
#         \n\n- Conclusion: Transitioning to EVs and promoting cleaner transportation technologies is crucial for mitigating the environmental impact of car emissions and combating climate change."
                        
     
     pdf.multi_cell(200, 10, txt = f"{text}",align = 'L')
    # save the pdf with name .pdf
    pdf.output("emission_report.pdf")   

 
