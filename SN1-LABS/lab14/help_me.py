import os
prog_dir = os.path.dirname(__file__) #get the path of this, current, file
initial_wdir = os.getcwd() #get the working directory of the Python interpreter
print("Python is operating from:\n{:^120s}".format(initial_wdir))
print("The current program lives in:\n{:^120s}".format(prog_dir))
print('''*These paths should be the same, if not, we need to change python's working directory to the location of the program.''')
print()

# If they differ, change change directory: go into the programs folder. 
if prog_dir != initial_wdir:
    print("The paths are not the same, so changing python working directory to the program directory")
    os.chdir(prog_dir) # change directory to that location
    print()
else: # otherwise, we're good!
    print("The paths are the same!")
