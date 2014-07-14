__author__ = 'isaac'
from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from pricecaculator.models import Usage, Use, Placement, Size, Territory,  Duration, PrintRun


class UsageForm(ModelForm):
    class Meta:
        model = Usage

UseFormset = inlineformset_factory(Usage, Use)
PlacementFormset = inlineformset_factory(Usage, Placement)
SizeFormset = inlineformset_factory(Usage, Size)
TerritoryFormset = inlineformset_factory(Usage, Territory)
DurationFormset = inlineformset_factory(Usage, Duration)
PrintRunFormset = inlineformset_factory(Usage, PrintRun)

