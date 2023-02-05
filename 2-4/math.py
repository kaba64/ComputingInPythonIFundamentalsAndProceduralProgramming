#basecapturerate = 0.33
#cpmultiplier = 0.75
#ball, curve, berry, throw, medal = 1, 1, 1, 1, 1
#baserate = (1 - (basecapturerate / (2 * cpmultiplier)))
#multipliers = ball * curve * berry * throw * medal
#probability = 1 - baserate ** multipliers
#print(round(probability, 2))
su = mystery_value_1 + mystery_value_2
dif = mystery_value_1 - mystery_value_2
pro = mystery_value_1 * mystery_value_2
qou = mystery_value_1 / mystery_value_2
print("The sum is 9{0}, the difference is{1}, the product is{2}, and the quotient is {3}".format(su,dif,pro,qou))
