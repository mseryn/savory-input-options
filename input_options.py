#!/usr/bin/python3

#***
#* SET OF FUNCTIONS TO DEAL WITH STANDARD INPUTS
#* Melanie Cornelius
#*
#* LICENSE: (fill later)
#*
#* Author's Note:
#*      This was made because I used similar functionality in code >2 times,
#*      so per personal rules, it's now a script.
#***

# MAKING CLASS
class input_set:
    def __init__(self, set_contents, set_name_str, group_set = None):
        self.content = set_contents
        self.name_str = set_name_str

    def contains(self, input_str):
        for e in self.content:
            if input_str == e:
                return True
            else:
                return False

#    def set_group_membership(self, set_group=group_name):
#        group_name.add_element(self)






# MAKING SET CONTENT

# Affirmation

YES = ('yes', 'y', '1', 'true', 'yep')
NO = ('no', 'n', '0', 'false', 'nope')

# Numbers
ZERO = ('0', 'zero', 'o')
ONE = ('1', 'one', 'on')
TWO = ('2', 'two', 'too', 'to', 'to')
THREE = ('3', 'three', 'tree', 'thee', 'thre')
FOUR = ('4', 'four', 'for', 'fou', 'fore')

# Halt commands
QUIT = ("q", "quit", "qiut")
CANCEL = ("c", "cancel", "cance;", "can", "enough already")
STOP = ("s", "stop", "st", "no more")

# MASTER SETS
MASTER = (YES, NO, ZERO, ONE, TWO, THREE, FOUR, QUIT, CANCEL, STOP)
AFFERMATION = (YES, NO)
HALT_CMDS = (QUIT, CANCEL, STOP)


# MAKING SET CLASSES

yes = input_set(YES, "yes")
no = input_set(NO, "no")

quit = input_set(QUIT, "quit")
cancel = input_set(CANCEL, "cancel")
stop = input_set(STOP, "stop")





# MAKING SET GROUPS
# Not working yet, ask Zack about passing around classes
#master = set_group("master")
#affermation = set_group("affirmation")
#halt_command = set_group("halt_command")






# CALLABLES

def in_any(input_str, return_subset_name = 1):
    pass

def yes_or_no(input_str):
    for e in yes.content:
        if input_str == e:
            return 1
    for e in no.content:
        if input_str == e:
            return 0
    return None

if __name__ == '__main__':
    print("In main. Debugging...")
    str = "no"
    bo = yes_or_no(str)
    print(bo)
    
