from django import template
from django.shortcuts import redirect
from django.templatetags.static import static
from django import template
from django.db.models import Sum
from django.shortcuts import get_object_or_404
from django.templatetags.static import static

from products.models import ProductModel

register = template.Library()


@register.simple_tag
def get_url_lang(request, lang):
    url = request.path.split('/')
    url[1] = lang
    url = '/'.join(url)
    return url


@register.simple_tag
def get_price(request, x):
    price = request.GET.get('price')
    if price:
        return price.split(';')[x]
    return 'null'


@register.simple_tag
def get_heart_icon(request, product):
    if request.user in product.wishlist.all():
        return static('/img/icon/iconmonstr-favorite-5-16-1.png')
    return static('/img/icon/heart.png')



@register.simple_tag
def get_cart_count(request):
    cart = request.session.get('cart')
    if cart:
        return len(cart)
    return 0

#
# @register.filter
# def in_cart(product, request):
#     return product in request.session.get('cart', [])
#
# # @register.simple_tag
# # def get_heart_icon(request, product):
# #     icon = '/img/icon/heart.png'
# #     if request.user in product.wishlist.all():
# #         icon = '/img/icon/iconmonstr-favorite-5-24.png'
# #     return static(icon)




#################################333

# @register.simple_tag
# def get_lang_url(request, lang):
#     url = request.path.split('/')
#     url[1] = lang
#
#     return '/'.join(url)
#
#
# @register.simple_tag
# def get_price(request, x):
#     price = request.GET.get('price')
#     if price:
#         return price.split(';')[x]
#     return 'null'
#
#
# @register.simple_tag
# def get_wishlist_icon(request, pk):
#     product = get_object_or_404(ProductModel, pk=pk)
#     if request.user in product.wishlist.all():
#         return static('/img/icon/heartr.png')
#     return static('/img/icon/heart.png')


@register.filter
def in_cart(product, request):
    return product.pk in request.session.get('cart', [])


@register.simple_tag
def cart_count(request):
    return len(request.session.get('cart', []))


# @register.simple_tag
# def get_cart_sum(request):
#     cart = request.session.get('cart')
#     if not cart:
#         return 0
#
#     return ProductModel.get_from_cart(request).aggregate(
#         Sum('real_price')
#     ).get('real_price__sum', 0)



@register.simple_tag
def get_cart_sum(request):
    cart = request.session.get('cart')
    if not cart:
        return 0

    return ProductModel.objects.filter(
        pk__in=cart
    ).aggregate(
        Sum('real_price')
    )['real_price__sum']
