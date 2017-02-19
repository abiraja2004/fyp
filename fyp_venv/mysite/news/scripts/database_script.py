from news.models import Post
from newspaper import Article
import newspaper

def run():
    url = 'http://fox13now.com/2013/12/30/new-year-new-laws-obamacare-pot-guns-and-drones/'
    article = Article(url)
    article.download()
    article.parse()
        
    url =article.url
    category = "politics"
    pub_date = article.publish_date
    location = "US"
    title = article.title
            
    content = article.text
            
    photo = article.top_image
    link = article.url
        
    post=Post(category=category, pub_date=pub_date, location=location, title=title,content=content, photo=photo,link=link)
    post.save()


