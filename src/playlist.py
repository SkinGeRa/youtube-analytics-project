import os
from googleapiclient.discovery import build
# import isodate


class PlayList:

    def __init__(self, playlist_id):
        self.API_KEY = os.getenv('YT_API_KEY')
        self.youtube = build('youtube', 'v3', developerKey=self.API_KEY)
        self.playlist_id = playlist_id
        self.playlists_info = self.youtube.playlists().list(part='snippet', id=playlist_id).execute()
        self.playlist_videos = self.youtube.playlistItems().list(playlistId=playlist_id,
                                                                 part='contentDetails, snippet',
                                                                 maxResults=50,
                                                                 ).execute()
        self.video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.playlist_videos['items']]
        self.video_response = self.youtube.videos().list(part='contentDetails,statistics',
                                                         id=','.join(self.video_ids)
                                                         ).execute()
        self.title = self.playlists_info["items"][0]["snippet"]["title"]
        self.url = f"https://www.youtube.com/playlist?list={self.playlist_id}"

    def total_duration(self):
        pass

    def show_best_video(self):
        max_liked = 0
        most_liked_video = 0
        for video in self.video_response['items']:
            if int(video['statistics']['likeCount']) > max_liked:
                most_liked_video = video['id']
                max_liked = int(video['statistics']['likeCount'])

        return f"https://youtu.be/{most_liked_video}"
