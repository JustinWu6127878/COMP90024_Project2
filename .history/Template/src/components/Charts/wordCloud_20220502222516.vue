<template>
  <!-- 为 ECharts 准备一个具备大小（宽高）的 DOM -->
  <div id="chartWordCloud" class="line-wrap"></div>
</template>
 
<script>
import * as echarts from "echarts";
import "echarts-wordcloud/dist/echarts-wordcloud";
require("echarts/theme/shine"); //引入主题

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

      var JosnList = [
          {name: "龙头镇", value: "111"},
          {name: "大埔镇", value: "222"},
          {name: "太平镇", value: "458"},
          {name: "沙埔镇", value: "445"},
          {name: "东泉镇", value: "456"},
          {name: "凤山镇", value: "647"},
          {name: "六塘镇", value: "189"},
          {name: "冲脉镇", value: "864"},
          {name: "寨隆镇", value: "652"},
      ];

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
            text
            emphasis: {
                focus: 'self',
                textStyle: {
                    shadowBlur: 10,
                    shadowColor: '#333'
                }
            },
            data: JosnList
        }]
      };
      this.ChartWordCloud = echarts.init(this.$el, "shine");
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