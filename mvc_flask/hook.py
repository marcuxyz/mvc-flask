class Hook:
    def register(self, hooks, **kwargs):
        if hooks:
            for hook in hooks.items():
                if hook[0] == "before_request":
                    kwargs["blueprint"].before_request(
                        getattr(kwargs["controller"](), hook[1])
                    )
