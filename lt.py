import tinkter as tk
import datetime
def get_prediction():
    current_minute=datetime.datetime.now().minute
    coin_outcomes={
        0:"Half red,Half Violet(Small)",
        1:"Green(Small)",
        2:"Red(Small)",
        3:"Green(Small)",
        4:"Red(Small)",
        5:"Half Green,Half Violet(Big)",
        6:"Red(Big)",
        7:"Green(Big)",
        8:"Red(Big)",
        9:"Green(Big)",
    }
    return coin_outcomes[current_minute%10]
def update_prediction():
    prediction =get_prediction()