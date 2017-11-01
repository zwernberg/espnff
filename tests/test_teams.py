import unittest
import json
from espnff.team import (Team)


class TeamTestCase(unittest.TestCase):

    def test_overall_standing(self):
        data = json.loads(open('tests/test_league.json').read())
        team = Team(data['leaguesettings']['teams']['1'])
        self.assertEquals(team.overall_standing, 3)

    def test_division_standing(self):
        data = json.loads(open('tests/test_league.json').read())
        team = Team(data['leaguesettings']['teams']['1'])
        self.assertEquals(team.division_standing, 1)

if __name__ == '__main__':
    unittest.main()
