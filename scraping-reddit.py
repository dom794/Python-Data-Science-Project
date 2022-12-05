import praw
import pandas as pd 

reddit = praw.Reddit(client_id='yrSRnqK9sjgvs08x0vQcIw', client_secret='TLtbICSYy8XgDu_x1YDSLObBWoG33Q', user_agent='Data Science Project')

postarray = []
top_posts_all_time = reddit.subreddit('all').top(limit=1000)
for post in top_posts_all_time:
    postarray.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])

print(postarray)


