################################  TASK_6   ########################################

from pprint import pprint
from Task_1 import scrape_top_list
from Task_5 import get_movie_list_details

def analyse_movies_language(movie_language):
	language=[]
	for movie in movie_language:
		for mov in movie['7_movie_language']:
			language.append(mov)
	language1=list(dict.fromkeys(language))
		
	first_list=[]
	for lang in range(len(language1)):
		second_list=str(lang)
		second_list=[]
		count=1
		for lang1 in language:
			if lang1 == language1[lang]:
				second_list.append(count)
				count+=1
		first_list.append(len(second_list))

	movie_lang_dic={}
	for ele in range(len(language1)):
		movie_lang_dic[language1[ele]]=first_list[ele]

	return (movie_lang_dic)

top_movies=scrape_top_list()
movie_detail_lists=get_movie_list_details(top_movies[:10])
print(analyse_movies_language(movie_detail_lists))
