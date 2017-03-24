<template>
  <div :id="sliderId"></div>
</template>

<script>
export default {
  name: 'slider',
  props: ['sliderValue', 'sliderMin', 'sliderMax', 'sliderStep'],
  data: function () {
      return {
          sliderId: this.uuid4(),
      }
  },
  mounted: function () {
      var slider = document.getElementById(this.sliderId)
      noUiSlider.create(slider, {
          start: this.sliderValue,
          step: Number(this.sliderStep),
          range: {
              'min': [this.sliderMin],
              'max': [this.sliderMax]
          },
          tooltips: [true, true],
          format: {
              to: function (value) {
                  if(typeof(slider.noUiSlider) !== 'undefined') {
                      var step = slider.noUiSlider.steps()[0][1];
                      if(step % 1 != 0) {
                          return value;
                      } else {
                          return Math.ceil(value);
                      }
                  } else {
                      return value;
                  }
              },
              from: function (value) {
                  if(typeof(slider.noUiSlider) !== 'undefined') {
                      var step = slider.noUiSlider.steps()[0][1];
                      if(step % 1 != 0) {
                          return value;
                      } else {
                          return Math.floor(value);
                      }
                  } else {
                      return value;
                  }
              }
          }
      })
      slider.noUiSlider.on('update', this.updateValue);
  },
  methods: {
      updateValue: function (value) {
          this.$emit('updated', value)
      },
      uuid4: function () {
          return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
              var r = Math.random() * 16 | 0, v = c === 'x' ? r : (r & 0x3 | 0x8)
              return v.toString(16)
          })
      },
  }
}
</script>

<style>
</style>
