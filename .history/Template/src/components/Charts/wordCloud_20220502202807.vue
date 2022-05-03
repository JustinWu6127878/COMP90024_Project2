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
      let option
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