from django.conf import settings
from django.urls import include, path, re_path
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views

#from django.contrib.sitemaps.views import sitemap
from django.conf.urls.i18n import i18n_patterns
#{%- if cookiecutter.use_async == 'y' %}
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#{%- endif %}
#{%- if cookiecutter.use_drf == 'y' %}
#from rest_framework.authtoken.views import obtain_auth_token
#{%- endif %}
#from posts.feeds import LastEntriesFeed
#from posts.sitemaps import PostSitemap

#sitemaps = {
#    'posts': PostSitemap,
#}


#from import subscription, unsubscription

urlpatterns = [
    #path("", TemplateView.as_view(template_name="pages/home.html"), 
    #    name="home"
    #),
    #path(
    #    "about/",
    #    TemplateView.as_view(template_name="pages/about.html"),
    #    name="about",
    #),
    path('', include('static_page.urls')),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management0
    #re_path("users/", include("base_new.users.urls", namespace="users")),
    # other urls
    re_path('accounts/', include('allauth.urls')),
    re_path('users/', include('users.urls')),
    #re_path('service/', include('services.urls')),
    # Your stuff: custom urls includes go here
    re_path('robots\.txt', include('robots.urls')),
    #path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
    #     name='django.contrib.sitemaps.views.sitemap'
    #)
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
#{%- if cookiecutter.use_async == 'y' %}
#if settings.DEBUG:
    # Static file serving when using Gunicorn + Uvicorn for local web socket development
#    urlpatterns += staticfiles_urlpatterns()
#{%- endif %}
#{% if cookiecutter.use_drf == 'y' %}
# API URLS
#urlpatterns += [
    # API base url
#    path("api/", include("config.api_router")),
    # DRF auth token
#    path("auth-token/", obtain_auth_token),
#]
#{%- endif %}
if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] \
            + urlpatterns
