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

class Club:
    def __init__(self, name, address):
        self.name = name
        self.address = address

class FitnessCenter:
    def __init__(self):
        self.members = []

    def add_member(self):
        member_id = input("Enter member ID: ")
        name = input("Enter name: ")
        membership_type = input("Enter membership type (s for Single Club, m for Multi-Club): ")
        if membership_type == "s":
            club_name = input("Enter club name: ")
            club_address = input("Enter club address: ")
            club = Club(club_name, club_address)
            member = SingleClubMember(member_id, name, club)
        elif membership_type == "m":
            member = MultiClubMember(member_id, name)
        else:
            print("Error: Invalid membership type.")
            return
        self.members.append(member)
        print(f"Member {member.name} ({member.member_id}) has been added.")

    def remove_member(self):
        member_id = input("Enter member ID: ")
        for member in self.members:
            if member.member_id == member_id:
                self.members.remove(member)
                print(f"Member {member.name} ({member.member_id}) has been removed.")
                return
        print(f"Error: Member {member_id} not found.")

    def display_member_info(self):
        member_id = input("Enter member ID: ")
        for member in self.members:
            if member.member_id == member_id:
                print(f"Member ID: {member.member_id}")
                print(f"Name: {member.name}")
                if isinstance(member, SingleClubMember):
                    print(f"Club: {member.club.name}")
                elif isinstance(member, MultiClubMember):
                    print(f"Points: {member.points}")
                return
        print(f"Error: Member {member_id} not found.")

    def check_in_member(self):
        member_id = input("Enter member ID: ")
        club_name = input("Enter club name: ")
        club_address = input("Enter club address: ")
        club = Club(club_name, club_address)
        for member in self.members:
            if member.member_id == member_id:
                member.check_in(club)
                return
        print(f"Error: Member {member_id} not found.")
