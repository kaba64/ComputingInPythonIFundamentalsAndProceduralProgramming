can_afford = False
destination_is_safe = True
educational_value = False
relatives_nearby = False
is_international = False
have_passport = True
afraid_to_fly = False
have_a_car = False
is_a_beach = False
is_warm = True
has_skiing = False
is_a_city = True
is_off_peak = True
has_attraction = False

if(((can_afford or (destination_is_safe and (educational_value or relatives_nearby))) and destination_is_safe)):
    if((is_international and have_passport and (not afraid_to_fly)) or ((not is_international) and (have_a_car or (not afraid_to_fly)))):
        if((is_a_beach and is_warm) or (has_skiing and (not is_warm)) or (is_a_city and (is_off_peak or has_attraction)) or ((is_a_beach and is_a_city) and (is_warm or (is_off_peak or has_attraction))) or ((has_skiing and is_a_city))):
            print(True)
        else:
            print(False)
    else:
        print(False)
else:
    print(False)
