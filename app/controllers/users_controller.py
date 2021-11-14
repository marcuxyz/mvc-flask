class UsersController:
    def index(self):
        return "users"

    def show(self, id):
        return f"user {id}"

    def new(self):
        return "form"

    def create(self):
        return "user created", 201

    def edit(self, id):
        return f"form"

    def update(self, id):
        return f"updated user: {id}"

    def delete(self, id):
        return f"delete user: {id}"
