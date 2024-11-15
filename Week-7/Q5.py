import csv

departments = {}
with open('Week-7/department.csv', mode='r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    for row in reader:
        DID, DName, DLocation = row
        departments[DID] = {'DName': DName, 'DLocation': DLocation, 'TotalSalary': 0, 'EmployeeCount': 0}

with open('Week-7/employees.csv', mode='r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    for row in reader:
        Name, EId, Salary, DID = row
        Salary = float(Salary)
        if DID in departments:
            departments[DID]['TotalSalary'] += Salary
            departments[DID]['EmployeeCount'] += 1

for DID, data in departments.items():
    if data['EmployeeCount'] > 0:
        average_salary = data['TotalSalary'] / data['EmployeeCount']
        print(f"Department: {data['DName']}, Location: {data['DLocation']}, Average Salary: {average_salary:.2f}")
    else:
        print(f"Department: {data['DName']}, Location: {data['DLocation']}, Average Salary: N/A")
