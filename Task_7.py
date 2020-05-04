###############################   TASK_7  ########################################

from pprint import pprint
from Task_1 import scrape_top_list
from Task_5 import get_movie_list_details

def analyse_movies_director(movie_director):
	dir_lst=[]
	for movie in movie_director:
		for dir in movie['3_movie_director']:
			dir_lst.append(dir)
		dir1=list(dict.fromkeys(dir_lst)) #Converting into dict for removing 
											#duplicates
	director_lst=[]
	for length in range(len(dir1)):
		lst=str(length)
		lst=[]
		count=1
		for director in dir_lst:
			if director == dir1[length]:
				lst.append(count)
				count+=1
		director_lst.append(len(lst))		
	
	#Putting all the data in dictionary	
	movie_director_dir={}
	for movie_dir in range(len(director_lst)):
		movie_director_dir[dir1[movie_dir]]=director_lst[movie_dir]

	return movie_director_dir


top_movies=scrape_top_list()
movie_detail_lists=get_movie_list_details(top_movies[:10])
print(analyse_movies_director(movie_detail_lists))
