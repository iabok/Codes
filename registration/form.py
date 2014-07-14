from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from .models import Recipe, Ingredient, Instruction


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe


IngredientFormSet = inlineformset_factory(Recipe, Ingredient)
InstructionFormSet = inlineformset_factory(Recipe, Instruction)