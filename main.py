import uvicorn

from AHDjango.asgi import application

if __name__ == '__main__':
    uvicorn.run(app='AHDjango.asgi:application', host='localhost', port=8000, reload=True)
