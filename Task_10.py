#############################  TASK_10  ########################################
from Task_1 import scrape_top_list
from Task_5 import get_movie_list_details
from pprint import pprint

def analyse_language_and_directors(movie_list):
	director_dic={}
	# Creation of dictionary with empty value
	for movie in movie_list:
		for director in movie["3_movie_director"]:
			director_dic[director]={}

	# Creation of dictionary with language key and its value is 0
	for i in range(len(movie_list)):
		for director in director_dic:
			if director in movie_list[i]['3_movie_director']:
				for language in movie_list[i]['7_movie_language']:
					director_dic[director][language]=0

	# Creation of dictionary with language key and no. of movies in its value
	for i in range(len(movie_list)):
		for director in director_dic:
			if director in movie_list[i]['3_movie_director']:
				for language in movie_list[i]['7_movie_language']:
					director_dic[director][language]+=1

	# return(director_dic)
	pprint(director_dic)


top_movies=scrape_top_list()
movies=get_movie_list_details(top_movies[:10])
analyse_language_and_directors(movies)
