class MessagesController:
    def index(self):
        return "messages"

    def show(self, id):
        return f"message {id}"

    def new(self):
        return "form"

    def create(self):
        return "message created", 201

    def edit(self, id):
        return f"form"

    def update(self, id):
        return f"updated messages: {id}"

    def delete(self, id):
        return f"delete message: {id}"
