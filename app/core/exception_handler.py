from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException


def register_exception_handlers(app: FastAPI):

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(
        request: Request,
        exc: RequestValidationError
    ):
        first_error = exc.errors()[0]

        field_name = first_error["loc"][-1]

        return JSONResponse(
            status_code=422,
            content={
                "status": False,
                "message": f"{field_name}: {first_error['msg']}"
            }
        )


    @app.exception_handler(StarletteHTTPException)
    async def http_exception_handler(
        request: Request,
        exc: StarletteHTTPException
    ):
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "status": False,
                "message": exc.detail
            }
        )