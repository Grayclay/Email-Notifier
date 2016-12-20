dates = ['10:50am','Dr. Strange','11:15am','12:30pm','2:45pm','Hogwash']
final = []

print dates

for t in dates:
	if 'am' in t:
		print(t)
		final.append(t)
	elif 'pm' in t:
		print(t)
		final.append(t)

print final