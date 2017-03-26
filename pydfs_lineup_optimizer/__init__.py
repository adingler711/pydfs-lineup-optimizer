__version__ = "1.0"

from .player import Player
from .exceptions import LineupOptimizerException, LineupOptimizerIncorrectTeamName, \
    LineupOptimizerIncorrectPositionName
from .lineup_optimizer import LineupOptimizer
from .lineup import Lineup
from .settings import YahooBasketballSettings, YahooFootballSettings, YahooHockeySettings, \
    FanDuelBasketballSettings, FanDuelFootballSettings, FanDuelHockeySettings, FanDuelBaseballSettings, \
    DraftKingsBasketballSettings, DraftKingsFootballSettings, DraftKingsHockeySettings, DraftKingBaseballSettings, \
    FantasyDraftBasketballSettings, FantasyDraftFootballSettings, FantasyDraftHockeySettings
from .constants import Site, Sport


settings_mapping = {
    Site.DRAFTKINGS: {
        Sport.BASKETBALL: DraftKingsBasketballSettings,
        Sport.FOOTBALL: DraftKingsFootballSettings,
        Sport.HOCKEY: DraftKingsHockeySettings,
        Sport.BASEBALL: DraftKingBaseballSettings,
    },
    Site.FANDUEL: {
        Sport.BASKETBALL: FanDuelBasketballSettings,
        Sport.FOOTBALL: FanDuelFootballSettings,
        Sport.HOCKEY: FanDuelHockeySettings,
        Sport.BASEBALL: FanDuelBasketballSettings,
    },
    Site.YAHOO: {
        Sport.BASKETBALL: YahooBasketballSettings,
        Sport.FOOTBALL: YahooFootballSettings,
        Sport.HOCKEY: YahooHockeySettings,
    },
    Site.FANTASY_DRAFT: {
        Sport.BASKETBALL: FantasyDraftBasketballSettings,
        Sport.FOOTBALL: FantasyDraftFootballSettings,
        Sport.HOCKEY: FantasyDraftHockeySettings,
    },
}


def get_optimizer(site, sport):
    try:
        return LineupOptimizer(settings_mapping[site][sport])
    except KeyError:
        raise NotImplementedError

