import tkinter as tk

# Life expectancy values listed 
values = [63.28, 65.26, 62.14, 57.61, 52.92, 48.50, 44.29, 40.02,
          35.72, 31.32, 27.13, 23.07, 19.31, 15.71, 12.54, 9.88, 7.92, 7.40]

# Assigning a variable to each age group by indexing
exp_0     = values[0]   # age 0
exp_1_4   = values[1]   # age 1-4
exp_5_9   = values[2]   # age 5-9
exp_10_14 = values[3]   # age 10-14
exp_15_19 = values[4]   # age 15-19
exp_20_24 = values[5]   # age 20-24
exp_25_29 = values[6]   # age 25-29
exp_30_34 = values[7]   # age 30-34
exp_35_39 = values[8]   # age 35-39
exp_40_44 = values[9]   # age 40-44
exp_45_49 = values[10]  # age 45-49
exp_50_54 = values[11]  # age 50-54
exp_55_59 = values[12]  # age 55-59
exp_60_64 = values[13]  # age 60-64
exp_65_69 = values[14]  # age 65-69
exp_70_74 = values[15]  # age 70-74
exp_75_79 = values[16]  # age 75-79
exp_80    = values[17]  # age 80+

# Create the main window
root = tk.Tk()
root.title("Life Expectancy Calculator")
root.geometry("400x250")

# Title label
tk.Label(root, text="LIFE EXPECTANCY CALCULATOR", font=("Arial", 14, "bold")).pack(pady=15)

# Age input label
tk.Label(root, text="Enter your age:", font=("Arial", 11)).pack()

# Age input box
age_entry = tk.Entry(root, font=("Arial", 11), justify="center")
age_entry.pack(pady=5)

# Result label starts empty, updates in the same window
result_label = tk.Label(root, text="", font=("Arial", 11), fg="green", wraplength=350)
result_label.pack(pady=15)

# Function that runs when the button is clicked
def calculate():
    age_input = age_entry.get().strip()

    if not age_input.isdigit():
        result_label.config(text="Please enter a valid whole number.", fg="red")

    else:
        age = int(age_input)

        if age == 0:
            result = f"You have a life expectancy of {exp_0} more years."
        elif 1 <= age <= 4:
            result = f"You have a life expectancy of {exp_1_4} more years."
        elif 5 <= age <= 9:
            result = f"You have a life expectancy of {exp_5_9} more years."
        elif 10 <= age <= 14:
            result = f"You have a life expectancy of {exp_10_14} more years."
        elif 15 <= age <= 19:
            result = f"You have a life expectancy of {exp_15_19} more years."
        elif 20 <= age <= 24:
            result = f"You have a life expectancy of {exp_20_24} more years."
        elif 25 <= age <= 29:
            result = f"You have a life expectancy of {exp_25_29} more years."
        elif 30 <= age <= 34:
            result = f"You have a life expectancy of {exp_30_34} more years."
        elif 35 <= age <= 39:
            result = f"You have a life expectancy of {exp_35_39} more years."
        elif 40 <= age <= 44:
            result = f"You have a life expectancy of {exp_40_44} more years."
        elif 45 <= age <= 49:
            result = f"You have a life expectancy of {exp_45_49} more years."
        elif 50 <= age <= 54:
            result = f"You have a life expectancy of {exp_50_54} more years."
        elif 55 <= age <= 59:
            result = f"You have a life expectancy of {exp_55_59} more years."
        elif 60 <= age <= 64:
            result = f"You have a life expectancy of {exp_60_64} more years."
        elif 65 <= age <= 69:
            result = f"You have a life expectancy of {exp_65_69} more years."
        elif 70 <= age <= 74:
            result = f"You have a life expectancy of {exp_70_74} more years."
        elif 75 <= age <= 79:
            result = f"You have a life expectancy of {exp_75_79} more years."
        else:
            result = f"You have a life expectancy of {exp_80} more years."

        result_label.config(text=result, fg="green")

# Calculate button
tk.Button(root, text="Calculate", font=("Arial", 11), command=calculate).pack()

# Keep the window open
root.mainloop()
