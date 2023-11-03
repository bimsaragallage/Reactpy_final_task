from fastapi import FastAPI
from reactpy.backend.fastapi import configure
from reactpy import component, event, html, use_state
import reactpy as rp
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient


@component
def register():
    ## Creating state
    alltodo = use_state([])
    first_name, set_first_name = use_state("")
    last_name, set_last_name = use_state("")
    gender, set_gender = use_state("")
    birthday, set_birthday = use_state(0)
    username, set_username = use_state("")
    password, set_password = use_state(0)

    def mysubmit2(event):
        newtodo1 = {"first_name": first_name,
                   "last_name": last_name,
                   "gender": gender,
                   "birthday": birthday,
                   "username": username,
                   "password": password}

        # push this to alltodo
        alltodo.set_value(alltodo.value + [newtodo1])
        login(newtodo1)  # function call to login function using the submitted data


    def handle_event(event):
        print(event)

    return html.div(
        {"style": {
            "padding": "50px",
            "text-align": "center",
            "background_image": "url(https://windows10spotlight.com/wp-content/uploads/2022/08/87c5ab7cdc5d302f5d630ed0d25f277c.jpg)",
            "background-size": "cover",
            "margin": "0px",
            "min-height": "500px",
            "min-width": "500px",
            "box-shadow": "5px 5px 5px rgba(0, 0, 0, 0.5)"
        }},
        ## creating form for submission
        html.form(
            {"on submit": mysubmit2},
            html.h1({"style": {
                "text-transform": "uppercase",
                "color": "#FFD700"
                }},
                "ReactPy & Mongodb"),
            html.h2({"style": {
                                "text-transform": "uppercase",
                                "color": "#FFD700"
                }},
                "Registration Form"),
            html.br(),
            html.p(),
            html.input(
                {
                    "type": "test",
                    "placeholder": "first name",
                    "on_change": lambda event: set_first_name(event["target"]["value"]),
                    "style":{
                            "width": "300px",
                            "height": "35px",
                            "font-size": "15px",
                            "margin-right": "30px"
                    }
                }
            ),
             html.input(
                {
                    "type": "test",
                    "placeholder": "last name",
                    "on_change": lambda event: set_last_name(event["target"]["value"]),
                    "style":{
                            "width": "300px",
                            "height": "35px",
                            "font-size": "15px"
                    }
                }
            ),
            html.br(),
            html.p(),
            html.br(),
            html.p(),
             html.select(
                {
                    "on_change": lambda event: set_gender(event["target"]["value"]),
                    "style":{
                            "width": "310px",
                            "height": "40px",
                            "font-size": "15px",
                            "margin-right": "30px"
                    }
                },
                [
                    html.option({"value": ""}, "Select Gender"),  # Optional placeholder
                    html.option({"value": "male"}, "Male"),
                    html.option({"value": "female"}, "Female"),
                ]
            ),
             html.input(
                {
                    "type": "date",
                    "placeholder": "birthday",
                    "on_change": lambda event: set_birthday(event["target"]["value"]),
                    "style":{
                            "width": "300px",
                            "height": "35px",
                            "font-size": "15px"
                    }
                }
            ),
            html.br(),
            html.p(),
            html.br(),
            html.p(),
            html.input(
                {
                    "type": "test",
                    "placeholder": "username",
                    "on_change": lambda event: set_username(event["target"]["value"]),
                    "style":{
                            "width": "300px",
                            "height": "35px",
                            "font-size": "15px",
                            "margin-right": "30px"
                    }
                }
            ),
            html.input(
                {
                    "type": "test",
                    "placeholder": "password",
                    "on_change": lambda event: set_password(event["target"]["value"]),
                    "style":{
                            "width": "300px",
                            "height": "35px",
                            "font-size": "15px"
                    }
                }
            ),
            html.br(),
            html.p(),
            html.br(),
            html.p(),
            # creating register button on form
            html.button(
                {
                    "type": "REGISTER NOW",
                    "on_click": event(
                        lambda event: mysubmit2(event), prevent_default=True),
                        "style":{
                            "width": "300px",
                            "height": "35px",
                            "font-size": "15px",
                            "background-color": "#FFDB58",
                            "border": "2px #FFDB58",
                            "border-radius": "10px"
                    }
                },
                "REGISTER NOW",
            ),
        )
    )


app = FastAPI()

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://admin:admin123@cluster0.vuldydd.mongodb.net/SignUp"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi("1"))
db = client["Reactpy_Task01"]
collection = db["Reactpy_collection"]
# Send a ping to confirm a successful connection
try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


def login(
    login_data: dict,
):  # removed async, since await makes code execution pause for the promise to resolve anyway. doesnt matter.
    first_name = login_data["first_name"]
    last_name = login_data["last_name"]
    gender = login_data["gender"]
    birthday = login_data["birthday"]
    username = login_data["username"]
    password = login_data["password"]

    # Create a document to insert into the collection
    document = {"first_name": first_name,
                   "last_name": last_name,
                   "gender": gender,
                   "birthday": birthday,
                   "username": username,
                   "password": password}

    # logger.info('sample log message')
    print(document)

    # Insert the document into the collection
    post_id = collection.insert_one(document).inserted_id  # insert document
    print(post_id)

    return {"message": "Login successful"}


configure(app, register)