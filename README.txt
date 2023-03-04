# VSCode plugins
    - Python (IntelliSense)
    - Thunder client

# Install FastAPI and server
    $ pip install fastapi
    $ pip install "uvicorn[standard]"

# Server start: 
    $ uvicorn main:app --reload  
    (notice that "main" is the name of the file to run)

# Server stop: CTRL+C

# Documentation using Swagger http://127.0.0.1:8000/docs
# Documentation using Redocly http://127.0.0.1:8000/redoc