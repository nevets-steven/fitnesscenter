"""Member class is for storing member information, has two child class
  SingleClubMember and MultiClubMember"""


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name

    def check_in(self, club):
        pass  # implemented in child classes


class SingleClubMember(Member):
    def __init__(self, member_id, name, club):
        self.member_id = member_id
        self.name = name
        self.club = club

    def check_in(self, club):
        if club.name != self.name:
            print(f"Alert! {self.name} is a member of {self.club.name}.Please check in at your club{self.club.name}.")
            return False
        else:
            print(f"Welcome {self.name} to {club.name}!")
            return True


class MultiClubMember(Member):
    def __init__(self, member_id, name, membership_points=0):
        self.member_id = member_id
        self.name = name
        self.membership_points = membership_points

    def check_in(self, club):
        self.membership_points += 1
        print(f"Welcome {self.name} to {club.name}! Membership points: {self.membership_points}")
        return True

