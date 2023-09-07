from datetime import datetime
from typing import List

class SocialChannel:
    def __init__(self, type: str, followers: int):
        self.type = type
        self.followers = followers

class Post:
    def __init__(self, caption: str, timestamp: datetime, channels: List[SocialChannel]):
        self.caption = caption
        self.timestamp = timestamp
        self.channels = channels

class SocialHero:
    def __init__(self):
        self.channels = []
        self.posts = []

    def post_to_youtube(self, channel: SocialChannel, message: str) -> None:
        print(f"Posting to YouTube: {message}")

    def post_to_facebook(self, channel: SocialChannel, message: str) -> None:
        print(f"Posting to Facebook: {message}")

    def post_to_twitter(self, channel: SocialChannel, message: str) -> None:
        print(f"Posting to Twitter: {message}")

    def post_a_message(self, channel: SocialChannel, message: str) -> None:
        if channel.type == "youtube":
            self.post_to_youtube(channel, message)
        elif channel.type == "facebook":
            self.post_to_facebook(channel, message)
        elif channel.type == "twitter":
            self.post_to_twitter(channel, message)

    def process_schedule(self) -> None:
        current_time = datetime.now()
        for post in self.posts:
            if post.timestamp <= current_time:
                for channel in self.channels:
                    self.post_a_message(channel, post.caption)

# Example
if __name__ == "__main__":
    hero = SocialHero()

    youtube_channel = SocialChannel("youtube", 1000)
    facebook_channel = SocialChannel("facebook", 5000)
    twitter_channel = SocialChannel("twitter", 2000)
    
    hero.channels.append(youtube_channel)
    hero.channels.append(facebook_channel)
    hero.channels.append(twitter_channel)

    post1 = Post("Hello!", datetime.now(), [youtube_channel, facebook_channel])
    post2 = Post("Check my new video!", datetime.now(), [youtube_channel, twitter_channel])
    post3 = Post("New stream today!", datetime.now(), [facebook_channel, twitter_channel])

    hero.posts.append(post1)
    hero.posts.append(post2)
    hero.posts.append(post3)

    hero.process_schedule()