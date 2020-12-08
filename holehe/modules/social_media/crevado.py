from holehe.core import *
from holehe.localuseragent import *


async def crevado(email, client, out):
    name = "crevado"
    headers = {
        'User-Agent': random.choice(ua["browsers"]["chrome"]),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://crevado.com',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'TE': 'Trailers',
    }

    req = await client.get("https://crevado.com")
    token = req.text.split(
        '<meta name="csrf-token" content="')[1].split('"')[0]

    data = {
        'utf8': '\u2713',
        'authenticity_token': token,
        'plan': 'basic',
        'account[full_name]': '',
        'account[email]': email,
        'account[password]': '',
        'account[domain]': '',
        'account[confirm_madness]': '',
        'account[terms_accepted]': '0',
        'account[terms_accepted]': '1',
    }

    r = await client.post('https://crevado.com/', headers=headers, data=data)
    try:
        msg_error = r.text.split('showFormErrors({"')[1].split('"')[0]
        if msg_error == "account_email":
            errorEMail = r.text.split(
                'showFormErrors({"account_email":{"error_message":"')[1].split('"')[0]
            if errorEMail == "has already been taken":
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
    except BaseException:
        out.append({"name": name,
                    "rateLimit": True,
                    "exists": False,
                    "emailrecovery": None,
                    "phoneNumber": None,
                    "others": None})
