import feedparser, re, time, json
print('0')
with open('config.js', 'r') as f: # Get config from file
    config = f.read().replace('const config = ','').strip() # Remove Javascript stuff
    print('1')
    
config = eval(re.sub(r'((?<!:)//).*?\n','', config).replace('\n','').replace(';','')) # Remove Javascript stuff
print('config', config)

rss2json = dict()
all_titles = []
maxPublishTime = eval(str(config['maxPublishTime'])) # in minutes
hrsTime = int(maxPublishTime/60) # For Google News RSS - needed in hours

time_now = time.time()

for rss_category in config['rssurl']:
    print(rss_category)
    rss_category_renamed = rss_category.replace('/','_') # If category name has /, class and id names in html will break
        rss2json[rss_category_renamed] = dict()
        for rss_url_full in config['rssurl'][rss_category]:
            rss_url = rss_url_full.split('::')[0]
            print(rss_url)
            
