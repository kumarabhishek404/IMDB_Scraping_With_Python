####################################  TASK_2  #####################################
from pprint import pprint
from Task_1 import scrape_top_list

def group_by_year(movies):#First arranged all the years in a list in sorted form and
	years=[]			  #after removed duplicate elements
	for i in movies:
		year=i['2_Year']
		if year not in years:
			years.append(year)

	movies_dict={i:[]for i in years} #main_dictionary_created instead of {i:''} we
	for i in movies:				#assign {i:[]} for taking input inside the list. 
		year=i['2_Year']
		for x in movies_dict:
			if str(x) == str(year): #comparing the items of movies_dict to element
				movies_dict[x].append(i) #of year 

	return (movies_dict)

scraped_data=scrape_top_list()
pprint(group_by_year(scraped_data))
