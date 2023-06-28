import os
from googleapiclient.discovery import build
from src.channel import Channel
import isodate


class PlayList:

    def __init__(self, playlist_id):
        self.API_KEY = os.getenv('YT_API_KEY')
        self.youtube = build('youtube', 'v3', developerKey=self.API_KEY)
        self.playlist_id = playlist_id
        self.playlists_info = Channel.get_service().playlists().list(part='snippet', id=playlist_id).execute()
        print(self.playlists_info)
        self.title = self.playlists_info["items"][0]["snippet"]["title"]
        self.url = f"https://www.youtube.com/playlist?list={self.playlist_id}"

    def total_duration(self):
        pass

    def show_best_video(self):
        pass
