class UsersController:
    def index(self, view, request):
        return "users"

    def show(self, view, request, id):
        return f"user {id}"

    def new(self, view, request):
        return "form"

    def create(self, view, request):
        return "user created", 201

    def edit(self, view, request, id):
        return f"form"

    def update(self, view, request, id):
        return f"updated user: {id}"

    def delete(self, view, request, id):
        return f"delete user: {id}"
