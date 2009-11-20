import getopt
from org.apache.lucene.analysis.standard import *;
from org.apache.lucene.analysis import *;
from org.apache.lucene.document import *;
from org.apache.lucene.index import *;
from org.apache.lucene.queryParser import *;
from org.apache.lucene.search import *;
from org.apache.lucene.store import *;
import re
import sys
import urllib
import urllib2
from java.lang import String
from BeautifulSoup import BeautifulSoup


def search(indexpath, term):#{{{
    index = FSDirectory.getDirectory(indexpath)
    q = QueryParser("all", WhitespaceAnalyzer()).parse(term)
    searcher = IndexSearcher(index);
    collector = TopDocCollector( 10 ); #hits per page
    searcher.search(q, collector);
    hits = collector.topDocs().scoreDocs;
    for i in xrange(0, len(hits)):
        docId = hits[i].doc;
        d = searcher.doc(docId);
        print str(i+1), ". " + d.get("infinitive")
    index.close()#}}}

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

def main(argv):
    try:
        SEARCH, CONJ, ADD = 1,2,3
        opts, args = getopt.getopt( argv, "scai:w:", ["search","conjugate", "add", "index=", "word="] )
        action, indexpath, word = None, None, None
        for opt, arg in opts:
            if opt in ("-s", "--search"):
                action = SEARCH
            elif opt in ("-c", "--conjugate"):
                action = CONJ
            elif opt in ("-a", "--add"):
                action = ADD
            elif opt in ("-i", "--index"):
                indexpath = arg
            elif opt in ("-w", "--word"):
                word = arg

        if not word or not indexpath or not action:
            usage()

        if action == SEARCH:
            search(indexpath, word)
        elif action == CONJ:
            print fortext(conjugate(gethtml(word)), word).encode('utf-8')
        elif action == ADD:
            print "add", word

    except getopt.GetoptError:
        usage()
        sys.exit(2)

def usage():
    print "usage!"

if __name__ == '__main__': main(sys.argv[1:])
