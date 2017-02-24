from rest_framework import serializers


class StringListField(serializers.ListField):
    child = serializers.CharField(read_only=True)


class ThingSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)


class RankSerializer(serializers.Serializer):
    friendlyname = serializers.CharField(read_only=True)
    name = serializers.CharField(read_only=True)
    value = serializers.IntegerField(read_only=True)


class SuggestionResultsSerializer(serializers.Serializer):
    best = serializers.IntegerField(read_only=True)
    not_recommended = serializers.IntegerField(read_only=True)
    player_count = serializers.CharField(read_only=True)
    recommended = serializers.IntegerField(read_only=True)
    numeric_player_count = serializers.IntegerField(read_only=True)


class SuggestedPlayerField(serializers.ListField):
    child = SuggestionResultsSerializer()


class BoardGameSerializer(serializers.Serializer):
    alternative_names = StringListField()
    artists = StringListField()
    rating_average = serializers.CharField(read_only=True)
    rating_average_weight = serializers.FloatField(read_only=True)
    rating_bayes_average = serializers.FloatField(read_only=True)
    categories = StringListField()
    description = serializers.CharField(read_only=True)
    designers = StringListField()
    expands = ThingSerializer()
    expansion = serializers.BooleanField(read_only=True)
    expansions = ThingSerializer()
    families = StringListField()
    id = serializers.IntegerField(read_only=True)
    image = serializers.URLField(read_only=True)
    implementations = StringListField()
    max_players = serializers.IntegerField(read_only=True)
    mechanics = StringListField()
    rating_median = serializers.FloatField(read_only=True)
    min_age = serializers.IntegerField(read_only=True)
    min_players = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    users_commented = serializers.IntegerField(read_only=True)
    rating_num_weights = serializers.IntegerField(read_only=True)
    users_owned = serializers.IntegerField(read_only=True)
    playing_time = serializers.IntegerField(read_only=True)
    min_playing_time = serializers.IntegerField(read_only=True)
    max_playing_time = serializers.IntegerField(read_only=True)
    publishers = StringListField()
    ranks = RankSerializer()
    rating_stddev = serializers.FloatField(read_only=True)
    player_suggestions = SuggestedPlayerField()
    thumbnail = serializers.URLField(read_only=True)
    users_trading = serializers.IntegerField(read_only=True)
    users_rated = serializers.IntegerField(read_only=True)
    users_wanting = serializers.IntegerField(read_only=True)
    users_wishing = serializers.IntegerField(read_only=True)
    year = serializers.CharField(read_only=True)
