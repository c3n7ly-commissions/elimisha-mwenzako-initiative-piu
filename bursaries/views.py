from django.views.generic.edit import FormView
from .create_form import CreateBursaryForm


class CreateBursaryApplicationView(FormView):
    template_name = "bursaries/create.html"
    form_class = CreateBursaryForm
