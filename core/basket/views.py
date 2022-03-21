from rest_framework.response import Response
from rest_framework import generics
from django.shortcuts import get_object_or_404

from posts.models import Post
from cart.serializers import OrderSerializer
from basket.basket import Basket


class OrderAddProduct(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = OrderSerializer

    def basket_summary(request):
        basket = Basket(request)
        return Response(request, {'basket': basket})


    def perform_create(request): # self, productid, productqty
        basket = Basket(request) # retrieve session data
        if request.POST.get('action') == 'post':
            product_id = int(request.POST.get('productid'))
            product_qty = int(request.POST.get('productqty'))
            product = get_object_or_404(Post, id=product_id)
            basket.add(product=product, qty=product_qty)

            basketqty = basket.__len__()
            response = Response({'qty': basketqty})
            return response


    # def basket_delete(request):
    #     basket = Basket(request)
    #     if request.POST.get('action') == 'post':
    #         product_id = int(request.POST.get('productid'))
    #         basket.delete(product=product_id)

    #         basketqty = basket.__len__()
    #         baskettotal = basket.get_total_price()
    #         response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal})
    #         return response


    # def basket_update(request):
    #     basket = Basket(request)
    #     if request.POST.get('action') == 'post':
    #         product_id = int(request.POST.get('productid'))
    #         product_qty = int(request.POST.get('productqty'))
    #         basket.update(product=product_id, qty=product_qty)

    #         basketqty = basket.__len__()
    #         baskettotal = basket.get_total_price()
    #         response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal})
    #         return response
