import json
import os
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id):
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.API_KEY = os.getenv('YT_API_KEY')
        self.youtube = build('youtube', 'v3', developerKey=self.API_KEY)
        self.__channel_id = channel_id
        self.channel = self.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        self.title = self.channel["items"][0]["snippet"]["title"]
        self.description = self.channel["items"][0]["snippet"]["description"]
        self.url = f"https://www.youtube.com/channel/{self.__channel_id}"
        self.subscriber_count = self.channel["items"][0]["statistics"]["subscriberCount"]
        self.video_count = self.channel["items"][0]["statistics"]["videoCount"]
        self.view_count = self.channel["items"][0]["statistics"]["viewCount"]

    def __str__(self):
        """Возвращаем название и ссылку на канал по шаблону `<название_канала> (<ссылка_на_канал>)"""
        return f"{self.title} ({self.url})"

    def __add__(self, other):
        """Используем метод для операции сложения"""
        return int(self.subscriber_count) + int(other.subscriber_count)

    def __sub__(self, other):
        """Используем метод для операции вычитания"""
        return int(self.subscriber_count) - int(other.subscriber_count)

    def __gt__(self, other):
        """Используем метод для операции сравнения «меньше»"""
        return int(self.subscriber_count) > int(other.subscriber_count)

    def __ge__(self, other):
        """Используем метод для операции сравнения «меньше или равно»"""
        return int(self.subscriber_count) >= int(other.subscriber_count)

    def __lt__(self, other):
        """Используем метод для операции сравнения «больше»"""
        return int(self.subscriber_count) < int(other.subscriber_count)

    def __le__(self, other):
        """Используем метод для операции сравнения «больше или равно»"""
        return int(self.subscriber_count) <= int(other.subscriber_count)

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))

    @property
    def channel_id(self):
        return self.__channel_id

    @classmethod
    def get_service(cls):
        """Получаем объект для работы с API вне класса"""
        api_key: str = os.getenv('YT_API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube

    def to_json(self, filename):
        """Создаем файл json с данными по каналу"""
        with open(filename, 'w', encoding="utf-8") as json_file:
            json.dump(self.channel, json_file, indent=2, ensure_ascii=False)
