import sqlite3


#Create instance of emissions database using this line (*PS : to be executed only once)
connection = sqlite3.connect('emissions.db')

cursor = connection.cursor()

#Create a table that has common emissions (*PS : to be executed only once)
cursor.execute("""CREATE TABLE emission (
               id INTEGER PRIMARY KEY,
               name TEXT,
               emission_reduction_tips VARCHAR(1000)
) """)

#Insert a row to our database (Single value)
# cursor.execute("INSERT INTO emission VALUES('1','Cars',' This comprehensive report examines the critical issue of CO2 emissions from automobiles, a significant contributor to global greenhouse gas emissions. With transportation being a major source of CO2 emissions worldwide, understanding the environmental impact of different types of vehicles is crucial for developing effective strategies to mitigate climate change.\
#         \n\n- Recommendations: \n \
#         Encourage the adoption of EVs through incentives and infrastructure development.\
#         \n- Promote hybrid vehicles as a transitional solution for those unable to switch to EVs immediately.\
#         \n- Implement stricter emissions standards and promote fuel-efficient technologies to reduce CO2 emissions from gasoline vehicles.\
#         \
#         \n\n- Conclusion: Transitioning to EVs and promoting cleaner transportation technologies is crucial for mitigating the environmental impact of car emissions and combating climate change.')")

#Insert a row to our database (multiple value)
all_emissions = [
    ('1','Cars','This comprehensive report examines the critical issue of CO2 emissions from automobiles, a significant contributor to global greenhouse gas emissions. With transportation being a major source of CO2 emissions worldwide, understanding the environmental impact of different types of vehicles is crucial for developing effective strategies to mitigate climate change.\
        \n\n- Recommendations: \n- Encourage the adoption of EVs through incentives and infrastructure development.\
        \n- Promote hybrid vehicles as a transitional solution for those unable to switch to EVs immediately.\
        \n- Implement stricter emissions standards and promote fuel-efficient technologies to reduce CO2 emissions from gasoline vehicles.\
        \
        \n\n- Conclusion: Transitioning to EVs and promoting cleaner transportation technologies is crucial for mitigating the environmental impact of car emissions and combating climate change.')
        ,#Seprator
        ('2','Boats','Since April 2019, ships have been required to submit verified data on CO2 emissions to the European Commission, which will publish the information from June 2019 onwards accompanied by ship and company identifiers.\
        \n\n- Recommendations: \n- Encourage the adoption of hybrid and electric boat technologies.\
        \n- Invest in infrastructure for electric boat charging stations.\
        \n- Implement regulations to limit CO2 emissions from marine vessels.\
        \
        \n\n- Conclusion: Transitioning to hybrid and electric boats is essential for reducing CO2 emissions from maritime transport and mitigating the environmental impact on marine ecosystems.')
        ,#Seprator
        ('3','Airplanes','Commercial airplanes emit significant amounts of CO2 during flight, contributing to climate change.\
        \n\n- Recommendations: \n- Invest in research and development of sustainable aviation fuels (SAFs) to reduce the carbon intensity of air travel.\
        \n- Implement carbon pricing mechanisms or emissions trading schemes to incentivize emissions reductions within the aviation sector.\
        \n- Encourage the adoption of more fuel-efficient aircraft and operational practices to minimize CO2 emissions.\
        \
        \n\n- Conclusion: Addressing CO2 emissions from airplanes is crucial for mitigating climate change. Collaboration among industry stakeholders, policymakers, and researchers is essential to develop and implement sustainable solutions that balance environmental concerns with the growing demand for air travel.')
        ,#Seprator
        ('4','Trains','This report evaluates the CO2 emissions associated with train transportation, an integral component of the global transit system.\
        \n\n- Recommendations: \n- Electrification: Promote the electrification of train systems to reduce reliance on diesel-powered locomotives and minimize CO2 emissions.\
        \n- Renewable Energy: Encourage the use of renewable energy sources such as solar and wind to power electric trains, further lowering their carbon footprint.\
        \n- Efficiency Improvements: Invest in technology and infrastructure upgrades to enhance the energy efficiency of train operations, thereby reducing overall CO2 emissions.\
        \
        \n\n- Conclusion: Transitioning to electric-powered trains and adopting renewable energy sources are vital steps in mitigating CO2 emissions from the rail transport sector. By prioritizing sustainability and efficiency, we can minimize the environmental impact of train travel and contribute to a greener future.')
        ,#Seprator
        ('5','Electricity','This report evaluates the CO2 emissions associated with electricity generation, highlighting its environmental impact and implications for climate change mitigation.\
        \n\n- Recommendations: \n- Transition to Renewable Energy: Promote the adoption of renewable energy sources such as solar and wind to reduce CO2 emissions from electricity generation.\
        \n- Invest in Carbon Capture and Storage (CCS): Implement CCS technologies to capture and store CO2 emissions from fossil fuel power plants, mitigating their environmental impact.\
        \n- Energy Efficiency Measures: Encourage energy efficiency initiatives to reduce overall electricity demand and emissions.\
        \
        \n\n- Conclusion: Shifting towards renewable energy sources and implementing carbon mitigation technologies are essential steps in reducing CO2 emissions from electricity generation, thereby mitigating climate change and fostering a sustainable energy future.')
]

connection.executemany("INSERT INTO emission VALUES (?,?,?)",all_emissions)

connection.commit()
connection.close()