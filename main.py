import fastapi
import uvicorn
from prometheus_fastapi_instrumentator import Instrumentator

from api import motd
from views import home, custom_metrics, sleep_demo, jokes, logger
from starlette.staticfiles import StaticFiles

main_app = fastapi.FastAPI()

# Include Prometheus metrics
Instrumentator().instrument(main_app).expose(main_app)


def configure():
    configure_routing()


def configure_routing():
    main_app.mount('/static', StaticFiles(directory='static'), name='static')
    main_app.include_router(motd.router)
    main_app.include_router(home.router)
    main_app.include_router(custom_metrics.router)
    main_app.include_router(sleep_demo.router)
    main_app.include_router(jokes.router)
    main_app.include_router(logger.router)


if __name__ == '__main__':
    configure()
    uvicorn.run(main_app, host='0.0.0.0', port=8000)
else:
    configure()
