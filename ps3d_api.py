from urllib.parse import urlencode

from requests import get, post


class PS3D:
    def __init__(
            self,
            url="http://pixelstrike3daws.com/",
            platform=11,
            version="8.9.0",
            X_Unity_Version="2020.3.11f1",
            playFabId="XXXXXXXXXXXXXXXX",
            token="XXXXXXXXXXXXXXXX-XXXXX-XXXXXXXXXXXXXXX-H4LgPw5gQp51hLqxNOX05Z5if5mHfXa6tlwTonic8Ms=",
            season=6,
            device_id="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            mobile=1,
            server="na1"
    ):
        self.url = url
        self.platform = platform
        self.version = version
        self.X_Unity_Version = X_Unity_Version
        self.playFabId = playFabId.upper()
        self.token = token
        self.season = season
        self.device_id = device_id.upper()
        self.mobile = mobile
        self.server = server

        self.account = self.get_account()

    def get_version_info(self):
        return get(self.url + "new/version-info2.php?platform=" + str(self.platform) + "&ver=" + self.version,
                   headers={"X-Unity-Version": self.X_Unity_Version}).json()

    def get_account(self):
        return post(self.url + "new/load-account.php?v=" + self.version,
                    headers={"X-Unity-Version": self.X_Unity_Version},
                    data=urlencode({
                        "playFabId": self.playFabId,
                        "sessionTicket": self.playFabId + '--' + self.token,
                        "season": self.season,
                        "hash": self.device_id
                    })).json()

    def get_servers(self):
        return post(self.url + "get-servers.php",
                    headers={"X-Unity-Version": self.X_Unity_Version},
                    data=urlencode({
                        "version": self.version,
                        "mobile": self.mobile
                    })).json()

    def set_status(self, status=1, game=''):
        return post(self.url + "social/set-status.php",
                    headers={"X-Unity-Version": self.X_Unity_Version},
                    data=urlencode({
                        "userID": self.account["userId"],
                        "userHash": self.account["userHash"],
                        "status": status,
                        "game": game,
                        "server": self.server
                    })).text

    def get_news(self):
        return post(self.url + "new/get-news.php?v=" + self.version,
                    headers={"X-Unity-Version": self.X_Unity_Version},
                    data=urlencode({
                        "playFabId": self.playFabId,
                        "sessionTicket": self.playFabId + '--' + self.token
                    })).json()

    def get_online_friends(self):
        return post(self.url + "new/get-online-friends.php?v=" + self.version,
                    headers={"X-Unity-Version": self.X_Unity_Version},
                    data=urlencode({
                        "playFabId": self.playFabId,
                        "sessionTicket": self.playFabId + '--' + self.token
                    })).json()["online"]

    def buy_item(self, item_id=1965):
        return post(self.url + "new/buy-item.php?v=" + self.version,
                    headers={"X-Unity-Version": self.X_Unity_Version},
                    data=urlencode({
                        "playFabId": self.playFabId,
                        "sessionTicket": self.playFabId + '--' + self.token,
                        "itemId": item_id
                    })).json()["code"]

    def validate_purchase(self):
        return post(self.url + "new/validate-purchase.php?v=" + self.version,
                    headers={"X-Unity-Version": self.X_Unity_Version},
                    data=urlencode({
                        "playFabId": self.playFabId,
                        "sessionTicket": self.playFabId + '--' + self.token
                    })).json()["code"]

    def get_invites(self):
        return post(self.url + "clans/get-invites.php",
                    headers={"X-Unity-Version": self.X_Unity_Version},
                    data=urlencode({
                        "userID": self.account["userId"],
                        "userHash": self.account["userHash"]
                    })).json()["invites"]

    def search_clans(self, clan="clan"):
        return post(self.url + "clans/search-clans.php",
                    headers={"X-Unity-Version": self.X_Unity_Version},
                    data=urlencode({
                        "userID": self.account["userId"],
                        "userHash": self.account["userHash"],
                        "search": clan
                    })).json()["clans"]

    def get_leaderboards(self, clanID=-1):
        return post(self.url + "clans/get-leaderboards.php",
                    headers={"X-Unity-Version": self.X_Unity_Version},
                    data=urlencode({
                        "clanID": clanID
                    })).json()

    def get_clan(self, clanID=1):
        return post(self.url + "clans/get-clan.php",
                    headers={"X-Unity-Version": self.X_Unity_Version},
                    data=urlencode({
                        "userID": self.account["userId"],
                        "userHash": self.account["userHash"],
                        "clanID": clanID
                    })).json()

    def get_profile(self, otherID=1):
        return post(self.url + "social/get-profile.php",
                    headers={"X-Unity-Version": self.X_Unity_Version},
                    data=urlencode({
                        "userID": self.account["userId"],
                        "userHash": self.account["userHash"],
                        "otherID": otherID
                    })).json()

    def follow(self, otherID=1):
        return post(self.url + "social/follow.php",
                    headers={"X-Unity-Version": self.X_Unity_Version},
                    data=urlencode({
                        "userID": self.account["userId"],
                        "userHash": self.account["userHash"],
                        "otherID": otherID
                    }))

    def unfollow(self, otherID=1):
        return post(self.url + "social/unfollow.php",
                    headers={"X-Unity-Version": self.X_Unity_Version},
                    data=urlencode({
                        "userID": self.account["userId"],
                        "userHash": self.account["userHash"],
                        "otherID": otherID
                    }))

    def load_stats(self, playerId=1):
        return post(self.url + "new/load-stats.php?v=" + self.version,
                    headers={"X-Unity-Version": self.X_Unity_Version},
                    data=urlencode({
                        "playFabId": self.playFabId,
                        "sessionTicket": self.playFabId + '--' + self.token,
                        "playerId": playerId
                    })).json()

    def load_following(self):
        return post(self.url + "new/load-following.php?v=" + self.version,
                    headers={"X-Unity-Version": self.X_Unity_Version},
                    data=urlencode({
                        "playFabId": self.playFabId,
                        "sessionTicket": self.playFabId + '--' + self.token,
                        "userId": self.account["userId"]
                    })).json()

    def update_display_name(self, displayName="TonicBoomerKewl"):
        return post(self.url + "new/update-display-name.php?v=" + self.version,
                    headers={"X-Unity-Version": self.X_Unity_Version},
                    data=urlencode({
                        "playFabId": self.playFabId,
                        "sessionTicket": self.playFabId + '--' + self.token,
                        "displayName": displayName
                    })).json()["code"]

    def sync_data(
            self,
            rank=1,
            prestige=0,
            display_name="TonicBoomerKewl",
            hat=-1,
            hatSkin=-1,
            trail=-1,
            gear=-1,
            gearSkin=-1,
            boots=-1,
            bootsSkin=-1,
            coins=0,
            credits_=0,
            pic='',
            skin=699,
            custom_skin=0,
            skin_type=0
    ):
        return post(self.url + "social/sync-data-5-5-0.php",
                    headers={"X-Unity-Version": self.X_Unity_Version},
                    data=urlencode({
                        "userID": self.account["userId"],
                        "userHash": self.account["userHash"],
                        "rank": rank,
                        "prestige": prestige,
                        "display_name": display_name,
                        "hat": hat,
                        "hatSkin": hatSkin,
                        "trail": trail,
                        "gear": gear,
                        "gearSkin": gearSkin,
                        "boots": boots,
                        "bootsSkin": bootsSkin,
                        "coins": coins,
                        "credits": credits_,
                        "pic": pic,
                        "skin": skin,
                        "custom_skin": custom_skin,
                        "skin_type": skin_type
                    }))

    def get_daily(self, gameMode="freeforall"):
        return post(self.url + "leaderboards/get-daily.php",
                    headers={"X-Unity-Version": self.X_Unity_Version},
                    data=urlencode({
                        "gameMode": gameMode
                    })).json()

    def get_currency(self):
        return post(self.url + "new/get-currency.php?v=" + self.version,
                    headers={"X-Unity-Version": self.X_Unity_Version},
                    data=urlencode({
                        "playFabId": self.playFabId,
                        "sessionTicket": self.playFabId + '--' + self.token
                    })).json()

    def open_case(self, parts=0):
        return post(self.url + "new/open-case.php?v=" + self.version,
                    headers={"X-Unity-Version": self.X_Unity_Version},
                    data=urlencode({
                        "playFabId": self.playFabId,
                        "sessionTicket": self.playFabId + '--' + self.token,
                        "parts": parts
                    })).json()

    def claim_free_case(self):
        return post(self.url + "new/claim-free-case.php?v=" + self.version,
                    headers={"X-Unity-Version": self.X_Unity_Version},
                    data=urlencode({
                        "playFabId": self.playFabId,
                        "sessionTicket": self.playFabId + '--' + self.token
                    })).json()

    def get_roster(self, clanID=1):
        return post(self.url + "clans/get-roster.php",
                    headers={"X-Unity-Version": self.X_Unity_Version},
                    data=urlencode({
                        "userID": self.account["userId"],
                        "userHash": self.account["userHash"],
                        "clanID": clanID
                    })).json()

    # BONUS API:
    @staticmethod
    def get_gameguardian_info(ver="101.1", lang="en_US"):
        return get("https://gameguardian.net/GG_logs/version.php?v=" + ver + "&l=" + lang + "&t=~~~" + lang + "~~~") \
            .text
