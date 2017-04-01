<template>
  <div class="container-fluid">
    <div v-for="message,k in messages" class="row" 
        style="z-index: 1050; position:fixed; right:2em; opacity: 0.8;" 
        :style="{top: (1+k)*5.5 + 'em'}">
      <alert :show.sync="message.show"  
              :type="message.type" width="400px" dismissable>
        <span class="icon-ok-circled alert-icon-float-left"></span>
        <strong>{{ message.type == 'success'?'Success':'Error'}}</strong>
        <p>{{ message.msg }}</p>
      </alert>
    </div>
    <h3>Game Selector</h3>
    <div class="row">
      <div class="col-sm-3">
        <accordion :one-at-atime="true" type="primary">
          <panel header="Filter Options">
            <div class="row form-group">
              <div class="col-sm-10 col-sm-offset-1">
                <select class="form-control" @change="addFilter">
                  <option disabled selected value="">Add Filter</option>
                  <option v-for="(filterOpts, filter) in filters"
                      :value="filter"
                      v-if="!filterOpts.shown">{{ filterOpts.name }}</option>
                </select>
              </div>
            </div>
            <div class="well well-sm" v-if="filters.expansions.shown">
              <div class="row">
                <label class="col-sm-4">
                  Exclude Expansions
                </label>
                <div class="col-sm-6">
                  <div class="togglebutton">
                      <label>
                        Off
                        <input type="checkbox" id="expansions" v-model="expansions">
                        <span class="toggle"></span>
                        On
                      </label>
                  </div>
                </div>
                <div class="col-sm-1">
                  <a href="#" 
                    @click.prevent="removeFilter('expansions')" 
                    class="pull-right">
                    <span class="glyphicon glyphicon-remove text-danger">&nbsp;</span></a>
                </div>
              </div>
            </div>

            <FilterSlider label="Player Count" :display="playerCount" v-if="filters.players.shown"
                          filterName="players" :min="1" :max="endPlayerCount" :step="1"></FilterSlider>
            
            <FilterSlider label="Playing Time" :display="playTime" v-if="filters.playing_time.shown"
                          filterName="playing_time" :min="0" :max="endPlayTime" :step="15"></FilterSlider>
            
            <FilterSlider label="Boardgame Weight" :display="gameWeight" v-if="filters.weight.shown"
                          filterName="weight" :min="0" :max="5" :step=".2"></FilterSlider>

            <FilterSlider label="Boardgame Rating" :display="gameRate" v-if="filters.rating.shown"
                          filterName="rating" :min="0" :max="10" :step=".5"></FilterSlider>
            
            <FilterSelection displayName="Category" :filterName="categoryFilter" 
                            :filterOpts="categories"
                            v-if="filters.categories.shown"></FilterSelection>
           
            <FilterSelection displayName="Mechanic" :filterName="mechanicFilter" 
                            :filterOpts="mechanics"
                            v-if="filters.mechanics.shown"></FilterSelection>
            
            <PollPlayers v-if="filters.suggested.shown"></PollPlayers>
          </panel>
          <panel header="Users" :isOpen="open" type="primary">
            <input type="text" 
                class="form-control" 
                value="" 
                placeholder="Enter Username"
                @keyup.enter="addUser" />

            <div class="row" v-for="user in users">
              <div class="col-sm-5" style="padding-top:1.5em;">
                {{ user.user }}
              </div>
              <div class="col-sm-4">
                <img :src="loading_url" v-if="!user.loaded" style="width:4em;"/>
              </div>
              <div class="col-sm-1">
                <a href="#" @click="removeUser(user.user)">
                  <span class="glyphicon glyphicon-remove text-danger" 
                      style="cursor:pointer; width:4em; padding-top:1.5em;">&nbsp;</span></a>
              </div>
            </div>
          </panel>
          <panel type="primary">
            <strong slot="header">
              Manual Hide 
            </strong>
            <div class="row">
              <label class="col-sm-7">Show Hide Option</label>
              <div class="col-sm-5">
                <div class="togglebutton">
                    <label>
                      Off
                      <input type="checkbox" id="manual" 
                              v-model="manualHide">
                      <span class="toggle"></span>
                      On
                    </label>
                </div>
              </div>
            </div>
            <div class="row" v-for="hidden in userHidden">
              <div class="col-sm-8">
                {{ getGame(hidden).name }}
              </div>
              <div class="col-sm-1">
                <a href="#" 
                  @click.prevent="removeUserHidden(hidden)" 
                  class="pull-right">
                  <span class="glyphicon glyphicon-remove text-danger">&nbsp;</span></a>
              </div>
            </div>
          </panel>
        </accordion>
      </div>
      <div class="col-sm-9">
        <GameList></GameList>
      </div>
    </div>
  </div>
</template>

<script>
import {accordion, alert, panel} from 'vue-strap'
import GameList from './GameList.vue'
import PollPlayers from './PollPlayers.vue'
import FilterSelection from './FilterSelection.vue'
import FilterSlider from './FilterSlider.vue'
import _ from 'lodash'
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'filtering',
  components: {
    panel,
    accordion,
    alert,
    GameList,
    PollPlayers,
    FilterSelection,
    FilterSlider
  },
  data: function () {
    return {
      open: true,
      mechanicFilter: 'mechanics',
      categoryFilter: 'categories',
      loading_url: LOADING_URL
    }
  },
  methods: {  
    ...mapActions([
      'computeHidden',
      'addFilter',
      'addUser',
      'removeUser',
      'calcGames',
      'removeFilter',
      'removeUserHidden'
    ]),
  },
  computed: {
    ...mapGetters([
      'filters',
      'users',
      'hidden',
      'endPlayerCount',
      'endPlayTime',
      'playerCount',
      'playTime',
      'gameWeight',
      'gameRate',
      'categories',
      'mechanics',
      'messages',
      'userHidden',
      'getGame'
    ]),
    expansions: {
      get() {
        return this.$store.getters.filters.expansions.value
      },
      set (value) {
        this.$store.dispatch('changeExpansions', value)
      }
    },
    manualHide: {
      get () {
        return this.$store.getters.manualHide
      },
      set (value) {
        this.$store.dispatch('manualHide', value)
      }
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
