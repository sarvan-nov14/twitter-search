
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from api_twitter.utils import authenticate_with_twitter


def search(request):

    # get twitter authenticated object
    twitter_api = authenticate_with_twitter()
    context = {}
    retrun_data = {}
    tweet_list = []
    hashtags = []

    if request.method == 'POST':

        search_term = request.POST.get('search')
        # calling twitter api for public search
        tweets = twitter_api.GetSearch(term=search_term,  raw_query=None, geocode=None,
                                       since_id=None, max_id=None, until=None, since=None, count=50, result_type='mixed')

        context = {
            "tweets": tweets
        }

    return render(request, 'api_twitter/home.html', context)
