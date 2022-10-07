from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse

from api_router import router as api_router
from core.events import create_start_app_handler, create_stop_app_handler
from core.settings import PROJECT_NAME, DEBUG, API_PREFIX


def get_application() -> FastAPI:
    application = FastAPI(
        title=PROJECT_NAME,
        debug=DEBUG,
        docs_url=None,
        redoc_url=None,
        openapi_url=None,
        default_response_class=ORJSONResponse,
    )
    application.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_methods=['*'],
        allow_headers=['*'],
        allow_credentials=True,
    )  # TODO

    application.add_event_handler('startup', create_start_app_handler(application))
    application.add_event_handler('shutdown', create_stop_app_handler(application))

    application.include_router(api_router, prefix=API_PREFIX)
    return application


app = get_application()
