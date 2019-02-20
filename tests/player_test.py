import unittest
from time import sleep
from fifa_py.player import get_player, Player, PlayerList, PlayerSummary, PlayerCareer, PlayerProfile, PlayerGameLogs, PlayerVsPlayer, TopPlayers


class GetPlayerTest(unittest.TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def testA(self):
        assert get_player('Lionel', 'Messi')
        assert get_player('Cristiano', 'Ronaldo')


class PlayerTest(unittest.TestCase):
    def setUp(self):
        self.pid = get_player(first_name='Lionel', last_name='Messi')
        self.vs_pid = get_player(first_name='Cristiano', last_name='Ronaldo')

    def tearDown(self):
        pass

    def testA(self):
        assert Player()
        assert PlayerList()
        assert PlayerSummary(pid=self.pid)
        assert PlayerCareer(pid=self.pid)
        assert PlayerProfile(pid=self.pid)
        assert PlayerGameLogs(pid=self.pid)
        assert PlayerVsPlayer(pid=self.pid, vs_pid=self.vs_pid)
        assert TopPlayers(country='esp')


class PlayerListTest(unittest.TestCase):
    def setUp(self):
        self.list = PlayerList()

    def tearDown(self):
        pass

    def testA(self):
        pass


class PlayerSummaryTest(unittest.TestCase):
    def setUp(self):
        pid = get_player(first_name='Lionel', last_name='Messi')
        self.player = PlayerSummary(player_id=pid, season=2016)

    def tearDown(self):
        pass
    
    def testA(self):
        assert self.player['appearances'] == 34
        assert self.player['starts'] == 32
        assert self.player['subs'] == 2
        assert self.player['minutes'] == 2828
        assert self.player['goals'] == 37
        assert self.player['assists'] == 9
        assert self.player['pk'] == 6
        assert self.player['fouls'] == 15


class PlayerCareerTest(unittest.TestCase):
    def setUp(self):
        pid = get_player('Lionel', 'Messi')
        self.player = PlayerCareer(pid)

    def tearDown(self):
        pass

    def testA(self):
        pass


class PlayerProfileTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testA(self):
        pass


class PlayerGameLogsTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testA(self):
        pass


class PlayerVsPlayerTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testA(self):
        pass


class TopPlayersTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testA(self):
        pass


if __name__ == '__main__':
    unittest.main()
