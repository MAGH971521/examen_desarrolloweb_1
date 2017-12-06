# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Libros

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, UpdateView, DeleteView, ListView, DetailView)
from .mixin import FormUserNeededMixin
from .forms import LibrosModelForms
from django.db.models import Q

# Create your views here.


def lista_libros(request):
    result_set = Libros.objects.all()
    context = {"result": result_set}
    return render(request, "lista_libros_ajax.html", context)


def detalle_libros(request, id=10):
    result_set = Libros.objects.get(id=id)
    context = {"result": result_set}
    return render(request, "detalle_libro.html", context)
# Examen 2


class LibroListView(ListView):
    template_name = 'lista_libros_ajax.html'

    def get_queryset(self, *args, **kargs):
        qs = Libros.objects.all().order_by("-pk")
        print self.request.GET
        query = self.request.GET.get('q', None)
        if query is not None:
            qs = qs.filter(
                Q(Nombre__icontains=query) | Q(Autor__icontains=query)
            )
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(LibroListView, self).get_context_data(*args, **kwargs)
        print context
        context['create_form'] = LibrosModelForms()
        context['create_url'] = reverse_lazy("libros_create")
        return context


class LibroCreateView(LoginRequiredMixin, FormUserNeededMixin, CreateView):
    form_class = LibrosModelForms
    template_name = "libro/create.html"
    success_url = "/libros/lista"
    login_url = "/admin"


class LibroUpdateView(UpdateView):
    queryset = Libros.objects.all()
    form_class = LibrosModelForms
    template_name = "libro/mod.html"
    success_url = "/libros/lista"


class LibroDeleteView(LoginRequiredMixin,  DeleteView):
    model = Libros
    template_name = "libro/delete.html"
    success_url = reverse_lazy("lista")
