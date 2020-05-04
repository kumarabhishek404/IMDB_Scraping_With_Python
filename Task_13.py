#######################################   Task_13   ################################

from pprint import pprint
from bs4 import BeautifulSoup
from Task_1 import scrape_top_list
from Task_12 import scrape_movie_cast
import os.path,time,requests,json

def scrape_movies_details_2(movies):
	#Creating all movie_details in seperation file. 
	# movie_link_lst=[]
	# for movie in movies:
	# 	movie_link=movie['5_Url']
	# 	movie_link_lst.append(movie_link)
	# print(len(movie_link_lst))

	# for link in range(250):
	# 	my_file=open(str(link) + ".json", 'a')
		# response=requests.get(movie_link_lst[link])
		# my_file.write(response.text)
		# my_file.close()

	#Loading all movie_details files.
	movie_name_lst=[]
	movie_year_lst=[]
	movie_genre_lst=[]
	movie_runtime_lst=[]
	movie_country_lst=[]
	movie_language_lst=[]
	movie_director_lst=[]
	movie_poster_url_lst=[]
	movie_bio_lst=[]
	movie_cast_lst=[]

	for link in range(250):
		# path = ("Each_movie_data/") 
		# my_file=open(str(link) + ".json", 'r')
		my_file = open(("Each_movie_data/")+str(link)+ ".json",'r')
		file_data=my_file.read()
		my_file.close()

		soup=BeautifulSoup(file_data,"html.parser")
		main_div=soup.find('div', class_='title-overview')

	  	#Name
		sub_div=main_div.find('div',class_='title_wrapper')
		mixed_name=sub_div.h1.get_text()
		movie_name=mixed_name[:-8]
		movie_name_lst.append(movie_name)
		# print(movie_name)

	 	#Year
		year=mixed_name[-6:-2]
		movie_year_lst.append(year)

	 	#Director
		sub_div=main_div.find('div', class_='credit_summary_item')
		movie_dir=[]
		for tag_a in sub_div.find_all('a'):
			movie_dir.append(tag_a.text)
		movie_director_lst.append(movie_dir)

	 	#Poster_url
		sub_div=main_div.find('div', class_="poster")
		movie_poster_url_lst.append(sub_div.a.img['src'])

	 	#Bio
		sub_div=main_div.find('div', class_='summary_text')
		bio=sub_div.get_text()
		movie_bio_lst.append(bio.strip())

	 	#Genre
		genre_lst=[]
		sub_div=main_div.find('div', class_='subtext')
		for genre in sub_div.find_all("a"):
			genre_lst.append(genre.get_text())
		genre1=genre_lst.pop()
		movie_genre_lst.append(genre_lst)

	 	#Runtime
		sub_div=main_div.find('div', class_='subtext')
		time=sub_div.time.get_text()
		runtime=time.strip()
		lst=['0','1','2','3','4','5','6','7','8','9']
		hour=runtime[0]
		if len(runtime) >=5:
			if runtime[4] in lst:
				minute=runtime[3:5]
				total=(int(hour)*60)+(int(minute))
				movie_runtime_lst.append(total)
			elif runtime[4] not in lst:
				minute=runtime[3]
				total=(int(hour)*60)+(int(minute))
				movie_runtime_lst.append(total)
		else:
			movie_runtime_lst.append(int(hour)*60)
		
	 	#Language and Country
		main_div=soup.find('div', attrs={'class':'article','id':'titleDetails'})
		sub_div=main_div.find_all('div')
		for div in sub_div:
			tag_h4=div.find_all('h4')
			for text in tag_h4:
				if "Language:" in text:
					tag=div.find_all('a')
					movie_language=[]
					for language in tag:
						# print(language.text)
						movie_language.append(language.text)
					movie_language_lst.append(movie_language)
				elif "Country:" in text:
					tag=div.find_all('a')
					for country in tag:
						movie_country=country.text
						movie_country_lst.append(movie_country)

	# Movie Cast
	for i in scraped_data:
		Movie_name=i['1_Name']
		with open("Movie_Cast_Files/"+Movie_name+".json") as file_data:
			Data=json.load(file_data)
			movie_cast_lst.append(Data)
		
	# print(movie_name_lst)
	# print(movie_year_lst)
	# print(movie_genre_lst)
	# print(movie_poster_url_lst)
	# print(movie_director_lst)
	# print(movie_bio_lst)
	# print(movie_runtime_lst)
	# print(movie_language_lst)
	# print(movie_country_lst)
	# print(movie_cast_lst)

	movie_detail=[]
	movie_details={'1_movie_name':'','2_movie_year':'','3_movie_director':'','4_movie_genre':'','5_movie_runtime':'','6_movie_country':'','7_movie_language':'','8_movie_poster_url':'','9_movie_bio':'','10_movie_cast':''}
	for element in range(250):
		movie_details['1_movie_name']=movie_name_lst[element]
		movie_details['2_movie_year']=movie_year_lst[element]
		movie_details['3_movie_director']=movie_director_lst[element]
		movie_details['4_movie_genre']=movie_genre_lst[element]
		movie_details['5_movie_runtime']=movie_runtime_lst[element]
		movie_details['6_movie_country']=movie_country_lst[element]
		movie_details['7_movie_language']=movie_language_lst[element]
		movie_details['8_movie_poster_url']=movie_poster_url_lst[element]
		movie_details['9_movie_bio']=movie_bio_lst[element]
		movie_details['10_movie_cast']=movie_cast_lst[element]

		movie_detail.append(movie_details)
		movie_details={'1_movie_name':'','2_movie_year':'','3_movie_director':'','4_movie_genre':'','5_movie_runtime':'','6_movie_country':'','7_movie_language':'','8_movie_poster_url':'','9_movie_bio':'','10_movie_cast':''}		
	return (movie_detail)


scraped_data=scrape_top_list()
scrape_movies_details_2(scraped_data)