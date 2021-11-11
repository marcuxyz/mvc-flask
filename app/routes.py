from mvc_flask import Router


Router.get("/", "home#index")
Router.get("/hello", "home#hello")

Router.all("users")
Router.all("messages", only="index show new create")
