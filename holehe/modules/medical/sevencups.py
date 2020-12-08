from holehe.core import *
from holehe.localuseragent import *


async def sevencups(email, client, out):
    name = "sevencups"
    headers = {
        'User-Agent': random.choice(ua["browsers"]["chrome"]), 'DNT': '1',
        'Connection': 'keep-alive', 'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Host': 'www.7cups.com', 'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'https://www.7cups.com',
        'Accept-Encoding': 'gzip, name=""late, br',
        'Referer': 'https://www.7cups.com/listener/CreateAccount.php', 'TE': 'Trailers',
        'Content-Type': 'multipart/form-data; boundary=---------------------------'

    }

    data = '-----------------------------\r\nContent-Disposition: form-data; name="email"\r\n\r\n' + email + '\r\n-----------------------------\r\nContent-Disposition: form-data; name="passwd"\r\n\r\n\r\n-----------------------------\r\nContent-Disposition: form-data; name="dobMonth"\r\n\r\n12\r\n-----------------------------\r\nContent-Disposition: form-data; name="dobDay"\r\n\r\n11\r\n-----------------------------\r\nContent-Disposition: form-data; name="dobYear"\r\n\r\n2010\r\n-----------------------------\r\nContent-Disposition: form-data; name="orgPass"\r\n\r\n\r\n-----------------------------\r\nContent-Disposition: form-data; name="data-request-datatype"\r\n\r\njson\r\n-----------------------------\r\nContent-Disposition: form-data; name="submit-value"\r\n\r\nnull\r\n-------------------------------\r\n'

    r = await client.post(
        'https://www.7cups.com/listener/CreateAccount.php',
        data=data,
        headers=headers)
    if r.status_code == 200:
        if "Account already exists with this email address" in r.text:
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
