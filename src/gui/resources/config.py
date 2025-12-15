"""
アプリケーションのデフォルト設定値を定義するモジュール

このモジュールには、アプリケーション全体で使用されるデフォルト値が含まれています。
設定値の一元管理により、変更が必要になった場合に簡単に更新できます。
"""

class AppConfig:
    """アプリケーション全体の設定を管理するクラス"""
    
    # アプリケーション設定
    APP_NAME = "OpenSuperWhisper"
    APP_ORGANIZATION = "OpenSuperWhisper"
    
    # 認証設定
    # NOTE: 互換性のため設定キー自体は main_window.py 側で "api_key" を引き続き使用します。
    DEFAULT_API_KEY = ""  # Azure OpenAI API Key
    DEFAULT_AZURE_OPENAI_ENDPOINT = ""  # e.g. https://{resource}.openai.azure.com/
    DEFAULT_AZURE_OPENAI_API_VERSION = "2024-02-15-preview"
    DEFAULT_AZURE_OPENAI_DEPLOYMENT = ""  # 空の場合は「選択モデルID」を deployment 名として使用
    
    # 機能設定
    DEFAULT_HOTKEY = "ctrl+shift+r"
    DEFAULT_AUTO_COPY = True
    DEFAULT_ENABLE_SOUND = True
    DEFAULT_SHOW_INDICATOR = True
    DEFAULT_MODEL = "gpt-4o-transcribe"
    
    # 言語設定
    DEFAULT_LANGUAGE = ""  # 空文字列は自動検出を意味する
    
    # サウンドファイルパス
    START_SOUND_PATH = "assets/start_sound.wav"
    STOP_SOUND_PATH = "assets/stop_sound.wav"
    COMPLETE_SOUND_PATH = "assets/complete_sound.wav" 