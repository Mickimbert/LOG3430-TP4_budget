import os

bad_hash = "e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c"
good_hash = "c1a4be04b972b6c17db242fc37752ad517c29402"

os.system(f"git bisect start {bad_hash} {good_hash}")
os.system("git bisect run python manage.py test")
os.system("git bisect reset")