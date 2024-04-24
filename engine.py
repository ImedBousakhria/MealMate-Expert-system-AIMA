from aima.logic import *
from util import map_budget_to_predicate

def inference_engine(kb, user_profile):
    current_user = user_profile["Name"]
    agenda = []
    agenda.append(expr(f"User({user_profile['Name']})"))
    for allergy in user_profile['Allergies']:
        agenda.append(expr(f"AllergicTo({user_profile['Name']}, {allergy})"))
        kb.tell(expr(f"AllergicTo({user_profile['Name']}, {allergy})"))
    agenda.append(expr(f"DietaryPreference({user_profile['Name']}, {user_profile['DietaryPreference']})"))
    agenda.append(expr(f"Goal({user_profile['Name']}, {user_profile['Goal']})"))
    agenda.append(expr(f"ActivityLevel({user_profile['Name']}, {user_profile['ActivityLevel']})"))
    agenda.append(expr(f"MealTypePref({user_profile['Name']}, {user_profile['MealTypePref']})"))
    
    
    kb.tell(expr(f"MealTypePref({user_profile['Name']}, {user_profile['MealTypePref']})"))
    kb.tell(expr(f"User({user_profile['Name']})"))
    kb.tell(expr(f"DietaryPreference({user_profile['Name']}, {user_profile['DietaryPreference']})"))
    kb.tell(expr(f"Goal({user_profile['Name']}, {user_profile['Goal']})"))
    kb.tell(expr(f"ActivityLevel({user_profile['Name']}, {user_profile['ActivityLevel']})"))


    if user_profile["Budget"]:
        map_budget_to_predicate(kb, user_profile["Name"], user_profile["Budget"], agenda)
        
    memory = {}
    seen = set() 
    while agenda:
        p = agenda.pop(0)
        if p in seen:
            continue 
        seen.add(p)
        if p == expr(f"FinalMeal(x, {current_user})") or p == expr(f"Recommend(x, {current_user})"):
            final_recommendations = list(fol_fc_ask(kb, p))
        if fol_fc_ask(kb, p):
            print(f'{p} is true.')
            memory[p] = True
        else:
            print(f'{p} is false.')
            memory[p] = False
            
        if memory.get(expr(f"LowBudget({current_user})"), True) and fol_fc_ask(kb, expr("LowBudget(x)")):
            agenda.append(expr(f"FinalMeal(x, {current_user})"))
        
        if memory.get(expr(f"AllergicTo({current_user}, Gluten)"), True) and fol_fc_ask(kb, expr("GlutenFree(x)")) or \
            memory.get(expr(f"MediumBudget({current_user})"), True) and fol_fc_ask(kb, expr("MediumBudget(x)")) or \
                memory.get(expr(f"HighBudget({current_user})"), True) and fol_fc_ask(kb, expr("HighBudget(x)")):
            agenda.append(expr(f"Recommend(x, {current_user})"))
            
        if memory.get(expr(f'ActivityLevel({current_user}, Sedentary)'), True) and fol_fc_ask(kb, expr('Breakfast(x)')) or\
            memory.get(expr(f'ActivityLevel({current_user}, Sedentary)'), True) and fol_fc_ask(kb, expr('Lunch(x)')) or\
                memory.get(expr(f'ActivityLevel({current_user}, Sedentary)'), True) and fol_fc_ask(kb, expr('Dinner(x)')) :
                    agenda.append(expr(f"FinalMeal(x, {current_user})"))
                    
        if memory.get(expr(f'ActivityLevel({current_user}, ExtremelyActive)'), True) and fol_fc_ask(kb, expr('HighCalorie(x)')) or\
            memory.get(expr(f'ActivityLevel({current_user}, ExtremelyActive)'), True) and fol_fc_ask(kb, expr('PostWorkout(x)')) or\
                memory.get(expr(f'ActivityLevel({current_user}, ExtremelyActive)'), True) and fol_fc_ask(kb, expr('PreWorkout(x)')) :
                    agenda.append(expr(f"FinalMeal(x, {current_user})"))
            
    return [memory, final_recommendations]

