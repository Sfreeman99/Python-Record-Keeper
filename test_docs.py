from core import *
from record_disk import *
#core test
def test_names():
    assert names({'Shedlia':{'Wins': 0, 'Losses': 0 }, 'Jo': {'Wins': 0, 'Losses': 0 }, 'Penny': {'Wins': 0, 'Losses': 0 }}, 'Shedlia', 'Jo') == {'Shedlia':{'Wins': 0, 'Losses': 0 }, 'Jo': {'Wins': 0, 'Losses': 0 }, 'Penny': {'Wins': 0, 'Losses': 0 }}



def test_names_does_something_else():
    assert (names({'Shedlia':{'Wins': 0, 'Losses': 0 }, 'Jo': {'Wins': 0, 'Losses': 0 }, 'Penny': {'Wins': 0, 'Losses': 0 }}, 'Shedlia', 'Billy') == 
            {'Shedlia':{'Wins': 0, 'Losses': 0 }, 'Jo':{'Wins': 0, 'Losses': 0 }, 'Billy':{'Wins': 0, 'Losses': 0 }, 'Penny':{'Wins': 0, 'Losses': 0 }})

def test_both_names_not_in():
    assert (names({'Shedlia':{'Wins': 0, 'Losses': 0 }, 'Jo': {'Wins': 0, 'Losses': 0 }, 'Penny': {'Wins': 0, 'Losses': 0 }}, 'Duke', 'Dil') ==
            {'Shedlia':{'Wins': 0, 'Losses': 0 }, 'Jo':{'Wins': 0, 'Losses': 0 }, 'Dil':{'Wins': 0, 'Losses': 0}, 'Penny':{'Wins': 0, 'Losses': 0 }, 'Duke': {'Wins': 0, 'Losses': 0}})

def test_record_maker1():
    assert (record_game('Shedlia', 5, 'Jo', 3, {'Shedlia':{'Wins': 0, 'Losses': 0}, 'Jo':{'Wins':0, 'Losses': 0}}) == 
            {'Shedlia': {'Wins': 1, 'Losses': 0}, 'Jo': {'Wins':0, 'Losses': 1}})

def test_record_game():
    assert record_game('Shedlia', 25, 'Jo', 23, {'Jo': {'Wins': 0, 'Losses': 0}, 'Shedlia':{'Wins': 0, 'Losses': 0}}) == {'Jo': {'Wins': 0, 'Losses': 1}, 'Shedlia':{'Wins': 1, 'Losses': 0}}
