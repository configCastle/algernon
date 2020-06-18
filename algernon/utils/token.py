"""Token operation for algernon."""
import jwt
from aiohttp import web

from algernon.constants import JWT_ALGORITHM, JWT_SECRET


async def check_token(access_token):
    """
    Check token for request.

    Args:
        access_token: token for access API.

    Raises:
        HTTPUnauthorized: token doesn't exist or invalid
    """
    if access_token is None:
        raise web.HTTPUnauthorized(
            reason='You bad person. Why are you did it?',
        )

    try:
        jwt.decode(
            access_token, JWT_SECRET, algorithms=[JWT_ALGORITHM],
        )
    except jwt.DecodeError:
        raise web.HTTPUnauthorized(
            reason='You give me bad token. Bakka',
        )
    except jwt.ExpiredSignatureError:
        raise web.HTTPUnauthorized(
            reason='You give me this token too late. Bakka',
        )
