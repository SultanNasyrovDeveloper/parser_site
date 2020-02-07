from landing.index.models import SiteSettings


def site_settings(request):
    return {'settings': SiteSettings.load()}
