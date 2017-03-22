from django.urls import reverse
from django.views import generic
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from . import plots

class IndexView(generic.TemplateView):
    template_name = "plotlyapp/index.html"

class Plot1DView(generic.TemplateView):
    template_name = "plotlyapp/plot.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(Plot1DView, self).get_context_data(**kwargs)
        context['plot'] = plots.plot1d()
        return context

class Plot2DView(generic.TemplateView):
    template_name = "plotlyapp/plot.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(Plot2DView, self).get_context_data(**kwargs)
        context['plot'] = plots.plot2d()
        return context

class Plot3DView(generic.TemplateView):
    template_name = "plotlyapp/plot.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(Plot3DView, self).get_context_data(**kwargs)
        context['plot'] = plots.plot3d()
        return context

class Plot1DMultipleView(generic.TemplateView):
    template_name = "plotlyapp/plot_multiple.html"

    def get_context_data(self, **kwargs):
        n = int(kwargs['n'])
        # Call the base implementation first to get a context
        context = super(Plot1DMultipleView, self).get_context_data(**kwargs)
        context['plot'] = plots.plot1d_multiple(n)
        return context

def plot1d_multiple_ajax(request,n):
    """
    Only handles AJAX queries
    """
    print (n)
    return HttpResponse(plots.plot1d_multiple(int(n)))


class PlotLiveView(generic.TemplateView):
    template_name = "plotlyapp/plot_live.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PlotLiveView, self).get_context_data(**kwargs)
        context['plot'] = plots.plotLive()
        return context

def  plot_live_update(request):
    '''
    Handle ajax call to update the live plot
    '''
    if request.is_ajax():
        data = plots.live_plot_get_data_serialized()
        # In order to allow non-dict objects to be serialized set the safe parameter to False
        return JsonResponse([data], safe=False)
    else:
        return HttpResponseBadRequest()
