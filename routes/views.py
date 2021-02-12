from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Route
from .forms import RouteForm
import logging


# Create your views here.

# def product_create_view(request):
#     my_form = RawProductForm(request.GET)
#     if request.method == 'POST':
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             print(my_form.cleaned_data)
#             # the ** is for the other reqiured fields to be saved that are not being passed from the form.
#             Product.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#     context = {
#         'form': my_form
#     }
#
#     return render(request, 'products/create.html', context)


def route_create_view(request):
    """
    plain html form
    :param request:
    :return:
    """
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        iframe_url = request.POST.get('iframe_url')
        url = request.POST.get('url')
        distance = request.POST.get('distance')
        Route.objects.create(title=title, description=description, iframe_url=iframe_url, url=url, distance=distance)

    context = {}

    return render(request, 'routes/create.html', context)


#
#
# def route_create_view(request, *args, **kwargs):
#     """
#         with Django realted stuff.
#     """
#     initial_data = {
#         'title': 'This is my title text'
#     }
#     # with initial data:
#     # form = ProductForm(request.POST or None, initial=initial_data)
#
#     obj = Route.objects.get(id=1)
#     form = RouteForm(request.POST or None, instance=obj)
#     if form.is_valid():
#         print("is valid")
#         form.save()
#         form = RouteForm()
#
#     context = {
#         'form': form
#     }
#
#     return render(request, 'routes/create.html', context)


def route_detail_view(request, id):
    # logging.basicConfig(level=logging.DEBUG)
    # logging.debug(request.user)

    # This will automatically throw 404 if id is invalid.
    # obj = get_object_or_404(Product, id=id)

    # Another way to throw 404 if the request is incorrect
    try:
        obj = Route.objects.get(id=id)
    except Route.DoesNotExist:
        raise Http404

    context = {
        'obj': obj
    }

    return render(request, 'routes/detail.html', context)


def route_list_view(request):
    queryset = Route.objects.all()

    context = {
        'obj_list': queryset
    }

    return render(request, 'routes/list.html', context)

# def product_delete_view(request, id):
#     obj = get_object_or_404(Product, id=id)
#
#     if request.method == "POST":
#         obj.delete()
#         redirect('../../../')
#
#     context = {
#         'obj': obj
#     }
#
#     return render(request, 'products/delete.html', context)
