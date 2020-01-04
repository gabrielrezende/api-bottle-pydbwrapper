from utils.formatter import Formatter


class ProcessesModel:

    def __init__(self, process):
        """
        Deal Model
        """
        self.id = process.id
        self.code = process.code
        self.name = process.name
        self.color = process.color
        self.additionalInformation = process.additionalInformation
        self.created_at = process.created_at
        self.updated_at = process.updated_at
