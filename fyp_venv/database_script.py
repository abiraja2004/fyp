import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), 'mysite'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
from django.conf import settings
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
from news.models import Post
from newspaper import Article
import newspaper

cnn_paper = newspaper.build('https://www.nytimes.com/')
    
for article in cnn_paper.articles:
    print(article.url)
#    if 'politics' in 'http://edition.cnn.com/2017/02/20/politics/donald-trump-first-month/index.html':
#        print("yes")
#    else:
#        print("no")
##    category = "politics"
##    pub_date = article.publish_date
##    print(article.publish_date)
##    location = "US"
##    title = article.title
##                                        
##    content = article.text
##                                        
##    photo = article.top_image
##    link = article.url
                                
    #post=Post(category=category, pub_date=pub_date, location=location, title=title,content=content, photo=photo,link=link)
    #post.save()
            
