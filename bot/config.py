import os

class Config:
    BOT_TOKEN=os.environ['BOT_TOKEN']
    SUDOS=os.environ['SUDOS']
    TELEGRAM_APP_HASH=os.environ['TELEGRAM_APP_HASH']
    TELEGRAM_APP_ID=int(os.environ['TELEGRAM_APP_ID'])
    
    if not TELEGRAM_TOKEN:
        raise ValueError(' BOT TOKEN not set')
    
    if not TELEGRAM_APP_HASH:
        raise ValueError("TELEGRAM_APP_HASH not set")

    if not TELEGRAM_APP_ID:
        raise ValueError("TELEGRAM_APP_ID not set")
