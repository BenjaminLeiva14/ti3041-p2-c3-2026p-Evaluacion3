from rest_framework import routers, viewsets

from .models import Visita
from .serializers import VisitaSerializer

class VisitaViewSet(viewsets.ModelViewSet):
    queryset = Visita.objects.all()
    serializer_class = VisitaSerializer

router = routers.DefaultRouter()
router.register(r'visitas', VisitaViewSet)