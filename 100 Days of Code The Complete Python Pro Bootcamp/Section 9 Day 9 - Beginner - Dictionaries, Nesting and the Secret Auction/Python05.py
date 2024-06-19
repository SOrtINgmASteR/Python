# Exercise - Lesson 23 - Dictionary in List

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
