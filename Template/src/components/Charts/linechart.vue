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


  updated() {
    this.$nextTick(() => {
      console.log("update123");
      if (this.show) {
        this.drawPieChart();
      }
    });
  },

  mounted() {
    this.$nextTick(() => {
      setTimeout(() => {
      this.drawLineChart()
      },20)
    });
  },
  methods: {
    drawLineChart() {
      if (this.chartsource) {
        this.chartLine = echarts.init(this.$el, "shine"); // 基于准备好的dom，初始化echarts实例
        let option = {
          title: {
            text: this.chartsource.title,
            x: "center",
          },
          // tooltip : {
          //     trigger: 'axis'
          // },
          legend: {
            data: this.chartsource.legend.data,
            left: "center",
            top: "bottom",
            orient: "horizontal",
          },
          calculable: true,
          xAxis: [
            {
              type: this.chartsource.xtype,
              // boundaryGap : false,
              axisTick: {
                show: false,
              },
              data: this.chartsource.xdata,
              // nameLocation: "middle",
              // nameTextStyle:{padding: 10, 
              // },
            },
          ],
          yAxis: [
            {
              type: "value",
              axisTick: {
                show: false,
              },
              name: this.chartsource.ydata,
            },
          ],
          series: this.chartsource.series,

          // [
          //     {
          //         name:'邮件营销',
          //         type:'line',
          //         stack: '总量',
          // type: "line",
          // itemStyle: {
          //   normal: {
          //     color: "yellow",
          //   },
          // },

          // lineStyle: {
          //   color: "yellow",
          // },
          //         data:[120, 132, 101, 134, 90, 230, 210]
          //     },
          //     {
          //         name:'联盟广告',
          //         type:'line',
          //         stack: '总量',
          //         data:[220, 182, 191, 234, 290, 330, 310]
          //     },
          //     {
          //         name:'视频广告',
          //         type:'line',
          //         stack: '总量',
          //         data: [150, 232, 201, 154, 190, 330, 410]
          //     },
          //     {
          //         name:'直接访问',
          //         type:'line',
          //         stack: '总量',
          //         data:[320, 332, 301, 334, 390, 330, 320]
          //     },
          //     {
          //         name:'搜索引擎',
          //         type:'line',
          //         stack: '总量',
          //         data:[820, 932, 901, 934, 1290, 1330, 1320]
          //     }
          // ]
        };
        // 使用刚指定的配置项和数据显示图表
        this.chartLine.setOption(option);
      }
    },
  },
};
</script>
 
<style scope>
.line-wrap {
  float:left;
  width: 50%;
  height: 400px;
}
</style>