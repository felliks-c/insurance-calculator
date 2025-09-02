from fastapi.responses import JSONResponse

def success_response(data, message="Success"):
    return JSONResponse(
        status_code=200,
        content={
            "status": "ok",
            "message": message,
            "data": data
        }
    )

def error_response(detail, status_code=400):
    return JSONResponse(
        status_code=status_code,
        content={
            "status": "error",
            "message": detail
        }
    )
