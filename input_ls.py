import attlist as att
import webscrapping as ws
import re

def features(url,webcon):
    x = [[]]
    #URL_LENGTH
    x[0].append(len(url))
    #WHOIS_REG_YEAR
    x[0].append(int(webcon[5][15:19]))
    #UPDATE_YEAR
    x[0].append(int(webcon[4][14:18]))
    #WHOIS_COUNTRY
    for line in webcon:
        if(att.r_country.match(line)):
            temp = line.split(': ')
            break
    string = 'WHOIS_COUNRTY--'+temp[1]
    for i in range(3,46):
        #print(i)
        if(att.li[i] == string):
            x[0].append(1)
        else:
            x[0].append(0)
    #WHOIS_STATE_CITY
    for line in webcon:
        if(att.r_state.match(line)):
            temp = line.split(': ')
            break
    string = 'WHOIS_COUNRTY--'+temp[1]
    for i in range(46,206):
        if(att.li[i] == string):
            x[0].append(1)
        else:
            x[0].append(0)
    #print(i)
    #DOMAIN_NAME
    string = 'DOMAIN_NAME--'+url
    for i in range(206,1139):
        if(att.li[i] == string):
            x[0].append(1)
        else:
            x[0].append(0)
    #print(i)
    return x

#x = features('google.com',ws.tag)
#print(len(x[0]))
