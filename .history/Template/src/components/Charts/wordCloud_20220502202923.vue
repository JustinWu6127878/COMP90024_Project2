<template>
  <!-- 为 ECharts 准备一个具备大小（宽高）的 DOM -->
  <div id="chartLine" class="line-wrap"></div>
</template>
 
<script>
import * as echarts from "echarts";
require("echarts/theme/shine"); //引入主题

export default {
  data() {
    return {
      chartLine: null,
    };
  },
  props: ["chartsource"],

  mounted() {
  
  },
  methods: {
    drawWordCloud() {
      let option = {
        tooltip: {
            show: true
        },
        series: [{
            name: 'Word',
            type: 'wordCloud',
            sizeRange: [10, 50],//文字范围
            //文本旋转范围，文本将通过rotationStep45在[-90,90]范围内随机旋转
            rotationRange: [-45, 90],
            rotationStep: 45,
            textRotation: [0, 45, 90, -45],
            //形状
            shape: 'circle',
            layoutAnimation: true,
            emphasis: {
                focus: 'self',
    
                textStyle: {
                    shadowBlur: 10,
                    shadowColor: '#333'
                }
            },
            data: JosnList
        }]
      }
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