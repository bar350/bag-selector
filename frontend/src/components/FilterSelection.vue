<template>
  <div class="well well-sm">
    <div class="row">
      <div class="col-sm-10 form-group" style="margin:0 0;">
        <select class="form-control" @change="selectVal">
            <option value="" disabled selected>Choose a {{displayName}}</option>
            <option :value="val" 
                v-for="val in filterOpts">{{ val }}</option>
        </select>
      </div>
      <div class="col-sm-1">
        <a href="#" 
          @click.prevent="removeFilter(filterName)" 
          class="pull-right">
          <span class="glyphicon glyphicon-remove text-danger">&nbsp;</span></a>
      </div>
    </div>
    <div class="row" v-for="val in filters[filterName].active">
      <label class="col-sm-5">{{ val }}</label>
      <div class="togglebutton col-sm-4">
        <label>
            <input type="checkbox" checked="" @change="toggleFilter({filter: filterName, value: val})">
            <span class="toggle"></span>
        </label>
      </div>
      <div class="col-sm-2">
        <a href="#" @click.prevent="removeFilterOption({filter: filterName, value: val})">
            <span class="glyphicon glyphicon-remove text-danger">&nbsp;</span></a>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
export default {
  name: 'filterselection',
  props: ['displayName', 'filterName', 'filterOpts'],
  data: function() {
    return {
    }
  },
  methods: {
    ...mapActions([
      'removeFilter',
      'removeFilterOption',
      'toggleFilter',
      'addSelection',
    ]),
    selectVal: function(event) {
      let value = event.target.value
      event.target.value = ''
      this.addSelection({ value: value, filterName: this.filterName})
    }
  },
  computed: {
    ...mapGetters([
      'filters'
    ]),
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
</style>
