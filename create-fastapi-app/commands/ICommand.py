class ICommand:
    def execute(self, *args, **kwargs):
        raise NotImplementedError
