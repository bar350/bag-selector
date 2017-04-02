<template>
  <div>
    <form :action="export_url" method="post">
      <div class="row">
        <div class="col-sm-5">
          BoardGame Count shown: {{ games.length - hidden.length }} of {{ games.length }}
        </div>
        <div class="col-sm-3">
          <button type="Submit">Export to Excel</button>
        </div>
        <div class="col-sm-2">
          <input type="radio" :value="false" v-model="tableDisplay">
          <label>Images</label>
        </div>
        <div class="col-sm-2">
          <input type="radio" :value="true" v-model="tableDisplay">
          <label>Table</label>
          <br>
        </div>
      </div>
      <div class="row">
        <br />
      </div>
      <div class="flex-container row" v-if="!tableDisplay">
        <div class="col-sm-3" v-for="game in games" v-if="hidden.indexOf(game.id) == -1">
          <input type="hidden" name="games" :value="game.id" />
          <input type="checkbox" @change="addUserHidden(game.id)" v-if="manualHide"/>
          <router-link :to="{ name: 'gameDetail', params: { id: game.id } }">
            <img :src="game.thumbnail" />
          </router-link>
          <table class="table table-striped">
            <thead>
              <tr>
                <td colspan="2">{{ game.name }}</td>
              </tr>
            </thead>
            <tbody>
              <tr v-for="rating in userRatings(game.id)">
                <td>{{ rating.user }}</td>
                <td>{{ rating.rating }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
      <div class="row" v-else>
        <table class="table table-bordered">
          <thead>
            <tr>
              <th v-if="manualHide">
                Hide
              </th>
              <th>
                <a href="#" @click.prevent="sortBy('name')">Name</a>
              </th>
              <th>
                <a href="#" @click.prevent="sortBy('rating_bayes_average')">Rating</a>
              </th>
              <th>
                <a href="#" @click.prevent="sortBy('rating_average_weight')">Weight</a>
              </th>
              <th>Player Count</th>
              <th>Playing Time</th>
              <th>Categories</th>
              <th>Mechanics</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="game in sortedGames" v-if="hidden.indexOf(game.id) == -1">
              <input type="hidden" name="games" :value="game.id" />
              <td v-if="manualHide">
                <input type="checkbox" @change="addUserHidden(game.id)" v-if="manualHide"/>
              </td>
              <td>
                <router-link :to="{ name: 'gameDetail', params: { id: game.id } }">
                  {{ game.name }}
                </router-link>
              </td>      
              <td>{{ game.rating_bayes_average }}</td>
              <td>{{ game.rating_average_weight }}</td>
              <td>{{ game.min_players }} <span v-if="game.min_players != game.max_players">- {{ game.max_players }}</span></td>
              <td>{{ game.min_playing_time }} <span v-if="game.min_playing_time != game.max_playing_time">- {{ game.max_playing_time }}</span></td>
              <td>{{ game.categories.join(', ') }}</td>
              <td>{{ game.mechanics.join(', ') }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </form>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
export default {
  name: 'gamelist',
  data: function() {
    return {
      tableDisplay: false,
      sortKey: 'name',
      export_url: EXCEL_URL
    }
  },
  methods: {
    ...mapActions([
      'addUserHidden'
    ]),
    sortBy: function(sortKey) {
      this.sortKey = sortKey
    }
  },
  computed: {
    ...mapGetters([
      'games',
      'hidden',
      'userRatings',
      'manualHide'
    ]),
    sortedGames: function(games) {
      let sortedGamesList = this.games
      let key = this.sortKey
      sortedGamesList.sort(function (a, b) { 
        if(typeof a[key] === 'string') {
          return a[key].localeCompare(b[key]) 
        } else {
          return a[key]-b[key]
        }
      })
      return sortedGamesList
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
</style>
