from django.db import models

class HashTags(models.Model):
    """ Model for save hashtag details """ 
    hashtag = models.CharField(max_length=30,  null=True, blank=True)
    no_of_times_viewed = models.CharField(max_length=30,  null=True, blank=True)
    searched_at = models.DateTimeField(auto_now=True, null=True, blank=True)


    @staticmethod
    def get_most_viewed_hashtag():
        """ Return top viewd hashtags """
        tags = HashTags.objects.order_by('-no_of_times_viewed').distinct()[:10]
        return tags
