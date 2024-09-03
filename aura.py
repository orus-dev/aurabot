from json import dumps, loads
import redis
from config import REDIS_URL, REDIS_USER, REDIS_PSW

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
    def __init__(self) -> None:
        redis_host = REDIS_URL.split(':')
        self.r = redis.Redis(host=redis_host[0], port=int(redis_host[1]), username=REDIS_USER, password=REDIS_PSW, decode_responses=True)
        self.load()
    
    def load(self) -> None:
        data = loads(self.r.get('data'))
        for k in data:
            self.data[k] = User(data[k]['balance'])

    def get(self, user_id) -> User | None:
        if user_id in self.data:
            return self.r.get(str(user_id))
    
    def add(self, user_id) -> User:
        self.data[user_id] = User(100)
        self.r.set
        return self.data[user_id]
            
    def save(self):
        data = {}
        for k in self.data:
            data[k] = self.data[k].to_dict()
        self.r.set('data', dumps(data, indent=2))