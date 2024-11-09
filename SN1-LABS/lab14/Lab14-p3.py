employee=['Bob','Helen','Joanne','Robert','Sam','Stephanie','Steve','Helen']
salary=[80000,56000,67300,105000,69100,70230,81500,40000]
status=['full-time','temporary','part-time','executive','study-leave',
        'maternity-leave','full-time','part-time']
vac_pay=[4.0,4.25,5.5,4.75,3.6,4.9,4.5,5.25]
for i in range(len(employee)):
    print(f"{employee[i]:10}{salary[i]:9}{vac_pay[i]:6.2f}  {status[i]}")
