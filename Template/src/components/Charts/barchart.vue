<template>
  <div id="charts" style="width: 600px; height: 400px"></div>
</template>

<script>
  import * as echarts from "echarts";

  export default {
   mounted() {
    this.$nextTick(() => {
      this.drawBarChart();
    });
  },
    methods: {
      drawBarCharts() {
        let charts = this.$echarts.init(document.getElementById("main"),
        "macarons"
        );
        let option = {
          title: {
            text: "逐月消费趋势", // 标题
            subtext: "柱状图", // 副标题
          },
          xAxis: {
            type: "category",
          },
          yAxis: {
            type: "value",
          },
          color: ["#1890ff", "#52c41a", " #faad14"], // 柱状图颜色
          dataset: {
            source: [
              // 数据源
              ["1月", 1330, 666, 560],
              ["2月", 820, 760, 660],
              ["3月", 1290, 1230, 780],
              ["4月", 832, 450, 890],
              ["5月", 901, 880, 360],
              ["6月", 934, 600, 700],
            ],
          },
          series: [
            // 图标列设置
            { type: "bar", stack: "total", name: "苹果" },
            { type: "bar", stack: "total", name: "梨子" },
            { type: "bar", stack: "total", name: "桃子" },
          ],
          tooltip: {
          // 提示框组件
          }
        };
        charts.setOption(option);
      },
    },
  };
</script>

<style lang="scss" scoped></style>
