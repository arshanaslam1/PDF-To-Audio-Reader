from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView, ListView, DetailView
from .forms import CreatePDFForm
from .models import PDFAudio


class HomeView(View):
    template_name = "notes/home.html"

    def get(self, request):
        if self.request.user.is_authenticated:
            return redirect(settings.LOGIN_REDIRECT_URL)
        else:
            return render(request, "main/home.html")


class PDFListView(View):
    def get(self, request):
        objs = PDFAudio.objects.filter(owner_id=request.user.id).order_by('-updated')[:8]
        data=[]
        for obj in objs:
            data.append({'pdf':str(obj.pdf), 'audio_rate': obj.audio_rate, 'volume_level': obj.volume_level, 'audio_voice':obj.audio_voice, 'audio_file':str(obj.audio_file)})
        return JsonResponse(data, status=200, safe=False)


class Detail(DetailView):

    model = PDFAudio

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        data = []
        data.append({'audio_file': obj.audio_url()})
        return JsonResponse(data, status=200, safe=False)




class CreatePDFView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = CreatePDFForm
    template_name = 'main/pdfaudio_form.html'
    success_message = 'you have Convert successfully'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.save()
        return super().form_valid(form)


class DashboardView(LoginRequiredMixin, ListView):
    model = PDFAudio
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['form'] = CreatePDFForm()
        return context

    def get_queryset(self):
        return self.model.objects.filter(owner_id=self.request.user.id).order_by('-updated')

