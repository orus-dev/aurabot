from json import dumps, loads
import redis
from config import REDIS_URL, REDIS_USER, REDIS_PSW

class User:
    user_id: str
    last_earned: float = 0.0
    def __init__(self, user_id: str, balance: int, last_earned: float = 0.0) -> None:
        self.balance = balance
        self.user_id = str(user_id)
        self.last_earned = float(last_earned)

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
    last_earns: dict[str, float]
    def __init__(self) -> None:
        redis_host = REDIS_URL.split(':')
        self.r = redis.Redis(host=redis_host[0], port=int(redis_host[1]), username=REDIS_USER, password=REDIS_PSW, decode_responses=True)
    
    def get(self, user_id) -> User | None:
        try:
            return User(user_id, int(self.r.get(str(user_id))), self.last_earns[user_id] if user_id in self.last_earns else 0.0)
        except:
            return None
    
    def add(self, user_id) -> User:
        u = User(user_id, 100)
        self.r.set(user_id, u.balance)
        return u

    def update(self, u: User):
        self.r.set(u.user_id, u.balance)
        self.last_earns[str(u.user_id)] = u.last_earned