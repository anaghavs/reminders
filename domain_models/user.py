from dataclasses import dataclass

@dataclass
class User:
    name: str
    email: str
    password_hash: str
