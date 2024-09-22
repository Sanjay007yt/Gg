import random
import string
import time
import names
import requests
import logging
import discord
from discord.ext import commands

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# List of proxies for rotation
proxies_list = [
    {'http': 'http://43.153.207.93:3128'},
    {'http': 'http://3.70.244.223:8090'},
    {'http': 'http://160.86.242.23:8080'},
    {'http': 'http://51.83.62.245:8080'},
    {'http': 'http://163.172.33.137:4478'},
    {'http': 'http://51.178.149.106:8080'},
    {'http': 'http://35.220.254.137:8080'},
    {'http': 'http://37.187.25.85:80'},
    {'http': 'http://188.121.128.246:10186'},
    {'http': 'http://67.43.227.227:11023'},
    {'http': 'http://211.104.20.205:8080'},
    {'http': 'http://8.219.97.248:80'},
    {'http': 'http://46.252.141.11:8080'},
    {'http': 'http://51.222.161.115:80'},
    {'http': 'http://20.27.86.185:8080'},
    {'http': 'http://18.143.143.176:8090'},
    {'http': 'http://43.134.32.184:3128'},
    {'http': 'http://4.159.28.85:8080'},
    {'http': 'http://47.250.159.65:8443'},
    {'http': 'http://66.65.181.6:8080'},
    {'http': 'http://165.227.253.99:8081'},
    {'http': 'http://67.43.236.19:17293'},
    {'http': 'http://67.43.227.228:23737'},
    {'http': 'http://116.101.29.135:5000'},
    {'http': 'http://103.154.25.94:8080'},
    {'http': 'http://67.43.236.20:10145'},
    {'http': 'http://72.10.160.90:1365'},
    {'http': 'http://4.158.61.174:8080'},
    {'http': 'http://67.43.236.22:22079'},
    {'http': 'http://222.108.214.168:8080'},
    {'http': 'http://218.164.23.136:8080'},
    {'http': 'http://72.10.164.178:1417'},
    {'http': 'http://72.10.160.91:8167'},
    {'http': 'http://218.164.27.125:8080'},
    {'http': 'http://18.231.62.245:3128'},
    {'http': 'http://150.109.244.218:59394'},
    {'http': 'http://4.158.2.131:8080'},
    {'http': 'http://20.44.188.17:3129'},
    {'http': 'http://125.99.106.250:3128'},
    {'http': 'http://178.48.68.61:18080'},
    {'http': 'http://85.172.174.3:3128'},
    {'http': 'http://47.91.65.23:3128'},
    {'http': 'http://47.89.184.18:3128'},
    {'http': 'http://20.44.189.184:3129'},
    {'http': 'http://217.219.45.90:8082'},
    {'http': 'http://67.43.227.226:30373'},
    {'http': 'http://77.232.36.15:1080'},
    {'http': 'http://67.43.227.229:16401'},
    {'http': 'http://18.209.220.0:3128'},
    {'http': 'http://38.242.199.124:8089'},
    {'http': 'http://72.10.160.92:5635'},
    {'http': 'http://185.198.72.98:3128'},
    {'http': 'http://123.126.158.50:80'},
    {'http': 'http://52.172.55.7:80'},
    {'http': 'http://52.13.143.246:80'},
    {'http': 'http://45.119.133.218:3128'},
    {'http': 'http://148.72.140.24:30127'},
    {'http': 'http://67.43.236.18:1853'},
    {'http': 'http://72.10.160.93:13931'},
    {'http': 'http://106.227.95.142:3129'},
    {'http': 'http://54.193.30.143:3128'},
    {'http': 'http://8.216.66.160:3128'},
    {'http': 'http://13.208.173.47:9002'},
    {'http': 'http://38.180.108.184:8888'},
    {'http': 'http://116.105.58.170:10001'},
    {'http': 'http://222.122.110.26:80'},
    {'http': 'http://209.121.164.50:31147'},
    {'http': 'http://47.238.130.212:80'},
    {'http': 'http://38.54.116.9:3128'},
    {'http': 'http://5.189.184.6:80'},
    {'http': 'http://36.89.235.239:3128'},
    {'http': 'http://171.228.172.129:10089'},
    {'http': 'http://8.211.42.167:3128'},
    {'http': 'http://94.183.230.166:3128'},
    {'http': 'http://47.237.92.86:80'},
    {'http': 'http://217.77.102.18:3128'},
    {'http': 'http://87.247.186.40:1081'},
    {'http': 'http://8.213.128.90:443'},
    {'http': 'http://103.171.244.40:8088'},
    {'http': 'http://119.96.113.193:30000'},
    {'http': 'http://176.100.13.15:8080'},
    {'http': 'http://119.96.195.62:30000'},
    {'http': 'http://79.132.139.143:1111'},
    {'http': 'http://20.219.176.57:3129'},
    {'http': 'http://20.204.212.76:3129'},
    {'http': 'http://20.204.212.45:3129'},
    {'http': 'http://112.19.241.37:19999'},
    {'http': 'http://58.240.211.250:7890'},
    {'http': 'http://58.215.177.24:3128'},
    {'http': 'http://185.191.236.162:3128'},
    {'http': 'http://201.151.252.120:80'},
    {'http': 'http://79.121.102.227:8080'},
    {'http': 'http://138.2.64.185:8118'},
    {'http': 'http://52.82.123.144:3128'},
    {'http': 'http://150.230.72.171:80'},
    {'http': 'http://24.106.221.230:53281'},
    {'http': 'http://43.133.59.220:3128'},
    {'http': 'http://120.28.195.40:8282'},
    {'http': 'http://186.215.87.194:6000'},
    {'http': 'http://145.40.97.148:9400'}
]

class ProxyManager:
    def __init__(self, proxies):
        self.proxies = proxies

    def get_random_proxy(self):
        return random.choice(self.proxies)

    def get_proxy(self):
        proxy = self.get_random_proxy()
        logger.info(f"Using proxy: {proxy}")
        return proxy

proxy_manager = ProxyManager(proxies_list)

def get_headers(Country, Language):
    session = requests.Session()
    while True:
        try:
            an_agent = f'Mozilla/5.0 (Linux; Android {random.randint(9, 13)}; {"".join(random.choices(string.ascii_uppercase, k=3))}{random.randint(111, 999)}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36'
            proxy = proxy_manager.get_proxy()
            
            res = session.get("https://www.facebook.com/", headers={
                'user-agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'},
                proxies=proxy, timeout=30)
            
            js_datr = res.text.split('["_js_datr","')[1].split('",')[0]
            r = session.get('https://www.instagram.com/api/v1/web/accounts/login/ajax/', headers={
                'user-agent': an_agent
            }, proxies=proxy, timeout=30).cookies

            headers1 = {
                'authority': 'www.instagram.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': f'{Language}-{Country},en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
                'cookie': f'dpr=3; csrftoken={r["csrftoken"]}; mid={r["mid"]}; ig_nrcb=1; ig_did={r["ig_did"]}; datr={js_datr}',
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': an_agent,
                'viewport-width': '980',
            }
            
            response1 = session.get('https://www.instagram.com/', headers=headers1, proxies=proxy, timeout=30)
            appid = response1.text.split('APP_ID":"')[1].split('"')[0]
            rollout = response1.text.split('rollout_hash":"')[1].split('"')[0]
            
            headers = {
                'authority': 'www.instagram.com',
                'accept': '*/*',
                'accept-language': f'{Language}-{Country},en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': f'dpr=3; csrftoken={r["csrftoken"]}; mid={r["mid"]}; ig_nrcb=1; ig_did={r["ig_did"]}; datr={js_datr}',
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/accounts/signup/email/',
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': an_agent,
                'viewport-width': '360',
                'x-asbd-id': '198387',
                'x-csrftoken': r["csrftoken"],
                'x-ig-app-id': str(appid),
                'x-ig-www-claim': '0',
                'x-instagram-ajax': str(rollout),
                'x-requested-with': 'XMLHttpRequest',
                'x-web-device-id': r["ig_did"],
            }
            return headers
        except Exception as e:
            logger.error(f"Error in get_headers: {e}")

def Get_UserName(Headers, Name, Email):
    try:
        proxy = proxy_manager.get_proxy()
        updict = {"referer": 'https://www.instagram.com/accounts/signup/birthday/'}
        Headers = {key: updict.get(key, Headers[key]) for key in Headers}
        
        while True:
            data = {
                'email': Email,
                'name': Name + str(random.randint(1, 99)),
            }

            response = requests.post(
                'https://www.instagram.com/api/v1/web/accounts/username_suggestions/',
                headers=Headers,
                data=data,
                proxies=proxy,
                timeout=30
            )
            if 'status":"fail' in response.text:
                logger.info(response.text)
            elif 'status":"ok' in response.text:
                logger.info(response.text)
                return random.choice(response.json()['suggestions'])
            else:
                logger.info(response.text)
    except Exception as e:
        logger.error(f"Error in Get_UserName: {e}")

def Send_SMS(Headers, Email):
    try:
        proxy = proxy_manager.get_proxy()
        data = {
            'device_id': Headers['cookie'].split('mid=')[1].split(';')[0],
            'email': Email,
        }

        response = requests.post(
            'https://www.instagram.com/api/v1/accounts/send_verify_email/',
            headers=Headers,
            data=data,
            proxies=proxy,
            timeout=30
        )
        return response.text
    except Exception as e:
        logger.error(f"Error in Send_SMS: {e}")

def Validate_Code(Headers, Email, Code):
    try:
        proxy = proxy_manager.get_proxy()
        updict = {"referer": 'https://www.instagram.com/accounts/signup/emailConfirmation/'}
        Headers = {key: updict.get(key, Headers[key]) for key in Headers}

        data = {
            'code': Code,
            'device_id': Headers['cookie'].split('mid=')[1].split(';')[0],
            'email': Email,
        }

        response = requests.post(
            'https://www.instagram.com/api/v1/accounts/check_confirmation_code/',
            headers=Headers,
            data=data,
            proxies=proxy,
            timeout=30
        )
        return response
    except Exception as e:
        logger.error(f"Error in Validate_Code: {e}")

def Create_Acc(Headers, Email, SignUpCode):
    try:
        proxy = proxy_manager.get_proxy()
        firstname = names.get_first_name()
        UserName = Get_UserName(Headers, firstname, Email)
        Password = firstname.strip() + '@' + str(random.randint(111, 999))

        updict = {"referer": 'https://www.instagram.com/accounts/signup/username/'}
        Headers = {key: updict.get(key, Headers[key]) for key in Headers}

        data = {
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{round(time.time())}:{Password}',
            'email': Email,
            'username': UserName,
            'first_name': firstname,
            'month': random.randint(1, 12),
            'day': random.randint(1, 28),
            'year': random.randint(1990, 2001),
            'client_id': Headers['cookie'].split('mid=')[1].split(';')[0],
            'seamless_login_enabled': '1',
            'tos_version': 'row',
            'force_sign_up_code': SignUpCode,
        }
        logger.info(f"Creating account with data: {data}")

        response = requests.post(
            'https://www.instagram.com/api/v1/web/accounts/web_create_ajax/',
            headers=Headers,
            data=data,
            proxies=proxy,
            timeout=30
        )
        logger.info(response.text)
        if '"account_created":true' in response.text:
            logger.info(f'UserName: {UserName}')
            logger.info(f'PassWord: {Password}')
            return {"username": UserName, "password": Password}
        return False
    except Exception as e:
        logger.error(f"Error in Create_Acc: {e}")

# Set up the Discord bot with intents
intents = discord.Intents.default()
intents.messages = True  # Enable the message intent
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command(name='create_account')
async def create_account(ctx, email: str):
    await ctx.send(f'Creating account for {email}...')
    headers = get_headers(Country='US', Language='en')

    ss = Send_SMS(headers, email)
    if 'email_sent":true' in ss:
        await ctx.send('Verification email sent! Please check your inbox for the code.')
        code_message = await bot.wait_for('message', check=lambda m: m.author == ctx.author)
        a = Validate_Code(headers, email, code_message.content)
        if 'status":"ok' in a.text:
            SignUpCode = a.json()['signup_code']
            success = Create_Acc(headers, email, SignUpCode)
            if success:
                embed = discord.Embed(title="Account created successfully!", color=discord.Color.green())
                embed.add_field(name="Email", value=email, inline=False)
                embed.add_field(name="UserName", value=success['username'], inline=False)
                embed.add_field(name="Password", value=success['password'], inline=False)
                embed.set_footer(text="THIS BOT CREATED BY @BROPRO007")
                
                await ctx.send(embed=embed)
            else:
                await ctx.send('Failed to create account.')
        else:
            await ctx.send('Failed to validate the code.')
    else:
        await ctx.send('Failed to send SMS.')

# Run the bot with your token
TOKEN = 'MTI4NDc0OTIxNjk3OTIyMjYxMg.Gxg5kq.WTsOvoZCnkBoyVV1C4Mibs7RjlwgiyOqY9t0YE'
bot.run(TOKEN)
