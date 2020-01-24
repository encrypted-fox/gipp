from rest_framework.response import Response
from rest_framework.views import APIView


class DocsView(APIView):

    @staticmethod
    def get(request, *args, **kwargs):
        api_docs = response = {
            "api/v0/": {
                "documentation": {
                    "swagger": request.build_absolute_uri("api/v0/swagger"),
                    "redoc": request.build_absolute_uri("api/v0/redoc"),
                },
                "admin": request.build_absolute_uri("api/v0/admin"),
                "authentication": {
                    "auth/register": request.build_absolute_uri("api/v0/auth/register"),
                    "auth/login": request.build_absolute_uri("api/v0/auth/login"),
                    "auth/refresh": request.build_absolute_uri("api/v0/auth/refresh"),
                    "auth/revoke": request.build_absolute_uri("api/v0/auth/revoke"),
                },
                "posts": {
                    "posts": request.build_absolute_uri("api/v0/posts"),
                },
                "constructor": {
                    "sites": request.build_absolute_uri("api/v0/sites"),
                    "statuses": request.build_absolute_uri("api/v0/statuses"),
                    "site_statuses": request.build_absolute_uri("api/v0/site_statuses"),
                    "html_heads": request.build_absolute_uri("api/v0/html_heads"),
                    "headers": request.build_absolute_uri("api/v0/headers"),
                    "footers": request.build_absolute_uri("api/v0/footers"),
                    "mains": request.build_absolute_uri("api/v0/mains"),
                    "added_blocks": request.build_absolute_uri("api/v0/added_blocks"),
                    "block_templates": request.build_absolute_uri("api/v0/block_templates"),
                },
            }
        }
        return Response(api_docs)
