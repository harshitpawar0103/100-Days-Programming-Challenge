# for loop in lists
scores = [150,142,185,120,171,184,149,24,59,68,199,78,65,89,86]

print(sum(scores))
print(max(scores))
print("\n\n")

max = 0
for score in scores : 
    if score > max:
        max = score

print(max)



# for loop in range

sum = 0
for i in range(1,101):
    sum += i
print(sum)



# for loop in range-step
for i in range(1,11,3):
    print(i)