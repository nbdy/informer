from . import SiteObject


class AmazonProduct(SiteObject):
    cc = "com"
    product_id = ""

    DROPDOWN_AVAILABLE = "dropdownAvailable"
    DROPDOWN_UNAVAILABLE = "dropdownUnavailable"

    def __init__(self, driver):
        SiteObject.__init__(self, driver)
        self.url = "https://www.amazon.%s/gp/product/%s/" % (self.cc, self.product_id)

    def on_dropdown_available(self):
        print("available")

    def on_dropdown_unavailable(self):
        print("unavailable")

    def dropdown_available(self):
        if self.element.get_attribute("class") == self.DROPDOWN_AVAILABLE:
            self.on_dropdown_available()
        else:
            self.on_dropdown_unavailable()

    def get(self):
        SiteObject.get(self)
        self.dropdown_available()


class AmazonDEProduct(AmazonProduct):
    cc = "de"


class AmazonCOMProduct(AmazonProduct):
    cc = "com"


class BoxFreshSpencer(AmazonDEProduct):
    product_id = "B071GC749G"


class BoxFreshSpencerBrown46(BoxFreshSpencer):
    target = "native_size_name_6"


class BoxFreshSpencerBrown40(BoxFreshSpencer):
    target = "native_size_name_0"
