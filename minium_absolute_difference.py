# Minium Absolute Difference

lst = [-53, -54, -13, 1, -92, -2, -96, 75]
i = 0
m = lst[0] - lst[1]
while i < len(lst):
    j = i+1
    while j < len(lst):
        v = lst[i] - lst[j]
        if abs(m) > abs(v):
            m = v
            pair = lst[i], lst[j]
        j+=1
    i+=1
print(abs(m))
