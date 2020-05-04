###############################  TASK_3  #########################################
from pprint import pprint
from Task_1 import scrape_top_list

def group_by_decade(movies):
	#making of sorted list of ascending order of years.
	years=[]
	for i in movies:
		year=i['2_Year']
		if year not in years:
			years.append(year)
			years=sorted(years)
	#Distribute the movies in according to decades
	decades=['1950','1960','1970','1980','1990','2000','2010','2020']
	lst2=[] 
	for i in decades:
		lst1=[]
		for j in movies:
			year1=str(j['2_Year'])
			if i[2]==year1[2]:
				lst1.append(j)
		lst2.append(lst1)
	#Putting all the data in a dictionary form
	year_dict={}
	for i in range(len(decades)):
		year_dict[decades[i]]=lst2[i]

	return year_dict

scraped_data=scrape_top_list()
pprint(group_by_decade(scraped_data))

