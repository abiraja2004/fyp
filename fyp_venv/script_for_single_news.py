from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), 'mysite'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
from django.conf import settings
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
from news.models import Post
from newspaper import Article
import newspaper

from textteaser import TextTeaser
from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.sum_basic import SumBasicSummarizer as SumBasicSummarizer
from sumy.summarizers.lsa import LsaSummarizer as LsaSummarizer
from sumy.summarizers.text_rank import TextRankSummarizer as TextRankSummarizer
from sumy.summarizers.lex_rank import LexRankSummarizer as LexRankSummarizer

from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

LANGUAGE = "English"
SENTENCES_COUNT = 10
number = 0

'''for single news'''
url = 'http://edition.cnn.com/2017/02/20/europe/russia-un-ambassador-vitaly-churkin-dead/index.html'
article = Article(url)
article.download()
article.parse()
article.nlp()

category = "politics"
pub_date = article.publish_date
location = "US"
title = article.title
                                                
content = article.text
photo = article.top_image
link = article.url

getText = open("input_article.txt", "w", encoding = 'utf-8-sig')
sys.stdout = getText
print(article.title)
print(article.text)
getText.close()

parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))

stemmer = Stemmer(LANGUAGE)

summarizer = LexRankSummarizer(stemmer)
summarizer.stop_words = get_stop_words(LANGUAGE)

#five-line summary
summary = open("five_line_summary.txt", "w", encoding = 'utf-8-sig')
sys.stdout = summary
for sentence in summarizer(parser.document, SENTENCES_COUNT - 5):
    print(sentence)
summary.close()

#ten-line summary
summary = open("ten_line_summary.txt", "w", encoding = 'utf-8-sig')
sys.stdout = summary 
for sentence in summarizer(parser.document, SENTENCES_COUNT):
    print(sentence)
    print("")
summary.close()

#sumbasic
summarizer =SumBasicSummarizer(stemmer)
summarizer.stop_words = get_stop_words(LANGUAGE)
summary = open("sumbasic.txt", "w", encoding = 'utf-8-sig')
sys.stdout = summary 
for sentence in summarizer(parser.document, SENTENCES_COUNT):
    print(sentence)
    print("")
summary.close()

#LSA
summarizer =LsaSummarizer(stemmer)
summarizer.stop_words = get_stop_words(LANGUAGE)
summary = open("LSA.txt", "w", encoding = 'utf-8-sig')
sys.stdout = summary 
for sentence in summarizer(parser.document, SENTENCES_COUNT):
    print(sentence)
    print("")
summary.close()

#textrank
summarizer =TextRankSummarizer(stemmer)
summarizer.stop_words = get_stop_words(LANGUAGE)
summary = open("textrank.txt", "w", encoding = 'utf-8-sig')
sys.stdout = summary 
for sentence in summarizer(parser.document, SENTENCES_COUNT):
    print(sentence)
    print("")
summary.close()

#lexrank
summarizer =LexRankSummarizer(stemmer)
summarizer.stop_words = get_stop_words(LANGUAGE)
summary = open("lexrank.txt", "w", encoding = 'utf-8-sig')
sys.stdout = summary 
for sentence in summarizer(parser.document, SENTENCES_COUNT):
    print(sentence)
    print("")
summary.close()

#featured-lexrank
with open('input_article.txt', 'r', encoding = 'utf-8-sig') as f:
    first_line = f.readline()
title = first_line
with open('input_article.txt', 'r', encoding = 'utf-8-sig') as f:
    text = f.read()
tt = TextTeaser()

sentences = tt.summarize(title, text)
file = open("tt.txt", "w", encoding = 'utf-8-sig')
for sentence in sentences:
    file.write("%s\n" % sentence)
file.close()

parser = PlaintextParser.from_file("tt.txt", Tokenizer(LANGUAGE))
summarizer =LexRankSummarizer(stemmer)
summarizer.stop_words = get_stop_words(LANGUAGE)
summary = open("featured-lexrank.txt", "w", encoding = 'utf-8-sig')
sys.stdout = summary 
for sentence in summarizer(parser.document, SENTENCES_COUNT):
    print(sentence)
    print("")
summary.close()

with open('five_line_summary.txt', encoding = 'utf8') as f:
    fivelinesummary = f.readlines()

with open('ten_line_summary.txt', encoding = 'utf8') as f:
    tenlinesummary  = f.readlines()

with open('sumbasic.txt', encoding = 'utf8') as f:
    sum_basic = f.readlines()

with open('LSA.txt', encoding = 'utf8') as f:
    LSA  = f.readlines()

with open('textrank.txt', encoding = 'utf8') as f:
    textrank  = f.readlines()

with open('lexrank.txt', encoding = 'utf8') as f:
    lexrank  = f.readlines()

with open('featured-lexrank.txt', encoding = 'utf8') as f:
    featured_lexrank  = f.readlines()


fivelinesummary=''.join(fivelinesummary)
tenlinesummary=''.join(tenlinesummary)
sum_basic=''.join(sum_basic)
LSA=''.join(LSA)
textrank=''.join(textrank)
lexrank=''.join(lexrank)
featured_lexrank=''.join(featured_lexrank)

post=Post(category=category, pub_date=pub_date, location=location, title=title,content=content, photo=photo,link=link, fivelinesummary=fivelinesummary, tenlinesummary=tenlinesummary, sum_basic=sum_basic, LSA=LSA, textrank=textrank, lexrank=lexrank, featured_lexrank=featured_lexrank)
post.save()
