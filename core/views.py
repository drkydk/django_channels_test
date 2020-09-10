from django.shortcuts import render
from rest_framework.views import APIView
from product.models import Product
from chat.models import Message, Channel


# Create your views here.
class HomePage(APIView):

    def get(self, request):
        if not request.session.session_key:
            request.session.save()
        session_id = request.session.session_key
        context = {
            'user': session_id,
            'user_short': session_id[:4],
            'product_list': Product.objects.filter(active=True)[:10],
            'channels': Channel.objects.filter(room_name__contains=session_id)
        }

        return render(template_name='index.html', request=request, context=context)
