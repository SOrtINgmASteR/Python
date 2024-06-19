# Nesting Lists & Dictionaries

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
