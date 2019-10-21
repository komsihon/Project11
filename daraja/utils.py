from ikwen.core.models import Service, Application

from daraja.models import DARAJA


def get_service_instance(request, using=None):
    app = Application.objects.get(slug=DARAJA)
    if using:
        return Service.objects.using(using).get(app=app, member=request.user)
    return Service.objects.get(app=app, member=request.user)
