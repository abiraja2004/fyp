import datetime
from haystack import indexes
from news.models import Post
from news.models import Quotation

# get the detail information of a news post
class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    content = indexes.CharField(model_attr='content')
    tenlinesummary = indexes.CharField(model_attr='tenlinesummary')
    pub_date = indexes.DateTimeField(model_attr='pub_date')
    photo = indexes.CharField(model_attr='photo')
    quotation = indexes.MultiValueField()
    speaker = indexes.MultiValueField()
    date = indexes.MultiValueField()
    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())
    
    def prepare_quotation(self, obj):
        return [o.quotation for o in obj.quotation.all()]	

    def prepare_speaker(self, obj):
        return [o.speaker for o in obj.quotation.all()]	
	
    def prepare_date(self, obj):
        return [o.date for o in obj.quotation.all()]	
