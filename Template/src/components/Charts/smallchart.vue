<template>
  <div id="chartPie" class="pie-wrap" />
</template>

<script>
import * as echarts from 'echarts'
require('echarts/theme/macarons') // 引入主题

export default {

  props: ['chartsource'],
  data() {
    return {
      chartPie: null
    }
  },

  updated() {
    this.$nextTick(() => {
      console.log('update123')
      if (this.show) {
        this.drawPieChart()
      }
    })
  },

  mounted() {
    this.$nextTick(() => {
      this.drawPieChart()
    })
  },
  methods: {
    drawPieChart() {
      const mytextStyle = {
        color: '#333',
        fontSize: 18
      }
      const mylabel = {
        show: true,
        position: 'center',
        offset: [40, 50],
        formatter: '{d}%',
        textStyle: mytextStyle
      }
      this.chartPie = echarts.init(
        document.getElementById('chartPie'),
        'macarons'
      )

      if (this.chartsource) {
        this.chartPie = echarts.init(this.$el, 'shine')
        this.chartPie.setOption({
          title: {
            text: this.chartsource.title,
            x: 'center',
            y: 'bottom'
          },
          //   tooltip: {
          //     trigger: 'item',
          //     formatter: "{a} <br/>{b} : {c} ({d}%)",
          //   },
          // legend: {
          //   data: this.chartsource.legend.data,
          //   left: "center",
          //   top: "bottom",
          //   orient: "horizontal",
          // },
          color: ['rgb(46 199 201)', 'rgb(90 177 239)', 'rgb(182 162 222)'],
          series: [
            {
              name: 'Percentage',
              type: 'pie',
              radius: ['50%', '70%'],
              center: ['50%', '50%'],
              data: this.chartsource.data,
              //   [
              //     // {value: 335, name: '直接访问'},
              //     // {value: 310, name: '邮件营销'},
              //     // {value: 234, name: '联盟广告'},
              //     // {value: 135, name: '视频广告'},
              //     // {value: 1548, name: '搜索引擎'}

              //   ],
              //   animationEasing: 'cubicInOut',
              //   animationDuration: 2600,
              label: {
                emphasis: mylabel
              }
            }
          ]
        })
      }
    }
  }
}
</script>

<style  scope>
.pie-wrap {
  width: 50%;
  height: 50%;
}
</style>
