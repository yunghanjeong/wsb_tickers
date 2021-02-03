# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 11:51:23 2020

@author: Yung
"""
# for local files and online data
import json

# for reddit api
import pandas as pd
import praw



class reddit_tools():
    """
    This is for initializing the reddit API, PRAW
    """
    def __init__(self, agent:str):
        api_id, api_secret = self.get_keys()
        self.reddit = praw.Reddit(client_id=api_id,
                     client_secret=api_secret,
                     user_agent=agent)
        
    #this function grabs api keys and returns them
    def get_keys(self):
        f = open("api_secret.json") #you many need to change this file path
        api_data = json.load(f)
    
        #return api keys 
        return api_data["id"], api_data["secret"]
    
    #accepts subreddit, top time limit, and post number limit
    #outputs data frame of post name and url
    def get_top_posts(self, subreddit:str, time:str = "week", limit:int = 10):
        """

        Parameters
        ----------
        subreddit : str
            DESCRIPTION.
        time : str, optional
           (all, day, hour, month, week, year). The default is "week".
        limit : int, optional
            number of posts. The default is 10.

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        #get posts
        posts = self.reddit.subreddit(subreddit).top(time, limit=limit)
        submission_url = []
        submission_title = []
        
        #obtain post data
        for post in posts:
            submission_url.append(post.url)
            submission_title.append(post.title)
        
        return pd.DataFrame({"title":submission_title, "url":submission_url})
    
    
