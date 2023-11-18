from mvc_flask import Router

Router.all("messages")
Router.all("callbacks", only=["index"])

api = Router.namespace("/api/v1")

api.get("/health", "health#index")

posts = api.namespace("/posts")
posts.all("posts", only="index")
# posts.get("", "posts#index")
# posts.post("", "posts#create")
# posts.get("/<id>", "posts#show")
# posts.put("/<id>", "posts#update")
# posts.get("/<id>", "posts#delete")
