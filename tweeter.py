import tweepy

consumer_key = "QLfgBMSVyNJ8pGBh3ZXmME2F9"
consumer_secret = "V82A0C9tfo29yCxNevEVmDsFbxs55LTFX2jPlK57Xd8cjKZxv3"
access_token = "1309003609-INGH1opatCqsa08wLmj6RvO8bRROflEmziWpBXX"
access_token_secret = "RxZDaVDNNR6AQ5K5PTdTTmKU5Uecb2PspUPt3r0UZ1itx"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

WOEID_ESPANA = 56043544

trends = api.get_place_trends(1)
print(trends)
football_trends = [trend for trend in trends if "football" in trend["name"].lower()]

for trend in football_trends:
    print(trend["name"])