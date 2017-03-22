from django.conf.urls import url

from . import views

app_name = 'plotlyapp'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^plot1d/$', views.Plot1DView.as_view(), name='plot1d'),
    url(r'^plot2d/$', views.Plot2DView.as_view(), name='plot2d'),
    url(r'^plot3d/$', views.Plot3DView.as_view(), name='plot3d'),
    url(r'^plot_live/$', views.PlotLiveView.as_view(), name='plot_live'),
    url(r'^plot_live_update/$', views.plot_live_update, name='plot_live_update'),
]
