import unittest
import fitnesscenter

class TestMember(unittest.TestCase):

    def test_check_in(self):
        # create a Club instance
        club = fitnesscenter.Club('Nir','b')
        # create a Member instance
        member = fitnesscenter.Member(1, "John")
        # call the check_in method
        result = member.check_in(club)
        self.assertEqual(fitnesscenter.Member.check_in(self,club), 0)

if __name__ == '__main__':
    unittest.main()