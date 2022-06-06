from project.dao.models.user import User


class UserDAO:

    def __init__(self, session):
        self.session = session

    def create(self, login_data):
        new_user = User(**login_data)
        self.session.add(new_user)
        self.session.commit()

    def get_one(self, email):
        user = self.session.query(User).filter(User.email == email).first()
        return user

