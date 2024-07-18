from datetime import datetime
class Employee:
    def __init__(self, fname, lname, dept, employee_id, age,address,doj) -> None:
        self.fname = fname
        self.lname = lname 
        self.dept = dept
        self.employee_id = employee_id
        self.age = age
        self.address = address
        self.doj = doj

    def number_of_years(self):
        years = datetime.now().year - self.doj
        return years


class Manager(Employee):
    def __init__(self, fname, lname, dept, employee_id, age, address, team_name, project_name,doj) -> None:
        super().__init__(fname, lname, dept, employee_id, age, address,doj)

        self.team_name = team_name
        self.project_name = project_name

    
employee1 = Manager('Ashish', 'Prabhu', 'data lake', 'WDA-3742', '40', 'home1', 'neucleo', 'datacleaning1', 2010)

print(employee1.number_of_years())

print(employee1.__dict__)

