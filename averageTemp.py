temperatures = [30.0,29,45,50,35.4,25.7,30.5]

total = 0 

for temp in temperatures:
    total += temp
    
    
print("Average Temperature of Cities : ",total/len(temperatures))