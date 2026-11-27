from fastapi import FastAPI,Depends,Header,HTTPException,Request
import time

app = FastAPI()

# Logger middleware
@app.middleware("http")
async def logger_middleware(request:Request,call_next):
    start = time.time()

    response = await call_next(request)

    end = time.time()
    print("path :",request.url.path ,end - start , "Time takend to execute")
    return response


# Middleware that run before req go to server function
# @app.middleware("http")
# async def middleware(request:Request,call_next):
#     print("Request Recived")

#     response = await call_next(request)

#     print("Response Sent")
#     return response

def verify_token(token:str = Header(None)):
    if token != "mysecrettoken":
        raise HTTPException(status_code=401,detail="UnAuthorize")
    return {
        "user":"Authorized User"
    }

# dependancy injection use to tun same logic code for selected routes
def current_user():
    return {"User":"DC"}

@app.get("/secure-route")
def secure_route(user = Depends(verify_token)):
    return {
        "message":"Secure Data Access",
        "user":user
    }


@app.get("/profile")
def get_profile(user = Depends(current_user)):    
    return user

@app.get("/dashboard")    
def get_dashboard(user = Depends(current_user)):
    return user