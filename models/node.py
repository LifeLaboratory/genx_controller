from models.base import BaseModel
import time


class Node(BaseModel):
    def __init__(self, id, ip, status):
        self.id = id
        self.ip = ip
        self.status = status
