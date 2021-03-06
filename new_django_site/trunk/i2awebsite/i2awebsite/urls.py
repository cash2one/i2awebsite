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
    url(r'^portfolio-more/$', TemplateView.as_view(
        template_name='portfolio-more.html'),
        {'menu_pos': 'portfolio'},
        name='portfolio-more',
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
    url(r'^solutions/$', TemplateView.as_view(
        template_name='solutions.html'),
        {'menu_pos': 'solutions'},
        name='solutions',
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
    url(r'^portfolio/telvise/$', TemplateView.as_view(
        template_name='portfolio/telvise.html'),
        {'menu_pos': 'portfolio'},
        name='portfolio-telvise',
    ),
        url(r'^portfolio/trekadoo/$', TemplateView.as_view(
        template_name='portfolio/trekadoo.html'),
        {'menu_pos': 'portfolio'},
        name='portfolio-trekadoo',
    ),
         url(r'^portfolio/impressme/$', TemplateView.as_view(
        template_name='portfolio/impressme.html'),
        {'menu_pos': 'portfolio'},
        name='portfolio-impressme',
    ),
         url(r'^portfolio/mflyer/$', TemplateView.as_view(
        template_name='portfolio/mflyer.html'),
        {'menu_pos': 'portfolio'},
        name='portfolio-mflyer',
    ),
        url(r'^portfolio/spendit/$', TemplateView.as_view(
        template_name='portfolio/spendit.html'),
        {'menu_pos': 'portfolio'},
        name='portfolio-spendit',
    ),
        url(r'^portfolio/creativeprocess/$', TemplateView.as_view(
        template_name='portfolio/creativeprocess.html'),
        {'menu_pos': 'portfolio'},
        name='portfolio-creativeprocess',
    ),
        url(r'^portfolio/fansircle/$', TemplateView.as_view(
        template_name='portfolio/fansircle.html'),
        {'menu_pos': 'portfolio'},
        name='portfolio-fansircle',
    ),
        url(r'^portfolio/nba_combine/$', TemplateView.as_view(
        template_name='portfolio/nba_combine.html'),
        {'menu_pos': 'portfolio'},
        name='portfolio-nba_combine',
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
    url(r'^portfolio/99brews/$', TemplateView.as_view(
        template_name='portfolio/99brews.html'),
        {'menu_pos': 'portfolio'},
        name='portfolio-99brews',
    ),
    url(r'^portfolio/balboa_park/$', TemplateView.as_view(
        template_name='portfolio/balboa_park.html'),
        {'menu_pos': 'portfolio'},
        name='portfolio-balboapark',
    ),
    url(r'^portfolio/swim_meet/$', TemplateView.as_view(
        template_name='portfolio/swim_meet.html'),
        {'menu_pos': 'portfolio'},
        name='portfolio-swim_meet',
    ),
    url(r'^portfolio/track_meet/$', TemplateView.as_view(
        template_name='portfolio/track_meet.html'),
        {'menu_pos': 'portfolio'},
        name='portfolio-track_meet',
    ),
    url(r'^portfolio/usnp/$', TemplateView.as_view(
        template_name='portfolio/usnp.html'),
        {'menu_pos': 'portfolio'},
        name='portfolio-usnp',
    ),
    url(r'^portfolio/battleship/$', TemplateView.as_view(
        template_name='portfolio/battleship.html'),
        {'menu_pos': 'portfolio'},
        name='portfolio-battleship',
    ),
    url(r'^portfolio/sandiego-museum-of-art/$', TemplateView.as_view(
        template_name='portfolio/sandiego-museum.html'),
        {'menu_pos': 'portfolio'},
        name='portfolio-sandiego-museum',
    ),
    url(r'^portfolio/lookbooker/$', TemplateView.as_view(
        template_name='portfolio/lookbooker.html'),
        {'menu_pos': 'portfolio'},
        name='portfolio-lookbooker',
    ),
    url(r'^portfolio/lifealert/$', TemplateView.as_view(
        template_name='portfolio/lifealert.html'),
        {'menu_pos': 'portfolio'},
        name='portfolio-lifealert',
    ),
    url(r'^portfolio/venissimo/$', TemplateView.as_view(
        template_name='portfolio/venissimo.html'),
        {'menu_pos': 'portfolio'},
        name='portfolio-venissimo',
    ),
    url(r'^portfolio/idwallet/$', TemplateView.as_view(
        template_name='portfolio/idwallet.html'),
        {'menu_pos': 'portfolio'},
        name='portfolio-idwallet',
    ),
    url(r'^portfolio/telemed/$', TemplateView.as_view(
        template_name='portfolio/telemed.html'),
        {'menu_pos': 'portfolio'},
        name='portfolio-telemed',
    ),
    url(r'^portfolio-mmajunkie/$', TemplateView.as_view(
        template_name='portfolio/mmajunkie.html'),
        {'menu_pos': 'portfolio'},
        name='portfolio-mmajunkie',
    ),
    url(r'^portfolio-bandwidthplace/$', TemplateView.as_view(
        template_name='portfolio/bandwidthplace.html'),
        {'menu_pos': 'portfolio'},
        name='portfolio-bandwidthplace',
    ),
    url(r'^portfolio-sportsusa/$', TemplateView.as_view(
        template_name='portfolio/sportsusa.html'),
        {'menu_pos': 'portfolio'},
        name='portfolio-sportsusa',
    ),
    url(r'^portfolio-insynchub/$', TemplateView.as_view(
        template_name='portfolio/insynchub.html'),
        {'menu_pos': 'portfolio'},
        name='portfolio-insynchub',
    ),
    url(r'^portfolio-theguru/$', TemplateView.as_view(
        template_name='portfolio/theguru.html'),
        {'menu_pos': 'portfolio'},
        name='portfolio-theguru',
    ),
)