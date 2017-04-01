<template>
  <div class="container" v-if="loaded">
    <router-link :to="{ name: 'gameFilter'}"
        tag="button" class="btn btn-info btn-raised"> &lt;&lt; Back to Selector</router-link>
    <h2>{{ boardgame.name }}</h2>
    <div class="row">
      <div class="col-sm-4">
        <img :src="boardgame.image" style="width:100%" />
      </div>
      <div class="col-sm-4">
        <vue-chart
            :chart-type="chartType"
            :columns="chartColumns"
            :rows="chartRows"
            :options="chartOptions"
        ></vue-chart>
      </div>
    </div>
    <div class="row">
      <div class="col-sm-5">
        <div class="row">
          <label class="col-sm-4">BGG ID: </label>
          <div class="col-sm-8">{{ boardgame.id }}</div>
        </div>
        <div class="row">
          <label class="col-sm-4">Players: </label>
          <div class="col-sm-8">{{ boardgame.min_players }} - {{ boardgame.max_players}}</div>
        </div>
        <div class="row">
          <label class="col-sm-4">Best At: </label>
          <div class="col-sm-8">{{ get_best_count }}</div>
        </div>
        <div class="row">
          <label class="col-sm-4">Recommended: </label>
          <div class="col-sm-8">{{ get_recommended_count }}</div>
        </div>
        <div class="row">
          <label class="col-sm-4">Playing Time: </label>
          <div class="col-sm-8">{{ boardgame.playing_time }}</div>
        </div>
        <div class="row">
          <label class="col-sm-4">Rating: </label>
          <div class="col-sm-8">{{ boardgame.rating_average }}</div>
        </div>
        <div class="row">
          <label class="col-sm-4">Bayes Rating: </label>
          <div class="col-sm-8">{{ boardgame.rating_bayes_average }}</div>
        </div>
        <div class="row">
          <label class="col-sm-4">Categories: </label>
          <div class="col-sm-8">{{ category_list }}</div>
        </div>
        <div class="row">
          <label class="col-sm-4">Mechanics: </label>
          <div class="col-sm-8">{{ mechanic_list }}</div>
        </div>
        <div class="row">
          <label class="col-sm-4">Description: </label>
          <div class="col-sm-8" style="white-space: pre-wrap;">{{ boardgame.description }}</div>
        </div>
      </div>
      <div class="col-sm-5 col-sm-offset-1">
        <div class="row" v-for="rank in boardgame.ranks">
          <label class="col-sm-4">
            {{ rank.friendlyname }}
          </label>
          <div class="col-sm-7">
            {{ rank.value }}
          </div>
        </div>
        <label><h4>Expansions: </h4></label>
        <div class="row" v-for="expansion in boardgame.expansions">
          <div class="col-sm-8 col-sm-offset-4">
            {{ expansion.name }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import _ from 'lodash'
export default {
  name: 'gamedetail',
  data: function() {
    return {
      boardgame: { ranks: [{}] },
      loaded: false,
      gameId: this.$route.params.id,
      chartType: 'ColumnChart',
      //chartType: 'PieChart',
      chartColumns: [ 
            { 'type': 'string', 'label': 'Player Count' }, 
            { 'type': 'number', 'label': 'Not Recommended' }, 
            { 'type': 'number', 'label': 'Recommended' }, 
            { 'type': 'number', 'label': 'Best' }
          ],
          chartOptions: {'title':'Player Suggestions',
                         'width':600,
                         'height':300,
                   'legend': { position: 'top', maxLines: 3 },
                         'isStacked': 'percent',
                       'series': {
                  0:{color:'red'},
                  1:{color:'yellow'},
                  2:{color:'green'}
                }
              },
    }
  },
  watch: {
    '$route': 'fetchData'
  },
  created () {
    this.fetchData();
  },
  methods: {
    fetchData: function() {
      this.gameId = this.$route.params.id;
      if(this.gameId) {
        let game = this.$store.getters.getGame(this.gameId)
        if(game) {
          this.boardgame = game 
          this.loaded = true
        } else {
          this.$http.get(this.gameId+'/').then(response => {
              // get body data
              this.boardgame = response.body;
              this.loaded = true;
          }, response => {
            // error callback
          });
        }
      }
    },
  },
  computed: {
    'category_list': function() {
      if(typeof this.boardgame.categories !== 'undefined') {
        return this.boardgame.categories.join(', ');
      } else {
        return '';
      }
    },
    'mechanic_list': function() {
      if(typeof this.boardgame.mechanics !== 'undefined') {
        return this.boardgame.mechanics.join(', ');
      } else {
        return '';
      }
    },
    'chartRows': function() {
      var rows = []
      _.each(_.sortBy(this.boardgame.player_suggestions,['numeric_player_count']), function(suggestion, index, player_suggestions) {
        rows.push([ suggestion.player_count, suggestion.not_recommended,
          suggestion.recommended, suggestion.best ]);
      });
      return rows;
    },
    'get_best_count': function() {
      var best_counts = [];
      var vm = this;
      _.each(this.boardgame.player_suggestions, function(suggestion, index, player_suggestions) {
        var total = suggestion.best + suggestion.recommended + suggestion.not_recommended;
        var percent = (suggestion.best/total)*100;
        if(percent >= 50) {
          best_counts.push(suggestion.player_count)
        }
      });
      return best_counts.join(', ');
    },
    'get_recommended_count': function() {
      var rec_counts = [];
      var vm = this;
      _.each(this.boardgame.player_suggestions, function(suggestion, index, player_suggestions) {
        var total = suggestion.best + suggestion.recommended + suggestion.not_recommended;
        var percent = (suggestion.recommended/total)*100;
        if(percent >= 50) {
          rec_counts.push(suggestion.player_count)
        }
      });
      return rec_counts.join(', ');
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
</style>
