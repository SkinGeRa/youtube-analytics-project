import os
from googleapiclient.discovery import build


class Video:
    """Класс для видео"""

    def __init__(self, video_id):
        """Экземпляр инициализируется id видео. Дальше все данные будут подтягиваться по API."""
        try:
            self.API_KEY = os.getenv('YT_API_KEY')
            self.youtube = build('youtube', 'v3', developerKey=self.API_KEY)
            self.video_id = video_id
            self.video = self.youtube.videos().list(id=self.video_id,
                                                    part='snippet,statistics,contentDetails,topicDetails').execute()
            self.title = self.video["items"][0]["snippet"]["title"]
            self.url = f"https://www.youtube.com/channel/{self.video_id}"
            self.viewers = self.video["items"][0]["statistics"]["viewCount"]
            self.like_count = int(self.video["items"][0]["statistics"]["likeCount"])
        except Exception:
            self.title = None
            self.like_count = None
            self.viewers = None
            self.url = None

    def __str__(self):
        return self.title


class PLVideo(Video):
    """Класс для плейлиста"""

    def __init__(self, video_id, playlist_id):
        """Наследует атрибуты класса Video, а также инициализирует id плейлиста"""
        super().__init__(video_id)
        self.playlist_id = playlist_id
