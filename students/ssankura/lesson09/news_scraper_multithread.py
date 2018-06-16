'''
Lesson09 - Multi Threaded news scaper
Author: Sireesha Sankuratripati
Summary: Modified the ayncio news scraper to implement multi threaded approach
'''

import time
import requests
import threading

NEWS_API_KEY = 'a91f5866575f4964a4eb15c2cfeb1cf6'
base_url = 'https://newsapi.org/v1/'
WORD = "trump"

global art_count
global word_count
global lock


# doesn’t really need to to async since this call is only made once to gather all news sources
def get_sources():
    url = base_url + "sources"
    params = {"language": "en", "apiKey": NEWS_API_KEY}
    resp = requests.get(url, params = params)
    data = resp.json()
    sources = [src['id'].strip() for src in data['sources']]
    print ("Printing sources")
    print (sources)
    return sources


def get_articles(source):
    "../vl/articles?source=associated-press&sortBy=top&apiKey=…"
    url = base_url + "articles"
    params = {"source": source,
              "apiKey": NEWS_API_KEY,
              "sortBy": "top"
              }
    print("requesting", source)
    resp = requests.get(url, params = params)
    if resp.json()['status'] != 200:
        print(f'something went wrong. {source}')
        print (f'printing resp {resp.json()}')
        return []
    
    data = resp.json()
    titles = [(str(art['title']) + str(art['description'])) for art in data['articles']]
    return titles

def count_word(word, titles):
    word = word.lower()
    count = 0
    for title in titles:
        if word in title.lower():
            count += 1
    return count

def split_sources_list(sources, num_parts=1):
    length = len(sources)
    length_each_part = length // num_parts
    print (length_each_part)
    new_split_lists = []
    for i in range(0,num_parts):
        print (f'Splitting Sources list from {i*length_each_part} to {(i+1)*length_each_part}')
        split_list = []
        if i == num_parts-1:
            split_list = sources[i*length_each_part:]
        else:
            split_list = sources[i*length_each_part:(i+1)*length_each_part]
        new_split_lists.append(split_list)
    return new_split_lists

def increment_global_title_word_count(cnt_titles_src, cnt_words_in_src):
    '''
    The global variables - art_count and word_count are the shared data which will be 
    modified by multiple threads. So, we need to obtain a lock before entering the
    Critical Section and release the lock once we exit the Critical Section
    '''
    global lock
    lock.acquire()
    art_count += cnt_titles_src
    word_count += cnt_words_in_src
    lock.release()


def worker_cnt_articles_word(source_list):
    for source in source_list:
        print (f"getting titles for {source}")
        titles = get_articles(source)
        word_cnt_source = count_word(WORD, titles)
        increment_global_title_word_count(len(titles), word_cnt_source) #need to acquire a lock before attempting this method???

def main():

    start = time.time()

    sources = []
    titles = []
    src_list = []
    art_count=0
    word_count=0

    # get the sources this is essentially synchronous
    sources = get_sources()

    src_list = split_sources_list(sources,2)
    sources_part1 = src_list[0]
    sources_part2 = src_list[1]

    #create 2 threads and make T1 run worker process on sources_part1 and T2 to run worker process on sources_part2
    lock = threading.Lock()
    thread_1 = threading.Thread(target = worker_cnt_articles_word, args = (sources_part1), name = "Thread_1")
    thread_2 = threading.Thread(target = worker_cnt_articles_word, args = (sources_part2), name = "Thread_2")

    thread_1.start()
    thread_2.start()

    thread_1.join()
    thread_2.join()

    print ("All threads completed processing")

    print(f'found {WORD}, {word_count} times in {art_count} articles')
    print(f'Process took {(time.time() - start):.0f} sec.')

if __name__ == "__main__":
    main()
