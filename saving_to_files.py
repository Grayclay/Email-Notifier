# text_file = open("Dates.txt", "a")

# text_file.write("1-7-2017")

#or also
dates = ["1-27-2017"]

with open("Dates.txt", "w") as write_file:
	write_file.write("Date: %s" % dates[0])
	
with open("Dates.txt", "r") as read_file:
	most_recent_date = read_file.readline()

print most_recent_date

