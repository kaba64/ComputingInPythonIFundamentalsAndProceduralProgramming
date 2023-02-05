message = "lol"
punct = "!"
num = 3

result = (num-1)*message + punct
for i in range(1,(num-1))
    result += (num-1)*message + punct
result += (num-1)*message
print(result)
