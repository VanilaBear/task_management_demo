from django.conf import settings
from django.utils import timezone
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed


class ExpiringTokenAuthentication(TokenAuthentication):
    """An extension to the TokenAuthentication class"""

    def authenticate_credentials(self, key):
        """Checks token's validity"""
        user, token = super().authenticate_credentials(key)

        if token.created < timezone.now() - settings.TOKEN_EXPIRATION_TIME:
            raise AuthenticationFailed("Token has expired")

        return user, token