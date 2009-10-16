import urllib, urllib2
from BeautifulSoup import BeautifulSoup

def gethtml(word):#{{{
    url = "http://www.conjugation.org/cgi-bin/conj.php"
    "word"
    params = {
             "rb1" : "list", # "table"
             "dpresent_indicative" : "yes",
             "dimperfect" : "yes",
             "dpreterite" : "yes",
             "dfuture" : "yes",
             "dconditional" : "yes",
             "dimperative" : "yes",
             "dp_sub" : "yes",
             "di_sub" : "yes",
             "dgerund" : "yes",
             "dp_participle" : "yes",
             "rb3" : "no", #no (subject pronouns?)
             "rb2" : "ra", #se
            }
    params['word'] = word
    data = urllib.urlencode( params )
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    return response.read()#}}}

def conjugate(html):
    soup = BeautifulSoup( html )
    tags = soup.findAll('strong')
    alltenses = ['Present Indicative:', 'Imperfect:', 'Preterite:', 'Future:', 'Conditional:', 'Imperative:', 'Present Subjunctive:', 'Imperfect Subjunctive:', 'Gerund:','Past Participle:']
    resultsDict = {}
    for t in tags:
        if t.string and t.string in alltenses:
            limit = 6
            if t.string in alltenses[-2:]: limit = 2
            key = t.string
            values = t.findAllNext(text=True, limit = limit)[1:]
            values = [v.encode('windows-1252').strip() for v in values]
            resultsDict[key] = values
    return resultsDict


