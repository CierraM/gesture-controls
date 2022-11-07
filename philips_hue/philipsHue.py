import requests
from philips_hue.lightGroup import LightGroup


class PhilipsHue():
    def __init__(self, userId):
        self.userId = userId
        self.baseUrl = f"https://192.168.0.81/api/{userId}"
        self.lightGroups = {}
        self.getLightGroups()

    def getLightGroups(self):
        r = requests.get(f"{self.baseUrl}/groups", verify=False)
        data = r.json()
        for key, value in data.items():
            name = value["name"]
            lightGroup = LightGroup(key, value, self.baseUrl)
            self.lightGroups[name] = lightGroup

