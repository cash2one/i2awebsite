from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'i2awebsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(
        template_name='home.html'),
        {'menu_pos': 'home'},
        name='home',
    ),
    url(r'^technologies/$', TemplateView.as_view(
        template_name='technologies.html'),
        {'menu_pos': 'technologies'},
        name='technologies',
    ),
    url(r'^portfolio/$', TemplateView.as_view(
        template_name='portfolio.html'),
        {'menu_pos': 'portfolio'},
        name='portfolio',
    ),
    url(r'^category/$', TemplateView.as_view(
        template_name='category.html'),
        {'menu_pos': 'categories', 'submenu_pos': 'webapps'},
        name='solutions-category',
    ),
    url(r'^solutions/ad_delivery/$', TemplateView.as_view(
        template_name='categories/ad_delivery.html'),
        {'menu_pos': 'categories', 'submenu_pos': 'ads'},
        name='solutions-ads',
    ),
    url(r'^solutions/consulting/$', TemplateView.as_view(
        template_name='categories/consulting.html'),
        {'menu_pos': 'categories', 'submenu_pos': 'consulting'},
        name='solutions-consulting',
    ),
    url(r'^solutions/digital_asset_management/$', TemplateView.as_view(
        template_name='categories/asset_management.html'),
        {'menu_pos': 'categories', 'submenu_pos': 'assets'},
        name='solutions-assets',
    ),
    url(r'^solutions/enterprise/$', TemplateView.as_view(
        template_name='categories/enterprise.html'),
        {'menu_pos': 'categories', 'submenu_pos': 'enterprise'},
        name='solutions-enterprise',
    ),
    url(r'^solutions/location_based/$', TemplateView.as_view(
        template_name='categories/location.html'),
        {'menu_pos': 'categories', 'submenu_pos': 'location'},
        name='solutions-location',
    ),
    url(r'^solutions/mobile/$', TemplateView.as_view(
        template_name='categories/mobile.html'),
        {'menu_pos': 'categories', 'submenu_pos': 'mobile'},
        name='solutions-mobile',
    ),
    url(r'^solutions/scheduling/$', TemplateView.as_view(
        template_name='categories/scheduling.html'),
        {'menu_pos': 'categories', 'submenu_pos': 'scheduling'},
        name='solutions-scheduling',
    ),
    url(r'^solutions/social/$', TemplateView.as_view(
        template_name='categories/social.html'),
        {'menu_pos': 'categories', 'submenu_pos': 'social'},
        name='solutions-social',
    ),
    url(r'^solutions/telephony/$', TemplateView.as_view(
        template_name='categories/telephony.html'),
        {'menu_pos': 'categories', 'submenu_pos': 'telephony'},
        name='solutions-telephony',
    ),
    url(r'^solutions/web/$', TemplateView.as_view(
        template_name='categories/web.html'),
        {'menu_pos': 'categories', 'submenu_pos': 'web'},
        name='solutions-web',
    ),
)
