import unittest
import datetime
from fitnesscenter import FitnessCenter, Club, SingleClubMember, MultiClubMember,Member


class TestMember_Finteness(unittest.TestCase):

    def setUp(self):
        # create a Club instance
        # create a Member instance
        self.club = Club("Test Club",'ClubA')
        self.member = SingleClubMember(1, "John Smith", self.club)
        self.club1 = Club(1, "Club 1")
        self.club2 = Club(2, "Club 2")
        self.member1 = MultiClubMember(1, "Anaye")
        self.fc = FitnessCenter()
    def test_check_in_Memeber(self):
        #Check in Memeber class check in method returns void/None
        self.assertEqual(Member.check_in(self,self.club), None)

    def test_check_in_correct_Single_club(self):
        # Test that member can check in to their own club
        self.assertTrue(self.member.check_in(self.club))

    def test_check_in_Single_wrong_club(self):
        # Test that member cannot check in to another club
        other_club = Club("Other Club",'Club B')
        expected_output = f"Alert! {self.member.name} is not a member of {other_club.name}.Please check in at your club{self.club.name}."
        with self.assertRaisesRegex(SystemExit, expected_output):
            self.member.check_in(other_club)

    def test_check_in_Multi_club(self):
        # Test initial membership points
        self.assertEqual(self.member1.membership_points, 0)
        # Test check-in at club 1
        self.assertTrue(self.member1.check_in(self.club1))
        self.assertEqual(self.member1.membership_points, 1)
        # Test check-in at club 1
        self.assertTrue(self.member1.check_in(self.club2))
        self.assertEqual(self.member1.membership_points, 2)
        # Test check-in at club 1 again
        self.assertTrue(self.member1.check_in(self.club1))
        self.assertEqual(self.member1.membership_points, 3)

    def test_club(self):
        # Test initialization of Club class
        club = Club("Chess Club", "123 Main St.")
        self.assertEqual(club.name, "Chess Club")
        self.assertEqual(club.address, "123 Main St.")



    if __name__ == '__main__':
     unittest.main()