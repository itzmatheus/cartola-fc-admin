from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class Player(models.Model):
    name = models.CharField(max_length=100)
    initial_proce = models.FloatField()

    def __str__(self) -> str:
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class MyTeam(models.Model):
    players = models.ManyToManyField(Player)

    def __str__(self) -> str:
        return [ player.name for player in self.players.all() ].__str__()

class Match(models.Model):
    match_date = models.DateTimeField()
    team_a = models.ForeignKey(Team, on_delete=models.PROTECT, related_name='team_a_matches')
    team_a_goal = models.IntegerField( default=0)
    team_b = models.ForeignKey(Team, on_delete=models.PROTECT, related_name='team_b_matches')
    team_b_goal = models.IntegerField( default=0)

    def __str__(self) -> str:
        return f"{self.team_a.name} x {self.team_b.name}"

class Action(models.Model):
    player = models.ForeignKey(Player, on_delete=models.PROTECT, related_name='player_actions')
    team = models.ForeignKey(Team, on_delete=models.PROTECT, related_name='team_matches')
    minutes = models.IntegerField()
    match = models.ForeignKey(Match, on_delete=models.PROTECT, related_name='match_actions')

    class Actions(models.TextChoices):
        GOAL = 'goal', 'Goal'
        ASSIST = 'assist', 'Assist'
        YELLOW_CARD = 'yellow_card', 'Yellow Card'
        RED_CARD = 'red_card', 'Red Card'

    action = models.CharField(max_length=50, choices=Actions.choices)

    def __str__(self) -> str:
        return f"{self.minutes}' - {self.player.name} - {self.action}"
