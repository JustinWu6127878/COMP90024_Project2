<script src="https://cdn.bootcdn.net/ajax/libs/proj4js/2.7.2/proj4.js"></script>
<template>
  <div>
    <div
      style="
        font-size:50px;
        font-weight:bold !important;
        padding:50px
        margin: 0 auto;
        text-align: center;
        color: #fff;
        font-family: Sans;
        background-image: linear-gradient(to right, #2277D2 0%, #6a11cb 90%);
      "
    >
      MELBOURNE THE MOST LIVEABLE CITY...?
    </div>
    <highcharts
      id="highchartsContainer"
      ref="chart"
      style="height: 60vh; margin-top: 5%; background-color: aliceblue"
      :constructor-type="'mapChart'"
      :options="chartOptions"
    />
  </div>
</template>
<script>
import worldMap from "@highcharts/map-collection/countries/au/au-all.topo.json";
export default {
  name: "ChartMap",
  props: {
    type: String,
    value: Array,
    text: String,
    subtext: String,
  },
  data() {
    return {
      dropdown: "",
      chartOptions: {
        chart: {
          // backgroundColor:'#aaffff',
          map: worldMap,
        },
        title: {
          text: " ",
        },
        mapNavigation: {
          enabled: true,
          buttonOptions: {
            verticalAlign: "bottom",
          },
        },
        // colorAxis: {
        //   min: 0,
        //   minColor: 'rgb(255,255,255)',
        //   maxColor: '#006cee'
        // },
        plotOptions: {
          series: {
            cursor: "pointer",
            events: {
              click: (event) => {
                if (event.point.category == "Adelaide") {
                  this.gotoAdelaide();
                }
                if (event.point.category == "Brisbane") {
                  this.gotoBrisbane();
                }
                if (event.point.category == "Melbourne") {
                  this.gotoMelbourne();
                }
                if (event.point.category == "Sydney") {
                  this.gotoSydney();
                }
              },
            },
          },
        },
        series: [
          {
            name: "Australia",
            states: {
              hover: {
                color: "#BADA55",
              },
            },
            dataLabels: {
              enabled: false,
              format: (e) => {
                return 1;
              },
            },
            allAreas: true,
            // 此处填写我们要渲染的数据，如果不填写，只有世界地图，没有悬浮颜色变化信息
            data: [],
          },
          {
            name: "Separators",
            type: "mapline",
            data: [],
            color: "#707070",
            showInLegend: false,
            enableMouseTracking: false,
          },
          {
            // Specify points using lat/lon
            type: "mappoint",
            name: "Cities",
            color: "#006cee",
            data: [
              {
                category: "Sydney",
                name: "Sydney",
                lat: -33.55,
                lon: 150.53,
              },
              {
                category: "Adelaide",
                name: "Adelaide",
                lat: -34.56,
                lon: 138.36,
              },
              {
                category: "Brisbane",
                name: "Brisbane",
                lat: -27.28,
                lon: 153.02,
              },
              {
                category: "Melbourne",
                name: "Melbourne",
                lat: -38,
                lon: 145,
              },
            ],
          },
        ],
        exporting: {
          enabled: false,
        },
        credits: {
          enabled: false,
        },
        tooltip: {
          headerFormat: "",
          pointFormat:
            "<b>{point.name}</b><br>Lat: {point.lat}, Lon: {point.lon}",
        },
        // tooltip: {
        //   backgroundColor: 'rgba(0, 0, 0, 0.7)',
        //   borderColor: 'rgba(0, 0, 0, 0.7)',
        //   style: {
        //     // 文字内容相关样式
        //     color: '#fff',
        //     fontSize: '14px',
        //     fontWeight: 'blod',
        //     fontFamily: 'Courir new'
        //   },
        //   formatter() {
        //     // 此处的this指向的是当前悬浮的pointer，return的值则为显示的数据。
        //     return 123
        //   }
        // }
      },
    };
  },
  created() {
    const that = this;
  },
  mounted() {
    this.initData();
  },
  methods: {
    handleCommand(command) {
      this.dropdown = command;
    },
    gotoAdelaide() {
      this.$router.push({
        path: "/example/adelaide",
        query: {
          index: this.dropdown,
        },
      });
    },
    gotoBrisbane() {
      this.$router.push({
        path: "/example/brisbane",
        query: {
          index: this.dropdown,
        },
      });
    },
    gotoMelbourne() {
      this.$router.push({
        path: "./example/melbourne",
        query: {
          index: this.dropdown,
        },
      });
    },
    gotoSydney() {
      this.$router.push({
        path: "./example/sydney",
        query: {
          index: this.dropdown,
        },
      });
    },
    initData() {
      const data = [];
      // worldMap.features.forEach((city, index) => {
      //   data.push([city.properties['hc-key'], index])
      // })
      this.chartOptions.series[0].data = data;
      this.chartOptions.series[1].data = data;
    },
  },
};
</script>
