from django.views.generic import ListView
from .models import Product

class ProductListView (ListView):
    model = Product
    template_name = 'produtos_list.html'
    context_object_name = 'products'
    paginate_by = 10