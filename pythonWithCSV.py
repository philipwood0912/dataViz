import csv
import numpy as np
import matplotlib.pyplot as plt

# figures out what data to use
categories = [] # these are the column headers in the CSV file
installs = [] # installs row
ratings = [] # ratings row

with open('data/googeplaystore.csv') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		# move the page column headers out of the actual data to get a clean dataset
		if line_count is 0: # this will be text not data
			print('pushing categories into seperate array')
			categories.append(row) # push the thext into an array
			line_count += 1 # increment the line count into next loop
		else:
			# grab the ratings data and push them into ratings array
			ratingsData = row[2]
			ratingsData = ratingsData.replace("NaN", "0")
			ratings.append(float(ratingsData)) # int will turn a string (text) into a number
			# print('pushing ratings data into the ratings array')
			installData = row[5]
			installData = installData.replace(",", "") # gets rid of commas

			installs.append(np.char.strip(installData, "+")) # gets rid of trailing +
			line_count += 1
# get some values we can work with
# how many ratings are 4+?
# how many are below 2?
# how many are in the middle?
np_ratings = np.array(ratings) # turn a plain Python list into a numpy array
popular_apps = np_ratings > 4
print("popular apps:", len(np_ratings[popular_apps]))

percent_popular = len(np_ratings[popular_apps]) / len(np_ratings) * 100
print(percent_popular)

unpopular_apps = np_ratings < 4
print("popular apps:", len(np_ratings[unpopular_apps]))

percent_unpopular = len(np_ratings[unpopular_apps]) / len(np_ratings) * 100
print(percent_unpopular)

kinda_popular = 100 - (percent_popular + percent_unpopular)
print(kinda_popular)

labels = "Sucks", "Meh", "Love it!"
sizes = [percent_unpopular, kinda_popular, percent_popular]
colors = ["yellowgreen", "lightgreen", "lightskyblue"]
explode = (0.1, 0.1, 0.15)

plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.legend(labels, loc=1)
plt.title("DO we love apps?")
plt.xlabel("user rating - apps installs (10000 apps)")
plt.show()


 # print('processed', line_count, 'lines of data')

print(categories)
print('first row of data', installs[0])
print('last row of data', installs[-1])
