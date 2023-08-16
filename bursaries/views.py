from django.views.generic import TemplateView


class CreateBursaryApplicationView(TemplateView):
    template_name = "bursaries/create.html"
