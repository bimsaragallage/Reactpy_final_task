from fastapi import FastAPI
from reactpy.backend.fastapi import configure
from reactpy import component, event, html, use_state
import reactpy as rp
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient


@component
def MyCrud():
    ## Creating state
    username, set_username = use_state("")
    password, set_password = use_state(0)
    message, set_message = use_state("")

    def mysubmit(event):
        newtodo = {"username": username, "password": password}

        #introduce new variable to check availability of entered inputs on database
        result = collection.find_one(newtodo)
        if result:
            set_message("Login successful!")
            
        else:
            set_message("You haven't registered yet!")
        

    return html.div(
        {"style": {
            "padding": "50px",
            "text-align": "center",
            "background_image": "url(https://images.pexels.com/photos/1037992/pexels-photo-1037992.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2)",
            "background-size": "cover",
            "margin": "0px",
            "min-height": "500px",
            "min-width": "500px",
            "margin": "0 auto",
            "background-color": "lightgray",
            "border-radius": "10px",
            "box-shadow": "0px 0px 10px rgba(0, 0, 0, 0.5)"
        }},

        ## creating form for submission
        html.form(
            {"on submit": mysubmit},
                html.h1({"style": {
                        "text-transform": "uppercase",
                        "color": "#2E8B57"
                        }},
                        "ReactPy & Mongodb"),
                html.h2({"style": {
                        "text-transform": "uppercase",
                        "color": "#2E8B57"
                        }},
                        "login Form"),
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
                    }
                }
            ),
            html.br(),
            html.p(),
            html.br(),
            html.input(
                {
                    "type": "test",
                    "placeholder": "Password",
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
            # creating login button on form
            html.button(
                {
                    "type": "Login",
                    "on_click": event(lambda event: mysubmit(event), prevent_default=True),
                        "style":{
                            "width": "200px",
                            "height": "35px",
                            "font-size": "15px",
                            "border-radius": "20px",
                            "background-color": "#FFDB58",
                            "border": "2px #FFDB58"
                }},
                "Login",
            ),
            html.br(),
            html.p(),
            #print the availability of entered inputs or error message
            html.p(message),
            html.br(),
            html.p(),
            #create a link to register form
            html.div("not a member? Register Now"),
        ),
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





configure(app, MyCrud)