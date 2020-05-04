###################################### TASK_11  ##################################

from Task_1 import scrape_top_list
from Task_5 import get_movie_list_details
from pprint import pprint

def analyse_movie_genre(movie_list):
	genre_list=[]
	list1=[]
	for genre in movie_list:
		for gen in genre['4_movie_genre']:
			list1.append(gen)
			genre_list=list(dict.fromkeys(list1))
	my_dict={}
	for i in genre_list:
		my_dict[i]={}
	for count in range(len(list1)):
		for dic in my_dict:
			if str(dic) == str(list1[count]):
				my_dict[dic]=0
	for count in range(len(list1)):
		for dic in my_dict:
			if str(dic) == str(list1[count]):
				my_dict[dic]+=1

	return my_dict


scraped_data=scrape_top_list()
movies=get_movie_list_details(scraped_data)
pprint(analyse_movie_genre(movies))