from aima.logic import *

meals = [
    {"name": "GrilledChickenSalad", "attributes": {"GlutenFree": True, "HighProtein": True, "LowCalorie": True, "Lunch": True}, "cost": 10},
    {"name": "SalmonWithQuinoa", "attributes": {"GlutenFree": True, "DairyFree": True, "HighProtein": True, "LowCalorie": True, "Dinner": True}, "cost": 15},
    {"name": "ChtithaBatata", "attributes": {"GlutenFree": True, "Vegetarian": True, "Dinner": True}, "cost": 8},
    {"name": "ChorbaFrik", "attributes": {"HighProtein": True, "Dinner": True}, "cost": 12},
    {"name": "VegetableStirFry", "attributes": {"GlutenFree": True, "DairyFree": True, "LowCalorie": True, "Lunch": True}, "cost": 8},
    {"name": "Makrout", "attributes": {"HighCarb": True, "Breakfast": True}, "cost": 5},
    {"name": "Rechta", "attributes": {"LowCalorie": True, "Dinner": True}, "cost": 7},
    {"name": "Msemen", "attributes": {"HighFiber": True, "Snack": True}, "cost": 3},
    {"name": "PoissonGrille", "attributes": {"GlutenFree": True, "DairyFree": True, "Dinner": True}, "cost": 16},
    {"name": "SteakWithSweetPotatoes", "attributes": {"GlutenFree": True, "DairyFree": True, "HighProtein": True, "Dinner": True}, "cost": 18},
    {"name": "QuinoaSalad", "attributes": {"GlutenFree": True, "DairyFree": True, "LowCalorie": True, "Lunch": True}, "cost": 7},
    {"name": "Chakhchoukha", "attributes": {"HighProtein": True, "Dinner": True}, "cost": 14},
    {"name": "MediterraneanWrap", "attributes": {"GlutenFree": False, "DairyFree": True, "LowCalorie": True, "Lunch": True}, "cost": 12},
    {"name": "Mahjouba", "attributes": {"BudgetFriendly": True, "Snack": True}, "cost": 2},
    {"name": "Baghrir", "attributes": {"HighCarb": True, "Snack": True}, "cost": 4},
    {"name": "Granita", "attributes": {"Vegan": True, "LowCarb": True, "Snack": True}, "cost": 6},
    {"name": "Dolma", "attributes": {"Vegetarian": True, "Dinner": True}, "cost": 10},
    {"name": "Pastilla", "attributes": {"HighProtein": True, "Dinner": True}, "cost": 18},
    {"name": "ChickenSoup", "attributes": {"LowCalorie": True, "Dinner": True}, "cost": 9},
    {"name": "TofuStirFry", "attributes": {"GlutenFree": True, "DairyFree": True, "LowCalorie": True, "Lunch": True}, "cost": 10},
    {"name": "EggWhiteOmelette", "attributes": {"HighProtein": True, "LowCalorie": True, "Breakfast": True}, "cost": 6},
    {"name": "GreekSalad", "attributes": {"GlutenFree": True, "DairyFree": True, "Lunch": True}, "cost": 8},
    {"name": "TeriyakiSalmon", "attributes": {"GlutenFree": True, "DairyFree": True, "HighProtein": True, "Dinner": True}, "cost": 15},
    {"name": "QuinoaStuffedPeppers", "attributes": {"GlutenFree": True, "DairyFree": True, "HighFiber": True, "Lunch": True}, "cost": 12},
    {"name": "ChickenCaesarSalad", "attributes": {"GlutenFree": False, "DairyFree": False, "HighProtein": True, "LowCalorie": True, "Lunch": True}, "cost": 10},
]

kb = FolKB()

# facts
for meal in meals:
    kb.tell(expr(f"LowBudget({meal['name']})")) if meal['cost'] <= 10 else None
    kb.tell(expr(f"MediumBudget({meal['name']})")) if 10 < meal['cost'] <= 15 else None
    kb.tell(expr(f"HighBudget({meal['name']})")) if meal['cost'] > 15 else None
    kb.tell(expr(f"Meal({meal['name']})"))
    for attribute, value in meal['attributes'].items():
        kb.tell(expr(f"{attribute}({meal['name']})")) if value else None
    kb.tell(expr(f"Cost({meal['name']}, {meal['cost']})"))



# cost: first level
kb.tell(expr('LowBudget(p) & LowBudget(x) ==> BudgetFriendly(x, p)'))
kb.tell(expr('MediumBudget(p) & MediumBudget(x) ==> BudgetFriendly(x, p)'))
kb.tell(expr('HighBudget(p) & HighBudget(x) ==> BudgetFriendly(x, p)'))

# define budget as level one constraint
kb.tell(expr("Recommend(x, p) & BudgetFriendly(x, p) ==> FinalMeal(x, p)"))

# weight
kb.tell(expr('LowCalorie(x) & Goal(p, WeightLoss) ==> Recommend(x, p)'))
kb.tell(expr('HighProtein(x) & Goal(p, MuscleGain) ==> Recommend(x, p)'))

# allergy
kb.tell(expr('GlutenFree(x) & AllergicTo(p, Gluten) ==> Recommend(x, p)'))
kb.tell(expr('DairyFree(x) & AllergicTo(p, Lactose) ==> Recommend(x, p)'))

# style
kb.tell(expr('LowCarb(x) & DietaryPreference(p, LowCarb) ==> Recommend(x, p)'))
kb.tell(expr('HighFiber(x) & DietaryPreference(p, HighFiber) ==> Recommend(x, p)'))
kb.tell(expr('Mediterranean(x) & DietaryPreference(p, Mediterranean) ==> Recommend(x, p)'))
kb.tell(expr('Vegan(p) & DairyFree(x) & Vegetarian(x) ==> Recommend(x, p)'))
kb.tell(expr('Vegetarian(p) & Vegetarian(x) ==> Recommend(x, p)'))

# meal type
kb.tell(expr('Breakfast(x) & MealTypePref(p, Breakfast) ==> Recommend(x, p)'))
kb.tell(expr('Lunch(x) & MealTypePref(p, Lunch) ==> Recommend(x, p)'))
kb.tell(expr('Dinner(x) & MealTypePref(p, Dinner) ==> Recommend(x, p)'))

# activity level
# Sedentary
kb.tell(expr('ActivityLevel(p, Sedentary) & Breakfast(x) ==> Recommend(x, p)'))
kb.tell(expr('ActivityLevel(p, Sedentary) & Lunch(x) ==> Recommend(x, p)'))
kb.tell(expr('ActivityLevel(p, Sedentary) & Dinner(x) ==> Recommend(x, p)'))

# Lightly Active
kb.tell(expr('ActivityLevel(p, LightlyActive) & Snack(x) ==> Recommend(x, p)'))

# Moderately Active
kb.tell(expr('ActivityLevel(p, ModeratelyActive) & Snack(x) ==> Recommend(x, p)'))
kb.tell(expr('ActivityLevel(p, ModeratelyActive) & PreWorkout(x) ==> Recommend(x, p)'))

# Very Active
kb.tell(expr('ActivityLevel(p, VeryActive) & Snack(x) ==> Recommend(x, p)'))
kb.tell(expr('ActivityLevel(p, VeryActive) & PreWorkout(x) ==> Recommend(x, p)'))
kb.tell(expr('ActivityLevel(p, VeryActive) & PostWorkout(x) ==> Recommend(x, p)'))

# Extremely Active
kb.tell(expr('ActivityLevel(p, ExtremelyActive) & PostWorkout(x) ==> Recommend(x, p)'))
kb.tell(expr('ActivityLevel(p, ExtremelyActive) & HighCalorie(x) ==> Recommend(x, p)'))

