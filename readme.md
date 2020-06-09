# py8fact

random facts scrapped from https://www.instagram.com/8fact/

![](./logo.jpg)

Last Scrapped: 9 Jun 2020


## Install

```bash
pip install py8fact
```

## Usage

```python
import py8fact

num_facts = py8fact.total_facts()

fact = py8fact.random_fact()

facts = py8fact.get_facts(5)
assert len(facts) == 5

all_facts = py8fact.get_facts(-1)
assert len(all_facts) == num_facts
```