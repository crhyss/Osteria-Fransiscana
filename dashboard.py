from jet.dashboard import modules
from django.utils.translation import gettext_lazy as _
from jet.dashboard.dashboard import Dashboard, AppIndexDashboard

class CustomIndexDashboard(Dashboard):
    columns = 3

    def init_with_context(self, context):
        self.children.append(modules.AppList(
            _('Aplicacion'),
            exclude=('social_django.*',),
            column=0,
            order=0
        ))
        self.available_children.append(modules.LinkList)
        self.children.append(modules.LinkList(
            _('Gestion'),
            children=[
                {
                    'title': _('Visualizar Ordenes'),
                    'url': '/ordenes/',
                    'external': False,
                },
                {
                    'title': _('Reclamos'),
                    'url': '/logeo/reclamo/lista/',
                    'external': False,
                },
            ],
            column=1,
            order=0
        ))
