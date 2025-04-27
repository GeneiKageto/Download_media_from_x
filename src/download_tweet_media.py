import os
from datetime import date

async def download_media(client, screen_user_id, count):
    # 親ディレクトリの取得
    parent_dir = os.path.dirname(os.path.dirname(__file__))
    
    # outputsディレクトリのパスを作成し、存在しなければ作成
    outputs_dir = os.path.join(parent_dir, "outputs")
    if not os.path.exists(outputs_dir):
        os.makedirs(outputs_dir)
    
    # 保存先ディレクトリをoutputs配下に作成
    save_dir = os.path.join(outputs_dir, screen_user_id + "_" + str(date.today()))
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    # ユーザーのツイートを取得
    user = await client.get_user_by_screen_name(screen_user_id)
    user_id = user.id
    tweets = await client.get_user_tweets(user_id, tweet_type='Media', count=count)
    
    for i, tweet in enumerate(tweets):
        # tweet.mediaはリスト形式らしいのでfor文で回す
        for j, media in enumerate(tweet.media):
            if media.type == 'photo':
                await media.download(os.path.join(save_dir, f'media_{i}_{j}.jpg'))
            elif media.type in ['animated_gif', 'video']:
                await media.streams[-1].download(os.path.join(save_dir, f'media_{i}_{j}.mp4'))
    print(f"Downloaded media for user ID: {screen_user_id} to directory: {save_dir}")
