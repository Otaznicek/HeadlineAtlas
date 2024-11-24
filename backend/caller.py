import requests
import json

class Caller():
    def __init__(self):
        self.urls = ["https://www.novinky.cz/clanek/krimi-v-plzni-vysetruji-brutalni-vrazdu-mlade-lekarky-podezrelym-je-kolega-40493821","https://www.novinky.cz/tag/valka-v-izraeli-96172","https://www.novinky.cz/clanek/valka-na-ukrajine-rusove-poprve-potvrdili-pritomnost-severokorejskych-vojaku-40493784"]
    def call(self):
        data = {
            "model": "wp-watt-3.52-16k",
            "content": f"Napiš mi lokace o které články {self.urls[0]},{self.urls[1]},{self.urls[2]} pojednávají, napiš mi zeměpisnou šířku, zeměpisnou výšku, a jméno lokace(město nebo země pokud město nevíš), pokud je jméno lokace země tak zeměpisnou výšku a šířku dej do hlavního města dané země, napiš mi to ve formátu json, nepiš nic jiného jenom ten json"
        }
        headers = {
            "Authorization": "Bearer 1ee0e7cd5150414e8950d815292cc750"
        }
        rsp = requests.post("https://beta.webpilotai.com/api/v1/watt", json=data, headers=headers)
        print("status_code:", rsp.status_code)
        return json.loads(rsp.content)

caller = Caller()
print(caller.call())