#!/usr/bin/python
import simplejson, sys
from xml.dom.ext import PrettyPrint
from xml.dom.ext.reader.Sax import FromXml
import traceback

from pygments import highlight
from pygments.formatters import Terminal256Formatter
from pygments.lexers import XmlLexer
from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
     Number, Operator, Generic

def main():
    piped_input = sys.stdin.read()
    do_it( piped_input )

def do_it(input):
    try:
        json_data = simplejson.loads( input )
        print simplejson.dumps(json_data, sort_keys=True, indent = 4) 
    except: #it's not json, maybe it's xml?
        try:
            xmllexer = XmlLexer()
            consoleformat = Terminal256Formatter()
            doc = FromXml(input)
            formatted = PrettyPrintFormatter()
            PrettyPrint(doc, formatted)
            print highlight(formatted.output, xmllexer, consoleformat)
        except Exception, e:
            print traceback.print_exc()
            print "Bad XML or File format unrecognized :("
            print input

class PrettyPrintFormatter:
    def __init__(self): self.output = ""
    def write(self, s): self.output += s

if __name__ == '__main__' : main()
