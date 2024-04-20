from aima.logic import *
from aima.utils import *

# Define the knowledge base
kb = FolKB()

# Add rules to the knowledge base
# Rules 1-25
# kb.tell(expr('Trendy(x) & Budget(x, "Low") ==> RecommendStatementEarrings(x)'))  # Rule 1
kb.tell(expr('Vintage(x) & Budget(x, "Moderate") ==> RecommendRetroDress(x)'))  # Rule 2
kb.tell(expr('Classic(x) & BodyType(x, "Tall") ==> RecommendTrenchCoat(x)'))  # Rule 3
kb.tell(expr('Eclectic(x) & Budget(x, "High") ==> RecommendMixedPrintDress(x)'))  # Rule 4
kb.tell(expr('Artsy(x) & Budget(x, "Moderate") ==> RecommendAbstractPrintTop(x)'))  # Rule 5
kb.tell(expr('Sporty(x) & Budget(x, "Low") ==> RecommendAthleticLeggings(x)'))  # Rule 6
kb.tell(expr('Elegant(x) & Budget(x, "High") ==> RecommendStructuredBlazer(x)'))  # Rule 7
kb.tell(expr('Romantic(x) & Budget(x, "Low") ==> RecommendFloralDress(x)'))  # Rule 8
kb.tell(expr('Preppy(x) & BodyType(x, "Petite") ==> RecommendALineSkirt(x)'))  # Rule 9
kb.tell(expr('Edgy(x) & Budget(x, "High") ==> RecommendLeatherJacket(x)'))  # Rule 10
kb.tell(expr('Minimalist(x) & Budget(x, "High") ==> RecommendStructuredBlazer(x)'))  # Rule 11
kb.tell(expr('Classic(x) & BodyType(x, "Tall") ==> RecommendTrenchCoat(x)'))  # Rule 12
kb.tell(expr('Eclectic(x) & Budget(x, "High") ==> RecommendMixedPrintDress(x)'))  # Rule 13
kb.tell(expr('Artsy(x) & Budget(x, "Moderate") ==> RecommendAbstractPrintTop(x)'))  # Rule 14
kb.tell(expr('Elegant(x) & Budget(x, "Low") ==> RecommendWrapDress(x)'))  # Rule 15
# kb.tell(expr('Trendy(x) & Budget(x, "Low") ==> RecommendStatementEarrings(x)'))  # Rule 16
kb.tell(expr('Vintage(x) & Budget(x, "Moderate") ==> RecommendRetroDress(x)'))  # Rule 17
kb.tell(expr('Classic(x) & BodyType(x, "Tall") ==> RecommendTrenchCoat(x)'))  # Rule 18
kb.tell(expr('Sporty(x) & BodyType(x, "PlusSize") ==> RecommendAthleticLeggings(x)'))  # Rule 19
kb.tell(expr('Preppy(x) & Budget(x, "Low") ==> RecommendALineSkirt(x)'))  # Rule 20
kb.tell(expr('Edgy(x) & Budget(x, "Low") ==> RecommendGraphicTee(x)'))  # Rule 21
kb.tell(expr('Minimalist(x) & Budget(x, "Low") ==> RecommendTShirt(x)'))  # Rule 22
kb.tell(expr('Romantic(x) & Budget(x, "High") ==> RecommendLaceDress(x)'))  # Rule 23
kb.tell(expr('Elegant(x) & Budget(x, "Moderate") ==> RecommendMidiDress(x)'))  # Rule 24
kb.tell(expr('Trendy(x) & Budget(x, "Moderate") ==> RecommendDenimJacket(x)'))  # Rule 25

kb.tell(expr('Trendy(x) & Budget(x, "Low") & NotAllergicTo(x, "Nickel") ==> RecommendStatementEarrings(x)'))  # Rule 26
kb.tell(expr('Elegant(x) & Budget(x, "moderate") & NotAllergicTo(x, "Wool") ==> RecommendCashmereSweater(x)'))  # Rule 27
kb.tell(expr('Romantic(x) & Budget(x, "High") & NotAllergicTo(x, "Polyester") ==> RecommendSilkBlouse(x)'))  # Rule 28
kb.tell(expr('Preppy(x) & Budget(x, "Low") & NotAllergicTo(x, "Latex") ==> RecommendPoloShirt(x)'))  # Rule 29
kb.tell(expr('Sporty(x) & BodyType(x, "PlusSize") & NotAllergicTo(x, "Nylon") ==> RecommendTrackPants(x)'))  # Rule 30

# Agenda and Memory
agenda = []  # Agenda to store conditions to be evaluated
memory = {}

user_profile = {
    "Name": "Me",
    "Style": "Trendy",
    "Budget": "Moderate",
    "BodyType": "Petite",
    "Allergies": ["Wool"]
}
possible_allergies = ['Nickel', 'Wool', 'Latex', 'Polyester', 'Nylon']


agenda.append(expr(f'{user_profile["Style"]}(Me)'))
agenda.append(expr(f'Budget(Me, {user_profile["Budget"]})'))
agenda.append(expr(f'BodyType(Me, {user_profile["BodyType"]})'))
for allergy in possible_allergies:
    if allergy not in user_profile['Allergies']:
        agenda.append(expr(f'NotAllergicTo(Me, {allergy})'))

seen = set()  # Keep track of the conditions already processed
while agenda:
    p = agenda.pop(0)
    if p in seen:
        continue  # Skip the condition if it has already been processed
    seen.add(p)
    if fol_fc_ask(kb, p):
        print(f'{p} is true.')
        memory[p] = True
    else:
        print(f'{p} is false.')
        memory[p] = False
    

