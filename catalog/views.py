from django.forms import formset_factory
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home_page.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.all()
        for product in products:
            product.active_version = product.versions.filter(is_active=True).first()
        context['products'] = products
        return context


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        VersionFormSet = formset_factory(VersionForm, extra=1)
        context['version_formset'] = VersionFormSet()
        return context

    def form_valid(self, form):
        new_product = form.save()
        new_product.save()
        selected_version = form.cleaned_data['version']
        selected_version.products.add(new_product)
        return super().form_valid(form)


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'

    def get_object(self, queryset=None):
        name = self.kwargs.get('name')
        return get_object_or_404(Product, name=name)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.object
        product.active_version = product.versions.filter(is_active=True).first()
        context['product'] = product
        return context


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    context_object_name = 'product'
    success_url = reverse_lazy("catalog:product_list")

    def get_object(self, queryset=None):
        name = self.kwargs.get('name')
        return get_object_or_404(Product, name=name)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        VersionFormSet = formset_factory(VersionForm, extra=1)
        context['version_formset'] = VersionFormSet()
        return context


def contacts(request):
    context = {
        'title': 'Contacts',
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}) {message}')
    return render(request, "catalog/contacts.html", context)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

    def get_object(self, queryset=None):
        name = self.kwargs.get('name')
        return get_object_or_404(Product, name=name)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.object
        product.active_version = product.versions.filter(is_active=True).first()
        context['product'] = product
        return context
