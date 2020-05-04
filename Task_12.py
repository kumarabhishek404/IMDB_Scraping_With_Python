################################   TASK_12  #######################################

# #### For Making the file in your computer

# from Task_1 import scrape_top_list
# from bs4 import BeautifulSoup
# from pprint import pprint
# import requests,time,os.path,json


# def scrape_movie_cast(movie_cast_url):
# 	if os.path.isfile("Movie_Cast_Files/"+Movie_name+".json"):
# 		return ("File_Exists")

# 	else:
# 		time.sleep(1)
# 		response=requests.get(movie_cast_url) # Requests for half links
# 		soup=BeautifulSoup(response.text,'html.parser')
# 		main_div=soup.find('div', attrs={"class":"article","id":"titleCast"})
# 		sub_div=main_div.find('div', class_="see-more")
# 		full_link=movie_cast_url+sub_div.a['href'] #Addition of two half links 
# 		time.sleep(1)
# 		respons2=requests.get(full_link)  # Requests for data scrape from full-link
# 		soup=BeautifulSoup(respons2.text,"html.parser")
# 		main_div2=soup.find('table', class_="cast_list")
# 		td = main_div2.find_all("td", class_="primary_photo")
# 		actor_id=[]
# 		actor_name=[]
# 		#Scrape Actor Id and Name
# 		my_list=[]
# 		my_dict={"Imdb_Id":"","Name":""}
# 		for count in td:
# 			tag_a=count.find('a')
# 			my_dict["Imdb_Id"]=tag_a['href'][6:-1]
# 			my_dict["Name"]=tag_a.img['title']
# 			my_list.append(my_dict)
# 			my_dict={"Imdb_Id":"","Name":""}

# 		with open("Movie_Cast_Files/"+Movie_name+".json", "w+") as file_data:
# 			json.dump(my_list, file_data, indent=4, sort_keys=True)
# 			return ("File_Created")

# movie_lst=[]
# for scraped_data in scrape_top_list():
# 	Movie_name=scraped_data['1_Name']
	# pprint(scrape_movie_cast(scraped_data['5_Url']))



################################   TASK_12  #######################################

##### For print the return data on the terminal

from Task_1 import scrape_top_list
from bs4 import BeautifulSoup
from pprint import pprint
import requests,time,os.path,json


def scrape_movie_cast(movie_cast_url):
	time.sleep(1)
	response=requests.get(movie_cast_url) # Requests for half links
	soup=BeautifulSoup(response.text,'html.parser')
	main_div=soup.find('div', attrs={"class":"article","id":"titleCast"})
	sub_div=main_div.find('div', class_="see-more")
	full_link=movie_cast_url+sub_div.a['href'] #Addition of two half links 
	time.sleep(1)
	respons2=requests.get(full_link)  # Requests for data scrape from full-link
	soup=BeautifulSoup(respons2.text,"html.parser")
	main_div2=soup.find('table', class_="cast_list")
	td = main_div2.find_all("td", class_="primary_photo")
	actor_id=[]
	actor_name=[]
	#Scrape Actor Id and Name
	my_list=[]
	my_dict={"Imdb_Id":"","Name":""}
	for count in td:
		tag_a=count.find('a')
		my_dict["Imdb_Id"]=tag_a['href'][6:-1]
		my_dict["Name"]=tag_a.img['title']
		my_list.append(my_dict)
		my_dict={"Imdb_Id":"","Name":""}

		
	return my_list

movie_lst=[]
for scraped_data in scrape_top_list():
	Movie_name=scraped_data['1_Name']
	# pprint(scrape_movie_cast(scraped_data['5_Url']))