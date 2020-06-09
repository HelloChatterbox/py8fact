import py8fact

num_facts = py8fact.total_facts()

fact = py8fact.random_fact()

facts = py8fact.get_facts(5)
assert len(facts) == 5

all_facts = py8fact.get_facts(-1)
assert len(all_facts) == num_facts
