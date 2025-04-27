from src.login import login
from src.download_tweet_media import download_media
import asyncio
from twikit import Client

screen_user_id = input("メディア欄をぶっこ抜きたい人のユーザーidを@なしで入力してね！ : ")
count = int(input(f"{screen_user_id}のツイートを何個前まで探す？ : "))

client = Client("ja-JP")

async def main():
    await login(client)
    await download_media(client, screen_user_id, count)
    print("Media download process completed.")

asyncio.run(main())
