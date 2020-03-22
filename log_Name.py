import logging

logging.basicConfig(filename='employee.log',level=logging.INFO,format='%(levelname)s:%(message)s')

class employee:
    """A sample employee calss"""

    def __init__(self,first,last):
        self.first = first
        self.last = last
        logging.info('Create Employee: {} - {}'.format(self.fullname,self.email))

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first,self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

emp_1 = employee('jhon','smoith')
emp_2 = employee('ibrahim','muzzammil')