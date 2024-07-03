class Game:
    def __init__(self, title):
        self.title = title
        self.game_results = []

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if hasattr(self, 'title'):
            raise Exception('Title cannot be changed after the game is instantiated')
        if isinstance(title, str) and len(title) > 0:
            self._title = title
        else:
            raise Exception('Title must be a string more than 0 characters')

    def results(self):
        return self.game_results

    def players(self):
        return list(set([result.player for result in self.game_results]))
        # players = []
        # for result in self.game_results:
        #     if result.player not in players:
        #         players.append(result.player)
        # return players

    def average_score(self, player):
        scores = [result.score for result in self.game_results if result.player == player]
        return sum(scores) / len(scores)

class Player:
    all_players = []

    def __init__(self, username):
        self.username = username
        self.player_results = []
        self.all_players.append(self)

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if isinstance(username, str) and 2 <= len(username) <= 16:
            self._username = username
        else:
            raise Exception('Username must be a string between 2 & 16 characters')
        
    @classmethod
    def highest_scored(cls, game):
        players_played = [player for player in cls.all_players if player.played_game(game)]
        if players_played:
            return max(players_played, key=lambda player: game.average_score(player))
        else:
            return None

    def results(self):
        return self.player_results

    def games_played(self):
        return list(set([result.game for result in self.player_results]))

    def played_game(self, game):
        return game in self.games_played()

    def num_times_played(self, game):
        count = 0
        for result in self.player_results:
            if result.game == game:
                count += 1
        return count


class Result:
    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score

        game.game_results.append(self)
        player.player_results.append(self)
        self.all.append(self)

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        if hasattr(self, 'score'):
            raise Exception('Score cannot be changed after result is instantiated')
        if isinstance(score, int) and 1<= score <= 5000:
            self._score = score
        else:
            raise Exception('Score must be an integer between 1 & 5000')
        
    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, player):
        if isinstance(player, Player):
            self._player = player
        else:
            raise Exception('Player must be an instance of the player class')
        
    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, game):
        if isinstance(game, Game):
            self._game = game
        else:
            raise Exception('Game must be an instance of the game class')
        
    