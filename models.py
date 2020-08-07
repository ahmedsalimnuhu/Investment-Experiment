from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Salim Nuhu'

doc = """
This is the CoP Experiment
"""

import random
class Constants(BaseConstants):

    name_in_url = 'COP_1'
    players_per_group = 2
    num_rounds = 8
    endowment = c(10)
    multiplication_factor = 3
    shocks = [0, 3]
    fine = c(7)
    other_fine = c(4)
    #random_return = random.choice(shocks)


    #instructions_template = 'COP_Experiment/instructions.html'

class Subsession(BaseSubsession):
    def creating_session(self):
        # self.group_randomly(fixed_id_in_group=True)
        if self.round_number == 3 or self.round_number == 7:
            random_return = random.choice(Constants.shocks)
            self.session.vars['random_return'] = random_return
        if self.round_number >= 5:
            # reverse the roles
            for group in self.get_groups():
                players = group.get_players()
                players.reverse()
                group.set_players(players)


class Group(BaseGroup):
    sent_amount = models.CurrencyField(
        min=0, max=Constants.endowment,
        label='''
     YOUR DECISION: I would like to send P2
        ''',
    )

    #tripled = models.CurrencyField(c(3) * c(sent_amount)
    #)

    sent_back_amount = models.CurrencyField(
       min=c(0), max= Constants.endowment*Constants.multiplication_factor,
        label='''
       YOUR DECISION: I would like to send back to P1
        ''',
    )


    amount_demanded = models.CurrencyField(
        min=0, max=30,
        label='''
                And I would like to request back from P2
                ''',
    )




class Player(BasePlayer):
    def role(self):
        if self.id_in_group == 1:
            return 'Sender'
        if self.id_in_group == 2:
            return 'Receiver'

