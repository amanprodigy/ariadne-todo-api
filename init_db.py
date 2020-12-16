from api import db
from datetime import datetime
from api.models import Todo


def populate():
    today = datetime.today().date()
    todo = Todo(description="Run a marathon", due_date=today, completed=False)
    print(todo.to_dict())
    db.session.add(todo)
    db.session.commit()
