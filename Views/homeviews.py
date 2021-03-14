from django.http import HttpResponse
from django.template.loader import get_template


class homeview():

    def home(self):
        plantilla = get_template('menu.html')
        return HttpResponse(plantilla.render())