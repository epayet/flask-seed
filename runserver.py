#!/usr/bin/env python3
from app import create_app

app = create_app(debug=True)

app.jinja_env.auto_reload = True

app.run(host="0.0.0.0")  #nosec
