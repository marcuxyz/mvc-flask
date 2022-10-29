from mvc_flask import Router

Router.all("messages", only="index show new create edit update delete")

api = Router.namespace("/api/v1")

api.get("/health", "health#index")

api.all("user")

posts = api.namespace("/posts")
posts.get("", "posts#index")
posts.post("", "posts#create")
posts.get("/<id>", "posts#show")
posts.put("/<id>", "posts#update")
posts.get("/<id>", "posts#delete")
