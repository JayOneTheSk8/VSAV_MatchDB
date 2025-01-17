import re
import os
from urllib.parse import urlparse, parse_qs, urlsplit
from googleapiclient.discovery import build

yt_service = build('youtube', 'v3', developerKey=os.environ['YOUTUBE_API_KEY'])

def is_youtube_url(url):
    youtube_regex = r'(https?:\/\/)?((www\.)?(youtube(-nocookie)?|youtube.googleapis)\.com.*(v\/|v=|vi=|vi\/|e\/|embed\/|user\/.*\/u\/\d+\/)|youtu\.be\/)([_0-9a-z-]+)'
    youtube_regex_match = re.match(youtube_regex, url)
    return bool(youtube_regex_match)

def get_youtube_video_id(yt_url):
    parsed_url = urlparse(yt_url)
    return parse_qs(parsed_url.query)['v'][0]

# helpful link: https://medium.com/mcd-unison/youtube-data-api-v3-in-python-tutorial-with-examples-e829a25d2ebd
def request_video_details(video_url):
    yt_id = get_youtube_video_id(video_url)
    # call youtube api
    response = yt_service.videos().list(part='snippet', id=yt_id).execute()
    # print(response['items'][0]['snippet'])
    video_details = response['items'][0]['snippet']
    uploader = video_details['channelTitle']
    date_uploaded = video_details['publishedAt']
    video_title = video_details['title']

    return {
        "uploader" : uploader,
        "date_uploaded" : date_uploaded,
        "video_title" : video_title
    }