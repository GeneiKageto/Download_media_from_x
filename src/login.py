import os
import json

async def login(client):
    cookie_path = os.path.join(os.path.dirname(__file__), 'cookies.json')
    if os.path.exists(cookie_path):
        client.load_cookies(cookie_path)
    else:
        # 認証情報を親ディレクトリのlogin_config.jsonから読み込み
        with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'login_config.json'), 'r') as f:
            config = json.load(f)
        await client.login(auth_info_1=config["auth_info_1"],
                           auth_info_2=config["auth_info_2"],
                           password=config["password"])
        client.save_cookies(cookie_path)
