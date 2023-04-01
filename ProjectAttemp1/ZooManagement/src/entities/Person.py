class Person():
    def __init__(self):
        pass

    def set_person_info(self, fullname, street, city, zipcode, us_state, dob):
        self.fullname = fullname
        self.street = street
        self.city = city
        self.zipcode = zipcode
        self.us_state = us_state
        self.dob = dob

    def set_more_info(self):
        pass

class Visitor(Person):
    def __init__(self):
        super().__init__()

    def set_more_info(self, ticket_num, ticket_type, visit_date, visitor_fullname):
        self.ticket_num = ticket_num
        self.ticket_type = ticket_type
        self.visit_date = visit_date
        self.visitor_fullname = visitor_fullname


class Employee(Person):
    def __init__(self):
        super().__init__()

    def set_more_info(self,id, hire_date, type, fullname):
        self.id = id
        self.hire_date = hire_date
        self.type = type
        self.fullname = fullname

    def set_employee_info(self):
        pass

class Zookeeper(Employee):
    def __init__(self):
        super().__init__()

    def set_employee_info(self, keeper_id, zemp_id, zskills):
        self.keeper_id = keeper_id
        self.zemp_id = zemp_id
        self.zskills = zskills

class Ostaff(Employee):
    def __init__(self):
        super().__init__()
    
    def set_employee_info(self, id, desk_num, department, oemp_id):
        self.id = id
        self.desk_num = desk_num
        self.department = department
        self.oemp_id = oemp_id

