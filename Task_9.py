#############################  TASK_9  #####################################

# import random
# help(random.randint)
# import time
# help(time.sleep)
import os,time,requests
from Task_1 import scrape_top_list

def scrape_movie_details_with_time(movies):
	cut_url_list=[]
	movie_url=[]

	#Creation of list of of original and cut url
	for movie in movies:
		movie_url.append(movie['5_Url'])
		cut=movie['5_Url'].replace("https://www.imdb.com/title/", "")
		cut_url=cut.replace("/", "")
		cut_url_list.append(cut_url)
	
	#Creation of file of name like as tt0066763,tt0345623.
	for count in range(len(cut_url_list)):
		if os.path.isfile(("Task_9_file/")+cut_url_list[count]):
			print("File Exist")
		else:
			time.sleep(3)
			response=requests.get(movie_url[count])
			with open(("Task_9_file/")+cut_url_list[count],"w") as file_data:
				file_data.write(response.text)
				file_data.close()
			print("File Created")

scraped_data=scrape_top_list()
scrape_movie_details_with_time(scraped_data)



# #

# import os

# def scrape_movie_details_with_time(movies):
# 	lis =[]
# 	movie_url=[]
# 	cut_url_list=[]
# 	for movie in movies:
# 		movie_url.append(movie['5_Url'])
# 		cut=movie['5_Url'].replace("https://www.imdb.com/title/", "")
# 		cut_url=cut.replace("/", "")
# 		cut_url_list.append(cut_url)
# 	# print(cut_url)
# 	for count in range(len(cut_url_list)):
# 		file=cut_url_list[count]+".json"
# 		# print("noe")
# 		if os.path.exists("Web_Scraping/"+file):
# 			with open("Web_Scraping/"+file,"r") as file_data:
# 				load_file=json.load(file_data)
# 				# print("yes")
# 				# print(load_file)
# 		else:
# 			print("no")
# 			response=requests.get(movie_url[count])
# 			my_dict={"1":'fg',"2":"vbn","3":"vb"}
# 			lis.append(my_dict)
# 		with open("Web_Scraping/"+file, "w+") as file_data:
# 			dump_file=json.dump(lis,file_data)
# 			print(dump_file)
# 			print(movie_url[count])

# scraped_deta=scrape_top_list()
# scrape_movie_details_with_time(scraped_deta)
