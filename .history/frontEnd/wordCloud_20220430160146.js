// import * as echarts from 'echarts'
// import 'echarts-wordcloud';

var chartDom = document.getElementById('wordCloud');
var myChart = echarts.init(chartDom);
var option;

const originData = [
    { name: '基因编辑', value: 1228 },
    { name: '婴儿', value: 981 },
    { name: '贺建奎', value: 363 },
  ]

myChart.setOption({
    series: [{
      type: 'wordCloud',
      shape: 'diamond',
      left: 'center',
      top: 'center',
      right: null,
      bottom: null,
      width: '70%',
      height: '80%',
      sizeRange: [12, 60],
      rotationRange: [-90, 90],
      rotationStep: 45,
      gridSize: 8,
      drawOutOfBound: false,
      textStyle: {
        normal: {
          fontFamily: 'sans-serif',
          fontWeight: 'normal'
        },
        emphasis: {
          shadowBlur: 10,
          shadowColor: '#333'
        }
      },
      data
    }]
  });
