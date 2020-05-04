############################  TASK 8   ##########################################

# Caching in python 
# Refactoring code in python
from Task_1 import scrape_top_list
from pprint import pprint
from bs4 import BeautifulSoup
import requests,os.path,json,time

def scrape_movie_details_2(movies):
	cut_url_list=[]
	movie_url=[]
	#Creation of list of of original and cut url
	for movie in movies:
		movie_url.append(movie['5_Url'])
		cut=movie['5_Url'].replace("https://www.imdb.com/title/", "")
		cut_url=cut.replace("/", "")
		cut_url_list.append(cut_url)
	
	movie_name_lst=[]
	movie_year_lst=[]
	movie_genre_lst=[]
	movie_runtime_lst=[]
	movie_country_lst=[]
	movie_language_lst=[]
	movie_director_lst=[]
	movie_poster_url_lst=[]
	movie_bio_lst=[]

	#Checking the existance of file if not exist then creating.
	movie_details={'1_movie_name':'','2_movie_year':'','3_movie_director':'','4_movie_genre':'','5_movie_runtime':'','6_movie_country':'','7_movie_language':'','8_movie_poster_url':'','9_movie_bio':''}
	for count in range(len(cut_url_list)):
		time.sleep(3)
		if os.path.exists(("Each_link_file/")+cut_url_list[count]+".json"):
			print('File_exits')
	# #Creation of file of name like as tt0066763,tt0345623.	
		else:
			response=requests.get(movie_url[count])
			soup=BeautifulSoup(response.text,"html.parser")
			main_div=soup.find('div', class_='title-overview')

			#Name
			sub_div=main_div.find('div',class_='title_wrapper')
			mixed_name=sub_div.h1.get_text()
			movie_name=mixed_name[:-8]
			movie_details['1_movie_name']=movie_name
		 	# Year
			year=mixed_name[-6:-2]
			movie_details['2_movie_year']=year
		 	#Director
			sub_div=main_div.find('div', class_='credit_summary_item')
			movie_dir=[]
			for tag_a in sub_div.find_all('a'):
				movie_dir.append(tag_a.text)
			movie_details['3_movie_director']=movie_dir

		 	#Poster_url
			sub_div=main_div.find('div', class_="poster")
			movie_poster=sub_div.a.img['src']
			movie_details['8_movie_poster_url']=movie_poster

		 	#Bio
			sub_div=main_div.find('div', class_='summary_text')
			movie_bio=sub_div.get_text().strip()
			movie_details['9_movie_bio']=movie_bio

		 	#Genre
			sub_div=main_div.find('div', class_='subtext')
			genre_lst=[]
			for genre in sub_div.find_all("a"):
				genre_lst.append(genre.get_text())
			movie_genre=genre_lst.pop()
			movie_details['4_movie_genre']=genre_lst

		 	#Runtime
			sub_div=main_div.find('div', class_='subtext')
			time1=sub_div.time.get_text()
			runtime=time1.strip()
			lst=['0','1','2','3','4','5','6','7','8','9']
			hour=runtime[0]
			if len(runtime) >=5:
				if runtime[4] in lst:
					minute=runtime[3:5]
					movie_runtime=(int(hour)*60)+(int(minute))
					movie_details['5_movie_runtime']=movie_runtime
				elif runtime[4] not in lst:
					minute=runtime[3]
					movie_runtime=(int(hour)*60)+(int(minute))
					movie_details['5_movie_runtime']=movie_runtime
			else:
				movie_runtime=int(hour)*60
				movie_details['5_movie_runtime']=movie_runtime

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
							movie_language.append(language.text)
							movie_details['7_movie_language']=movie_language
					elif "Country:" in text:
						tag=div.find_all('a')
						for country in tag:
							movie_country=country.text
							movie_details['6_movie_country']=movie_country

			
			with open(("Each_link_file/")+cut_url_list[count]+".json","w+") as file_data:
				json.dump(movie_details, file_data, indent=4, sort_keys=True)
				print("File created")

			movie_details={'1_movie_name':'','2_movie_year':'','3_movie_director':'','4_movie_genre':'','5_movie_runtime':'','6_movie_country':'','7_movie_language':'','8_movie_poster_url':'','9_movie_bio':''}		


# scraped_deta=scrape_top_list()
# scrape_movie_details_2(scraped_deta)
