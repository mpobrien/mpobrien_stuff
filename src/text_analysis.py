from org.apache.lucene.analysis import *;
from org.apache.lucene.document import *;
from org.apache.lucene.index import *;
from org.apache.lucene.queryParser import *;
from org.apache.lucene.search import *;
from org.apache.lucene.store import *;
import re
import string
from java.lang import String

stopwords = ['la','el','los','las','de','del','en','que','para','por','con','una','un','y','o','su','sus']
punctuation = re.compile(r'[.?!,":;]-') #TODO: deal with the dash correctly
ws_analyzer = WhitespaceAnalyzer()

def analyze(text, index):
    print "analyzing"
    words = String(text.strip()).split('\s+')
    searcher = IndexSearcher(index);
    for w in words:
        w2 = strip_punctuation(w).strip()
        if not w2 or w2 in stopwords: continue
        print "looking up", w2
        q = QueryParser("all", ws_analyzer).parse(w2)
        collector = TopDocCollector( 3 ); #hits per page
        searcher.search(q, collector);
        hits = collector.topDocs().scoreDocs;
        for i in xrange(0, len(hits)):
            docId = hits[i].doc;
            d = searcher.doc(docId);
            print w2, "might come from the infinitive", d.get("infinitive")



def strip_punctuation(word):
    return filter(lambda x: x not in string.punctuation, word.lower())

if __name__ == '__main__':
    sampletext_file = open('/home/mike/projects/mpobrien_stuff/sampletext.txt','r')
    text = sampletext_file.read()
    print text
    sampletext_file.close()
    index = FSDirectory.getDirectory('/home/mike/projects/mpobrien_stuff/index/wordindex');
    analyze(text, index)
