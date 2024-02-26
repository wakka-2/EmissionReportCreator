# Use this libaray to implement Pie chart/graphs
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import random

# Python program to create
# a pdf file
from fpdf import FPDF

def random_color():
    return "#{}{}{}{}{}{}".format(*(random.choice("0123456789abcdef") for _ in range(6)))

def show_plot(activities,slices):
        
     # color for each label
     colors = [random_color() for _ in range(len(activities))]
     # colors = ['r', 'y','g', 'b'] #todo: add random colors to match actvities list
     
     # plotting the pie chart
     plt.pie(slices, labels = activities, colors=colors, 
          startangle=90, shadow = True, explode = (0, 0.1,0), #add explode to match (make it dynamic)
          radius = 1.2,pctdistance=0.85, autopct = '%1.0f%%')
               # radius = 1.2,pctdistance=0.85, autopct = '%1.1f%%')

     
     # plotting legend
     plt.legend()
     
     #draw circle
     centre_circle = plt.Circle((0,0),0.90,fc='white')
     fig = plt.gcf()
     fig.gca().add_artist(centre_circle)

     # Equal aspect ratio ensures that pie is drawn as a circle
     plt.axis('equal')  
     plt.tight_layout()

     axes = plt.axes([0.81, 0.000001, 0.1, 0.075])
     bnext = Button(axes, 'Create',color="grey")
     bnext.on_clicked(show_report)

     # showing the plot
     plt.show()
 
def show_report(*args, **kwargs):
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
 
    # add another cell
     
    pdf.cell(200, 10, txt = f"Here we will create the pdf report {TYPE1} blah blah blah blah blah blah",
         ln = 2, align = 'L')
 
    # save the pdf with name .pdf
    pdf.output("emission_report.pdf")   

 
