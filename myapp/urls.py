
from django.urls import path,include
from django import urls
from myapp import views

urlpatterns = [
  
    path("",views.index),
    path("contact/",views.contact),
    path("about/",views.about),
    path("coming/",views.coming),
    path("login/",views.login),
    path("register/",views.register),
    path("shop/",views.shop),
    path("single/",views.single),
    path("logout/",views.logout),
    path("productadd/",views.productadd),
    path("delete/",views.delt),
    path("edit/",views.edit),
    path("update/",views.update),
    path("status/",views.status),
    path("productview/",views.productview),
    path("editpro/",views.editpro),
    path("deletepro/",views.deletepro),
    path("updatepro/",views.update_product),
    path("blocks/",views.blocks),
    path("cards/",views.cards),
    path("carousels/",views.carousels),
    path("forms/",views.forms),
    path("indexadmin/",views.indexadmin),
    path("people/",views.people),
    path("pricing/",views.pricing),
    path("product_addcart/",views.product_addcart),
    path("cart/",views.cart),
    path("delete_cartitem/",views.delete_cartitem),
    path("payment/",views.payment),
    path("makepayments/",views.makepayments),
    path("search/",views.search),
    path("clearcart/",views.clearcart),
    path("subcribe/",views.subcribe),
    path("userdetail/",views.userdetail),
    path("changepass/",views.changepass),
    path("forgotpass/",views.forgotpass),
    path("forgotpasschange/",views.forgotpasschange),




    







]
