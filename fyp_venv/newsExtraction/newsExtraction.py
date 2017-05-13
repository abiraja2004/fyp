from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from textteaser import TextTeaser
from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.sum_basic import SumBasicSummarizer as SumBasicSummarizer
from sumy.summarizers.lsa import LsaSummarizer as LsaSummarizer
from sumy.summarizers.text_rank import TextRankSummarizer as TextRankSummarizer
from sumy.summarizers.lex_rank import LexRankSummarizer as LexRankSummarizer
from sumy.summarizers.lex_rank import LexRankSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

from newspaper import Article

import sys
import os
import newspaper

newspaper3k_url = 'http://newspaper.readthedocs.io/en/latest/user_guide/install.html'

LANGUAGE = "English"
SENTENCES_COUNT = 10

def main():
    try:
        if len(sys.argv) < 2:
            print("Please input news article parameter")
            sys.exit(-1)
        else:
            url = sys.argv[1]

        article = news_crewler(url)
        sumy_test(url)
        textteaser_test()
        
        
    except Exception as e:
        print ('Error in connect ' , e)

def news_crewler(url):
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()

    getText = open("input_sample.txt", "w", encoding = 'utf-8-sig')
    sys.stdout = getText
    print(article.text)
    getText.close()

    # Basic info
    summary = open("summary_list.txt", "w", encoding = 'utf-8-sig')
    sys.stdout = summary
    print("Title:\t" + article.title + "\n")
    print("url:\t" + url + "\n")

    print("Image:\t" + article.top_image + "\n")
    print("Keywords: \t")
    for p in article.keywords: print(p)
    print("\nText:\n" + article.text + "\n")
    summary.close()

    return article

def sumy_test(url):
    summary = open("summary_list.txt", "a", encoding = 'utf-8-sig')
    sys.stdout = summary
    
    parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
    # or for plain text files
    # parser = PlaintextParser.from_file("document.txt", Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)

    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)

    print("Sumy_FiveLine:") 
    for sentence in summarizer(parser.document, SENTENCES_COUNT - 5):
        print(sentence)
    print("\n")

    print("Sumy_TenLine:") 
    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        print(sentence)
        print("")
    print("\n")

    summary.close()

def textteaser_test():
    
    summary = open("summary_list.txt", "a", encoding = 'utf-8-sig')
    sys.stdout = summary

    # obtain the input article from url
    #url = "http://www.nytimes.com/2016/11/17/us/politics/donald-trump-administration-twitter.html?ref=politics"
    #parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
    
    # obtain the input article from plain text files
    parser = PlaintextParser.from_file("input_sample.txt", Tokenizer(LANGUAGE))
   
    # define the language, by dafult it is English
    stemmer = Stemmer(LANGUAGE)

    # SumBasic algorithm
    summarizer =SumBasicSummarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)
    print("SumBasic:") 
    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        print(sentence)
    print("\n")

    # LSA algorithm
    summarizer =LsaSummarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)
    print("Latent Semantic Analysis:")   
    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        print(sentence)
    print("\n")

    # TextRank algorithm
    summarizer =TextRankSummarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)
    print("TextRank:")    
    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        print(sentence)
    print("\n")

    # LexRank algorithm
    summarizer =LexRankSummarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)
    print("LexRank:")    
    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        print(sentence)
    print("\n")

    #Featured-LexRank algorithm
    with open('input_sample.txt', 'r', encoding = 'utf-8-sig') as f:
        first_line = f.readline()
    title = first_line
    with open('input_sample.txt', 'r', encoding = 'utf-8-sig') as f:
        text = f.read()
    tt = TextTeaser()

    sentences = tt.summarize(title, text)
    file = open("tt.txt", "w", encoding = 'utf-8-sig')
    print("Featured-LexRank:")
    for sentence in sentences:
        file.write("%s\n" % sentence)
    file.close()

    parser = PlaintextParser.from_file("tt.txt", Tokenizer(LANGUAGE))
    summarizer =LexRankSummarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)    
    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        print(sentence)
    print("\n")

    summary.close()


if __name__ == "__main__":
   main()
