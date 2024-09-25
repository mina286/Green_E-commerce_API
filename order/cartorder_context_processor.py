
from .models import CartOrder
from django.contrib.auth.models import User
def get_cartorder_or_create(request):
    if request.user.is_authenticated :
        cart_order ,created = CartOrder.objects.get_or_create(user = request.user,cart_order_state='inprogress')
        return {'cart_order':cart_order}
    else:
        return {}
