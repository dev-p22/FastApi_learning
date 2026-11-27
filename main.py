from fastapi import FastAPI
from pydantic import BaseModel
from routes import todos

app = FastAPI()



class Address(BaseModel):
    city:str
    pincode:int

    
class User(BaseModel):
    name:str
    age : int
    password : str
    address : Address # Link to Address Schema Nested JSON

class UserResponse(BaseModel):
    name:str
    age : int
    address : Address

class Product(BaseModel):
    name : str
    type : str
    price : int


app.include_router(todos.router)



@app.get("/")
def home():
    return {"message":"Hello There"}

@app.get("/about")
def about():
    return {"message" : "about page"}

@app.get("/users", response_model=UserResponse) # it should return user response stricly how we define shcema for return
def users():
    return{"name" : "xzy" , "age":32 ,"address": { "pincode" : 23 , "city": "visnagar"} }

# dynamic path
@app.get("/users/{user_id}")
def get_user(user_id : int):
    return {"User_id":user_id}

# Query Params /users?name=mohi&sort=asc
#Always give optional params and also default value can be avilable as well
@app.get("/products")
def get_products(product : str = None, sort : str = None , limit : int = 10):
    return {"Name":product , "sort" : sort , "limit" : limit}


#post request
@app.post("/create-user", status_code= 201)
def create_user(user:User):
    return {
        "message" : "User Created",
        "success" : True,
        "data" : user
    }


@app.post("/create-product")
def create_product(product:Product):
    return {
        "message" : "Product Created",
        "Success" : True,
        "data" : product
    }
