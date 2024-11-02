import pandas as pd
employee_df = pd.read_csv('Week-10\employees.csv')
department_df = pd.read_csv('Week-10\departments.csv')

merged_df = pd.merge(employee_df, department_df, on='DID', how='inner')

merged_df = merged_df.rename(columns={
    'Name': 'Ename',
    'EId': 'Eid',
    'Salary': 'Esalary',
    'DID': 'EDID',
    'DName': 'DName',
    'DLocation': 'DLocation'
})

print(merged_df)
merged_df.to_csv('Emp_Dep.csv', index=False)
