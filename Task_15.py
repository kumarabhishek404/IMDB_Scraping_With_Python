# ####################################  Task 15   ####################################

from Task_13 import scrape_movies_details_2
from Task_1 import scrape_top_list
from pprint import pprint


def analyse_actor(movie_list):
	Id_lst=[]
	Name_lst=[]
	full_cast=[]
	for movie in movie_list:
		for cast in movie['10_movie_cast'][:5]:
			full_cast.append(cast['Imdb_Id'])
			if cast['Imdb_Id'] not in Id_lst:
				Id_lst.append(cast['Imdb_Id'])
				Name_lst.append(cast['Name'])
			else:
				pass
				
	#Making of Rank list
	rank_list=[]
	for i in Id_lst:
		rank=1
		for j in full_cast:
			if i == j:
				rank+=1
		rank_list.append(rank)

	# Name and No of movies dict 
	my_lst=[]
	dict1={'Name':'',"No_of_movies":''}
	for j in range(len(Name_lst)):
		dict1['Name']=Name_lst[j]
		dict1['No_of_movies']=rank_list[j]
		my_lst.append(dict1)
		dict1={'Name':'',"No_of_movies":''}
	pprint(my_lst)
	
scraped_data=scrape_top_list()
movie_list=scrape_movies_details_2(scraped_data)
analyse_actor(movie_list)
