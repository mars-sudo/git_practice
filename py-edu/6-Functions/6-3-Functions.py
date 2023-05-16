# You can go a step further by storing your functions in a separate file called a module
# then importing that module into your main program. 
# An import statement tells Python to make the code in a module available in the
# currently running program file. 

# All import statements should be written at the beginning of the file. 

import user_profile as up

profile = up.build_profile('nelson','mandela',location='africa',field='politics')
print(profile)

# module_name.function_name() - this is used to call the function

# from module_name import function_name - this is used to import a specific functions
# from module_name import function_0, function_1, function_2


###################################################################
# Styling Functions
# Functions should have descriptinve names, and these names should use lowercase letters and underscores

# Every functions should have a comment that explains concisely what the function does

# def function_name(value_0, parameter_1='value')

# def function_name(
#                   parameter_0, parameter_1,
#                   parameter_2, parameter3  ):
#       function body