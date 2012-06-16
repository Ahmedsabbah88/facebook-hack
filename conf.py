import os

class Config(object):
    DEBUG = True
    TESTING = False
    LOG_LEVEL = os.environ.get('LOG_LEVEL', 'DEBUG')
    FBAPI_APP_ID = os.environ.get('FACEBOOK_APP_ID')
    FBAPI_APP_SECRET = os.environ.get('FACEBOOK_SECRET')
    FBAPI_SCOPE = [
        'user_checkins', 
        'user_photos', 
        'user_activities',
        'user_videos',
        'user_likes', 
        'user_status',
        'user_events',
        'friends_checkins',
        'friends_activities',
        'friends_photos',
        'friends_status',
        'friends_likes',
        'read_stream',
        'read_requests',
        'read_insights',
        'read_friendlists',
        'read_mailbox',
        'status_update',
    ]
