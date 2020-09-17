from django.conf import settings

def global_setting(request):
    """
    settings for the site
    """
    return {
        'SITE_NAME': settings.SITE_NAME,
        'SITE_DESC': settings.SITE_DESCRIPTION,
        'SITE_KEY': settings.SECRET_KEY,
        #'SITE_MAIL': settings.SITE_MAIL,
        #'SITE_ICP': settings.SITE_ICP,
        #'SITE_ICP_URL': settings.SITE_ICP_URL,
        'SITE_TITLE': settings.SITE_TITLE,
    }