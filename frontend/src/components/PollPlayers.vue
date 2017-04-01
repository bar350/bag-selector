<template>
  <div class="well well-sm" v-if="filters.suggested.shown">
      <div class="row">
        <div class="col-sm-10">
          <label>(Poll) Number of Players</label>
        </div>
        <div class="col-sm-1">
          <a href="#" 
            @click.prevent="removeFilter('suggested')" 
            class="pull-right">
            <span class="glyphicon glyphicon-remove text-danger">&nbsp;</span></a>
        </div>
      </div>
      <div class="row">
        <div class="col-sm-4">
          <label>At least</label>
        </div>
        <div class="col-sm-3 form-group" style="margin:0 0;">
          <select class="form-control" 
              v-model="filters.suggested.percent"
              @change="computeHidden">
            <option v-for="n in 10" 
              :value="n*10">{{ n*10 }}%</option>
          </select>
        </div>
        <div class="col-sm-4">
          <label> of voters</label>
        </div>
      </div>
      <div class="row">
        <div class="col-sm-2">
          <label>voted</label>
        </div>
        <div class="col-sm-9 form-group" style="margin:0 0;">
          <select class="form-control" 
              v-model="filters.suggested.rate"
              @change="computeHidden">
            <option value="best">Best</option>
            <option value="bestorrec">Best or Recommended</option>
            <option value="not">Not Recommended</option>
          </select>
        </div>
      </div>
      <div class="row">
        <div class="col-sm-2">
          <label>with </label>
        </div>
        <div class="col-sm-4">
          <input type="text" class="form-control" 
              v-model="filters.suggested.players"
              @keyup="computeHidden">
        </div>
        <div class="col-sm-3">
          <label> players</label>
        </div>
      </div>
    </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
export default {
  name: 'gamelist',
  data: function() {
    return {
    }
  },
  methods: mapActions([
    'computeHidden'
  ]),
  computed: mapGetters([
    'games',
    'filters',
  ])
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
</style>
