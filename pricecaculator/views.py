from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView


from pricecaculator.forms import UsageForm, UseFormset, PlacementFormset, SizeFormset, TerritoryFormset,\
    DurationFormset, PrintRunFormset

from pricecaculator.models import Usage


class PriceCreateView(CreateView):
    template_name = 'pricecaculator/price_add_form.html'
    model = Usage
    form_class = UsageForm
    success_url = 'success/'

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        use_form = UseFormset()
        placement_form = PlacementFormset()
        size_form = SizeFormset()
        territory_form = TerritoryFormset()
        duration_form = DurationFormset()
        print_run_form = PrintRunFormset()
        return self.render_to_response(
            self.get_context_data(form=form,
                                  use_form=use_form,
                                  placement_form=placement_form,
                                  size_form=size_form,
                                  territory_form=territory_form,
                                  duration_form=duration_form,
                                  print_run_form=print_run_form))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        use_form = UseFormset(self.request.POST)
        placement_form = PlacementFormset(self.request.POST)
        size_form = SizeFormset(self.request.POST)
        territory_form = TerritoryFormset(self.request.POST)
        duration_form = DurationFormset(self.request.POST)
        print_run_form = PrintRunFormset(self.request.POST)

        if (form.is_valid() and use_form.is_valid() and placement_form.is_valid() and
            size_form.is_valid() and territory_form.is_valid() and duration_form.is_valid()
                and print_run_form.is_valid()):
            return self._form_valid(form,
                                    use_form,
                                    placement_form,
                                    size_form,
                                    territory_form,
                                    duration_form,
                                    print_run_form)

        else:
            return self._form_invalid(form,
                                      use_form,
                                      placement_form,
                                      size_form,
                                      territory_form,
                                      duration_form,
                                      print_run_form)

    def _form_valid(self, form, use_form, placement_form, size_form, territory_form, duration_form, print_run_form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        self.object = form.save()

        use_form.instance = self.object
        use_form.save()

        placement_form.instance = self.object
        placement_form.save()

        size_form.instance = self.object
        size_form.save()

        territory_form.instance = self.object
        territory_form.save()

        duration_form.instance = self.object
        duration_form.save()

        print_run_form.instance = self.object
        print_run_form.save()

        return HttpResponseRedirect(self.get_success_url())

    def _form_invalid(self, form, use_form, placement_form, size_form, territory_form, duration_form, print_run_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form,
                                  use_form=use_form,
                                  placement_form=placement_form,
                                  size_form=size_form,
                                  territory_form=territory_form,
                                  duration_form=duration_form,
                                  print_run_form=print_run_form))
