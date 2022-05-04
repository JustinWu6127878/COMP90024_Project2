<template>
  <!-- 为 ECharts 准备一个具备大小（宽高）的 DOM -->
  <div id="chartWordCloud" class="line-wrap"></div>
</template>
 
<script>
import * as echarts from "echarts";
import "echarts-wordcloud/dist/echarts-wordcloud";
require("echarts/theme/shine"); //引入主题

console.log("Hello")

// $.ajax({

//   type:'GET',
//   url:"http://127.0.0.1:2889/wordCloud_data",
//   dataType:'json',
//   success:function(data){
//     // console.log(data['data_line']);
//     console.log(data);

//     }
// });


export default {
  data() {
    return {
      ChartWordCloud: null,
    };
  },
  
  props: ["chartsource"],

  mounted() {
    this.drawWordCloud()
    // this.debug()
    
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
    },

    debug(){
      console.log("Hello")
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