# Creating variables for the task
red_light = []
yellow_light = []
green_light = []
active_time = []
time = []

# The path where the given data file is found. It may vary for every user.
path = "YOUR_PATH_TO_DIRECTORY_OF_THE_FILE"

# Calculating the occurances
def Occurances(data):
    occurace = 0
    for i in range(0, len(data)):
        if data[i] == "1":
            occurace = occurace + 1
    return occurace

# Calculating the active time of the light
def Time_Active(light, active_time):
    time_active = 0
    for i in range(0, len(light)):
        if light[i] == "1":
            time_active = time_active + int(active_time[i])
    return time_active

# Finding times of the light
def Finding_the_times(light, time):
    active_times = []
    for i in range(0, len(light)):
        if light[i] == "1":
            active_times.append(time[i])
    return active_times

# Finding the cycles
def Finding_full_cycles(light1, light2, light3):
    # If there would be no mistakes in the data, we could just count the number of green signals and it would be the cycle number.
    # But now, because there are mistakes in the data we need to check the sequence Red-Yellow-Green-Yellow-Red as it is.
    cycles = 0
    for i in range(0, len(light1) - 4, 4):
        if light1[i] == "1" and light2[i+1] == "1" and light3[i+2] == "1" and light2[i+3] == "1" and light1[i+4] == "1":
            cycles = cycles + 1
    return cycles

# Finding the mistakes in rows
def Finding_mistakes(light1, light2, light3):
    mistake_line = []
    # Checking for all of the mistake conditions in the file
    for i in range(0, len(light1)):
        if light1[i] == "1" and light2[i] == "1":
            mistake_line.append(i)
        elif light1[i] == "1" and light3[i] == "1":
            mistake_line.append(i)
        elif light2[i] == "1" and light3[i] == "1":
            mistake_line.append(i)
        elif light1[i] == "1" and light2[i] == "1" and light3[i] == "1":
            mistake_line.append(i)
        elif light1[i] == "0" and light2[i] == "0" and light3[i] == "0":
            mistake_line.append(i)
        else:
            continue
    # If there are mistakes, return all of the indexesof mistaken rows
    if len(mistake_line) > 0:
        return mistake_line
    # If there is no mistake in file, return 0
    else:
        return 0

# If the file is found do all of the tasks
try:
    # Reading the given file
    with open(f"{path}data.txt", "r") as filestream:
        # Skipping the header row
        next(filestream)
        for line in filestream:
            # Separating the data
            currentline = line.split(",")
            # Assign data to the variables
            red_light.append(currentline[0])
            yellow_light.append(currentline[1])
            green_light.append(currentline[2])
            active_time.append(currentline[3])
            time.append(currentline[4].rsplit("\n")[0])
    
    # Task 1. Find the number of red, yellow & green occurrences.

    print(f"Red light occurances: {Occurances(red_light)}\n")
    print(f"Yellow light occurances: {Occurances(yellow_light)}\n")
    print(f"Green light occurances: {Occurances(green_light)}\n")

    # Task 2. Find how long each colour was active for.

    print(f"Red light active time: {Time_Active(red_light, active_time)} seconds\n")
    print(f"Yellow light active time: {Time_Active(yellow_light, active_time)} seconds\n")
    print(f"Green light active time: {Time_Active(green_light, active_time)} seconds\n")

    # Task 3. Find all times when Green was active (by time)

    print(f"Green light active times: {Finding_the_times(green_light, time)}\n")

    # Task 4. Find the number of complete cycles Red-Yellow-Green-Yellow-Red in the data

    print(f"Full cycles in the data: {Finding_full_cycles(red_light, yellow_light, green_light)}\n")

    # Task 5. Find number of lines with mistakes (multiple colours active at the same time or no colours active)

    print(f"Number of lines with mistakes: {Finding_mistakes(red_light, yellow_light, green_light)}\n") 

# If there is no such file, print this error
except Exception as FileExistsError:
    print("There is no such file!")