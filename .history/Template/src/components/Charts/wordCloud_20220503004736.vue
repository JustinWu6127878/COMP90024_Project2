<template>
  <!-- 为 ECharts 准备一个具备大小（宽高）的 DOM -->
  <div id="chartWordCloud" class="line-wrap"></div>
</template>
 
<script>
import * as echarts from "echarts";
import "echarts-wordcloud/dist/echarts-wordcloud";
require("echarts/theme/shine"); //引入主题

$.ajax({

  type:'GET',
  url:"http://127.0.0.1:2889/chart_data",
  dataType:'json',
  success:function(data){
    console.log(data['data_line']);
    // console.log(data);
      var chartDom = document.getElementById('hp_lineChart');
      var myChart = echarts.init(chartDom);
      var option;

      option = {
      //   title: {
      //     text: 'House Price from 2017 to 2021 in Melbourne'
      //   },
        tooltip: {
          trigger: 'axis'
        },
        xAxis: {
          type: 'category',
          data: ['2017', '2018', '2019', '2020', '2021']
        },
        yAxis: {
          type: 'value'
        },
        series: [
          {
           /* data: [
              1752534.3599999999, 1676329.3, 1651656.94, 1770922.6199999999,
              2021429.28
            ],*/
            data: data['data_line'],
            type: 'line'
          }
        ]
      };

      option && myChart.setOption(option);
    }
});


export default {
  data() {
    return {
      ChartWordCloud: null,
    };
  },
  
  props: ["chartsource"],

  mounted() {
    this.drawWordCloud()
  },
  methods: {
    drawWordCloud() {

      let option = {
        title:{
          text: this.chartsource.title,
          x:"center"
        },
        tooltip: {
            show: true
        },
        series: [{
            name: 'WordCloud',
            type: 'wordCloud',
            sizeRange: [10, 50],//文字范围
            //文本旋转范围，文本将通过rotationStep45在[-90,90]范围内随机旋转
            rotationRange: [-45, 90],
            rotationStep: 45,
            textRotation: [0, 45, 90, -45],
            //形状
            shape: 'circle',
            layoutAnimation: true,
            textStyle:{
              // color: "#03b1fc"
            },
            emphasis: {
                focus: 'self',
                textStyle: {
                    shadowBlur: 10,
                    shadowColor: '#333'
                }
            },
            data: this.chartsource.data
        }]
      };
      this.ChartWordCloud = echarts.init(this.$el);
      this.ChartWordCloud.setOption(option)
    }
  }
};
</script>
 
<style scope>
.line-wrap {
  width: 50%;
  height: 400px;
}
</style>