from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns('',
		url(r'^$',views.index, name = 'index'),
		url(r'^blog/$',views.blog, name = 'blog'),
		url(r'^view_post/(?P<slug>[^\.]+)/$',views.view_post,name='view_post'),
		url(r'^about/$',views.about, name='about'),
		url(r'^add_comment/(?P<slug>[^\.]+)/$',views.add_comment, name='add_comment'),
		url(r'^month/(\d+)/(\d+)/$',views.month, name= "month"),
		url(r'^tag/(?P<slug>[^\.]+)/$',views.view_post_by_tag,name='tag'),
		)