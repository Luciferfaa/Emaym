from holehe.core import *
from holehe.localuseragent import *


async def treasureclassifieds(email, client, out):
    name = "treasureclassifieds"
    headers = {
        'User-Agent': random.choice(ua["browsers"]["chrome"]),
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en,en-US;q=0.5',
        'Referer': 'https://forum.treasureclassifieds.com/member.php',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://forum.treasureclassifieds.com',
        'DNT': '1',
        'Connection': 'keep-alive',
        'TE': 'Trailers',
    }
    try:
        r = await client.get("https://forum.treasureclassifieds.com/member.php", headers=headers)
        if "Your request was blocked" in r.text or r.status_code != 200:
            out.append({"name": name,
                        "rateLimit": True,
                        "exists": False,
                        "emailrecovery": None,
                        "phoneNumber": None,
                        "others": None})
            return None
    except BaseException:
        out.append({"name": name,
                    "rateLimit": True,
                    "exists": False,
                    "emailrecovery": None,
                    "phoneNumber": None,
                    "others": None})
        return None

    headers['X-Requested-With'] = 'XMLHttpRequest'

    params = {
        'action': 'email_availability',
    }
    try:
        data = {
            'email': email,
            'my_post_key': r.text.split('var my_post_key = "')[1].split('"')[0]
        }
        r = await client.post('https://forum.treasureclassifieds.com/xmlhttp.php', headers=headers, params=params, data=data)
    except BaseException:
        out.append({"name": name,
                    "rateLimit": True,
                    "exists": False,
                    "emailrecovery": None,
                    "phoneNumber": None,
                    "others": None})
        return None
    if "Your request was blocked" not in r.text and r.status_code == 200:
        if "email address that is already in use by another member." in r.text:
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
                    "rateLimit": True,
                    "exists": False,
                    "emailrecovery": None,
                    "phoneNumber": None,
                    "others": None})
