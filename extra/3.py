hot = True
cold = False
rainy = True
windy = False
snowy = False
if(cold or (hot and not rainy)):
    print("Hat: ",True)
else:
    print("Hat: ",False)

if(cold and (snowy or rainy)):
    print("Gloves: ",True)
else:
    print("Gloves: ",False)

if(hot or snowy or rain):
    print("Umbrella: ",True)
else:
    print("Umbrella: ",False)

if((cold and windy) or (cold and snowy)):
    print("Scarf: ",True)
else:
    print("Scarf: ",False)
