import time, requests, json, urllib.parse, hashlib, random, uuid


class TTCookies:
    def __init__(self, session: requests.Session, data: str):
        self.session = session

        self.sdk_version = "2"
        self.passport_sdk_version = "19"
        self.xtt_dm_status = "login=0;ct=0"
        self.host = "api16-va.tiktokv.com"
        self.user_agent = "okhttp/3.10.0.1"
        self.data = data
        self.app_version = "19.1.3"

        self.devices = [
            "SM-E426B",
            "SM-M326B",
            "SM-A528B",
            "SM-F711B",
            "SM-F926B",
            "SM-A037G",
            "SM-A225F",
            "SM-A226B",
            "SM-M426B",
            "SM-A525F",
        ]

    def unix(self, spoof: int = 0) -> str:
        if spoof == 0:
            _unix = str(int(time.time()))
        else:
            _unix = str(round(time.time(), spoof)).replace(".", "")
        return _unix

    def stub(self):
        _stub = str(hashlib.md5(self.data.encode()).hexdigest()).upper()
        return _stub

    def headers(self):
        _headers = {
            "x-ss-stub": self.stub(),
            "accept-encoding": "gzip",
            "passport-sdk-version": self.passport_sdk_version,
            "sdk-version": self.sdk_version,
            "x-ss-req-ticket": self.unix(spoof=3),
            "x-tt-dm-status": self.xtt_dm_status,
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "host": self.host,
            "connection": "Keep-Alive",
            "user-agent": self.user_agent,
        }

        return _headers

    def params(self):
        params = {
            "passport-sdk-version": self.passport_sdk_version,
            "os_api": "25",
            "device_type": random.choices(self.devices),
            "ssmix": "a",
            "manifest_version_code": "2021901030",
            "dpi": "320",
            "carrier_region": "IE",
            "uoo": "0",
            "region": "US",
            "carrier_region_v2": "310",
            "app_name": "musical_ly",
            "version_name": self.app_version,
            "timezone_offset": "7200",
            "ts": self.unix(),
            "ab_version": self.app_version,
            "cpu_support64": "false",
            "ac2": "wifi",
            "ac": "wifi",
            "app_type": "normal",
            "host_abi": "armeabi-v7a",
            "channel": "googleplay",
            "update_version_code": "2021901030",
            "_rticket": self.unix(spoof=3),
            "device_platform": "android",
            "iid": random.randint(1000000000000000000, 9999999999999999999),
            "build_number": self.app_version,
            "locale": "en",
            "op_region": "IE",
            "version_code": str(self.app_version).replace(".", "0"),
            "timezone_name": "Africa/Harare",
            "cdid": str(uuid.uuid4()),
            "openudid": "0e96eaebc0c2e44f",
            "device_id": random.randint(1000000000000000000, 9999999999999999999),
            "sys_region": "US",
            "app_language": "en",
            "resolution": "900*1600",
            "device_brand": "samsung",
            "language": "en",
            "os_version": "7.1.2",
            "aid": "1233",
            "mcc_mnc": "31002",
        }

        return str(urllib.parse.urlencode(params))
    
    def load_cookies(self):

        req = self.session.post(
            url=(
                "https://"
                + "api16-va.tiktokv.com"
                + "/passport/user/login/?"
                + self.params()
            ),
            headers=self.headers(),
            data = self.data
        )

if __name__ == "__main__":
    sess = requests.Session()
    TTCookies(
        session = sess,
        data = "password=&account_sdk_source=app&username=&mix_mode=1&multi_login=1",
    ).load_cookies()

    print(
        json.dumps(
            sess.cookies.get_dict(), 
            indent=4
        )
    )
