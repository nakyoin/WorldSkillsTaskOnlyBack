from rest_framework.authentication import TokenAuthentication


class BearerAuth(TokenAuthentication):
    keyword='Bearer'