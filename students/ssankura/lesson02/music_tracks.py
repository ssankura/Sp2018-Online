#!/usr/bin/env python3

'''
Lesson02 - Assignment 01 - Generators and Closures 
Author: Sireesha Samkuratripati
TASK1: Reads Music from Pandas, Filters Music based on criteria - Artist = 'Ed Shreeran' and prints the results
TASK2: Implemented generator - filter_music_generator which returns one music record at a time with the data - Track name, artist name, energy level, danceability and loudness
TASK3: Implemented Closure - music_high_energy - which takes as input the filename of the music input file feed - it had a nested func which filters music (from input file) based on energy level (sent as input)
'''


import pandas as pd
dash = "-" *120

def filter_music_pandas_iterrows():
	''' Used comprehension to filter and print all the tracks by Ed Sheeran
	'''
	music = pd.read_csv("featuresdf.csv")
	music.head()
	music.describe()
	result_list = [(row['name'],row['artists'],row['energy'],row['danceability'],row['loudness']) for index,row in music.iterrows() if row['artists'] == 'Ed Sheeran']
	print (dash)
	print ("***** Printing Sorted Result based on Artist = 'Ed Sheeran'")
	sorted_list = sorted(result_list,key = lambda x: x[2],reverse = True)
	print_music_List(sorted_list)
	
def filter_music_generator():
	'''Generator function which returns the next music track which belong to Ed Sheeran
	'''
	music = pd.read_csv("featuresdf.csv")
	music.head()
	music.describe()
	for index,row in music.iterrows():
		if row['artists'] == 'Ed Sheeran':
			yield [(row['name'],row['artists'],row['energy'],row['danceability'],row['loudness'])]

def music_high_energy(music_file_name = 'featuresdf.csv'):
	'''Closure function which takes as input a file name for the music track indo and wraps around the filter mucsic method that filters music based on energy level
	'''
	music = pd.read_csv(music_file_name)
	music.head()
	music.describe()
	def filter_music(energy_level):
		result_list =  [(row['name'],row['artists'],row['energy'],row['danceability'],row['loudness']) for index,row in music.iterrows() if row['energy'] > energy_level]
		return result_list
	return filter_music

def print_music_List(music_list):
	'''Helper method which prints the music tracks
	'''
	space1 = ' '*37
	space2 = ' '*15
	space3 = ' '*2
	print (dash)
	print ("Music Name" + space1 + " Artist" + space2 + " Energy  Danceability  Loudness")
	print (dash)
	for item in music_list:
		print(f"{item[0]:45}  {item[1]:20}  {item[2]:.5f} {item[3]:.10f} {item[4]:.10f}")


if __name__ == "__main__":
	'''name == main method
	invokes the filter music and the closure method
	'''
	filter_music_pandas_iterrows()
	
	music_features_df = music_high_energy('featuresdf.csv')

	print (dash)
	print (dash)
	print ("***** Printing High Energy Music Tracks - Energy level > 0.80")
	print_music_List(music_features_df(0.80))

	print (dash)
	print (dash)
	print ("***** Printing High Energy Music Tracks - Energy level > 0.85")
	print_music_List(music_features_df(0.85))

	print (dash)
	print (dash)
	print ("***** Printing High Energy Music Tracks - Energy level > 0.90")
	print_music_List(music_features_df(0.9))

	print (dash)
	print ("********** Printing Music List Using filter_music_generator **********")
	print (dash)
	print (dash)

	gen = filter_music_generator()
	while True:
		result = next(gen)
		print (result)
		#print (f"result[0]:40 	result[1]:20	result[2]:.5f	result[3]:.10f 	result[4]:.10f")

	