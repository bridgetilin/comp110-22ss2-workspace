"""Demonstrations of dictionary capabilities."""

# Declaring the type of a dictionary
schools: dict[str, int]

# Initialize to an empty dictionary (could be done in one step with above
schools = dict()

# Set a key-value pairing in the dictionary
schools["UNC"] = 19_400
schools["Duke"] = 6717
schools["NCSU"] = 26150

# print a dictionary literal representation 
print(schools)

# Access a value by its key -- "lookup"
print(f"UNC has {schools['UNC']} students")

#Remove a key-value pair
# by its key
schools.pop("Duke")

# Test for exisitence of a key
is_duke_present: bool = "Duke" in schools 
print(f"Duke is present: {is_duke_present}")

print(schools)

# Update/ Reassign a key-value pair
schools["UNC"] = 20000
schools["NCSU"] += 200

# Example of dictionary literals

schools = {}  # same as dict()
print(schools)

# alternatively, initialze key-value pairs 
schools = {"UNC": 19400, "Duke": 6717, "NCSU": 26150}
print(schools)

# What happens when a key doesn't exist??
# print(schools["UNCC"])

# Example looping over the keys of a dict
for key in schools:
    print(f"Key: {key} -> Value: {schools[key]}")

for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")
    print(type(school))
    print(type(schools[school]))