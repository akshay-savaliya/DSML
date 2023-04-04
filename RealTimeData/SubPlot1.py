import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

data = pd.read_csv('plotdata.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

plt.plot(ages, dev_salaries, color='#444444', linestyle='--', label='All Devs')
plt.plot(ages, py_salaries, label='Python')
plt.plot(ages, js_salaries, label='JavaScript')

plt.legend()
plt.title('Median Salary by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary')

plt.tight_layout()
plt.show()