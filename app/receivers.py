from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import Player, Team, Match, Action

##### PLAYER EVENTS #####

@receiver(post_save, sender=Player)
def publish_player_created(sender, instance: Player, created: bool, **kwargs):
    if created:
        print('Player created', instance)

##### TEAM EVENTS #####

@receiver(post_save, sender=Team)
def publish_team_created(sender, instance: Team, created: bool, **kwargs):
    if created:
        print('Team created', instance)

##### MATCH EVENTS #####

@receiver(post_save, sender=Match)
def publish_match_created(sender, instance: Match, created: bool, **kwargs):
    if created:
        print('Match created', instance)

@receiver(pre_save, sender=Match)
def get_old_match(sender, instance: Match, **kwargs):
    try:
        instance._pre_save_instance = Match.objects.get(pk=instance.pk)
    except Match.DoesNotExist:
        instance._pre_save_instance = None

@receiver(post_save, sender=Match)
def publish_new_match_result(sender, instance: Match, created: bool, **kwargs):
    
    is_team_a_make_goal = instance._pre_save_instance and instance._pre_save_instance.team_a_goal != instance.team_a_goal
    is_team_b_make_a_goal = instance._pre_save_instance and instance._pre_save_instance.team_b_goal != instance.team_b_goal

    if not created and (is_team_a_make_goal or is_team_b_make_a_goal):
        print('Match goal updated', instance)

##### ACTION EVENTS #####

@receiver(post_save, sender=Action)
def publish_action_added(sender, instance: Action, created: bool, **kwargs):
    if created:
        print('Action created', instance)