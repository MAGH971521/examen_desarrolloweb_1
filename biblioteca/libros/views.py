# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Libros

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (CreateView, UpdateView, DeleteView, ListView, DetailView)
from .mixin import FormUserNeededMixin

# Create your views here.


def lista_libros(request):
    result_set = Libros.objects.all()
    context = {"result": result_set}
    return render(request, "lista_libros.html", context)


def detalle_libros(request, id=10):
    result_set = Libros.objects.get(id=id)
    context = {"result": result_set}
    return render(request, "detalle_libro.html", context)
# Examen 2


class LibroCreateView(LoginRequiredMixin, FormUserNeededMixin, CreateView):
    form_class = LibrosModelForm
    template_name = "libro/create.html"
    success_url = "/libros/create"
    login_url = "/admin"


class LibroUpdateView(LoginRequiredMixin, UpdateView):
    queryset = Libros.objects.all()
    form_class = LibrosModelForm
    template_name = "libro/mod.html"
    success_url = "/libros/update"


class LibroDeleteView(LoginRequiredMixin,  DeleteView):
    model = Libros
    template_name = "libros/delete.html"
    success_url = "/libros/delete"
