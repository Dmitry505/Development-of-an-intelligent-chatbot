class VectorStoreError(Exception):
    """Ошибка, связанная с векторным хранилищем."""
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

class LanguageModelError(Exception):
    """Ошибка, связанная с языковой моделью."""
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)
