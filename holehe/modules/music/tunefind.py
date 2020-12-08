from holehe.core import *
from holehe.localuseragent import *


async def tunefind(email, client, out):
    name = "tunefind"
    headers = {
        'User-Agent': random.choice(ua["browsers"]["firefox"]),
        'Referer': 'https://www.tunefind.com/',
        'x-tf-react': 'true',
        'Origin': 'https://www.tunefind.com',
        'Connection': 'keep-alive',
        'Content-Type': 'multipart/form-data; boundary=---------------------------'
    }
    r = await client.get("https://www.tunefind.com/user/join", headers=headers)
    try:
        crsf_token = r.text.split('"csrf-token" content="')[1].split('"')[0]
    except BaseException:
        out.append({"name": name,
                    "rateLimit": True,
                    "exists": False,
                    "emailrecovery": None,
                    "phoneNumber": None,
                    "others": None})
        return None
    data = '$-----------------------------\r\nContent-Disposition: form-data; name="username"\r\n\r\n\r\n-----------------------------\r\nContent-Disposition: form-data; name="email"\r\n\r\n' + \
        str(email) + '\r\n-----------------------------\r\nContent-Disposition: form-data; name="password"\r\n\r\n\r\n-------------------------------\r\n'
    r = await client.post('https://www.tunefind.com/user/join', headers=headers, data=data)
    if "email" in r.json()["errors"].keys():
        if "Someone is already registered with that email address" in str(
                r.json()["errors"]["email"]):
            out.append({"name": name,
                        "rateLimit": False,
                        "exists": True,
                        "emailrecovery": None,
                        "phoneNumber": None,
                        "others": None})
        else:
            out.append({"name": name,
                        "rateLimit": False,
                        "exists": False,
                        "emailrecovery": None,
                        "phoneNumber": None,
                        "others": None})
    else:
        out.append({"name": name,
                    "rateLimit": False,
                    "exists": False,
                    "emailrecovery": None,
                    "phoneNumber": None,
                    "others": None})
