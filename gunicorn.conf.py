from multiprocessing import cpu_count


def max_workers() -> int:
    if cpu_count() <= 2:
        return cpu_count()
    else:
        return cpu_count() + 1


bind = "0.0.0.0:8000"
workers = 1
worker_class = "uvicorn.workers.UvicornWorker"
