from fifa_py import _api_scrape, _get_json, _form_endpoint
from fifa_py.constants import CURRENT_SEASON

class Match:
    '''
    Returns data related to a single match
    How is this different from MatchSummary?
    Args:
    Returns:
    Raises:
    '''
    _endpoint = 'matches'
    
    def __init__(self, match_id, **kwargs):
        endpoint = _form_endpoint([self._endpoint, match_id])
        self.json = _get_json(endpoint=endpoint)
    
    def info(self):
        return _api_scrape(json=self.json, key='match')


class MatchList:
    '''
    Returns a list of matches, can be more specific given a league or time frame
    
    Args:
    Returns:
    Raises:
    '''

    _endpoint = 'matches'

    def __init__(self, 
                matchday=None,
                status=None,
                league_id=None,
                dateTo=None,
                dateFrom=None,
                **kwargs):
        endpoint = _form_endpoint([self._endpoint])
        self.json = _get_json(endpoint=endpoint, 
                                filters={
                                    'matchday': matchday,
                                    'status': status,
                                    'competitions': league_id,
                                    'dateTo': dateTo,
                                    'dateFrom': dateFrom
                                })
        

    def info(self):
        return _api_scrape(json=self.json, key='matches')


class MatchSummary:
    '''
    Returns a detailed summary of the match

    Args:
    Returns:
    Raises:
    '''

    _endpoint = 'matches'

    def __init__(self, match_id, **kwargs):
        pass

    def info(self):
        pass


class MatchLineup:
    '''
    Returns the lineup for a specific match

    Args:
    Returns:
    Raises:
    '''

    def __init__(self, match_id, **kwargs):
        pass