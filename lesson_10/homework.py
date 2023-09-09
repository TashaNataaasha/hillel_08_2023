from abc import ABC, abstractmethod
from typing import List
from time import time

class SocialChannel(ABC):
    def __init__(self, name: str, followers: int):
        self.name = name
        self.followers = followers

    @abstractmethod
    def post_message(self, message: str):
        pass

class YouTubeChannel(SocialChannel):
    def post_message(self, message: str):
        print(f"Posting on YouTube: {message}")

class FacebookChannel(SocialChannel):
    def post_message(self, message: str):
        print(f"Posting on Facebook: {message}")

class TwitterChannel(SocialChannel):
    def post_message(self, message: str):
        print(f"Posting on Twitter: {message}")

class Post:
    def __init__(self, message: str, timestamp: int):
        self.message = message
        self.timestamp = timestamp

def process_schedule(posts: List[Post], channels: List[SocialChannel]) -> None:
    current_time = time()  
    for post in posts:
        if post.timestamp <= current_time:
            for channel in channels:
                channel.post_message(post.message)

# Example:


youtube_channel = YouTubeChannel("youtube", 1200000)
facebook_channel = FacebookChannel("facebook", 500000)
twitter_channel = TwitterChannel("twitter", 200000)


posts = [
    Post("Check out my new video!", 1630848000),
    Post("Exciting news coming tomorrow!", 1630934400),  
]


channels = [youtube_channel, facebook_channel, twitter_channel]


process_schedule(posts, channels)