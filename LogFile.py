import logging

logging.basicConfig(filename='test.log',level=logging.DEBUG,format='%(asctime)s:%(levelname)s:%(message)s')
def add (x,y):
    """Add fucntion"""
    return x + y

def sub(x,y):
    """Substraction function"""
    return x - y
def Multiply(x,y):
    """Multiply function"""
    return x * y

def divide(x,y):
    """Divide function"""
    return x / y

num_1 = 20
num_2 = 10

add_result = add(num_1,num_2)
logging.debug('Add : {}  + {}  = {}'.format(num_1,num_2, add_result))

sub_result = sub(num_1,num_2)
logging.info('Sub : {}  - {}  = {}'.format(num_1,num_2, sub_result))

Mul_result = Multiply(num_1,num_2)
logging.warning('Mul : {}  * {}  = {}'.format(num_1,num_2, Mul_result))

Divide_result = divide(num_1,num_2)
logging.warning('Div : {}  / {}  = {}'.format(num_1,num_2, Divide_result))
