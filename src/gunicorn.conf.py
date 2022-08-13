# https://docs.gunicorn.org/en/stable/settings.html
bind = "0.0.0.0:8000"
worker_class = "uvicorn.workers.UvicornWorker"
loglevel = "info"
accesslog = "-"
