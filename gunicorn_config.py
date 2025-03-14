# Optimized for Render's free tier (512MB RAM)
timeout = 120
workers = 1
worker_class = "gthread"
threads = 2
bind = "0.0.0.0:$PORT"