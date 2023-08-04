from django.forms.widgets import ClearableFileInput, CheckboxSelectMultiple
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = 'products/custom_widget_templates/custom_clearable_file_input.html'


class CustomCheckboxSelectMultiple(CheckboxSelectMultiple):
    allow_multiple_selected = True
    input_type = "checkbox"
    template_name = "products/custom_widget_templates/custom_checkbox_with_color.html"
    option_template_name = "django/forms/widgets/checkbox_option.html"
