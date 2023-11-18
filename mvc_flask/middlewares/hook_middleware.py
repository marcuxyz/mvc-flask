class HookMiddleware:
    def register(self, controller_instance, blueprint_instance):
        attrs = [
            attr for attr in dir(controller_instance) if attr in self.accept_attributes
        ]

        if attrs:
            for attr in attrs:
                values = getattr(controller_instance, attr)
                for value in values:
                    hook_method = getattr(controller_instance, value)
                    getattr(blueprint_instance, attr)(hook_method)

    @property
    def accept_attributes(self):
        return [
            "before_request",
            "after_request",
            "teardown_request",
            "after_app_request",
            "before_app_request",
            "teardown_app_request",
            "before_app_first_request",
        ]
