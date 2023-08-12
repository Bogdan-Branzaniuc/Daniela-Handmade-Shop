from django_unicorn.components import UnicornView
from products.models import AvailableColor
from scipy.spatial import KDTree
from webcolors import CSS3_HEX_TO_NAMES, hex_to_rgb
from django.contrib import messages


class AdminAddColorFormView(UnicornView):
    available_colors = None
    hexcolor = None
    name = None
    soft_deleted_colors = None

    def mount(self):
        self.available_colors = AvailableColors.objects.all()
        self.hexcolor = '#000000'
        self.name = 'black'
        self.soft_deleted_colors = []

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
            messages.error(
                self.request, f'{self.name} is already in the available colors')
        self.call('pageReload')

    def soft_delete(self, color):
        self.soft_deleted_colors.append(color)

    def restore_color(self, color):
        self.soft_deleted_colors.remove(color)

    def perma_delete_color(self, color):
        AvailableColors.objects.get(name_EN=color).delete()
        self.soft_deleted_colors.remove(color)
        self.call('pageReload')
        messages.success(
            self.request, f"Successfully deleted {color} from available colors")
