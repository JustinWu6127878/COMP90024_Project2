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
  var optionFour = {
    tooltip: {
        show: true
    },
    series: [{
        type: 'wordCloud',
        shape: 'circle',
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
  };
  var myChartFour = echarts.init(document.getElementById('wordCloud'));
  //使用制定的配置项和数据显示图表
  myChartFour.setOption(optionFour);