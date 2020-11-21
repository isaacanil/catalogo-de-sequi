from tethys_sdk.base import TethysAppBase, url_map_maker


class CatalogoDeSequiaRd(TethysAppBase):
    """
    Tethys app class for Catalogo De Sequia RD.
    """

    name = 'Catálogo en Línea de Sequías'
    index = 'catalogo_de_sequia_rd:home'
    icon = 'catalogo_de_sequia_rd/images/icon.gif'
    package = 'catalogo_de_sequia_rd'
    root_url = 'catalogo-de-sequia-rd'
    color = '#c0392b'
    description = 'Historial de ocurrencia de sequias en el territorio dominicano.'
    tags = 'Sequía'
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='catalogo-de-sequia-rd',
                controller='catalogo_de_sequia_rd.controllers.home'
            ),
        )

        return url_maps