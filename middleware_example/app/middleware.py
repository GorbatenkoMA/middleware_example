from django.utils.deprecation import MiddlewareMixin
from .models import UserProfile

class ProfileMiddlewareMiddleware(MiddlewareMixin):

    def process_request(self, request):
        # print(request.user.is_anonymous())
        if not request.user.is_anonymous:
            print(request.user)
            print('ProfileMiddlewareMiddleware executed')
            obj = UserProfile.objects.get(user=request.user)
            request.session['timezone'] = obj.timezone
