'''
Lesson01 - Assignment 01 - Comprehensions
Author: Sireesha Samkuratripati
Reads Music from Pandas 
Filters Music based on criteria - danceability > 0.9 and loudness < -5.0
Prints the Results after Sorting - using ZIP and Iteration
'''


import pandas as pd
dash = "-" *90

def filter_music_pandas_iterrows():
	music = pd.read_csv("featuresdf.csv")
	music.head()
	music.describe()
	result_list = [(row['name'],row['artists'],row['danceability'],row['loudness']) for index,row in music.iterrows() if row['danceability'] > 0.8 and row['loudness'] < -5.0]
	print ("***** Printing Sorted Result based on Danceability >0.8 and Loudness < -5.0 *****")
	sorted_list = sorted(result_list,key = lambda x: x[2],reverse = True)
	print_music_List(sorted_list)
	
	
def filter_music_pandas_zip():
	music = pd.read_csv("featuresdf.csv")
	music.head()
	music.describe()
	result_list = sorted([(n,a,d,l) for (n,a,d,l) in zip(music.name, music.artists, music.danceability, music.loudness) if d > 0.8 and l < -5.0], reverse=False)
	print(dash)
	print ("***** Using ZIP: Printing Sorted Result based on Danceability >0.8 and Loudness < -5.0 *****")
	print_music_List(result_list)

def print_music_List(music_list):
	space1 = ' '*32
	space2 = ' '*15
	space3 = ' '*2
	print (dash)
	print ("Music Name" + space1 + " Artist" + space2 + " Danceability  Loudness")
	print (dash)
	for item in music_list:
		print(f"{item[0]:40}  {item[1]:20}  {item[2]:.10f} {item[3]:.10f}")

if __name__ == "__main__":
	filter_music_pandas_iterrows()
	filter_music_pandas_zip()