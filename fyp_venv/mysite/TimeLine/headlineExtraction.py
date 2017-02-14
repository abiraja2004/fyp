import os
import sys
import django
import json
import logging
import shutil
from django.core.management import call_command     # use call_command
from django.conf import settings                    # use settings.comfigure()
#from pprint import pprint                          # print line by line
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer as LexRankSummarizer
from sumy.summarizers.lsa import LsaSummarizer as LsaSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
import sys

# default language
LANGUAGE = "English"
# number of sentences in the summary
SENTENCES_COUNT  = 3

# export database !!!NOT YET FINISHED!!!
# in command line, we use : python3 manage.py dumpdata news.post > db.json

#settings.configure()                #solving django.core.exceptions.ImproperlyConfigured: Requested setting USE_I18N
#output = open("db.xml", 'w')

## == python3 manage.py dumpdata news.post > db.json in terminal/commandline

## call_command(function, app, ...)
#django.setup()
#call_command('dumpdata', "news", format='xml', indent=4, stdout=output)
#output.close()

output = ""
summary = open("input.txt", "w", encoding = 'utf-8-sig')
file = open("headline_summary.txt", "w", encoding = 'utf-8-sig')
#sys.stdout = summary
date = ""

# filter data
try:
    with open("db.json") as data_file:
        data = json.load(data_file)

    for index in range(len(data)):
        if data[index]["fields"]["pub_date"][:10] != date or index == len(data)-1:
            if date != "" :
                # LexRank algorithm
                local_summary.close()
                sys.stdout = file
                #summarizer = LexRankSummarizer(Stemmer(LANGUAGE))
                summarizer =LsaSummarizer(Stemmer(LANGUAGE))                
                summarizer.stop_words = get_stop_words(LANGUAGE)               
                headline = PlaintextParser.from_file(date + ".txt", Tokenizer(LANGUAGE))

                print(date)
                for sentence in summarizer(headline.document, SENTENCES_COUNT):
                    print(sentence)
                    
            output = output + data[index]["fields"]["pub_date"][:10] + "\n"
            date = data[index]["fields"]["pub_date"][:10]
            local_summary = open(date + ".txt", "w", encoding = 'utf-8-sig')
            #local_summary.write(date + "\n")
        #output = output + data[index]["fields"]["title"] + "\n" + (data[index]["fields"]["pub_date"])[:10] + "\n"

        local_summary.write(str(index) + ")" + data[index]["fields"]["title"] + ".\n")
        output = output + data[index]["fields"]["title"] + ".\n"
except:
    logging.exception("ERROR: filter data")
    

summary.write(output)

summary.close()
local_summary.close()
file.close()
