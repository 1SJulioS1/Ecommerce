from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

access_token_ = {200: openapi.Response(
    description='Success',
    schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'access token': openapi.Schema(type=openapi.TYPE_STRING,
                                                   description='Bearer Token',
                                                   ),
                    'refresh token': openapi.Schema(
                        type=openapi.TYPE_STRING,
                        description='Bearer Token',
                    )
                }
    )
),
}
