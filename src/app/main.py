from fastapi import FastAPI, HTTPException
from mangum import Mangum

from .environments import Environments

from .errors.entity_errors import ParamNotValidated

app = FastAPI()

member_repo = Environments.get_member_repo()()


@app.get("/")
def execute_get_pra_barra():
    member = member_repo.get_first_member()
    return {
        "member_id": member.member_id,
        "member": member.to_dict(),
    }


handler = Mangum(app, lifespan="off")
