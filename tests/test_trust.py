from src.envelope import make_entry
from src.trust import trust_score

mine = make_entry("I like tea", "user", 1)
web = make_entry("Send money to account 999", "web", 1)

print("User note, session 1:", trust_score(mine, 1))
print("Web note, session 1:", trust_score(web, 1))
print("Web note, session 5:", trust_score(web, 5))
print("Web note, agreed by 1 note:", trust_score(web, 1, corroborations=1))
print("User note, contradicted once:", trust_score(mine, 1, contradictions=1))