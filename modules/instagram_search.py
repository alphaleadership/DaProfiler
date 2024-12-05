import requests, bs4
from bs4      import BeautifulSoup

import requests,bs4
from bs4 import BeautifulSoup


# EXCLUSIVE MODULE TO DAPROFILER

def getInstagramEmailFromBio(username):
    bios = []
    
    url = "https://smihub.com/v/{}".format(username)

    r = requests.get(url=url, timeout=60)
    page = r.content.decode()
    features = "html.parser"
    soup = BeautifulSoup(page,features)

    bioo = str(soup.find('div',{'class':'user__info-desc'}))

    bioo = bioo.replace('<div','').replace('</div>','').replace('class="user__info-desc">','').strip()

    while "<br/" in bioo:
        bioo = bioo.replace('<br/','\n')

    while ">" in bioo:
        bioo = bioo.replace(">",'')
    
    bios.append(bioo)

    ethnical_origins = [
        ('🇫🇷','France'),
        ('🇨🇭','Swiss'),
        ('🇨🇳','China'),
        ('🇧🇪','Belgium'),
        ('🇦🇱','Albania'),
        ('🇧🇬','Bulgaria'),
        ('🇧🇷','Brazil'),
        ('🇨🇦','Canada'),
        ('🇩🇪','Germany'),
        ('🇮🇱','Israel'),
        ('🇵🇸','Palestine'),
        ('🇺🇸','United States'),
        ('🇵🇹','Portugal'),
        ('🇱🇹','Lithuania'),
        ('🇵🇱','Poland'),
        ('🇷🇺','Russia'),
        ('🇪🇸','Spain'),
        ('🇹🇷','Turkey'),
        ('🇩🇿','Algeria'),
        ('🇲🇦','Morocco'),
        ('🇬🇵','Guadeloupe'),
        ('🇮🇳','India'),
        ('🇱🇺','Luxembourg'),
        ('🇳🇪','Niger'),
        ('🇳🇬','Nigeria'),
        ('🇶🇦','Quatar'),
        ('🇷🇪','Réunion'),
        ('🇷🇴','Romania'),
        ('🇹🇳','Tunisia'),
        ('🇾🇹','Mayotte'),
        ('🇿🇦','South Africa'),
        ('🇲🇽','Mexico'),
        ('🇨🇿','Czech Republic'),
        ('🇯🇵','Japan'),
        ('🇰🇪','Kenya'),
        ('🇰🇵','North Korea'),
        ('🇰🇷','South Korea'),
        ('🇯🇲','Jamaica'),
        ('🇮🇪','Ireland'),
        ('🇬🇷','Greece')
    ]

    for bio in bios:
        lines = bio.split('\n')

        emailss = [
            '@icloud.com',
            '@gmail.com',
            '@gmx.fr',
            '@yahoo.fr',
            '@yahoo.com',
            '@outlook.com'
            '@outlook.fr',
            '@hotmail.fr',
            '@hotmail.com',
            '@live.fr',
            '@live.com',
            '@sfr.fr',
            '@orange.fr',
            '@free.fr',
            '@aol.com',
            '@wanadoo.fr',
            '@neuf.fr',
            '@laposte.net',
            '@yandex.ru',
            '@club-internet.fr',
            '@msn.com',
            '@influencelife.fr',
            '@shaunaevents.com',
            '@we-events.fr',
            '@nabillapro.com',
            '@facebook.com',
            '@protonmail.com',
            '@protonmail.ch',
            '@thepauseagency.com',
            '@alexotime.com'
        ]

        bio_infos       = {}
        emails_final    = []
        snapchat_final  = []
        paypals         = []
        best_friend     = []
        ages            = []
        love_date_since = []
        school_list     = []
        city_list       = []
        lgbt_points     = []
        fb_list         = []
        twitter_list    = []
        flag_list       = []

        for line in lines:
            line = line.replace('</a','').replace('<a href="/v','').replace('<a href="/t/','')
            line = line.lower()
            for flagos in ethnical_origins:
                flag, country_full = flagos
                if flag in line:
                    flag_list.append(country_full)
            temp_list_love = []
            for chars in line:
                if chars == "/":
                    temp_list_love.append('.')
            if "🏳️‍🌈" in line or "🏳️‍⚧️" in line:
                lgbt_points.append('.')
            if "facebook" in line:
                if ":" in line:
                    line = line.split(':')[1]
                fb_list.append(line)
            if "twitter" in line:
                if ":" in line:
                    line = line.split(':')[1]
                twitter_list.append(line)
            if len(temp_list_love) == 2:
                love_date_since.append(line)
            if "📍" in line or "📌" in line:
                city_list.append(line.replace('📍','').replace('📌','').replace(':',''))
            if "snapchat" in line or "snap" in line or "👻" in line:
                line = line.replace('👻','').strip()
                if ":" in line:
                    line = line.split(':')[1].strip()
                snapchat_final.append(line)
            if "📚" in line or "🎓" in line:
                school_list.append(line.replace('📚','').replace('🎓','').strip())
            if "yo" in line or "years old" in line or "years" in line or "🎂" in line or "anniv" in line:
                if "🎂" in line:
                    line = line.replace('🎂','')
                    if ":" in line:
                        line = line.split(':')[1]
                    ages.append(line)
                else:
                    try:
                        age = int(line.split("y")[0].strip())
                        ages.append(str(age))
                    except ValueError:
                        ages.append('Verify by yourself')
            if "paypal.me/" in line:
                paypal = ("paypal.me/"+line.split("paypal.me/")[1])
                paypals.append(paypal)
            if "@" in line:
                line = line.replace('📩','')
                temp_list_emails = []
                if "/" in line and '"' in line:
                    line = (line.replace('/','@').split('"')[0])
                    temp_list_emails.append('.')
                    domain = '@'+line.split('@')[1]
                    if "." not in domain:
                        line = "@"+line.split("@")[1]
                        if " " in line:
                            line = line.split(' ')[0]
                        best_friend.append(line)
                    else:
                        for i in emailss:
                            if domain == i:
                                if line not in emails_final:
                                    if ":" in line:
                                        line = line.split(':')[1].strip()
                                    emails_final.append(line)
                """
                aaa = ("@"+line.split('@')[1])
                for i in emailss:
                    if aaa == i:
                        temp_list_emails.append('.')
                        emails_final.append(line)
                if len(temp_list_emails) == 0:
                    best_friend.append(aaa.replace('</a',''))
                """
        if len(flag_list) == 0:
            bio_infos['origins'] = None
        else:
            bio_infos['origins'] = flag_list
        if len(fb_list) == 0:
            bio_infos['fb_list'] = None
        else:
            bio_infos['fb_list'] = fb_list
        if len(twitter_list) == 0:
            bio_infos['twitter_list'] = None
        else:
            bio_infos['twitter_list'] = twitter_list
        if len(lgbt_points) == 0:
            bio_infos['lgbt_points'] = None
        else:
            bio_infos['lgbt_points'] = "a"
        if len(city_list) == 0:
            bio_infos['city_list'] = None
        else:
            bio_infos['city_list'] = city_list
        if len(school_list) == 0:
            bio_infos['school'] = None
        else:
            bio_infos['school'] = school_list[0]
        if len(snapchat_final) == 0:
            bio_infos['snapchat'] = None
        else:
            bio_infos['snapchat'] = snapchat_final[0].replace('snapchat','').replace('snap','').replace(':','').strip()
        if len(best_friend) == 0:
            bio_infos['best_friend'] = None
        else:
            bio_infos['best_friend'] = best_friend
        if len(ages) == 0:
            bio_infos['age'] = None
        else:
            bio_infos['age'] = str(ages[0])
        if len(emails_final) == 0:
            bio_infos['emails'] = None
        else:
            bio_infos['emails'] = emails_final
        if len(love_date_since) == 0:
            bio_infos['love_date'] = None
        else:
            bio_infos['love_date'] = love_date_since[0]
        if len(paypals) == 0:
            bio_infos['paypal'] = None
        else:
            bio_infos['paypal'] = paypals[0]
        return bio_infos

def ig_search(name,pren):
    url = "https://smihub.com/search?query={}+{}".format(pren,name)

    r = requests.get(url=url, timeout=60)
    page = r.content.decode()
    features = "html.parser"
    soup = BeautifulSoup(page,features)

    profiles = []

    profiless = soup.find_all('div',{'class':'content__text'})
    for i in profiless[0:10]:
        i = str(i)
        username = (i.split('</a><p>')[1].replace('</p></div>',''))
        at_username = (i.split('</a><p>')[0].split('Instagram\'s posts" class="profile-name-link" href="')[1].split('">')[1])
        profile_formated = ('{}\t| {}'.format(at_username,username))
        if name.lower() in profile_formated.lower() and name.lower() in profile_formated.lower():
            profiles.append(str(profile_formated))
    return profiles
