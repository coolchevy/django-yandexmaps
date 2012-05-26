from django.template import Library, TemplateSyntaxError, Node, Variable
from django.template.loader import get_template
from django.template import Context
from django.contrib.sites.models import Site
from yandexmaps.settings import DEFAULT_WIDTH,DEFAULT_HEIGHT,YANDEXMAPS_API_KEY

register = Library()

class YandexMapByAddressNode(Node):
    def __init__(self, address, title, wh):
        self.address = Variable(address)
        self.title = Variable(title)
        self.wh = wh

    def render(self, context):
        if not YANDEXMAPS_API_KEY:
            raise TemplateSyntaxError('YANDEXMAPS_API_KEY is undefined in settings.py')
        address = self.address.resolve(context)
        title = self.title.resolve(context)
        ctx = {
                'map_width':DEFAULT_WIDTH,
                'map_height':DEFAULT_HEIGHT,
                "title":title,
                "address":address,
                "API_KEY":YANDEXMAPS_API_KEY,
                "copyright":Site.objects.get_current().domain,
                }
        if self.wh:
            ctx.update({
                'map_width':self.wh[0],
                'map_height':self.wh[1],
                })
        t = get_template("yandexmaps/map_by_address.html")
        return t.render(Context(ctx))

@register.tag
def yandex_map_by_address(parser, token):
    """
    {% yandex_map_by_address address infobox width,height %}
    """
    bits = token.split_contents()
    if len(bits)<3:
        raise TemplateSyntaxError('%s tag requires more arguments' % bits[0])
    if len(bits) == 4:
        wh = bits[3].split(",")
        if len(wh)<2:
            raise TemplateSyntaxError('%s tag has invalid wight,height argument' % bits[0])
    else:
        wh = None
    return YandexMapByAddressNode(bits[1],bits[2],wh)
