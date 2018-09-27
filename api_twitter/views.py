
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from api_twitter.utils import authenticate_with_twitter
from api_twitter.models import HashTags


def search(request):

    # get twitter authenticated object
    twitter_api = authenticate_with_twitter()
    context = {}
    retrun_data = {}
    tweet_list = []
    hashtags = []

    if request.method == 'POST':

        search_term = request.POST.get('search')
        
        if "#" in search_term:
            hastag, is_exist = HashTags.objects.get_or_create(hashtag=search_term)

            if not is_exist:
                hastag.no_of_times_viewed = int(hastag.no_of_times_viewed) + 1
            else:
                hastag.no_of_times_viewed = 1
            hastag.save()
            top_hashtags = HashTags.get_most_viewed_hashtag()
        # calling twitter api for public search
        tweets = twitter_api.GetSearch(term=search_term,  raw_query=None, geocode=None,
                                       since_id=None, max_id=None, until=None, since=None, count=50, result_type='mixed', include_entities=True)

        context = {
            "tweets": tweets,
            "top_hashtags": top_hashtags
        }

    return render(request, 'api_twitter/home.html', context)
