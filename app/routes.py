from mvc_flask import Router

Router.get("/", "home#index")
Router.get("/hello", "home#hello")
Router.post("/messages", "messages#create")
Router.put("/users/<id>", "users#update")
Router.delete("/users/<id>", "users#delete")
