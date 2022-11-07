import requests
import json

class LightGroup():

    def __init__(self, id, lightGroupJson, baseUrl):
        self.id = id
        self.lightGroup = lightGroupJson
        self.baseUrl = baseUrl

    def syncState(self):
        r = requests.get(f"{self.baseUrl}/groups/{self.id}", verify=False)
        data = r.json()
        self.lightGroup = data

    def toggle(self):
        self.syncState()
        if self.lightGroup["state"]["all_on"]:
            self.lightsOff()
        else:
            self.lightsOn()

    def lightsOn(self):
        data = {
                   "on": True
               }

        r = requests.put(
            url=f"{self.baseUrl}/groups/{self.id}/action",
            data=json.dumps(data),
            verify=False)

    def lightsOff(self):
        data = {
                   "on": False
               }

        r = requests.put(
            url=f"{self.baseUrl}/groups/{self.id}/action",
            data=json.dumps(data),
            verify=False)

    def brightnessUp(self):
        self.syncState()
        brightness = self.lightGroup["action"]["bri"]
        if brightness <= 254:
            if brightness <= 234:
                brightness += 20
            else:
                brightness = 254

        data = {
            "bri": brightness
        }

        r = requests.put(
            url=f"{self.baseUrl}/groups/{self.id}/action",
            data=json.dumps(data),
            verify=False)

    def brightnessDown(self):
        self.syncState()
        brightness = self.lightGroup["action"]["bri"]
        if brightness >= 0:
            if brightness >= 20:
                brightness -= 20
            else:
                brightness = 0

        data = {
            "bri": brightness
        }

        r = requests.put(
            url=f"{self.baseUrl}/groups/{self.id}/action",
            data=json.dumps(data),
            verify=False)
