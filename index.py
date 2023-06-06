#Problem Statement Task-2
#With the same attachment, use each worksheet as a CSV file and write a script (Bash or Python) 
# that generates the same report. Data is to be read from the CSV files not from a database.



import csv
def generate_report(department_csv, employee_csv, salary_csv):    
        department_salaries = []
        # Calculate average salary for each department
        average_salaries = {}    
        
        for row in csv.DictReader(open(salary_csv)):
           emp_id = row['Emp_ID']        
           month = row['Month']
           amount = float(row['Amount'])        
           if emp_id not in average_salaries:
            average_salaries[emp_id] = {'total_salary': 0, 'total_months': 1}        
            average_salaries[emp_id]['total_salary'] += amount
            average_salaries[emp_id]['total_months'] += 1
        
        for emp_id, values in average_salaries.items():        
            average_salary = values['total_salary'] / values['total_months']
        average_salaries[emp_id] = average_salary
        departments = {}    
        
        for row in csv.DictReader(open(department_csv)):
          dept_id = row['Dept_ID']        
          dept_name = row['Dept_Name']
          departments[dept_id] = dept_name
          employees = {}    
          
        for row in csv.DictReader(open(employee_csv)):
          emp_id = row['Emp_ID']        
          dept_id = row['Dept_ID']
        if emp_id in average_salaries and dept_id in departments:
            if dept_id not in department_salaries:                
                department_salaries.append((departments[dept_id], average_salaries[emp_id]))
            else:                
                department_salaries[dept_id] += average_salaries[emp_id]
        department_salaries.sort(key=lambda x: x[1], reverse=True)
        
    # Select the top 3 departments
        top_3_departments = department_salaries[:3]
    # Print the report    
        print("DEPT_NAME")
        print("AVG_MONTHLY_SALARY (USD)")    
        print("")
        for department, average_salary in top_3_departments:        
          print(department)
          print(average_salary)        
          print()
        
# Specify the paths or names of the CSV files for departments, employees, and salaries
department_csv = "Departments.csv"
employee_csv = "Employees.csv"
salary_csv = "Salaries.csv"
generate_report(department_csv, employee_csv, salary_csv)