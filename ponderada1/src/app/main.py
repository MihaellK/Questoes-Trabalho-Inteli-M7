from typing import Union

from fastapi import FastAPI


from fastapi.responses import FileResponse 
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Também é possivel servir html com o codigo abaixo

# app.mount("/", StaticFiles(directory="src/app/templates",html = True), name="static")


# templates = Jinja2Templates(directory="templates")

@app.get("/")
def read_root():
    return FileResponse('app/templates/index.html')



