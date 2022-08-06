from mvc_flask import Router

Router.all("messages", only="index show new create edit update delete")
