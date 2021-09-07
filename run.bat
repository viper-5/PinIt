@echo off
@REM For development and not deployment
SET FLASK_APP=app.py
SET FLASK_DEBUG=true
SET FLASK_ENV=development
SET FLASK_DEBUG=1
flask run