from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from publishers import views
from django.conf.urls import include

urlpatterns = [
	url(r'^publishers/$', views.PublishersList.as_view()),
	url(r"^publishers/(?P<pk>[a-z0-9$-_.+!*'(),?]+)/$", views.PublisherDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]