from django.urls import path
from .views import home, Otros, venadd,add_cart10, add_cart1, less_cart10, cart, vendetail, venlist, add_cart, less_cart, clean_cart, delete_cart, login, Frutas, Verduras, Comidas, proadd, prolist, promod, prodel, boddel, bodadd, bodlist

urlpatterns=[
    path('', home, name="home"),
    path('login/', login, name="login"),
    path('frutas/', Frutas, name="Frutas"),
    path('verduras/', Verduras, name="Verduras"),
    path('comidas/', Comidas, name="Comidas"),
    path('otros/', Otros, name="Otros"),
    path('proadd/', proadd, name="proadd"),
    path('prolist/', prolist, name="prolist"),  
    path('promod/<id>/', promod, name="promod"),
    path('prodel/<id>', prodel, name="prodel"),
    path('bodlist/', bodlist, name="bodlist"),
    path('bodadd/', bodadd, name="bodadd"),
    path('boddel/<id>', boddel, name="boddel"),
    path('cart/', cart, name="cart"),
    path('add_cart/<int:id>/', add_cart, name="add_cart"),
    path('add_cart1/<int:id>/', add_cart1, name="add_cart1"),
    path('add_cart10/<int:id>/', add_cart10, name="add_cart10"),
    path('less_cart/<int:id>/', less_cart, name="less_cart"),
    path('less_cart10/<int:id>/', less_cart10, name="less_cart10"),
    path('delete_cart/<int:id>', delete_cart, name="delete_cart"),
    path('clean_cart/', clean_cart, name="clean_cart"),
    path('venadd/', venadd, name="venadd"),
    path('venlist/', venlist, name="venlist"),
    path('vendetail/<id>', vendetail, name="vendetail"),
]