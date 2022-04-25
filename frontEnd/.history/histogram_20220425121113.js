option = {
    title:{
      text: "Comparison of sentiment in major cities"
    },
    xAxis: {
      type: 'category',
      data: ['Melbourne', 'Sydney', 'Perth', 'Adelaide', 'Brisbane']
    },
    yAxis: {
      type: 'value'
    },
    series: [
      {
        data: [
          {
            value:120,
            itemStyle: {
              color: '#a90000'
            }
          },
          150,
          80,
          70,
          110,
          130
        ],
        type: 'bar'
      }
    ]
  };