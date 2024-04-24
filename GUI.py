import tkinter as tk
from tkinter import ttk
from kb import kb
from engine import inference_engine
from aima.logic import *

def submit():
    user_profile = {
        "Name": name_entry.get().title(),
        "Allergies": [allergies_listbox.get(i) for i in allergies_listbox.curselection()],
        "DietaryPreference": preferences_var.get(),
        "Goal": goal_var.get() if goal_var.get() != "Not selected" else None,
        "ActivityLevel": activity_var.get() if activity_var.get() != "Not selected" else None,
        "MealTypePref": meal_type_var.get() if meal_type_var.get() != "Not selected" else None,
        "Budget": int(budget_entry.get()) if budget_entry.get() != "" else None
    }
    
    
    recommendations = inference_engine(kb, user_profile)
    memory = recommendations[0]
    meals = recommendations[1]
    for meal, value in memory.items():
        if value:
            print(f'{meal}')
            results_text.insert(tk.END, f"{meal}\n")
    
    results_text.insert(tk.END, f"Recommended Meals for {user_profile['Name']}:\n")
    for meal in meals:
        print(meal)
        results_text.insert(tk.END, f"{meal}\n")

root = tk.Tk()
root.geometry('600x600')

name_label = tk.Label(root, text="Name")
name_entry = tk.Entry(root)

allergies_label = tk.Label(root, text="Allergies (ctrl+click to select multiple)")
allergies_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, height=3)
allergies_listbox.insert(1, "Gluten")
allergies_listbox.insert(2, "Lactose")


preferences_label = tk.Label(root, text="Dietary Preferences")
preferences_var = tk.StringVar(root)
preferences_var.set("None")  # default value
preferences_option = ttk.Combobox(root, textvariable=preferences_var, values=["None", "Vegan", "Vegetarian"])


goal_label = tk.Label(root, text="Goal")
goal_var = tk.StringVar(root)
goal_var.set("Not selected")  # default value
goal_option = ttk.Combobox(root, textvariable=goal_var, values=["Not selected", "WeightLoss", "MuscleGain"])


activity_label = tk.Label(root, text="Activity Level")
activity_var = tk.StringVar(root)
activity_var.set("Not selected")  # default value
activity_option = ttk.Combobox(root, textvariable=activity_var, values=["Not selected", "Sedentary", "LightlyActive", "ModeratelyActive", "VeryActive", "ExtremelyActive"])


meal_type_label = tk.Label(root, text="Meal Type Preference")
meal_type_var = tk.StringVar(root)
meal_type_var.set("Not selected")  # default value
meal_type_option = ttk.Combobox(root, textvariable=meal_type_var, values=["Not selected", "Breakfast", "Lunch", "Dinner", "Snack"])


budget_label = tk.Label(root, text="Budget (in Algerian dinars)")
budget_entry = tk.Entry(root)

submit_button = tk.Button(root, text="Submit", command=submit)
results_text = tk.Text(root)  # Text widget to display the results

name_label.pack()
name_entry.pack()

allergies_label.pack()
allergies_listbox.pack()

preferences_label.pack()
preferences_option.pack()

goal_label.pack()
goal_option.pack()

activity_label.pack()
activity_option.pack()

meal_type_label.pack()
meal_type_option.pack()

budget_label.pack()
budget_entry.pack()

submit_button.pack()
results_text.pack()

root.mainloop()
