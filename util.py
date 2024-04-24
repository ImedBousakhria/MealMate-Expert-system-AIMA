from aima.logic import *

def map_budget_to_predicate(kb, user, user_input, agenda):
    if user_input < 50:
        agenda.append(expr(f"LowBudget({user})"))
        # kb.tell(expr(f"LowBudget({user})"))
    elif 50 <= user_input <= 100:
        agenda.append(expr(f"MediumBudget({user})"))
        # kb.tell(expr(f"MediumBudget({user})"))

    else:
        agenda.append(expr(f"HighBudget({user})"))
        # kb.tell(expr(f"HighBudget({user})"))
