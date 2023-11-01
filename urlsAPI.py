import utilis

ENDPOINT_PLAYLIST="https://api.spotify.com/v1/playlists/"
def ENDPOINT_PLAYLISTS_USER(user_id): 
    return "https://api.spotify.com/v1/users/"+user_id+"/playlists"
URL_ME="https://api.spotify.com/v1/me"
def ENDPOINT_LIST_PLAYLIST(playlist_id):
    return "https://api.spotify.com/v1/playlists/"+playlist_id