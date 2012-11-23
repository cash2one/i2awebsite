# coding: utf8
#!/usr/bin/env python
import os
from datetime import datetime

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util, template
from google.appengine.api import mail

from django.template import RequestContext
from django.shortcuts import render_to_response

DEBUG = False
GOOGLE_API_KEY = ''

technologies = {
    'python': {
        'icon': 'tech_used_01',
        'title': 'Python',
        'url': 'python'
        },
    'django': {
        'icon': 'tech_used_02',
        'title': 'Django framework',
        'url': 'django'
        },
    'celery': {
        'icon': 'tech_used_03',
        'title': 'Celery framework',
        'url': 'celery'
        },
    'mysql': {
        'icon': 'tech_used_04',
        'title': 'MySQL',
        'url': 'mysql'
        },
    'openstreetmap': {
        'icon': 'tech_used_05',
        'title': 'OpenStreetMap mapping solution',
        'url': 'openstreetmap'
        },
    'rabbitmq': {
        'icon': 'tech_used_06',
        'title': 'RabbitMQ message queue',
        'url': 'rabbitmq'
        },
    'rabbitmq': {
        'icon': 'tech_used_06',
        'title': 'RabbitMQ message queue',
        'url': 'rabbitmq'
        },
    'cassandra': {
        'icon': 'tech_used_07',
        'title': 'Apache Cassandra',
        'url': 'cassandra'
        },
    'solr': {
        'icon': 'tech_used_08',
        'title': 'Apache Solr full text enterprise search',
        'url': 'apachesolr'
        },
    'apache': {
        'icon': 'tech_used_09',
        'title': 'Apache Web Server',
        'url': 'apachews'
        },
    'linux': {
        'icon': 'tech_used_10',
        'title': 'Linux OS',
        'url': 'linux'
        },
    'ios': {
        'icon': 'tech_used_11',
        'title': 'iOS',
        'url': 'ios'
        },
    'android': {
        'icon': 'tech_used_12',
        'title': 'Android',
        'url': 'android'
        },
    'java': {
        'icon': 'tech_used_13',
        'title': 'Java',
        'url': 'java'
        },
    'php': {
        'icon': 'tech_used_14',
        'title': 'PHP 5',
        'url': 'php'
        },
    'symfony': {
        'icon': 'tech_used_15',
        'title': 'Symfony framework',
        'url': 'symfony'
        },
    'flash': {
        'icon': 'tech_used_16',
        'title': 'Flash',
        'url': 'flash'
        },
    'twilio': {
        'icon': 'tech_used_17',
        'title': 'Twilio SMS|VoiceCalls',
        'url': 'twilio'
        },
    'blackberry': {
        'icon': 'tech_used_18',
        'title': 'Blackberry',
        'url': 'blackberry'
        },
    'postgresql': {
        'icon': 'tech_used_19',
        'title': 'PostgreSQL database',
        'url': 'postgresql'
        },
    'postgis': {
        'icon': 'tech_used_20',
        'title': 'PostGIS Geospatial extensions',
        'url': 'postgis'
        },
    'apex': {
        'icon': 'tech_used_21',
        'title': 'Salesforce Apex',
        'url': 'apex'
        },
    'symbian': {
        'icon': 'tech_used_22',
        'title': 'Symbian',
        'url': 'symbian'
        },
    'dotnet': {
        'icon': 'tech_used_23',
        'title': '.NET Framework',
        'url': 'dotnet'
        },
    'skype': {
        'icon': 'tech_used_24',
        'title': 'Skype API',
        'url': 'skype'
        },
    'jquery': {
        'icon': 'tech_used_25',
        'title': 'jQuery',
        'url': 'jquery'
        },
    'oradb': {
        'icon': 'tech_used_26',
        'title': 'Oracle DB',
        'url': 'oradb'
        },
    'mssql': {
        'icon': 'tech_used_27',
        'title': 'Microsoft SQL Server',
        'url': 'mssql'
        },
    'opencv': {
        'icon': 'tech_used_28',
        'title': 'OpenCV',
        'url': 'opencv'
        }
}

projects = {
    'mom_method':{
        'title': 'MoM Method',
        'caption': 'MoM Method',
        'img_thumb': '/site_media/img/portfolio/mom_thumb.jpg',
        'img_wide': '/site_media/img/portfolio/mom_wide.jpg',
        'img_wide_alt': 'MoM Method, parenting application',
        'featured': False,
        'solution_web': True,
        'solution_digital_asset': True,
        'solution_scheduling': True,
        'solution_telephony': True,
        'url': '/portfolio/saas-applications/mom_method',
        'category': 'saas-applications',
        'techs': ['jquery', 'python', 'django', 'celery', 'mysql', 'apache', 'linux'],
        'challenge': u'Create an interactive website to teach children how to learn how to maintain a schedule and complete tasks.'
        },
    'tripbucket':{
        'title': 'Tripbucket.com - Travel Social Networking',
        'caption': 'Tripbucket',
        'img_thumb': '/site_media/img/portfolio/tripbucket_thumb.jpg',
        'img_wide': '/site_media/img/portfolio/tripbucket_wide.jpg',
        'img_wide_alt': 'Tripbucket - dream it, plan it, do it, share it',
        'featured': True,
        'solution_digital_asset': True,
        'solution_scheduling': True,
        'solution_mobile': True,
        'solution_location': True,
        'url': '/portfolio/location-platforms/tripbucket',
        'category': 'location-platforms',
        'techs': ['jquery', 'python', 'django', 'celery', 'openstreetmap', 'rabbitmq', 'postgresql', 'postgis', 'cassandra', 'solr', 'apache', 'linux'],
        'challenge': u'Create a website consumers could use to create a bucket list of dreams and track, record, and share their experiences with friends and other community members.'
        },
    'tripbucket_ad_platform':{
        'title': 'Tripbucket - Travel Targeted Ad Platform',
        'caption': 'Tripbucket Ad Platform',
        'img_thumb': '/site_media/img/portfolio/tripbucket_ad_thumb.jpg',
        'img_wide': '/site_media/img/portfolio/tripbucket_ad_wide.jpg',
        'img_wide_alt': 'Tripbucket - dream it, plan it, do it, share it',
        'featured': False,
        'url': '/portfolio/ad-platforms/tripbucket_ad_platform',
        'category': 'ad-platforms',
        'techs': ['python', 'java', 'postgresql', 'apache', 'linux'],
        'challenge': u'Create an ad platform that allows advertisers to send targeted ads to consumers who use travel-related web-based and mobile applications.'
        },
    'tripbucket_mobile':{
        'title': 'Tripbucket - Mobile Travel App',
        'caption': 'Tripbucket mobile',
        'img_thumb': '/site_media/img/portfolio/tripbucket_mobile_thumb.jpg',
        'img_wide': '/site_media/img/portfolio/tripbucket_mobile_wide.jpg',
        'img_wide_alt': 'Tripbucket - dream it, plan it, do it, share it',
        'featured': False,
        'solution_ad_delivery': True,
        'url': '/portfolio/mobile-apps/tripbucket_mobile',
        'category': 'mobile-apps',
        'techs': ['ios', 'android'],
        'challenge': u'Create a companion mobile TripBucket application that would work on iPhones and Android-based cell phones.'
        },
    'moasis':{
        'title': 'Moasis Global - Hyper Location Ad Platform',
        'caption': 'Moasis',
        'img_thumb': '/site_media/img/portfolio/moasis_thumb.jpg',
        'img_wide': '/site_media/img/portfolio/moasis_wide.jpg',
        'img_wide_alt': 'Moasis Global',
        'featured': True,
        'solution_ad_delivery': True,
        'solution_web': True,
        'solution_digital_asset': True,
        'solution_scheduling': True,
        'solution_location': True,
        'url': '/portfolio/ad-platforms/moasis',
        'category': 'ad-platforms',
        'techs': ['jquery', 'python', 'django', 'celery', 'mysql', 'openstreetmap', 'rabbitmq', 'cassandra', 'java', 'apache', 'linux', 'ios', 'android'],
        'challenge': u'Create a hyper location-based ad platform that allows advertisers to send targeted ads to people based on their location.'
        },
    'att':{
        'title': 'AT&amp;T eCommerce Site',
        'caption': 'AT&amp;T eCommerce Site',
        'img_thumb': '/site_media/img/portfolio/att_thumb.jpg',
        'img_wide': '/site_media/img/portfolio/att_wide.jpg',
        'img_wide_alt': 'AT&amp;T eCommerce Site',
        'featured': True,
        'solution_ad_delivery': True,
        'solution_enterprise': True,
        'solution_web': True,
        'solution_location': True,
        'solution_telephony': True,
        'url': '/portfolio/saas-applications/att',
        'category': 'saas-applications',
        'techs': ['jquery', 'php', 'symfony', 'mysql', 'apache', 'linux'],
        'challenge': u'Create an eCommerce website to resell AT&T home services and integrate a web-based application that interacts with AT&T’s web services.'
        },
    'mobile_deposit':{
        'title': 'Mobile Check Deposit',
        'caption': 'Mobile Check Deposit',
        'img_thumb': '/site_media/img/portfolio/bank_thumb.jpg',
        'img_wide': '/site_media/img/portfolio/bank_wide.jpg',
        'img_wide_alt': 'Mobile Check Deposit',
        'featured': True,
        'solution_consulting': True,
        'solution_mobile': True,
        'url': '/portfolio/mobile-apps/mobile_deposit',
        'category': 'mobile-apps',
        'techs': ['dotnet', 'java', 'blackberry', 'symbian', 'ios', 'skype'],
        'challenge': u'Create a secure distributed web and mobile solution that enables financial services organizations to offer remote check deposit capture to consumers and business customers.'
        },
    'facial_recognition':{
        'title': 'Facial Recognition Application R&D',
        'caption': 'Facial Recognition Application R&D',
        'img_thumb': '/site_media/img/portfolio/facial_thumb.jpg',
        'img_wide': '/site_media/img/portfolio/facial_wide.jpg',
        'img_wide_alt': 'Facial Recognition Application R&D',
        'featured': False,
        'solution_consulting': True,
        'url': '/portfolio/saas-applications/facial_recognition',
        'category': 'saas-applications',
        'techs': ['jquery', 'python', 'django', 'apache', 'linux', 'postgresql', 'opencv'],
        'challenge': u'Create a product that utilizes facial recognition software to match facial characteristics between groups of people.'
        },
    'knowledge_management_system':{
        'title': 'Knowledge Management System',
        'caption': 'Knowledge Management System',
        'img_thumb': '/site_media/img/portfolio/knowledge_thumb.jpg',
        'img_wide': '/site_media/img/portfolio/knowledge_wide.jpg',
        'img_wide_alt': 'Knowledge Management System',
        'featured': False,
        'solution_enterprise': True,
        'url': '/portfolio/saas-applications/knowledge_management_system',
        'category': 'saas-applications',
        'techs': ['java', 'oradb', 'mssql', 'apache'],
        'challenge': u'Create a SaaS application that enables globally distributed organizations to collaborate with each other seamlessly while retaining and protecting their intellectual capital. The client needed to create a flexible SaaS KMS that would cover needs from many different industries.'
        },
    'nba_team_applications':{
        'title': 'NBA Team Applications',
        'caption': 'NBA Team Applications',
        'img_thumb': '/site_media/img/portfolio/nba_thumb.jpg',
        'img_wide': '/site_media/img/portfolio/nba_wide.jpg',
        'img_wide_alt': 'NBA Team Applications',
        'featured': False,
        'solution_mobile': True,
        'url': '/portfolio/mobile-apps/nba_team_applications',
        'category': 'mobile-apps',
        'techs': ['python', 'django', 'celery', 'mysql', 'java', 'ios', 'android', 'linux'],
        'challenge': u'Create mobile applications that are used by NBA teams to stay connected with their fan base. The apps needed to work across multiple platforms and be capable of providing the quickest updates available while handling tens of thousands of users simultaneously.'
        },
    'nhl_team_applications':{
        'title': 'NHL Team Mobile Applications',
        'caption': 'NHL Team Mobile Applications',
        'img_thumb': '/site_media/img/portfolio/nhl_thumb.jpg',
        'img_wide': '/site_media/img/portfolio/nhl_wide.jpg',
        'img_wide_alt': 'NHL Team Mobile Applications',
        'featured': True,
        'solution_mobile': True,
        'url': '/portfolio/mobile-apps/nhl_team_applications',
        'category': 'mobile-apps',
        'techs': ['python', 'django', 'mysql', 'java', 'ios', 'android', 'linux'],
        'challenge': u'Create mobile applications used by NHL teams to stay connected with their fans. The apps were required to work across multiple platforms and provide near real-time game updates, while simultaneously handling tens of thousands of concurrent users.'
        },
    'salesforce':{
        'title': 'Saleforce.com to eCommerce Sites',
        'caption': 'Saleforce.com to eCommerce Sites',
        'img_thumb': '/site_media/img/portfolio/sale_thumb.jpg',
        'img_wide': '/site_media/img/portfolio/sale_wide.jpg',
        'img_wide_alt': 'Saleforce.com to eCommerce Sites',
        'featured': False,
        'solution_enterprise': True,
        'solution_consulting': True,
        'solution_telephony': True,
        'url': '/portfolio/saas-applications/salesforce',
        'category': 'saas-applications',
        'techs': ['jquery', 'java', 'mysql', 'linux', 'apex'],
        'challenge': u'Build a web-based application that seamlessly integrates the client’s many eCommerce applications into Salesforce.com. The solution needed to consolidate all the call center agents into one telephony solution based on Salesforce.com.'
        },
    'socialjane':{
        'title': 'SocialJane - Women Social Network',
        'caption': 'SocialJane - Women Social Network',
        'img_thumb': '/site_media/img/portfolio/socialjane_thumb.jpg',
        'img_wide': '/site_media/img/portfolio/socialjane_wide.jpg',
        'img_wide_alt': 'SocialJane - Women Social Network',
        'featured': False,
        'url': '/portfolio/saas-applications/socialjane',
        'category': 'saas-applications',
        'techs': ['jquery', 'php', 'mysql', 'linux', 'apache'],
        'challenge': u'Complete a social networking site designed for women.'
        },
    'speed_test':{
        'title': 'Bandwidthplace.com - Speedtest Site',
        'caption': 'Bandwidthplace.com - Speedtest Site',
        'img_thumb': '/site_media/img/portfolio/speed_thumb.jpg',
        'img_wide': '/site_media/img/portfolio/speed_wide.jpg',
        'img_wide_alt': 'Bandwidthplace.com - Speedtest Site',
        'featured': False,
        'url': '/portfolio/saas-applications/speed_test',
        'category': 'saas-applications',
        'techs': ['jquery', 'php', 'flash', 'linux', 'apache'],
        'challenge': u'Create a website that would allow people to test the speed of their Internet connection.'
        },
    'technical_support':{
        'title': 'Technical Support eCommerce Site',
        'caption': 'Technical Support eCommerce Site',
        'img_thumb': '/site_media/img/portfolio/tsd_thumb.jpg',
        'img_wide': '/site_media/img/portfolio/tsd_wide.jpg',
        'img_wide_alt': 'Technical Support eCommerce Site',
        'featured': False,
        'url': '/portfolio/saas-applications/technical_support',
        'category': 'saas-applications',
        'techs': ['jquery', 'php', 'symfony', 'mysql', 'apache', 'linux'],
        'challenge': u'Create a website to resell Tech Support for Dummies (TSD) services that integrates into the company’s web services.'
        },
    'independa':{
        'title': 'Home Healthcare Monitoring',
        'caption': 'Home Healthcare Monitoring',
        'img_thumb': '/site_media/img/portfolio/independa_thumb.jpg',
        'img_wide': '/site_media/img/portfolio/independa_wide.jpg',
        'img_wide_alt': 'Home Healthcare Monitoring',
        'featured': True,
        'solution_enterprise': True,
        'solution_web': True,
        'solution_digital_asset': True,
        'solution_scheduling': True,
        'solution_telephony': True,
        'url': '/portfolio/saas-applications/independa',
        'category': 'saas-applications',
        'techs': ['python', 'django', 'celery', 'jquery', 'postgresql', 'rabbitmq', 'twilio', 'apache', 'linux'],
        'challenge': u'Create a cloud based solution that extends and enhances the independence of an elderly loved ones and help postpone an assisted living situation.'
        },
    'startup-website':{
        'title': 'Startup Marketing Website',
        'caption': 'Startup Marketing Website',
        'img_thumb': '/site_media/img/portfolio/startup_thumb.jpg',
        'img_wide': '/site_media/img/portfolio/startup_wide.jpg',
        'img_wide_alt': 'Startup Marketing Website',
        'featured': False,
        'solution_consulting': True,
        'url': '/portfolio/saas-applications/startup-website',
        'category': 'saas-applications',
        'techs': ['php', 'mysql', 'linux', 'jquery'],
        'challenge': u'Create a marketing website prior to the launch of a new web-based product to attract additional funding for the product and beta users.'
        },
    'sport-ad-server':{
        'title': 'B3 Connect – Sports Team Targeted Ad Platform',
        'caption': 'B3 Connect – Sports Team Targeted Ad Platform',
        'img_thumb': '/site_media/img/portfolio/sport_ad_thumb.jpg',
        'img_wide': '/site_media/img/portfolio/sport_ad_wide.jpg',
        'img_wide_alt': 'B3 Connect – Sports Team Targeted Ad Platform',
        'featured': False,
        'solution_ad_delivery': True,
        'solution_location': True,
        'url': '/portfolio/ad-platforms/sport-ad-server',
        'category': 'ad-platforms',
        'techs': ['python', 'django', 'linux', 'java', 'mysql', 'apache', 'ios', 'android'],
        'challenge': u'Create an ad platform that allows advertisers to send targeted ads to people who use sports related web-based and mobile applications.'
        }
}

class MainPage(webapp.RequestHandler):
    def initialize(self, request, response):
        super(MainPage, self).initialize(request, response)
        path = self.request.path[1:] or '/'
        dir = path.split('/')
        project = projects.get(dir[-1], None) if 'portfolio/' in request.path else None
        techs = [val for key, val in technologies.items() if key in project['techs']] if project else None
        self.template_file = 'templates/aboutus.html' if path == '/' else 'templates/' + '/'.join(dir) + '.html'
        self.ctx = {'DEBUG': DEBUG, 
                    'GAPI': GOOGLE_API_KEY,
                    'page': path if path != '/' else 'aboutus',
                    'projects': projects,
                    'SITE_MEDIA': '%s/site_media' % request.path.split('/')[0],
                    'template': dir[-1],
                    'project': project,
                    'techs': techs,
                    'featured': filter(lambda x: x['featured'], projects.values()),
                    'not_featured': filter(lambda x: not x['featured'], projects.values()),
                    }
    def get(self):
        path = os.path.join(os.path.dirname(__file__), self.template_file)
        self.response.out.write(template.render(path, self.ctx))

class ContactPage(MainPage):
    def post(self, *args):
        message = mail.EmailMessage()
        message.sender = 'mpiwowarczyk@i2asolutions.com'
        message.to = 'inquiry@i2asolutions.com'
        message.subject = 'Message from i2a website'
        message.body = "Email from <%s>\n\n%s\n\nGenerated on: %s" % \
           (self.request.get('email'), self.request.get('txt'), datetime.today())
        message.send()
        self.redirect('/contact')

def main():
    webapp.template.register_template_library('filters')
    application = webapp.WSGIApplication(
       [('/', MainPage), 
        ('/careers', MainPage), 
        ('/process', MainPage), 
        ('/technologies', MainPage),
        ('/portfolio', MainPage),
        ('/portfolio/mobile-apps', MainPage),
        ('/portfolio/saas-applications', MainPage),
        ('/portfolio/location-platforms', MainPage),
        ('/portfolio/ad-platforms', MainPage),
        ('/solutions-enterprise', MainPage),
        ('/solutions-consulting', MainPage),
        ('/solutions-mobile', MainPage),
        ('/solutions-web', MainPage),
        ('/solutions-digital-asset', MainPage),
        ('/solutions-ad-delivery', MainPage),
        ('/solutions-scheduling-alerting', MainPage),
        ('/solutions-location-platforms', MainPage),
        ('/solutions-telephony', MainPage),
        ('/expertise', MainPage),
        ('/contact', ContactPage),
        ] + [(project['url'], MainPage) for project in projects.values()],
        debug=DEBUG)
    util.run_wsgi_app(application)

if __name__ == '__main__':
    main()

