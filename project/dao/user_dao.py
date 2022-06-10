from project.dao.models.user import User


class UserDAO:

    def __init__(self, session):
        self.session = session

    def get_user_profile(self, email):
        user = self.session.query(User).filter(User.email == email).one()
        return user

    def update_user_profile(self, user):
        self.session.add(user)
        self.session.commit()

    def update_user_password(self, user):
        self.session.add(user)
        self.session.commit()
