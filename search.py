import requests
import json
import praw
from pprint import pprint

def cybersecurity_keywords():
    return [
        'cyber security',
        'Botnet',
        'botnet',
        'DDOS',
        'ddos',
        'dedicated denial of service',
        'denial of service',
        'malware',
        'cyber security',
        'virus',
        'trojan',
        'keylogger',
        'Cyber Command',
        'cyber command',
        '2600',
        'spammer',
        'spam',
        'phish',
        'phishing',
        'rootkit',
        'phreaking',
        'cain and abel',
        'Cain and Able',
        'brute forcing',
        'brute-forcing',
        'brute force'
        'brute-force',
        'bruteforce',
        'sql injection',
        'mysql injection',
        'cyber attack',
        'cyber terror',
        'hacker',
        'hack',
        'conficker',
        'worm',
        'scam',
        'scammer'
    ]

def terrorism_keywords():
    return [
        'terrorism',
        'Al Queda',
        'terror',
        'attack',
        'Iraq',
        'Afghanistan',
        'Iran',
        'Pakistan',
        'Agro',
        'environmental terrorist',
        'eco terrorism',
        'conventional weapon',
        'target',
        'weapons grade',
        'dirty bomb',
        'enriched',
        'nuclear',
        'chemical weapon',
        'biological weapon',
        'ammonium nitrate',
        'improvised explosive device',
        'IED',
        'Abu Sayyaf',
        'Hamas',
        'FARC',
        'Armed Revolutionary Forces Colombia',
        'IRA',
        'Irish Republican Army',
        'ETA',
        'Euskadi ta Askatasuna',
        'Basque Separatists',
        'Hezbollah',
        'Tamil Tiger',
        'PLF',
        'Palestine Liberation Front',
        'PLO',
        'Palestine Libration Organization',
        'car bomb',
        'Jihad',
        'Taliban',
        'weapons cache',
        'suicide bomber',
        'suicide attack',
        'suspicious substance',
        'AQAP',
        'Al Qaeda Arabian Peninsula',
        'AQIM'
        'Al Qaeda in the Islamic Maghreb',
        'TTP',
        'Tehrik-i-Taliban Pakistan',
        'Yemen',
        'pirates',
        'extremism',
        'Somalia',
        'Nigeria',
        'radicals',
        'Al-Shabaab',
        'home grown',
        'plot',
        'nationalist',
        'recruitment',
        'fundamentalism',
        'Islamist'

    ]

def multi_search(keyword_list):
    reddit = praw.Reddit(
        client_id='ypRz2owAJ3YKBg',
        client_secret='yCYUfXOLrVzLswYWoRevzG1Sx-U',
        user_agent='Sybil'
    )

    cybersecurity = reddit.subreddit('cybersecurity').hot(limit=100)
    politics = reddit.subreddit('politics').hot(limit=100)
    security = reddit.subreddit('security').hot(limit=100)
    conspiracy = reddit.subreddit('conspiracy').hot(limit=100)
    deepweb = reddit.subreddit('deepweb').hot(limit=100)
    cryptocurrency = reddit.subreddit('cryptocurrency').hot(limit=100)
    worldnews = reddit.subreddit('worldnews').hot(limit=100)


    subreddit_list = [
        cybersecurity,
        politics,
        security,
        conspiracy,
        deepweb,
        cryptocurrency,
        worldnews
        ]

    comments_dict = {}
    for item in subreddit_list:
        for submission in cybersecurity:
            for word in keyword_list:
                    if word in submission.selftext:
                        data = submission.selftext
                        transformed_data = 'text=' + submission.selftext
                        if word not in  comments_dict:
                            comments_dict[word] = []
                        comments_dict[word].append({
                            'comment': data,
                            'permalink': 'https://www.reddit.com' 
                            + submission.permalink
                            })

        for k, v in comments_dict.items():
            for item in v:
                transformed_data = 'text=' + item['comment']
                encoded_data = transformed_data.encode('utf-8')
                r = requests.post(
                    'http://text-processing.com/api/sentiment/',
                    data=encoded_data
                )
                item['sentiment'] = r.text
        
        print(comments_dict)
        return comments_dict