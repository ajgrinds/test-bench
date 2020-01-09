import datetime
# times any functions in the local scope. Make multiple functions to compare times and find speed


for local_var in list(locals()):
    if not local_var.startswith('__') and local_var != 'datetime':
        time1 = datetime.datetime.now()
        eval(f'{local_var}()')
        time2 = datetime.datetime.now()
        print(f"{local_var} took {time2 - time1}")
