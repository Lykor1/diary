from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Entry
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin


class LockedView(LoginRequiredMixin):
    login_url = 'admin:login'


class EntryListView(LockedView, ListView):
    model = Entry
    queryset = Entry.objects.all().order_by('-date_created')


class EntryDetailView(LockedView, DetailView):
    model = Entry


class EntryCreateView(LockedView, SuccessMessageMixin, CreateView):
    model = Entry
    fields = ['title', 'content']
    success_url = reverse_lazy('entry-list')
    success_message = 'Ваша запись была добавлена!'


class EntryUpdateView(LockedView, SuccessMessageMixin, UpdateView):
    model = Entry
    fields = ['title', 'content']
    success_message = 'Ваша запись была обновлена!'

    def get_success_url(self):
        return reverse_lazy(
            'entry-detail',
            kwargs={'pk': self.object.id}
        )


class EntryDeleteView(LockedView, SuccessMessageMixin, DeleteView):
    model = Entry
    success_url = reverse_lazy('entry-list')
    success_message = 'Ваша запись была удалена!'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)
