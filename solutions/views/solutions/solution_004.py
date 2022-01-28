from django.views.generic.base import TemplateView


class Solution004(TemplateView):
    template_name = "solutions/solution_004/view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["show_information"] = False

        return context