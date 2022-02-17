#!/usr/bin/python
import argparse
import configparser

from apiclient.discovery import build
from apiclient.errors import HttpError


YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
MAX_RESULTS = 50

def youtube_search(options):
    
    # 設定ファイルの読み込み
    config = configparser.ConfigParser()
    config.read('./settings.ini')

    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
        developerKey=config['SETTINGS']['DEVELOPER_KEY'])

    # 検索の実行
    search_response = youtube.search().list(
        q=options.q,
        part="id,snippet",
        maxResults=MAX_RESULTS
    ).execute()

    # 検索結果から動画タイトルを抽出してリスト化
    videos = []
    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            videos.append("%s (%s)" % (search_result["snippet"]["title"],
            search_result["id"]["videoId"]))
    
    # 検索結果のリスト表示
    print("Videos:(%s件)\n" % len(videos), "\n".join(videos), "\n")


if __name__ == "__main__":

    # コマンドライン引数の取得
    parser = argparse.ArgumentParser()
    parser.add_argument("q", help="Search term")
    args = parser.parse_args()

    # キーワードの検索
    try:
        youtube_search(args)
    except HttpError as e:
        print("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))
    finally:
        print("スクリプトを終了します")