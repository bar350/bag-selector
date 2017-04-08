import Vue from 'vue';
import Vuex from 'vuex';
import _ from 'lodash'

// Load vuex into the Vue instance
Vue.use(Vuex);

export const store = new Vuex.Store({
    state: {
        games: [],
      	userGames: {},
      	manualHide: false,
      	userHidden: [],
      	filters: {
	        expansions: {
	          name: 'Exclude Expansions',
	          shown: false,
	          value: false
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
	    messages: [],
	    users: [],
      	hidden: [],
    	endPlayerCount: 10,
    	endPlayTime: 300
    },
    getters: {
    	games: state => {
    		return state.games;
    	},
    	userGames: state => {
    		return state.userGames;
    	},
    	manualHide: state => {
    		return state.manualHide;
    	},
	    userHidden: state => {
	    	return state.userHidden;
	    },
    	filters: state => {
    		return state.filters;
    	},
    	users: state => {
    		return state.users;
    	},
    	messages: state => {
    		return state.messages;
    	},
    	hidden: state => {
    		return state.hidden;
    	},
    	endPlayerCount: state => {
    		return state.endPlayerCount;
    	},
    	endPlayTime: state => {
    		return state.endPlayTime;
    	},
    	// Get all the categories on the currently loaded games 
	    categories: state => {
	      let cats = []
	      _.each(state.games, function (game, index, games) {
	        _.each(game.categories, function (category, f, categories) {
	          if (_.indexOf(cats, category) === -1) {
	            cats.push(category)
	          }
	        })
	      })
	      cats.sort()
	      return cats
	    },
	    // Get all the mechanics on the currently loaded games
	    mechanics: state => {
	      let cats = []
	      _.each(state.games, function (game, index, games) {
	        _.each(game.mechanics, function (category, f, mechanics) {
	          if (_.indexOf(cats, category) === -1) {
	            cats.push(category)
	          }
	        })
	      })
	      cats.sort()
	      return cats
	    },
	    // Return a display for player count filter
	    playerCount: state => {
	      let countStr = state.filters.players.value[0] + ' To ' + state.filters.players.value[1]
	      if (state.filters.players.value[1] == state.endPlayerCount) {
	        countStr += '+'
	      }
	     
	      return countStr
	    },
	    // Return a display for player time filter
	    playTime: state => {
	      let countStr = state.filters.playing_time.value[0] + ' To ' + state.filters.playing_time.value[1]
	      if (state.filters.playing_time.value[1] == state.endPlayTime) {
	        countStr += '+'
	      }
	     
	      return countStr
	    },
	    // Return a display for game Weight filter
	    gameWeight: state => {
	      let countStr = state.filters.weight.value[0] + ' To ' + state.filters.weight.value[1]
	     
	      return countStr
	    },
	    // Return a display for game rate filter
	    gameRate: state => {
	      let countStr = state.filters.rating.value[0] + ' To ' + state.filters.rating.value[1]
	      return countStr
	    },
	    /* Check methods for the filters to see if a given game meets the filter specifications */
	    checkExpansions: (state) => (game) => {
	      // If Game is an expansion and the expansion filter has been added
	      // as well if the expansion fiter is on
	      if (state.filters.expansions.shown &&
	        state.filters.expansions.value && game.expansion) {
	        return true
	      }
	      return false
	    },
	    checkPlayers: (state, getters) => (game) => {
	      if (!state.filters.players.shown) {
	        return false
	      }
	      // If minimum required players is greater than the max filtered
	      if (game.min_players > state.filters.players.value[1] &&
	        state.filters.players.value[1] !== state.endPlayerCount) {
	        return true
	      }
	      if (game.max_players < state.filters.players.value[0]) {
	        return true
	      }
	      return false
	    },
	    checkRating: (state, getters) => (game) =>  {
	      if (!state.filters.rating.shown) {
	        return false
	      }

	      if (game.rating_bayes_average > state.filters.rating.value[1] ||
	        game.rating_bayes_average < state.filters.rating.value[0]) {
	        return true
	      }

	      return false
	    },
	    checkWeight: (state, getters) => (game) =>  {
	      if (!state.filters.weight.shown) {
	        return false
	      }

	      if (game.rating_average_weight > state.filters.weight.value[1] ||
	        game.rating_average_weight < state.filters.weight.value[0]) {
	        return true
	      }

	      return false
	    },
	    checkPlayingTime: (state, getters) => (game) =>  {
	      if (!state.filters.playing_time.shown) {
	        return false
	      }

	      if (game.min_playing_time > state.filters.playing_time.value[1] &&
	        state.filters.playing_time.value[1] !== state.endPlayTime) {
	        return true
	      }
	      if (game.max_playing_time < state.filters.playing_time.value[0]) {
	        return true
	      }

	      return false
	    },
	    checkCategories: (state, getters) => (game) =>  {
	      if (!state.filters.categories.shown) {
	        return false
	      }

	      // If game has categories in the exclude categories list
	      if (_.intersection(game.categories, state.filters.categories.excluded).length) {
	        return true
	      }
	      // if categories have been specified that are not excluded
	      // then only show those with those categories
	      if (!_.intersection(game.categories, state.filters.categories.active).length &&
	        state.filters.categories.active.length !== state.filters.categories.excluded.length) {
	        return true
	      }

	      return false
	    },
	    checkMechanics: (state, getters) => (game) =>  {
	      if (!state.filters.mechanics.shown) {
	        return false
	      }

	      // If game has mechanics in the exclude mechanics list
	      if (_.intersection(game.mechanics, state.filters.mechanics.excluded).length) {
	        return true
	      }
	      // if mechanics have been specified that are not excluded
	      // then only show those with those mechanics
	      if (!_.intersection(game.mechanics, state.filters.mechanics.active).length &&
	        state.filters.mechanics.active.length !== state.filters.mechanics.excluded.length) {
	        return true
	      }

	      return false
	    },
	    checkSuggestions: (state, getters) => (game) =>  {
	      if (!state.filters.suggested.shown || !state.filters.suggested.players) {
	        return false
	      }

	      let hasValidSuggestion = false
	      _.each(game.player_suggestions, function (suggestion, index, playerSuggestions) {
	        if (suggestion.numeric_player_count == state.filters.suggested.players) {
	          let total = suggestion.best + suggestion.recommended + suggestion.not_recommended
	          let percent = 0
	          if (state.filters.suggested.rate === 'best') {
	            percent = (suggestion.best / total) * 100
	          } else if (state.filters.suggested.rate === 'bestorrec') {
	            percent = ((suggestion.best + suggestion.recommended) / total) * 100
	          } else {
	            percent = (suggestion.not_recommended / total) * 100
	          }
	          if (percent >= state.filters.suggested.percent) {
	            hasValidSuggestion = true
	          }
	        }
	      })
	      if (!hasValidSuggestion) {
	        return true
	      }

	      return false
	    },
	    checkhidden: (state, getters) => (game) =>  {
	      if (getters.checkExpansions(game)) {
	        return true
	      }
	      if (getters.checkPlayers(game)) {
	        return true
	      }
	      if (getters.checkRating(game)) {
	        return true
	      }
	      if (getters.checkWeight(game)) {
	        return true
	      }
	      if (getters.checkPlayingTime(game)) {
	        return true
	      }
	      if (getters.checkCategories(game)) {
	        return true
	      }
	      if (getters.checkMechanics(game)) {
	        return true
	      }

	      if (getters.checkSuggestions(game)) {
	        return true
	      }

	      if (getters.userHidden.length > 0) {
	      	let indexCat = _.indexOf(state.userHidden, game.id)
	    	if (indexCat !== -1) {
	        	return true
	        }
	      }

	      return false
	    },
	    getGame: (state, getters) => (gameId) => {
	    	let game = _.find(state.games, function(obj) {
	    		return obj.id == gameId;
	    	})
	    	if(typeof game === 'undefined') {
	    		return false
	    	}
	    	
	    	return game
	    },
	    userRatings: (state, getters) => (gameId) => {
	    	let ratings = []
	    	_.each(state.userGames, function (gamesRpt, user, users) {
	    		let game = _.find(gamesRpt.collection.items, function(obj) {
		    		return obj.id == gameId;
		    	})
		    	if(typeof game !== 'undefined' && game.rating) {
		    		ratings.push({user: user, rating: game.rating})
		    	}
	    	})
	    	return ratings
	    }
    },
    mutations: {
	    addHidden: (state, id) => {
	    	state.hidden.push(id)
	    },
	    manualHide: (state) => {
	    	state.manualHide = !state.manualHide
	    },
	    addUserHidden: (state, hideId) => {
	    	state.userHidden.push(hideId)
	    },
	    removeUserHidden: (state, hideId) => {
	    	let indexCat = _.indexOf(state.userHidden, hideId)
	    	if (indexCat !== -1) {
	        	state.userHidden.splice(indexCat, 1)
	        }
	    },
	    addMessage: (state, payload) => {
	    	state.messages.push(payload)
	    },
	    removeMessage: (state) => {
	    	state.messages.shift()
	    },
	    addFilter: (state, event) => {
	      let value = event.target.value
	      state.filters[value].shown = true
	      event.target.value = ''
	    },
	    removeFilter: (state, filter) => {
	      state.filters[filter].shown = false
	    },
	    changeExpansions: (state) => {
	      state.filters.expansions.value = !state.filters.expansions.value
	    },
	    updateSlider: (state, payload) => {
	      state.filters[payload.filter].value = payload.value
	    },
	    toggleFilter: (state, payload) => {
	      let indexCat = _.indexOf(state.filters[payload.filter].excluded, payload.value)
	      if (indexCat !== -1) {
	        state.filters[payload.filter].excluded.splice(indexCat, 1)
	      } else {
	        state.filters[payload.filter].excluded.push(payload.value)
	      }
	    },
	    removeFilterOption: (state, payload) => {
	      let indexCat = _.indexOf(state.filters[payload.filter].excluded, payload.value)
	      if (indexCat !== -1) {
	        state.filters[payload.filter].excluded.splice(indexCat, 1)
	      }
	      indexCat = _.indexOf(state.filters[payload.filter].active, payload.value)
	      if (indexCat !== -1) {
	        state.filters[payload.filter].active.splice(indexCat, 1)
	      }
	    },
	    categorySelection: (state, event) => {
	      let value = event.target.value
	      event.target.value = ''
	      state.filters.categories.active.push(value)
	    },
	    mechanicSelection: (state, event) => {
	      let value = event.target.value
	      event.target.value = ''
	      state.filters.mechanics.active.push(value)
	    },
	    addSelection: (state, payload) => {
	    	state.filters[payload.filterName].active.push(payload.value)
	    },
	    removeUser: (state, user) => {
	      let indexUser = _.findIndex(state.users, function(o) { return o.user == user; })
	      if (indexUser !== -1) {
	        state.users.splice(indexUser, 1)
	      }
	      if (typeof state.userGames[user] !== 'undefined') {
	        delete state.userGames[user]
	      }
	    },
	    calcGames: (state) => {
	      let games = {}
	      _.each(state.userGames, function (gamesRpt, user, users) {
	        _.each(gamesRpt.games, function (game, index, gamesRpt) {
	          games[game.id] = game
	        })
	      })
	      let gameList = _.values(games)
	      gameList.sort(function (a, b) { return a.name.localeCompare(b.name) })
	      state.games = gameList
	    },
	    addUser: (state, payload) => {
	    	state.users.push(payload)
	    },
	    userLoaded: (state, user) => {
	    	let indexUser = _.findIndex(state.users, function(o) { return o.user == user; })
	      	if (indexUser !== -1) {
	      		state.users[indexUser].loaded = true
	      	}
	    },
	    addUserGames: (state, payload) => {
	    	state.userGames[payload.user] = {games: payload.games, collection: payload.collection}
	    },
	    clearHidden: (state) => {
	    	state.hidden = []
	    }
    },
    actions: {
    	computeHidden: ({commit, getters}) => {
	      commit('clearHidden')

	      _.each(getters.games, function (game, index, games) {
	        if (getters.checkhidden(game)) {
	         	commit('addHidden', game.id)
	        }
	      })
    	},
    	addMessage: ({commit}, payload) => {
    		commit('addMessage', payload)
    		setTimeout(function(){ commit('removeMessage') }, 3000);
    	},
    	addFilter: ({dispatch, commit}, payload) => {
    		commit('addFilter', payload)
    		dispatch('computeHidden')
    	},
    	manualHide: ({dispatch, commit}, payload) => {
    		commit('manualHide', payload)
    	},
    	addUserHidden: ({dispatch, commit}, payload) => {
    		commit('addUserHidden', payload)
    		dispatch('computeHidden')
    	},
	    removeUserHidden: ({dispatch, commit}, payload) => {
    		commit('removeUserHidden', payload)
    		dispatch('computeHidden')
    	},
		removeFilter: ({dispatch, commit}, payload) => {
			commit('removeFilter', payload)
    		dispatch('computeHidden')
		},
		changeExpansions: ({commit, dispatch}, payload) => {
			commit('changeExpansions', payload)
    		dispatch('computeHidden')
		},
		updateSlider: ({commit, dispatch}, payload) => {
			commit('updateSlider', payload)
    		dispatch('computeHidden')
		},
		toggleFilter: ({commit, dispatch}, payload) => {
			commit('toggleFilter', payload)
    		dispatch('computeHidden')
		},
		removeFilterOption: ({commit, dispatch}, payload) => {
			commit('removeFilterOption', payload)
    		dispatch('computeHidden')
		},
		categorySelection: ({commit, dispatch}, payload) => {
			commit('categorySelection', payload)
    		dispatch('computeHidden')
		},
		mechanicSelection: ({commit, dispatch}, payload) => {
			commit('mechanicSelection', payload)
    		dispatch('computeHidden')
		},
		calcGames: ({commit, dispatch}, payload) => {
			commit('calcGames', payload)
    		dispatch('computeHidden')
		},
		removeUser: ({commit, dispatch}, payload) => {
			commit('removeUser', payload)
    		dispatch('calcGames')
		},
		addUser: function ({commit, dispatch} , payload) {
	      var user = payload.target.value
	      commit('addUser', { user: user, loaded: false})
	      // GET /someUrl
	      Vue.http.get('?username=' + user).then(response => {
	        // get body data
	        commit('addUserGames', { user: user, games: response.body.games, collection: response.body.collection})
	        dispatch('addMessage', { type: 'success', show: true, msg: user + ' Added Successfully!'})
	        commit('userLoaded', user)
	        dispatch('calcGames')
	      },
	      response => {
	        // error callback
	        dispatch('addMessage', { type: 'danger', show: true, msg: response.body.status +' (' + user + ')'})
	        dispatch('removeUser', user)
	      })
	      payload.target.value = ''
	    },
	    addSelection: function ({commit, dispatch} , payload) {
	    	commit('addSelection', payload)
	    	dispatch('computeHidden')
	    }
    },
    // modules: {
    //     counter
    // }
});