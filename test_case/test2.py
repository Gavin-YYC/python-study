breakfirst_special = 'Texas Omelet'
breakfirst_notes = 'Contains ...'

lunch_special = 'Greek ..'
lunch_notes = 'Like ...'

dinner_special = 'ghjk'
dinner_notes = 'Top ahhfa'

meal_time = raw_input('Which mealtime do you want? [breakfirst, lunch, dinner] ')
print 'Special for {}: '.format( meal_time )

if meal_time == 'breakfirst':
    print breakfirst_special
    print breakfirst_notes
elif meal_time == 'lunch':
    print lunch_special
    print lunch_notes
elif meal_time == 'dinner':
    print dinner_special
    print dinner_notes
else: 
    print 'sorry, {} dahs'.format( meal_time )
