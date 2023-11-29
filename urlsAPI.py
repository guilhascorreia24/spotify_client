

ENDPOINT_PLAYLIST="https://api.spotify.com/v1/playlists/"
def ENDPOINT_PLAYLISTS_USER(user_id): 
    return "https://api.spotify.com/v1/users/"+user_id+"/playlists"
URL_ME="https://api.spotify.com/v1/me"
def ENDPOINT_LIST_PLAYLIST(playlist_id):
    return "https://api.spotify.com/v1/playlists/"+playlist_id


def URL_HISTORY(after,before):
    if after!=None and before==None: return "https://api.spotify.com/v1/me/player/recently-played?after="+after
    elif before!=None and after==None: return "https://api.spotify.com/v1/me/player/recently-played?before="+before
    elif after!=None and before!=None : return "https://api.spotify.com/v1/me/player/recently-played?after="+after+"&before="+before
    return "https://api.spotify.com/v1/me/player/recently-played"