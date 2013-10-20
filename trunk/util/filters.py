import re
from google.appengine.ext import webapp

try:
  from google.appengine._internal.django.utils.safestring import mark_safe
  from google.appengine._internal.django.utils.html import conditional_escape
except ImportError:
  # For unit tests, just return the same string.
  mark_safe = lambda x: x
  conditional_escape = lambda x: x

register = webapp.template.create_template_register()

def obfuscate(email, linktext=None, autoescape=None):
    """
    Given a string representing an email address,
	returns a mailto link with rot13 JavaScript obfuscation.

    Accepts an optional argument to use as the link text;
	otherwise uses the email address itself.
    """
#    if autoescape:
#        esc = conditional_escape
#    else:
#        esc = lambda x: x

    esc = lambda x: x

    email = re.sub('@','\\\\100', re.sub('\.', '\\\\056', \
        esc(email))).encode('rot13')

    if linktext:
        linktext = esc(linktext).encode('rot13')
    else:
        linktext = email

    rotten_link = """<script type="text/javascript">document.write \
        ("<n uers=\\\"znvygb:%s\\\">%s<\\057n>".replace(/[a-zA-Z]/g, \
        function(c){return String.fromCharCode((c<="Z"?90:122)>=\
        (c=c.charCodeAt(0)+13)?c:c-26);}));</script>""" % (email, linktext)
    return mark_safe(rotten_link)
obfuscate.needs_autoescape = True
register.filter(obfuscate)
