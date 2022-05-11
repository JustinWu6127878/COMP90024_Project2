<template>
  <div class="echart" :id="myChart" :style="myChartStyle"></div>
</template>

<script>
import * as echarts from "echarts";

export default {  
  data() {
    return {
      chartBar: null,
      myChartStyle: { float: "left", width: "50%", height: "400px" } //图表样式
    };
  },

  props: ["myChart","chartsource"],

  mounted() {
      this.initEcharts();
  },
  methods: {
    initEcharts() {
      // 多列柱状图
      let mulColumnZZTData = {
        title: {
          text: this.chartsource.title,
          x:"center",
        },
        xAxis: {
          data: this.chartsource.xdata,
          axisLabel: this.chartsource.xLabel,
        },
        // 图例
        legend: {
          data: this.chartsource.legend,
          y:"bottom",
          x:"center",
        },
    
        yAxis: this.chartsource.yAxis,
        //  [{
        //   name: "zuoce",
        //   min:0,
        //   max: 80000,
        //   splitNumber:6,
        // },
        // {
        //   name: "%",
        //   min:0,
        //   max: 100,
        //   splitNumber:6,
        // }],
        series: [
          {
            type: "bar" , //形状为柱状图
            data: this.chartsource.ydata1,
            name: this.chartsource.legend[0], // legend属性
            label: {
              // 柱状图上方文本标签，默认展示数值信息
              show: true,
              position: "top"
            }
          },
          {
            type: "bar", //形状为柱状图
            data: this.chartsource.ydata2,
            name: this.chartsource.legend[1], // legend属性
            yAxisIndex:this.chartsource.yAxisIndex,
            label: {
              // 柱状图上方文本标签，默认展示数值信息
              show: true,
              position: "top"
            },
          },
        ]
      };
      this.ChartBar = echarts.init(document.getElementById(this.myChart));
      this.ChartBar.setOption(mulColumnZZTData);
      //随着屏幕大小调节图表
      // window.addEventListener("resize", () => {
      //   myChart.resize();
      // });
    }
  }
};
</script>



