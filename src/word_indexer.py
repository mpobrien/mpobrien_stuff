from org.apache.lucene.analysis.standard import *;
from org.apache.lucene.analysis import *;
from org.apache.lucene.document import *;
from org.apache.lucene.index import *;
from org.apache.lucene.queryParser import *;
from org.apache.lucene.search import *;
from org.apache.lucene.store import *;
import re
from java.lang import String

alltenses = [('present',6),
             ('imperfect',6),
             ('preterite',6),
             ('future',6),
             ('conditional',6),
             ('imperative',5),
             ('present_sub',6),
             ('imperfect_sub',6),
             ('gerund',1),
             ('pastpart',1) ]

pronouns = ["i", "youinformal", "hesheyou", "we", "youvos", "theyyoupl"]



def indexfile(f, w):
    i = 0
    for line in f:
        words = re.split('\s*',line.strip())
        if len(words) != 50:
            print "skipping " , words
            print len(words)
            continue
        else:
            d = createDoc(words)
            w.addDocument( d )
        print i
        i += 1

def createDoc(words):
    doc = Document()
    doc.add(Field("infinitive", words[0], Field.Store.YES, Field.Index.UN_TOKENIZED))
    start_word = 1
    for tensename, num_words in alltenses:
        if num_words == 6: temp_pronouns = pronouns
        elif num_words == 5: temp_pronouns = pronouns[1:]
        else: temp_pronouns = [""] * num_words
        for i, w in enumerate(words[start_word:start_word+num_words]):
            fieldname = '_'.join((tensename, temp_pronouns[i]))
            doc.add(Field(fieldname, w, Field.Store.YES, Field.Index.UN_TOKENIZED))
        doc.add(Field("all", ' '.join(words), Field.Store.NO, Field.Index.TOKENIZED))
    return doc

print "here we go"

if __name__ == '__main__':
    print "opening index"
    index = FSDirectory.getDirectory('/home/mike/projects/mpobrien_stuff/index/wordindex');
    #w = IndexWriter(index, WhitespaceAnalyzer(), True, IndexWriter.MaxFieldLength.UNLIMITED);
    #rawdata = open('/home/mike/projects/mpobrien_stuff/output.txt','r')
    #indexfile(rawdata, w)
    #w.close();

    q = QueryParser("all", WhitespaceAnalyzer()).parse('une')
    searcher = IndexSearcher(index);
    collector = TopDocCollector( 10 ); #hits per page
    searcher.search(q, collector);
    hits = collector.topDocs().scoreDocs;
    for i in xrange(0, len(hits)):
        docId = hits[i].doc;
        d = searcher.doc(docId);
        print str(i+1), ". " + d.get("infinitive")

