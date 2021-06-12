import pandas as pd
import numpy  as np
import uuid
from tkinter.filedialog import askopenfilename

#Retrieving the csv file
flat_data = askopenfilename()

#Reads the csv file 
flat_data = pd.read_csv (flat_data)
flat_data[["salary", "salary_incremen"]] = flat_data[["salary", "salary_incremen"]].apply(pd.to_numeric)

employees = flat_data[['first_name','last_name','salary']]

#Function that creates Unique ID's 
def IDs():
    global a
    a = []
    for i in range(len(employees.index)):
        a.append(i)
        a[i] = str(uuid.uuid4().fields[-1])[:5]
    return a

#adding id and department_id col to employees
IDs()
employees['id'] = a
IDs()
employees['department_id'] = a

#creating department dataset
department = employees[['department_id']]
dept_name = flat_data['dept_name'].tolist()
salary_increment = flat_data['salary_incremen'].tolist()
department['name'] = dept_name
department['salary_increment'] = salary_increment

#creating updated salary

updated_salaries = employees.merge(department, left_on='department_id', right_on='department_id')

updated_salaries['updated_salary'] = updated_salaries['salary'] * (1 + (updated_salaries['salary_increment']/100)) 

updated_salaries = updated_salaries[['id','updated_salary']]
                                        
