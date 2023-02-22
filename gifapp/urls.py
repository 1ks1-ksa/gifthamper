from django.urls import path
from .views import *

urlpatterns=[
    path('shopreg/',shopreg),
    path('shoplog/',shoplog),
    path('propage/',profpage),
    path('index/',indexpage),
    path('siglog/',siglog),
    path('imgupload/',imageupload),
    path('prodisplay/',prodisplay),
    path('prodel/<int:id>',prodelete),
    path('proedit/<int:id>',proedit),
    path('viewall/',viewallpro),
    path('userreg/',regis),
    path('userlog/',uslog),
    path('usl/',usl),
    path('uspro/',uspro),
    path('verify/<auth_token>',verify),
    path('userviewpro/',userprodisplay),
    path('addcart/<int:id>',addcart),
    path('cartdis/',displaycart),
    path('wishlist/<int:id>',wishlistuser),
    path('wishdis/',displaywishlist),
    path('cartremove/<int:id>',removecart),
    path('wishremove/<int:id>',removewish),
    path('cartbuy/<int:id>',cartbuy),
    path('bill/',bill),
    path('cardpay/',cardpay),
    path('shopnot/',shopnotimodel)
]