class GameStats:
  """Keep track of game's stats"""

  def __init__(self, ai_game):
    """Initialize game's stats"""
    self.settings = ai_game.settings
    self.reset_stats()
    self.game_active = False

  def reset_stats(self):
    self.ships_left = self.settings.ship_limit
    self.score = 0