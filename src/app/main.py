from fastapi import FastAPI, HTTPException
from mangum import Mangum

from .environments import Environments

from .errors.entity_errors import ParamNotValidated

from .enums.item_type_enum import ItemTypeEnum

from .entities.item import Item


app = FastAPI()

repo = Environments.get_item_repo()()
member_repo = Environments.get_member_repo()()


@app.get("/")
def execute_get_pra_barra():
    return member_repo.get_first_member()


handler = Mangum(app, lifespan="off")
