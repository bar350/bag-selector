<template>
  <div class="well well-sm">
    <div class="row">
      <label class="col-sm-10">
        {{ label }}  ({{ display }})
      </label>
      <div class="col-sm-1">
        <a href="#" 
          @click.prevent="removeFilter(filterName)" 
          class="pull-right">
          <span class="glyphicon glyphicon-remove text-danger">&nbsp;</span></a>
      </div>
    </div>
    <div class="row">
      <div class="col-sm-10 col-sm-offset-1">
        <div class="slider shor">
          <slider :slider-value="filters[filterName].value" 
            :slider-min="min" 
            :slider-max="max" 
            :slider-step="step" 
            v-on:updated="updateSlider({filter: filterName,value: $event})"></slider>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import Slider from './Slider.vue'
export default {
  name: 'filterslider',
  props: ['label', 'display', 'filterName', 'min', 'max', 'step'],
  components: { Slider },
  data: function() {
    return {
    }
  },
  methods: {
    ...mapActions([
      'removeFilter',
      'updateSlider'
    ]),
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
