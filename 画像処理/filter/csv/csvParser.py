import csv
with open('zengin.csv', 'rt') as f:
	reader = csv.reader(f)
	for row in reader:
		print (row)