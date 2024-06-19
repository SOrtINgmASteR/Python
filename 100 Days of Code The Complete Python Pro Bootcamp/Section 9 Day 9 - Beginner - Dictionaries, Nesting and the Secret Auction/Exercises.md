<h2 style="text-align:center">DAY - 9</h2>  

<h3 style="text-align:center;">Lesson 22 - Grading Program</h3>  

```python
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

for student in student_scores:
    if student_scores[student] >= 91:
        student_scores[student] = "Outstanding"
    elif student_scores[student] >= 81:
        student_scores[student] = "Exceeds Expectations"
    elif student_scores[student] >= 71:
        student_scores[student] = "Acceptable"
    else:
        student_scores[student] = "Fail"

print(student_scores)
```

<h3 style="text-align:center;">Travel Log (Nesting Lists & Dictionaries)</h3>  

```python
# Lists inside Dictionary

destinations1 = {"Bangladesh": ["Dhaka", "Cumilla", "Barishal"],
                 "India": ["Kolkata", "Delhi", "Bangalore"],
                 "Indonesia": ["Jakarta", "Makassar"]
                 }
print(f"{destinations1['Bangladesh']}")
print(f"{destinations1['Indonesia']}")


# Dictionaries inside Dictionary

destinations2 = {"Bangladesh": {"Dhaka": 6, "Cumilla": 50, "Barishal": 4},
                 "India": {"Kolkata": 4, "Delhi": 11, "Bangalore": 5},
                 "Indonesia": {"Jakarta": 3, "Makassar": 2}
                 }
print(f"{destinations2['Bangladesh']}")
print(f"{destinations2['Indonesia']}")


# Dictionaries inside List

destinations3 = [{"Dhaka": 6, "Cumilla": 50, "Barishal": 4},
                 {"Kolkata": 4, "Delhi": 11, "Bangalore": 5},
                 {"Jakarta": 3, "Makassar": 2}
                 ]
print(f"{destinations3[0]}")
print(f"{destinations3[2]}")
```

<h3 style="text-align:center;">Lesson 23 - Dictionary in List</h3>  

```python
def add_new_country(travel_log, country, visits, list_of_cities):
    new_country = {"country": country, "visits": visits, "cities": list_of_cities}
    travel_log.append(new_country)


country = input()
visits = int(input())
list_of_cities = eval(input())

travel_log = [{"country": "France", "visits": 12, "cities": ["Paris", "Lille", "Dijon"]},
              {"country": "Germany", "visits": 5, "cities": ["Berlin", "Hamburg", "Stuttgart"]},
              ]

add_new_country(travel_log, country, visits, list_of_cities)

print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")
```

<h3 style="text-align:center;">Blind Auction Program</h3>  
```python

```