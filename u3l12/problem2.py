health = input('What is your health? ')
health = int(health)

while health > 100:
	print('That value is too high!')
	health = input('What is your health? ')
	health = int(health)

if health == 100:
	print('You are at full health.')

elif health >= 90:
	print('You have taken some minor damage. Health at ' + str(health) + ".")

elif health >= 50:
	print('You only have ' + str(health) + ' health.')

elif health >= 20:
	print('You are at ' + str(health) + ' health. You may want to start fighting back.')

elif health >= 1:
	print("You are at " + str(health) + " health! Critical warning!!!")  

else:
	print('You died...')