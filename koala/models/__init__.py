"""
Core models

"""
from pyramid.security import Allow, Authenticated


class SiteRootFactory(object):
    """Every Pyramid site that implements authentication/authorization needs a root factory,
       We may implement ACLs at the resource level, but the site-level ACL is defined here
    """
    __acl__ = [
        (Allow, Authenticated, 'view')
    ]

    def __init__(self, request):
        pass

