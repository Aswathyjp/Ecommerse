from django.urls import path
from . import views
app_name = 'ecomerseapp'

urlpatterns = [
     path("",views.allprodcat,name='allprodcat'),
     path("<slug:c_slug>/",views.allprodcat,name='product_by_category'),
     path("<slug:c_slug>/<slug:p_slug>/", views.prodetail, name='productcatdetail')

]