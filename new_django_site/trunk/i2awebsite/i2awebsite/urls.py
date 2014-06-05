from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'i2awebsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

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
    url(r'^careers/$', TemplateView.as_view(
        template_name='careers.html'),
        {'menu_pos': 'careers'},
        name='careers',
    ),
    url(r'^contact/$', TemplateView.as_view(
        template_name='contact.html'),
        {'menu_pos': 'contact'},
        name='contact',
    ),
    url(r'^our_process/$', TemplateView.as_view(
        template_name='our_process.html'),
        name='our_process',
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
    url(r'^portfolio/atnt/$', TemplateView.as_view(
        template_name='portfolio/atnt.html'),
        {'menu_pos': 'portfolio'},
        name='portfolio-atnt',
    ),
    url(r'^portfolio/billpay/$', TemplateView.as_view(
        template_name='portfolio/billpay.html'),
        {'menu_pos': 'portfolio'},
        name='portfolio-billpay',
    ),
    url(r'^portfolio/facial/$', TemplateView.as_view(
        template_name='portfolio/facial.html'),
        {'menu_pos': 'portfolio'},
        name='portfolio-facial',
    ),
    url(r'^portfolio/fanserv/$', TemplateView.as_view(
        template_name='portfolio/fanserv.html'),
        {'menu_pos': 'portfolio'},
        name='portfolio-fanserv',
    ),
    url(r'^portfolio/independa/$', TemplateView.as_view(
        template_name='portfolio/independa.html'),
        {'menu_pos': 'portfolio'},
        name='portfolio-independa',
    ),
    url(r'^portfolio/kms/$', TemplateView.as_view(
        template_name='portfolio/kms.html'),
        {'menu_pos': 'portfolio'},
        name='portfolio-kms',
    ),
    url(r'^portfolio/moasis/$', TemplateView.as_view(
        template_name='portfolio/moasis.html'),
        {'menu_pos': 'portfolio'},
        name='portfolio-moasis',
    ),
    url(r'^portfolio/mobile_check/$', TemplateView.as_view(
        template_name='portfolio/mobile_check.html'),
        {'menu_pos': 'portfolio'},
        name='portfolio-mobile_check',
    ),
    url(r'^portfolio/mom/$', TemplateView.as_view(
        template_name='portfolio/mom.html'),
        {'menu_pos': 'portfolio'},
        name='portfolio-mom',
    ),
    url(r'^portfolio/nba/$', TemplateView.as_view(
        template_name='portfolio/nba.html'),
        {'menu_pos': 'portfolio'},
        name='portfolio-nba',
    ),
    url(r'^portfolio/nba_dev/$', TemplateView.as_view(
        template_name='portfolio/nba_dev.html'),
        {'menu_pos': 'portfolio'},
        name='portfolio-nba_dev',
    ),
    url(r'^portfolio/nba_rtp/$', TemplateView.as_view(
        template_name='portfolio/nba_rtp.html'),
        {'menu_pos': 'portfolio'},
        name='portfolio-nba_rtp',
    ),
    url(r'^portfolio/nhl/$', TemplateView.as_view(
        template_name='portfolio/nhl.html'),
        {'menu_pos': 'portfolio'},
        name='portfolio-nhl',
    ),
    url(r'^portfolio/salesforce/$', TemplateView.as_view(
        template_name='portfolio/salesforce.html'),
        {'menu_pos': 'portfolio'},
        name='portfolio-salesforce',
    ),
    url(r'^portfolio/socialjane/$', TemplateView.as_view(
        template_name='portfolio/socialjane.html'),
        {'menu_pos': 'portfolio'},
        name='portfolio-socialjane',
    ),
    url(r'^portfolio/tdg/$', TemplateView.as_view(
        template_name='portfolio/tdg.html'),
        {'menu_pos': 'portfolio'},
        name='portfolio-tdg',
    ),
    url(r'^portfolio/tech_support/$', TemplateView.as_view(
        template_name='portfolio/tech_support.html'),
        {'menu_pos': 'portfolio'},
        name='portfolio-tech_support',
    ),
    url(r'^portfolio/tripbucket_ad/$', TemplateView.as_view(
        template_name='portfolio/tripbucket_ad.html'),
        {'menu_pos': 'portfolio'},
        name='portfolio-tripbucket_ad',
    ),
    url(r'^portfolio/tripbucket_mobile/$', TemplateView.as_view(
        template_name='portfolio/tripbucket_mobile.html'),
        {'menu_pos': 'portfolio'},
        name='portfolio-tripbucket_mobile',
    ),
    url(r'^portfolio/tripbucket_web/$', TemplateView.as_view(
        template_name='portfolio/tripbucket_web.html'),
        {'menu_pos': 'portfolio'},
        name='portfolio-tripbucket_web',
    ),
)
