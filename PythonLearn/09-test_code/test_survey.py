"""test survey AnonymousSurvey"""
import pytest

from survey import AnonymousSurvey


@pytest.fixture
def general_sur():
    question = 'What is your favorite language?'
    ano_sur = AnonymousSurvey(question)
    return ano_sur

def test_single_language_survey(general_sur):
    """test single language"""
    language = 'english'
    general_sur.store_responce(language)
    assert language in general_sur.response

def test_tree_language_survey(general_sur):
    """test three language"""
    language = ['english','french','madarin','spanish']
    for lan in language:
        general_sur.store_responce(lan)

    for lan in language:
        assert lan in general_sur.response
    
        
