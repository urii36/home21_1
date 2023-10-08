from django import forms

from catalog.models import Version, Product


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
    version = forms.ModelChoiceField(queryset=Version.objects.all(), required=False, empty_label="Выберите версию")


class Meta:
    model = Product
    fields = ['name', 'description', 'preview_description', 'image', 'category', 'price', 'version']


def clean_name(self):
    name = self.cleaned_data['name'].lower()
    for word in self.forbidden_words:
        if word in name:
            raise forms.ValidationError(f"Нельзя использовать слово '{word}' в названии продукта.")
    return name


def clean_description(self):
    description = self.cleaned_data['description'].lower()
    for word in self.forbidden_words:
        if word in description:
            raise forms.ValidationError(f"Нельзя использовать слово '{word}' в описании продукта.")
    return description


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = ['number', 'name', 'is_active']
