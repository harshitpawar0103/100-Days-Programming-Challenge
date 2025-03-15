us_states = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", 
    "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", 
    "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", 
    "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", 
    "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", 
    "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", 
    "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", 
    "Wisconsin", "Wyoming"
]

print(us_states)
print(us_states[0])
print(us_states[-1])
print(us_states[0:4])
print(us_states[0::4])
print(us_states[1::4])

us_states.append("AngelaLand")
print(us_states[-1])

us_states.extend(["Panamerica","instania","Homeland"]) # extends iterables in list
print(us_states[-1])


us_states.insert(5,"totaland")
print(us_states[5])
