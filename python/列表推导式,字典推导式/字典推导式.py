a = {chr(i+97):str(i+10) for i in range(10)}
b = {chr(i+97):i+10 for i in range(10) if i%2 == 0}
print(a)
print(b)