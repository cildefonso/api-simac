from fastapi import APIRouter

from api.imac.endpoints import artigo
from api.imac.endpoints import usuario


api_router = APIRouter()

api_router.include_router(artigo.router, prefix='/artigos', tags=['artigos'])
api_router.include_router(
    usuario.router, prefix='/usuarios', tags=['usuarios'])
