from org.apache.lucene.analysis.standard import *;
from org.apache.lucene.document import *;
from org.apache.lucene.index import *;
from org.apache.lucene.queryParser import *;
from org.apache.lucene.search import *;
from org.apache.lucene.store import *;

def addDoc(w, value):
    doc = Document()
    doc.add(Field("title", value, Field.Store.YES, Field.Index.ANALYZED))
    w.addDocument(doc)

index = FSDirectory.getDirectory('/home/mike/projects/mpobrien_stuff/index/testindex');
w = IndexWriter(index, StandardAnalyzer(), True, IndexWriter.MaxFieldLength.UNLIMITED);
addDoc(w, "Lucene in Action");
addDoc(w, "Lucene for Dummies");
addDoc(w, "Managing Gigabytes");
addDoc(w, "The Art of Computer Science");
w.close();


q = QueryParser("title", StandardAnalyzer()).parse('lucene');
searcher = IndexSearcher(index);
collector = TopDocCollector( 10 ); #hits per page
searcher.search(q, collector);
hits = collector.topDocs().scoreDocs;
print len(hits), hits

for i in xrange(0, len(hits)):
    docId = hits[i].doc;
    d = searcher.doc(docId);
    print str(i+1), ". " + d.get("title")


