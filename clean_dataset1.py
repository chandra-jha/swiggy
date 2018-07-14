import csv
file_loc = ''
count = 0
with open(file_loc) as csvfile(delimiter = ','):
	reader = csv.reader(csvfile)
	for row in reader:
		count = count + 1
		if count > 1:
			data = row.split(',',9)
			items = data[9]
			
