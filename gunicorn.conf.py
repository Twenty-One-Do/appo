from multiprocessing import cpu_count

from appo_api.config import settings


def max_workers() -> int:
    if cpu_count() <= 2:
        return cpu_count()
    else:
        return cpu_count() + 1


bind = '0.0.0.0:8000' if settings.ENVIRONMENT == 'PROD' else '0.0.0.0:8001'
workers = 1
worker_class = 'uvicorn.workers.UvicornWorker'
