
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants







class instructions(Page):

    def is_displayed(self):
        return self.round_number == 1

class Basic_Inst(Page):

    def is_displayed(self):
        return self.round_number == 1




class reverse(Page):
    def is_displayed(self):
        return self.round_number == 5



class Basic(Page):
    form_model = 'group'
    form_fields = ['sent_amount']


    def is_displayed(self):
        return (self.player.id_in_group == 1 and self.round_number == 1) or (self.player.id_in_group == 2 and self.round_number == 5)


    def vars_for_template(self):
        participant = self.participant
        return {
            'redemption_code': participant.label,
        }



class SendBack(Page):
    form_model = 'group'
    form_fields = ['sent_back_amount']

    def is_displayed(self):
        return (self.player.id_in_group == 2 and self.round_number == 1) or (self.player.id_in_group == 1  and self.round_number == 5)

    def vars_for_template(self):
        participant = self.participant
        return {
            'tripled_amount': self.group.sent_amount * Constants.multiplication_factor,

            'less_endowment': Constants.endowment - self.group.sent_amount,

            'redemption_code': participant.label,
            'total_amount': Constants.endowment + self.group.sent_amount * Constants.multiplication_factor,
         }


    def sent_back_amount_choices(self):
       return currency_range(
            c(0),
            self.group.sent_amount * Constants.multiplication_factor,
           c(1)
        )





####################################################
class Fine45_Inst(Page):

    def is_displayed(self):
        return self.round_number == 2


class Fine45(Page):
    form_model = 'group'
    form_fields = ['sent_amount', 'amount_demanded']

    def error_message(self, values):
        print('values is', values)
        if values["amount_demanded"] > 3 * values["sent_amount"]:
            return 'The amount you are requesting is more than what P2 will receive'


    def is_displayed(self):
        return (self.player.id_in_group == 1 and self.round_number == 2) or (self.player.id_in_group == 2 and self.round_number == 6)


    def vars_for_template(self):
        participant = self.participant
        return {
            'redemption_code': participant.label,
        }



class Fineback(Page):
    form_model = 'group'
    form_fields = ['sent_back_amount']



    def is_displayed(self):
        return (self.player.id_in_group == 2 and self.round_number == 2) or (self.player.id_in_group == 1 and self.round_number == 6)

    def vars_for_template(self):
        participant = self.participant
        return {
            'tripled_amount': self.group.sent_amount * Constants.multiplication_factor,

            'less_endowment': Constants.endowment - self.group.sent_amount,

            'redemption_code': participant.label,
            'total_amount': Constants.endowment + self.group.sent_amount * Constants.multiplication_factor,
            'less_fine': Constants.endowment + self.group.sent_amount * Constants.multiplication_factor - self.group.amount_demanded - Constants.other_fine,
        }

    def sent_back_amount_choices(self):
        return currency_range(
            c(0),
            self.group.sent_amount * Constants.multiplication_factor,
            c(1)
        )

##################################################
class Shock_inst(Page):

    def is_displayed(self):
        return self.round_number == 3

class Shock(Page):
    form_model = 'group'
    form_fields = ['sent_amount']

    def is_displayed(self):
        return (self.player.id_in_group == 1 and self.round_number == 3) or (self.player.id_in_group == 2 and self.round_number == 7)

    def vars_for_template(self):
        participant = self.participant
        return {
            'redemption_code': participant.label,
        }




class SendBackRandom(Page):
    form_model = 'group'
    form_fields = ['sent_back_amount']

    def is_displayed(self):
        return (self.player.id_in_group == 2 and self.round_number == 3) or (self.player.id_in_group == 1 and self.round_number == 7)

    def vars_for_template(self):
        participant = self.participant
        return {
            'random_amount': self.session.vars['random_return'] * self.group.sent_amount,

            'redemption_code': participant.label,

            'total_random': Constants.endowment + self.group.sent_amount * self.session.vars['random_return'],
        }


    def sent_back_amount_choices(self):
        return currency_range(
            c(0),
            self.group.sent_amount * self.session.vars['random_return'],
            c(1)
        )

####################################################################

class Pun_inst(Page):

    def is_displayed(self):
        return self.round_number == 4


class Punishment(Page):
    form_model = 'group'
    form_fields = ['sent_amount', 'amount_demanded']

    def error_message(self, values):
        print('values is', values)
        if values["amount_demanded"] > 3 * values["sent_amount"]:
            return 'The amount you are requesting is more than what P2 will receive'


    def is_displayed(self):
        return (self.player.id_in_group == 1 and self.round_number == 4) or (self.player.id_in_group == 2 and self.round_number == 8)


    def vars_for_template(self):
        participant = self.participant
        return {
            'redemption_code': participant.label,
        }


class SendBackPunishment(Page):
    form_model = 'group'
    form_fields = ['sent_back_amount']



    def is_displayed(self):
        return (self.player.id_in_group == 2 and self.round_number == 4) or (self.player.id_in_group == 1 and self.round_number == 8)

    def vars_for_template(self):
        participant = self.participant
        return {
            'tripled_amount': self.group.sent_amount * Constants.multiplication_factor,

            'less_endowment': Constants.endowment - self.group.sent_amount,

            'redemption_code': participant.label,
            'total_amount': Constants.endowment + self.group.sent_amount * Constants.multiplication_factor,
            'less_fine': Constants.endowment + self.group.sent_amount * Constants.multiplication_factor - self.group.amount_demanded - Constants.fine,
        }

    def sent_back_amount_choices(self):
        return currency_range(
            c(0),
            self.group.sent_amount * Constants.multiplication_factor,
            c(1)
        )


######################################################



###################################################################################
class WaitForP1(WaitPage):
    pass

class MyWaitPage(WaitPage):
    group_by_arrival_time = True

    def is_displayed(self):
        return self.round_number == 1


    #title_text = "Waiting for your partner to make a decision"
    #body_text = "Once they have made a decision, this page will disappear and you will be asked to make a different decision"
###################################################################
class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):

            group = self.group
            if self.round_number == 3 or self.round_number == 7:
                p1 = group.get_player_by_id(1)
                p2 = group.get_player_by_id(2)
                p1.payoff = Constants.endowment - group.sent_amount + group.sent_back_amount
                p2.payoff = Constants.endowment + self.session.vars['random_return'] * group.sent_amount - group.sent_back_amount
            else:
                p1 = group.get_player_by_id(1)
                p2 = group.get_player_by_id(2)
                p1.payoff = Constants.endowment - group.sent_amount + group.sent_back_amount
                p2.payoff = Constants.endowment + group.sent_amount * Constants.multiplication_factor - group.sent_back_amount


class Results(Page):
    def is_displayed(self):
        return self.round_number == 1 or self.round_number ==2 or self.round_number == 4 or self.round_number == 5 or self.round_number == 6 or self.round_number == 8

    def vars_for_template(self):
        participant = self.participant
        return {
            'tripled_amount': self.group.sent_amount * Constants.multiplication_factor,

            'less_endowment': Constants.endowment - self.group.sent_amount,

            'redemption_code': participant.label,
            'total_amount': Constants.endowment + self.group.sent_amount * Constants.multiplication_factor,

        }




class Shockresults(Page):
    def is_displayed(self):
        return self.round_number == 3 or self.round_number == 7

    def vars_for_template(self):
        participant = self.participant
        return {
             'tripled_amount': self.group.sent_amount * Constants.multiplication_factor,

             'less_endowment': Constants.endowment - self.group.sent_amount,

             'redemption_code': participant.label,

             'random_amount': self.session.vars['random_return'] * self.group.sent_amount,

             'total_random': Constants.endowment + self.group.sent_amount * self.session.vars['random_return'],
        }

class  Everypage(Page):
    def is_displayed(self):
        return self.round_number != 4 or  self.round_number != 8
               #or  self.round_number == 4 or self.round_number == 5


class Lastpage(Page):
    def is_displayed(self):
        return self.round_number == 4
class Next(Page):
    def is_displayed(self):
        return self.round_number == 8


page_sequence = [
    #formpage,
    MyWaitPage,
   instructions,
    Basic_Inst,
    reverse,
    Basic,
    Fine45_Inst,
    Shock_inst,
    Shock,
    Pun_inst,
    Punishment,
    Fine45,
    WaitForP1,
    SendBack,
    SendBackRandom,
    SendBackPunishment,
    Fineback,
    ResultsWaitPage,
    Everypage,
    Lastpage,
    Next
    #Results,
   #Shockresults,
    ]
