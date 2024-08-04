# my user agent is : Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36
# print(r.html.find('title' , first= True).text) 
# requests-html==0.10.0
# lxml==4.9.1 (first install  this one)



from requests_html import HTMLSession
import spech_to_text

def Weather():
    s  =  HTMLSession()
    query = "india"
    url = f'https://www.google.com/search?q=weather+{query}'
    #what is my user agent --> search in google
    r  = s.get(url , headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/127.0.0.0'})

    #Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/#537.36 Edg/127.0.0.0

    #get an id from the google by inpect the weather page
    temp  = r.html.find('span#wob_tm' , first= True).text
    #print(temp)
    unit = r.html.find('div.vk_bk.wob-unit span.wob_t' , first= True).text
    #print(unit)
    desc  = r.html.find('span#wob_dc' , first= True).text
    #print(desc)
    return temp+" "+unit+" "+ desc
#Weather()