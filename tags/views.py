from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Tag, Like, Search
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import F
from .api import FlickrAPI
import json


def index(request):
    most_search_tags = Tag.objects.order_by('-count')[:22]
    tag = request.GET.get('tag')
    page = request.GET.get('page')

    context = {
        "most_search_tags": most_search_tags
    }

    if tag:
        searched_tag, created = Tag.objects.get_or_create(name=tag)

        if request.user.is_authenticated:
            Search.objects.update_or_create(user=request.user, tag=searched_tag)

        api_result = FlickrAPI(tag, page)
        images = api_result.constructed_urls()

        if not created and not page:
            searched_tag.count = F('count') + 1
            searched_tag.save()

        context.update({
            'images': images,
            'next_page': 2 if not page else int(page) + 1,
            'previous_page': None if not page else int(page) - 1,
        })

    if request.user.is_authenticated:
        if tag:
            user_likes = request.user.like_set.values_list('image_url', flat=True)
            context.update({'user_likes': user_likes})
        previous_search_tags = request.user.search_set.select_related().only('tag__name').order_by('-searched_at')[:21]
        context.update({'previous_search_tags': previous_search_tags})

    return render(request, 'tags/index.html', context)


def post_user_likes(request):
    if request.is_ajax() and request.user.is_authenticated:
        image_url = request.POST.get('image_url')
        liked_image, created = Like.objects.get_or_create(image_url=image_url)
        if liked_image in request.user.like_set.all():
            liked_image.users.remove(request.user)
            is_saved = False
            if not liked_image.users.count():
                liked_image.delete()
        else:
            liked_image.users.add(request.user)
            is_saved = True

        return HttpResponse(
            json.dumps({'message': True, 'is_saved': is_saved}),
            content_type='application/json'
        )
    else:
        return HttpResponse(
            json.dumps({'message': False}),
            content_type='application/json'
        )


class UserFavoriteListView(LoginRequiredMixin, ListView):
    template_name = 'tags/liked.html'
    context_object_name = 'images'

    def get_queryset(self):
        return self.request.user.like_set.all()
