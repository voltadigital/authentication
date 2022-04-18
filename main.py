from fastapi import FastAPI, staticfiles
from fastapi.responses import FileResponse, RedirectResponse
from fastapi.middleware.wsgi import WSGIMiddleware
from flask import Flask, escape, request,render_template

web = Flask('vdauth')
api = FastAPI()

@web.route('/login')
def loginscreen():
    return render_template('login.html')

@api.get("/")
def indexredir():
    return RedirectResponse('/web/login', 302)

api.mount("/web", WSGIMiddleware(web))