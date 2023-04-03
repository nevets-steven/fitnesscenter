import datetime

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name

    def check_in(self, club):
        pass  # implemented in child classes

class SingleClubMember(Member):
    def __init__(self, member_id, name, club):
        super().__init__(member_id, name)
        self.club = club

    def check_in(self, club):
        if club.name != self.club.name:
            print(f"Error: You are a member of {self.club.name}. Please check in there instead.")
            return
        print(f"Welcome, {self.name}!")

class MultiClubMember(Member):
    def __init__(self, member_id, name, points=0):
        super().__init__(member_id, name)
        self.points = points

    def check_in(self, club):
        self.points += 1
        print(f"Welcome, {self.name}! You have earned 1 point.")

