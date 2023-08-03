from django_unicorn.components import UnicornView
from products.forms import AvailableColorsForm
from products.models import AvailableColors
from scipy.spatial import KDTree
from webcolors import CSS3_HEX_TO_NAMES, hex_to_rgb
from django.contrib import messages



class AdminAddColorFormView(UnicornView):

    form_class = AvailableColorsForm

    available_colors = None
    hexcolor = None
    name = None

    def mount(self):
        self.available_colors = AvailableColors.objects.all()
        self.hexcolor = '#000000'
        self.name = 'black'

    def add_color(self):
        def convert_rgb_to_names(rgb_tuple):
            # a dictionary of all the hex and their respective names in css3
            # source https://medium.com/codex/rgb-to-color-names-in-python-the-robust-way-ec4a9d97a01f
            css3_db = CSS3_HEX_TO_NAMES
            names = []
            rgb_values = []
            for color_hex, color_name in css3_db.items():
                names.append(color_name)
                rgb_values.append(hex_to_rgb(color_hex))

            kdt_db = KDTree(rgb_values)
            distance, index = kdt_db.query(rgb_tuple)
            return names[index]

        self.name = convert_rgb_to_names(hex_to_rgb(self.hexcolor))

        if not AvailableColors.objects.filter(name_EN=self.name).exists():
            AvailableColors.objects.create(
                name_EN=self.name,
                hexcolor=self.hexcolor
            )
        else:
            messages.error(self.request, 'This color is already available')
        self.call('pageReload')