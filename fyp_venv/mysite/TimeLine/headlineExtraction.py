import os
import sys
import django
import json
import logging
import shutil
from django.core.management import call_command     # use call_command
from django.conf import settings                    # use settings.comfigure()
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
# File Not File error handling
error_to_catch = getattr(__builtins__,'FileNotFoundError', IOError)

Dir = "./TimeLine/RawData/"

# export database !!!NOT YET FINISHED!!!
# in command line, we use : python3 manage.py dumpdata news.post > db.json

#settings.configure()                #solving django.core.exceptions.ImproperlyConfigured: Requested setting USE_I18N
#output = open("db.xml", 'w')

## == python3 manage.py dumpdata news.post > db.json in terminal/commandline

## call_command(function, app, ...)
#django.setup()
#call_command('dumpdata', "news", format='xml', indent=4, stdout=output)
#output.close()

def getSummarizedList(sqs):
    output = ""
    
    # Directory checking
    if not os.path.exists(Dir):
        os.makedirs(Dir)
        
    try:
        summary = open(Dir + "input.txt", "w", encoding = 'utf-8-sig')
        file = open(Dir + "headline_summary.txt", "w", encoding = 'utf-8-sig')
    except error_to_catch:
        print("!")
    #sys.stdout = summary
    date = ""
    # filtering data
    for i in sqs:
        title = i.title.rstrip()
        pub_date = dateReformat(i.pub_date)

        if pub_date != date:
            if date != "":
                local_summary.close()
                # LexRank algorithm
                sys.stdout = file
                #summarizer = LexRankSummarizer(Stemmer(LANGUAGE))
                summarizer =LsaSummarizer(Stemmer(LANGUAGE))                
                summarizer.stop_words = get_stop_words(LANGUAGE)               
                headline = PlaintextParser.from_file(Dir + date + ".txt", Tokenizer(LANGUAGE))

                for sentence in summarizer(headline.document, SENTENCES_COUNT):
                    print(sentence)

            output = output + pub_date + "\n"
            date = pub_date
            local_summary = open(Dir + date + ".txt", "w", encoding = 'utf-8-sig')
        
        local_summary.write(title + ".\n")
        output = output + title + ".\n"

        #For last post summarization#
        if title == sqs.latest('pub_date').title.rstrip():
            local_summary.close()
            sys.stdout = file
            summarizer =LsaSummarizer(Stemmer(LANGUAGE))                
            summarizer.stop_words = get_stop_words(LANGUAGE)               
            headline = PlaintextParser.from_file(Dir + date + ".txt", Tokenizer(LANGUAGE))
            for sentence in summarizer(headline.document, SENTENCES_COUNT):
                print(sentence)
        #############################

    summary.write(output)
    file.close()
    summary.close()
    testing = readSummarizerResultToList("headline_summary.txt")
    
    return testing

def readSummarizerResultToList(filename):
    headlineSummary = open(Dir + filename, "r", encoding = 'utf-8-sig')
    headlinelist = headlineSummary.read().splitlines()
    headlineSummary.close()
    return headlinelist

def dateReformat(date):
    # Input: datetime class
    fDate = str(date.year) + "-" + str(date.month) + "-" + str(date.day)
    return fDate

#logging.basicConfig(level=logging.INFO)
#logging.info(getSummarizedList())
