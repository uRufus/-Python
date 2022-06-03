class Logger:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Logger, cls).__new__(cls)
        return cls.instance

    def _log_data(name, log):
        with open(f'framework/logs/{name}', mode='a', encoding='utf-8') as f:
            f.write(f'{log}\n')



