import json
import os
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.API_KEY = os.getenv('YT_API_KEY')
        self.youtube = build('youtube', 'v3', developerKey=self.API_KEY)
        self.channel_id = channel_id
        self.channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.title = self.channel["items"][0]["snippet"]["title"]
        self.description = self.channel["items"][0]["snippet"]["description"]
        self.url = f"https://www.youtube.com/channel/{self.channel_id}"
        self.subscriberCount = self.channel["items"][0]["statistics"]["subscriberCount"]
        self.video_count = self.channel["items"][0]["statistics"]["videoCount"]
        self.viewCount = self.channel["items"][0]["statistics"]["viewCount"]


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        info = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(json.dumps(info, indent=2, ensure_ascii=False))
