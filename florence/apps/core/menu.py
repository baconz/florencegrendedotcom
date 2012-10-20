from cms.models import Page
from menus.base import Modifier
from menus.menu_pool import menu_pool

class ZinniaMenuModifier(Modifier):
    """

    """
    def modify(self, request, nodes, namespace, root_id, post_cut, breadcrumb):
        """We want all parts of zinnia to show the blog selected."""
        if post_cut:
            return nodes
        # Find out if it is a Zinnia Page
        try:
            blog_page = Page.objects.filter(
                title_set__application_urls="ZinniaApphook"
            ).get()
        except Page.DoesNotExist:
            blog_page = None
        if blog_page and request.path.startswith("/%s" % blog_page.get_path()):
            for node in nodes:
                if node.title == blog_page.get_title():
                    node.selected = True
        # Not sure what this does?
        count = 0
        for node in nodes:
            node.counter = count
            count += 1
        return nodes

menu_pool.register_modifier(ZinniaMenuModifier)
