from jet.dashboard import modules
from django.utils.translation import gettext_lazy as _
from jet.dashboard.dashboard import Dashboard, AppIndexDashboard

class CustomIndexDashboard(Dashboard):
    columns = 3

class DefaultAppIndexDashboard(AppIndexDashboard):
    def init_with_context(self, context):
        self.available_children.append(modules.LinkList)

        self.children.append(modules.ModelList(
            title=_('Application models'),
            models=self.models(),
            column=0,
            order=0
        ))
        
class CustomIndexDashboard(Dashboard):
    columns = 3

    def init_with_context(self, context):
        self.available_children.append(modules.LinkList)
        self.children.append(modules.LinkList(
            _('Gestion'),
            children=[
                {
                    'title': _('Reclamos'),
                    'url': '/admin/cliente/reclamo/',
                    'external': False,
                },
                {
                    'title': _('Graficos'),
                    'url': '/graficos/',
                    'external': False,
                },
                {
                    'title': _('Modelo Predictivo'),
                    'url': '/prediccion/',
                    'external': False,
                },
                {
                    'title': _('Ventas'),
                    'url': '/admin/web/venta/',
                    'external': False,
                },
            ],
            column=1,
            order=0
        ))
        self.children.append(modules.AppList(
            _('Aplicaciones'),
            exclude=('auth.*','social_django.*'),
            column=0,
            order=0
        ))
