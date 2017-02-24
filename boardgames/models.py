from django.db import models


# Create your models here.
class GameCategory(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category


class GameMechanic(models.Model):
    mechanic = models.CharField(max_length=100)

    def __str__(self):
        return self.mechanic


class BoardGame(models.Model):
    boardgame_rank = models.FloatField(blank=True, null=True)
    categories = models.ManyToManyField(GameCategory)
    description = models.TextField()
    bgg_id = models.IntegerField()
    image_url = models.CharField(max_length=300, blank=True, null=True)
    max_players = models.IntegerField()
    mechanics = models.ManyToManyField(GameMechanic, blank=True)
    min_age = models.IntegerField()
    min_players = models.IntegerField()
    name = models.CharField(max_length=400)
    playing_time = models.IntegerField()
    rating_average = models.FloatField()
    average_weight = models.FloatField()
    expansion = models.BooleanField()
    rating_bayes_average = models.FloatField(blank=True, null=True)
    thumbnail_url = models.CharField(max_length=300, blank=True, null=True)
    year = models.CharField(max_length=10)
    updated = models.DateField(auto_now=True, editable=False)

    def __str__(self):
        return self.name

    def get_best_count(self):
        best_list = []
        for suggestion in self.player_suggestions.all():
            total = suggestion.best + suggestion.recommended + suggestion.not_recommended
            if total != 0 and (suggestion.best / total) * 100 > 50:
                best_list.append(suggestion.player_count)
        best_list.sort()
        return ", ".join(best_list)

    def get_recommended_count(self):
        best_list = []
        for suggestion in self.player_suggestions.all():
            total = suggestion.best + suggestion.recommended + suggestion.not_recommended
            if total != 0 and ((suggestion.recommended + suggestion.best) / total) * 100 > 50:
                best_list.append(suggestion.player_count)
        best_list.sort()
        return ", ".join(best_list)


class PlayerSuggestion(models.Model):
    player_count = models.CharField(max_length=3)
    recommended = models.IntegerField(blank=True, null=True)
    not_recommended = models.IntegerField(blank=True, null=True)
    best = models.IntegerField(blank=True, null=True)
    board_game = models.ForeignKey(BoardGame, related_name='player_suggestions')

    def __str__(self):
        return "{} (Best: {}, Recommended: {}, Not Recommended {})".format(
            self.player_count, self.best, self.recommended, self.not_recommended)
