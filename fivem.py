import requests, json
class FiveM:
    data = {}
    def __init__(self, ip, port):
        self.setData(ip, port)
    def setData(self, ip, port):
        self.data["ip"] = ip
        self.data["port"] = port
    def getServerInfo(self):
        return requests.get("http://"+self.data["ip"]+":"+self.data["port"]+"/info.json").json()
    def getPlayersInfo(self):
        return requests.get("http://"+self.data["ip"]+":"+self.data["port"]+"/players.json").json()