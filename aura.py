from json import dump, load

class User:
    def __init__(self, balance: int) -> None:
        self.balance = balance

    def set_balance(self, balance) -> int:
        self.balance = balance
        return self.balance
        
    def add_balance(self, balance) -> int:
        self.balance += balance
        return self.balance

    def to_dict(self) -> dict:
        return {'balance': self.balance}
    
    def to_md(self) -> str:
        return f"**- balance: {self.balance}**"

class Aura:
    data: dict[str, User] = {}
    file = ''
    def __init__(self, file: str) -> None:
        with open(file, 'r')as f:
            self.file = file
            data = load(f)
            for k in data:
                self.data[k] = User(data[k]['balance'])
    
    def load(self) -> None:
        with open(self.file, 'r')as f:
            data = load(f)
            for k in data:
                self.data[k] = User(data[k]['balance'])

    def get(self, user_id) -> User | None:
        if user_id in self.data:
            return self.data[user_id]
    
    def add(self, user_id) -> User:
        self.data[user_id] = User(10)
        return self.data[user_id]
            
    def save(self):
        data = {}
        for k in self.data:
            data[k] = self.data[k].to_dict()
        with open(self.file, 'w')as f:
            dump(data, f, indent=2)