<template>
  <!-- 为 ECharts 准备一个具备大小（宽高）的 DOM -->
  <div id="chartWordCloud" class="line-wrap" />
</template>
 
<script>
import * as echarts from "echarts";
import "echarts-wordcloud/dist/echarts-wordcloud";
import $ from 'jquery';
require("echarts/theme/shine"); //引入主题

console.log("Hello")

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
          x:"center",
          textStyle: { // 主标题文本样式{"fontSize": 18,"fontWeight": "bolder","color": "#333"}
                     fontFamily: 'Arial',
                     fontSize: 24,
                     fontStyle: 'normal',
                     fontWeight: 'bold',
                     color:'#2277D2'
                 }
        },
        tooltip: {
            show: true
        },
        series: [{
            name: 'WordCloud',
            type: 'wordCloud',
            shape: 'circle',
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
    },

    debug(){
      console.log("Hello")
    },


  }
};
</script>
 
<style scope>
.line-wrap {
  width:100%;
  height: 400px;
}
</style>