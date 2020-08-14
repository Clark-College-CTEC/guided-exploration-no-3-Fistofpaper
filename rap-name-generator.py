# Guided Exploration No. 3
# Damon Kaiser
#
# Random library required for random number generation
import random
# Create list to store the rap names
possible_names = []
# Open new file for those names to be stored to
outputFile = open('rap-names-output.txt', 'w')
# Open text file as read only and assign as variable
with open('rap-names.txt', 'r') as dataFile:
    # Begin for loop on data in opened file
    for name in dataFile:
        # remove possible line feeds from data and append to list
        possible_names.append(name.rstrip())
# Request user input for how many names to create
count = int(input('How many rap names would you like to create? '))
# Request user input for how many parts to each name
parts = int(input('How many parts should the name contain? '))
# Begin for loop to iterate the number of full names requested
for i in range(count):
    # Create list to hold name parts
    name_parts = []
    # Begin for loop to iterate the number of parts per name requested
    for j in range(parts):
        # Randomly select name parts from possible names list and append to name parts list
        name_parts.append(
            possible_names[random.randint(0, len(possible_names)-1)])
    # Join the name parts list together with a space delimiter and send to the outputFile variable
    outputFile.write(f"{' '.join(name_parts)}\n")
    # Print the results sent to the file in the terminal
    print(f"{' '.join(name_parts)}")
# Close the output file and end program after line 21 completes looping
outputFile.close()
