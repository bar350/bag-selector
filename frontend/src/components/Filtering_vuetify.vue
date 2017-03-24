<template>
  <v-container fluid>
    <h3>Game Selector</h3>
    <v-row>
      <v-col xs3="xs3">
        <v-expansion-panel id="accordion" class="grey lighten-4">
          <v-expansion-panel-content>
            <div slot="header"  class="grey lighten-4">Filter Options</div>
            <v-card>
              <v-card-text>
                <v-row>
                  <v-col xs10="xs10">
                    <select class="form-control" @change="addFilter">
                      <option disabled selected value="">Add Filter</option>
                      <option v-for="(filterOpts, filter) in filters"
                          :value="filter"
                          v-if="!filterOpts.shown">{{ filterOpts.name }}</option>
                    </select>
                  </v-col>
                </v-row>
              </v-card-text>
            </v-card>
            <v-card class="grey lighten-2" v-if="filters.expansions.shown">
              <v-card-text>
                <v-row>
                  <v-col xs5="xs5">
                    <label>
                      Exclude Expansions
                    </label>
                  </v-col>
                  <v-col xs5="xs5">
                    <v-switch primary v-model="filters.expansions.value" @change="computeHidden" light />
                  </v-col>
                  <v-col xs1="xs1">
                    <a href="#"
                      @click.prevent="removeFilter('expansions')"
                      class="pull-right">
                      <v-icon class="red--text">clear</v-icon></a>
                  </v-col>
                </v-row>
              </v-card-text>
            </v-card>
            <v-card class="grey lighten-2" v-if="filters.players.shown">
              <v-card-text>
                <v-row>
                  <v-col xs10="xs10">
                    <label>
                      Player Count  ({{ playerCount }})
                    </label>
                  </v-col>
                  <v-col xs1="xs1">
                    <a href="#"
                      @click.prevent="removeFilter('players')"
                      class="pull-right">
                      <v-icon class="red--text">clear</v-icon></a>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col xs10="xs10">
                    <v-slider v-model="e1" :min="1" :max="endPlayerCount" :step="1" light />
                    <div class="shor">
                      <slider :slider-value="filters.players.value"
                        :slider-min="1"
                        :slider-max="endPlayerCount"
                        :slider-step="1"
                        v-on:updated="updateSlider('players',$event)"></slider>
                    </div>
                  </v-col>
                </v-row>
              </v-card-text>
            </v-card>
            <v-card class="grey lighten-2" v-if="filters.playing_time.shown">
              <v-card-text>
                <v-row>
                  <v-col xs10="xs10">
                    <label>
                      Playing Time  ({{ playTime }})
                    </label>
                  </v-col>
                  <v-col xs1="xs1">
                    <a href="#"
                      @click.prevent="removeFilter('playing_time')"
                      class="pull-right">
                      <v-icon class="red--text">clear</v-icon></a>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col xs10="xs10">
                    <div class="shor">
                      <slider :slider-value="filters.playing_time.value"
                        :slider-min="0"
                        :slider-max="endPlayTime"
                        :slider-step="15"
                        v-on:updated="updateSlider('playing_time', $event)"></slider>
                    </div>
                  </v-col>
                </v-row>
              </v-card-text>
            </v-card>
            <v-card class="grey lighten-2" v-if="filters.weight.shown">
              <v-card-text>
                <v-row>
                  <v-col xs10="xs10">
                    <label>
                      Boardgame Weight ({{ gameWeight }})
                    </label>
                  </v-col>
                  <v-col xs1="xs1">
                    <a href="#"
                      @click.prevent="removeFilter('weight')"
                      class="pull-right">
                      <v-icon class="red--text">clear</v-icon></a>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col xs10="xs10">
                    <div class="shor">
                      <slider :slider-value="filters.weight.value"
                        :slider-min="0"
                        :slider-max="5"
                        :slider-step=".2"
                        v-on:updated="updateSlider('weight', $event)"></slider>
                    </div>
                  </v-col>
                </v-row>
              </v-card-text>
            </v-card>
            <v-card class="grey lighten-2" v-if="filters.rating.shown">
              <v-card-text>
                <v-row>
                  <v-col xs10="xs10">
                    <label>
                      Boardgame Rating  ({{ gameRate }})
                    </label>
                  </v-col>
                  <v-col xs1="xs1">
                    <a href="#"
                      @click.prevent="removeFilter('rating')"
                      class="pull-right">
                      <v-icon class="red--text">clear</v-icon></a>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col xs10="xs10">
                    <div class="shor">
                      <slider :slider-value="filters.rating.value"
                        :slider-min="0"
                        :slider-max="10"
                        :slider-step=".5"
                        v-on:updated="updateSlider('rating', $event)"></slider>
                    </div>
                  </v-col>
                </v-row>
              </v-card-text>
            </v-card>
            <v-card class="grey lighten-2" v-if="filters.categories.shown">
              <v-card-text>
                <v-row>
                  <v-col xs10="xs10">
                    <select class="form-control" @change="categorySelection">
                        <option value="" disabled selected>Choose a category</option>
                        <option :value="category"
                            v-for="category in categories">{{ category }}</option>
                    </select>
                  </v-col>
                  <v-col xs1="xs1">
                    <a href="#"
                      @click.prevent="removeFilter('categories')"
                      class="pull-right">
                      <v-icon class="red--text">clear</v-icon></a>
                  </v-col>
                </v-row>
                <v-row class="row" v-for="category in filters.categories.active">
                  <v-col xs5="xs5">
                    <label>{{ category }}</label>
                  </v-col>
                  <v-col xs4="xs4">
                    <v-switch primary @change="toggleFilter('categories',category)" light />
                  </v-col>
                  <v-col xs2="xs2">
                    <a href="#"
                        @click.prevent="removeFilterOption('categories',category)" >
                      <v-icon class="red--text">clear</v-icon></a>
                  </v-col>
                </v-row>
              </v-card-text>
            </v-card>
            <v-card class="grey lighten-2" v-if="filters.mechanics.shown">
              <v-card-text>
                <v-row>
                  <v-col xs10="xs10">
                    <select class="form-control" @change="mechanicSelection">
                        <option value="" disabled selected>Choose a Mechanic</option>
                        <option :value="mechanic"
                            v-for="mechanic in mechanics">{{ mechanic }}</option>
                    </select>
                  </v-col>
                  <v-col xs1="xs1">
                    <a href="#"
                      @click.prevent="removeFilter('mechanics')"
                      class="pull-right">
                      <v-icon class="red--text">clear</v-icon></a>
                  </v-col>
                </v-row>
                <v-row v-for="mechanic in filters.mechanics.active">
                  <v-col xs5="xs5">
                    <label>{{ mechanic }}</label>
                  </v-col>
                  <v-col xs4="xs4">
                    <v-switch primary @change="toggleFilter('mechanics',mechanic)" light />
                  </v-col>
                  <v-col xs2="xs2">
                    <a href="#" @click.prevent="removeFilterOption('mechanics',mechanic)">
                        <v-icon class="red--text">clear</v-icon></a>
                  </v-col>
                </v-row>
              </v-card-text>
            </v-card>
            <v-card class="grey lighten-2" v-if="filters.suggested.shown">
              <v-card-text>
                <v-row>
                    <v-col xs10="xs10">
                      <label>(Poll) Number of Players</label>
                    </v-col>
                    <v-col xs1="xs1">
                      <a href="#"
                        @click.prevent="removeFilter('suggested')"
                        class="pull-right">
                        <v-icon class="red--text">clear</v-icon></a>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col xs4="xs4">
                      <label>At least</label>
                    </v-col>
                    <v-col xs3="xs3">
                      <select class="form-control"
                          v-model="filters.suggested.percent"
                          @change="computeHidden">
                        <option v-for="n in 10"
                          :value="n*10">{{ n*10 }}%</option>
                      </select>
                    </v-col>
                    <v-col xs4="xs4">
                      <label> of voters</label>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col xs2="xs2">
                      <label>voted</label>
                    </v-col>
                    <v-col xs9="xs9">
                      <select class="form-control"
                          v-model="filters.suggested.rate"
                          @change="computeHidden">
                        <option value="best">Best</option>
                        <option value="bestorrec">Best or Recommended</option>
                        <option value="not">Not Recommended</option>
                      </select>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col xs2="xs2">
                      <label>with </label>
                    </v-col>
                    <v-col xs4="xs4">
                      <input type="text" class="form-control"
                          v-model="filters.suggested.players"
                          @change="computeHidden">
                    </v-col>
                    <v-col xs3="xs3">
                      <label> players</label>
                    </v-col>
                  </v-row>
              </v-card-text>
            </v-card>
          </v-expansion-panel-content>
        </v-expansion-panel>
        <v-expansion-panel expand class="grey lighten-4">
          <v-expansion-panel-content>
            <div slot="header">Users</div>
            <v-card>
              <v-card-text>
                <input type="text"
                    class="form-control"
                    value=""
                    placeholder="Enter Username"
                    @keyup.enter="addUser" />

                <v-row v-for="user in users">
                  <v-col xs9="xs9">
                    {{ user }}
                  </v-col>
                  <v-col xs1="xs1">
                    <a href="#"
                      @click.prevent="removeUser(user)"
                      class="pull-right">
                      <v-icon class="red--text">clear</v-icon></a>
                  </v-col>
                </v-row>
              </v-card-text>
            </v-card>
          </v-expansion-panel-content>
        </v-expansion-panel>
      </v-col>
      <v-col xs9="xs9">
        <v-row>
          <v-col xs5="xs5">
            BoardGame Count shown: {{ games.length - hidden.length }} of {{ games.length }}
          </v-col>
        </v-row>
        <v-row>
          <v-col xs3="xs3" v-for="game in games" v-if="_.indexOf(hidden, game.id) === -1">
            <router-link :to="{ name: 'gameDetail', params: { id: game.id } }">
              <img :src="game.thumbnail" />
            </router-link><br />
            <label>{{ game.name }}</label>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import Slider from './Slider.vue'
import _ from 'lodash'
export default {
  name: 'filtering',
  components: {
    Slider
  },
  data: function () {
    return {
      games: [],
      userGames: {},
      game_url: '',
      filters: {
        expansions: {
          name: 'Exclude Expansions',
          shown: false,
          value: true
        },
        players: {
          name: 'Player Count',
          shown: false,
          value: [1, 10]
        },
        playing_time: {
          name: 'Playing Time',
          shown: false,
          value: [0, 300]
        },
        weight: {
          name: 'Game Weight',
          shown: false,
          value: [0, 5]
        },
        rating: {
          name: 'Game Rating',
          shown: false,
          value: [0, 10]
        },
        categories: {
          name: 'Categories',
          shown: false,
          active: [],
          excluded: []
        },
        mechanics: {
          name: 'Mechanics',
          shown: false,
          active: [],
          excluded: []
        },
        suggested: {
          name: 'Suggested Player (poll)',
          shown: false,
          percent: 10,
          rate: 'best',
          players: 4
        }
      },
      users: [],
      endPlayerCount: 10,
      endPlayTime: 300,
      hidden: []
    }
  },
  methods: {
    addFilter: function (event) {
      var value = event.target.value
      this.filters[value].shown = true
      event.target.value = ''
      this.computeHidden()
    },
    removeFilter: function (filter) {
      this.filters[filter].shown = false
      this.computeHidden()
    },
    checkExpansions: function (game) {
      // If Game is an expansion and the expansion filter has been added
      // as well if the expansion fiter is on
      if (this.filters.expansions.shown &&
        !this.filters.expansions.value && game.expansion) {
        return true
      }
      return false
    },
    checkPlayers: function (game) {
      if (!this.filters.players.shown) {
        return false
      }
      // If minimum required players is greater than the max filtered
      if (game.min_players > this.filters.players.value[1] &&
        this.filters.players.value[1] !== this.endPlayerCount) {
        return true
      }
      if (game.max_players < this.filters.players.value[0]) {
        return true
      }
      return false
    },
    checkRating: function (game) {
      if (!this.filters.rating.shown) {
        return false
      }

      if (game.rating_bayes_average > this.filters.rating.value[1] ||
        game.rating_bayes_average < this.filters.rating.value[0]) {
        return true
      }

      return false
    },
    checkWeight: function (game) {
      if (!this.filters.weight.shown) {
        return false
      }

      if (game.rating_average_weight > this.filters.weight.value[1] ||
        game.rating_average_weight < this.filters.weight.value[0]) {
        return true
      }

      return false
    },
    checkPlayingTime: function (game) {
      if (!this.filters.playing_time.shown) {
        return false
      }

      if (game.min_playing_time > this.filters.playing_time.value[1] &&
        this.filters.playing_time.value[1] !== this.endPlayTime) {
        return true
      }
      if (game.max_playing_time < this.filters.playing_time.value[0]) {
        return true
      }

      return false
    },
    checkCategories: function (game) {
      if (!this.filters.categories.shown) {
        return false
      }

      // If game has categories in the exclude categories list
      if (_.intersection(game.categories, this.filters.categories.excluded).length) {
        return true
      }
      // if categories have been specified that are not excluded
      // then only show those with those categories
      if (!_.intersection(game.categories, this.filters.categories.active).length &&
        this.filters.categories.active.length !== this.filters.categories.excluded.length) {
        return true
      }

      return false
    },
    checkMechanics: function (game) {
      if (!this.filters.players.shown) {
        return false
      }

      // If game has mechanics in the exclude mechanics list
      if (_.intersection(game.mechanics, this.filters.mechanics.excluded).length) {
        return true
      }
      // if mechanics have been specified that are not excluded
      // then only show those with those mechanics
      if (!_.intersection(game.mechanics, this.filters.mechanics.active).length &&
        this.filters.mechanics.active.length !== this.filters.mechanics.excluded.length) {
        return true
      }

      return false
    },
    checkSuggestions: function (game) {
      if (!this.filters.suggested.shown) {
        return false
      }

      var vm = this
      var hasValidSuggestion = false
      _.each(game.player_suggestions, function (suggestion, index, playerSuggestions) {
        if (suggestion.numeric_player_count === vm.filters.suggested.players) {
          var total = suggestion.best + suggestion.recommended + suggestion.not_recommended
          var percent = 0
          if (vm.filters.suggested.rate === 'best') {
            percent = (suggestion.best / total) * 100
          } else if (vm.filters.suggested.rate === 'bestorrec') {
            percent = ((suggestion.best + suggestion.recommended) / total) * 100
          } else {
            percent = (suggestion.not_recommended / total) * 100
          }
          if (percent >= vm.filters.suggested.percent) {
            hasValidSuggestion = true
          }
        }
      })
      if (!hasValidSuggestion) {
        return true
      }

      return false
    },
    checkhidden: function (game) {
      if (this.checkExpansions(game)) {
        return true
      }
      if (this.checkPlayers(game)) {
        return true
      }
      if (this.checkRating(game)) {
        return true
      }
      if (this.checkWeight(game)) {
        return true
      }
      if (this.checkPlayingTime(game)) {
        return true
      }
      if (this.checkCategories(game)) {
        return true
      }
      if (this.checkMechanics(game)) {
        return true
      }
      if (this.checkSuggestions(game)) {
        return true
      }

      return false
    },
    // changeExpansions: function () {
    //   this.filters.expansions.value = !this.filters.expansions.value
    //   this.computeHidden()
    // },
    computeHidden: function () {
      this.hidden = []
      var vm = this
      _.each(this.games, function (game, index, games) {
        if (vm.checkhidden(game)) {
          vm.hidden.push(game.id)
        }
      })
    },
    updateSlider: function (filter, value) {
      this.filters[filter].value = value
      this.computeHidden()
    },
    toggleFilter: function (filter, value) {
      var indexCat = _.indexOf(this.filters[filter].excluded, value)
      if (indexCat !== -1) {
        this.filters[filter].excluded.splice(indexCat, 1)
      } else {
        this.filters[filter].excluded.push(value)
      }
      this.computeHidden()
    },
    removeFilterOption: function (filter, value) {
      var indexCat = _.indexOf(this.filters[filter].excluded, value)
      if (indexCat !== -1) {
        this.filters[filter].excluded.splice(indexCat, 1)
      }
      indexCat = _.indexOf(this.filters[filter].active, value)
      if (indexCat !== -1) {
        this.filters[filter].active.splice(indexCat, 1)
      }
      this.computeHidden()
    },
    categorySelection: function (event) {
      var value = event.target.value
      event.target.value = ''
      this.filters.categories.active.push(value)
      this.computeHidden()
    },
    mechanicSelection: function (event) {
      var value = event.target.value
      event.target.value = ''
      this.filters.mechanics.active.push(value)
      this.computeHidden()
    },
    gameUrl: function (id) {
      return this.game_url.slice(0, -2) + id + '/'
    },
    addUser: function (event) {
      var value = event.target.value
      this.users.push(value)
      // GET /someUrl
      this.$http.get('?username=' + value).then(response => {
        // get body data
        this.userGames[value] = response.body
        this.calcGames()
      },
      response => {
        // error callback
      })
      event.target.value = ''
    },
    removeUser: function (user) {
      var indexUser = _.indexOf(this.users, user)
      if (indexUser !== -1) {
        this.users.splice(indexUser, 1)
      }
      if (typeof this.userGames[user] !== 'undefined') {
        delete this.userGames[user]
      }
      this.calcGames()
    },
    calcGames: function () {
      var games = {}
      _.each(this.userGames, function (gamesRpt, user, users) {
        _.each(gamesRpt, function (game, index, gamesRpt) {
          games[game.id] = game
        })
      })
      var gameList = _.values(games)
      gameList.sort(function (a, b) { return a.name.localeCompare(b.name) })
      this.games = gameList
      this.computeHidden()
    }
  },
  computed: {
    playerCount: function () {
      var countStr = this.filters.players.value[0] + ' To ' + this.filters.players.value[1]
      if (this.filters.players.value[1] === this.endPlayerCount) {
        countStr += '+'
      }
      return countStr
    },
    playTime: function () {
      var countStr = this.filters.playing_time.value[0] + ' To ' + this.filters.playing_time.value[1]
      if (this.filters.playing_time.value[1] === this.endPlayTime) {
        countStr += '+'
      }
      return countStr
    },
    gameWeight: function () {
      var countStr = this.filters.weight.value[0] + ' To ' + this.filters.weight.value[1]
      return countStr
    },
    gameRate: function () {
      var countStr = this.filters.rating.value[0] + ' To ' + this.filters.rating.value[1]
      return countStr
    },
    categories: function () {
      var cats = []
      _.each(this.games, function (game, index, games) {
        _.each(game.categories, function (category, f, categories) {
          if (_.indexOf(cats, category) === -1) {
            cats.push(category)
          }
        })
      })
      cats.sort()
      return cats
    },
    mechanics: function () {
      var cats = []
      _.each(this.games, function (game, index, games) {
        _.each(game.mechanics, function (category, f, mechanics) {
          if (_.indexOf(cats, category) === -1) {
            cats.push(category)
          }
        })
      })
      cats.sort()
      return cats
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
  .flex-container {
    display: flex;
    flex-flow: row wrap;
  }
  div.noUi-tooltip {
      position: relative;
      top:1em;
  }
  div.noUi-handle.noUi-active {
      transform: scale3d(1,1,1);
  }
  div.noUi-origin[style^="left: 0"] .noUi-handle {
      border-color: #009688;
      background-color: #009688;
  }
  div.noUi-origin {
      background: #009688;
  }
  div.noUi-origin:last-child {
      background: #c8c8c8;
  }
  div.input-group {
    margin: 0;
  }
</style>
