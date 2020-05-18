from django.conf.urls import url, include
from . import views

app_name = 'vksearch'

urlpatterns = [
    url(r'^search/$', views.get_search_params, name='get_search_params'),
    url(r'^search_result/$', views.SearchView.as_view(), name='get_search_result'),

    url(r'^add_filter_1/$', views.add_search_filter, name='add_search_filter'),
    url(r'^add_filter_2/$', views.get_new_filter_2, name='get_new_filter_2'),
    url(r'^add_result/$', views.add_filter_result, name='add_filter_result'),

    url(r'^delete_filter/$', views.delete_filter, name='delete_filter'),
    url(r'^delete_filter_result/$', views.delete_filter_result, name='delete_filter_result'),
]
