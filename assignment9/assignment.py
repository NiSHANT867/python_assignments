class user_defined_exception(Exception):
    def __init__(self,arg):
        self.arg = arg

import maths_operation as n

try:
    raise user_defined_exception("User defined exception")
except user_defined_exception as u:
    print(u.arg)
obj = n.math_operation(10,40)
obj.power()
obj.trigno()
obj.basic()
obj.rest()