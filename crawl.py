import urllib, urllib2
from BeautifulSoup import BeautifulSoup

class MissingData(Exception):#{{{
    def __init__(self, message):
        Exception.__init__(self)
        self.message = message
    def __repr__(self):
        return self.message#}}}

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

def conjugate(html):#{{{
    soup = BeautifulSoup( html )
    tags = soup.findAll('strong')
    alltenses = ['Present Indicative:', 'Imperfect:', 'Preterite:', 'Future:', 'Conditional:', 'Imperative:', 'Present Subjunctive:', 'Imperfect Subjunctive:', 'Gerund:','Past Participle:']
    resultsDict = {}
    for t in tags:
        if t.string and t.string in alltenses:
            limit = 7
            if t.string in alltenses[-2:]: limit = 2
            if t.string == alltenses[5]: limit = 6
            key = t.string
            values = t.findAllNext(text=True, limit = limit)[1:]
            values = [v.strip() for v in values]
            resultsDict[key] = values
    return resultsDict#}}}

def fortext(conj, infinitive):#{{{
    alltenses = ['Present Indicative:', 'Imperfect:', 'Preterite:', 'Future:', 'Conditional:', 'Imperative:', 'Present Subjunctive:', 'Imperfect Subjunctive:', 'Gerund:','Past Participle:']
    output_list = [infinitive]
    for t in alltenses:
        results = conj[t]
        if t in (alltenses[-1], alltenses[-2]): 
            if len(results) != 1: raise MissingData(t + ": " + str(len(results)))
        else: 
            if t == alltenses[5]:
                if len(results) != 5:  
                    print t, len(results)
                    raise MissingData(t + ": " + str(len(results)))
            elif len(results) != 6:  
                print t, len(results)
                raise MissingData(t + ": " + str(len(results)))
        output_list += results
    return ' '.join(output_list)#}}}

def doit(file, outfile):
    for line in file:
        try:
            theword = line.strip()
            outline = fortext(conjugate(gethtml(theword)), theword).encode('utf-8')
            outfile.write( outline + '\n' )
        except:
            print line, "skipping"

if __name__ == '__main__':
    infile = open('verbs.txt','r')
    outfile = open('output.txt','w')
    doit(infile, outfile)
