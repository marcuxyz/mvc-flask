class MessagesController:
    def index(self, view, request):
        return view("messages/index.html")

    def show(self, view, request, id):
        return f"message {id}"

    def new(self, view, request):
        return "form"

    def create(self, view, request):
        return "message created", 201

    def edit(self, view, request, id):
        return f"form"

    def update(self, view, request, id):
        return f"updated messages: {id}"

    def delete(self, view, request, id):
        return f"delete message: {id}"
