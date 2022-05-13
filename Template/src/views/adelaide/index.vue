<template>
  <div class="dashboard-container">
      <div class="dashboard-intro">
        <div class="background">
          <div class="dashboard-title">
            <h1 style="color: #2277d2">{{ adelaide.name }}</h1>
            <p class="white">State:</p>
            <p style="color: #2277d2">{{ adelaide.state }}</p>
          </div>

          <div class="dashboard-overview">
            <p class="white">
              Total population:
              <b>{{ milliFormat(adelaide.pop) }} </b>
            </p>
            <p class="white">
              Born overseas:
              <b>{{ milliFormat(adelaide.over) }}</b>
            </p>
            <p class="white">
              Age 50+ percentage: <b>{{ adelaide.age50 + "%" }}</b>
            </p>
            <p class="white">
              Age 60+ percentage: <b>{{ adelaide.age65 + "%" }}</b>
            </p>
            <p class="white">
              Median annual income:
              <b>{{ "$" + milliFormat(adelaide.income) }}</b>
            </p>
          </div>
        </div>
      </div>

    <el-divider />

    <div class="dashboard-topics">
      <h2>Topics</h2>
      <p>
        These are three topics for Adelaide, SA. Explore the metrics and graphs
        behind the numbers.
      </p>
    </div>

    <div class="dashboard-collapse">
      <Collapse
        :piechart1="piechart1"
        :barchart1="barchart1"
        :barchart2="barchart2"
        :barchart3="barchart3"
        :covidRow1="covidRow1"
        :covidColumn1="covidColumn1"
        :covidRow2="covidRow2"
        :covidColumn2="covidColumn2"
        :barchart4="barchart4"
        :barchart5="barchart5"
        :barchart6="barchart6"
        :barchart7="barchart7"
        :engagementRow1="engagementRow1"
        :engagementColumn1="engagementColumn1"
        :engagementRow2="engagementRow2"
        :engagementColumn2="engagementColumn2"
        :inflationRow1="inflationRow1"
        :inflationColumn1="inflationColumn1"
        :inflationRow2="inflationRow2"
        :inflationColumn2="inflationColumn2"
        :linechart1="linechart1"
        :linechart2="linechart2"
        :wordCloudChart="wordCloudChart"
      />
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

import CityOverview from "../../class/Overview.js";

import Engagement from "../../class/Engagement.js";

import TwitterPerDay from "../../class/TwitterPerDay.js";

import Covid from "../../class/Covid.js";

import TableModel from "../../components/TableModel.vue";

import Collapse from "../../components/CollapseCom.vue";

import Piechart from "../../components/Charts/piechart.vue";

import Linechart from "@/components/Charts/linechart.vue";

import $ from "jquery";

const engagement = new Engagement(49.17, 21.2333, 28.0, 25.03);
const engagementMel = new Engagement(49.52, 27.4507, 31.5, 29.85);

const twitterperday = new TwitterPerDay("adel");

const twitterperdayMel = new TwitterPerDay('melb');

const income = [31.1, 24.8, 22.0, 3.9, 2.1, 8.5, 0.5, 6.9];
const incomeMel = [26.6, 22.5, 23.0, 5.1, 3.4, 10.6, 0.6, 8.2];

const degree = [21.2333, 8.7648, 19.2852, 42.2988, 8.4178];
const degreeMel = [27.4507, 9.4669, 15.2528, 38.618, 9.2116];

const gas = [146.4, 127.6, 114.6, 126.9, 141.6, 142.7, 120.7, 142.8];
const gasMel = [145.7, 126.3, 116.4, 128.7, 143.4, 141.1, 123.9, 147.6];
const gasNa = [148.8, 129.6, 117.8, 129.3, 144.3, 142, 123.4, 147.8];

const house = [406000, 425000, 440000, 450000, 465000, 475000];
const houseMel = [547500,555000, 610500, 665000, 732000, 712000];
const houseNa = [460000, 480000, 500000, 525000, 553000, 545000];

const covid = new Covid(39, 4934, 448, 57.9, 'adel');
const covidMel = new Covid(125, 1499, 1630, 54.9, 'melb');

const adelaide = new CityOverview(
  "Adelaide",
  "South Australia",
  1359760,
  340314,
  35.9,
  17.6,
  48043
);

export default {
  name: "Dashboard",
  computed: {
    ...mapGetters(["name"]),
  },

  components: {
    TableModel,
    Collapse,
    Piechart,
    Linechart,
  },

  data() {
    return {
      adelaide: new CityOverview(
        "Adelaide",
        "South Australia",
        1359760,
        340314,
        35.9,
        17.6,
        48043
      ),

      covidRow1: [
        {
          item: "Number of hospitals ",
          num: covid.hos,
        },
        {
          item: "Covid-19 active cases",
          num: covid.active,
        },
        {
          item: "Number of vaccination clinics",
          num: covid.clinincs,
        },
        {
          item: "Vaccination rate",
          num: covid.rate + "%",
        },
      ],
      covidColumn1: [
        {
          prop: "item",
          label: "COVID-19 data of the city",
        },
        {
          prop: "num",
          label: "",
        },
      ],

      covidRow2: [
        {
          item: "Positive comments rate: ",
          num: covid.pos + "%",
        },
        {
          item: "Negative comments rate: ",
          num: covid.neg + "%",
        },
        {
          item: "Neutral comments rate: ",
          num: covid.neu + "%",
        },
      ],
      covidColumn2: [
        {
          prop: "item",
          label: "Twitter comments in the state",
        },
        {
          prop: "num",
          label: "",
        },
      ],

      engagementRow1: [
        {
          item: "Male percentage: ",
          num: engagement.male + "%",
        },
        {
          item: "Female percentage: ",
          num: engagement.female + "%",
        },
        {
          item: "Graduate higher than bachelor degree:",
          num: engagement.edu + "%",
        },
        {
          item: "Born overseas percentage:",
          num: engagement.overper + "%",
        },
        {
          item: "Annual income > $10,000 percentage: ",
          num: engagement.income + "%",
        },
      ],
      engagementColumn1: [
        {
          prop: "item",
          label: "Engagement data of the city",
        },
        {
          prop: "num",
          label: "",
        },
      ],

      engagementRow2: [
        {
          item: twitterperday.date1,
          num: twitterperday.number1,
        },
        {
          item: twitterperday.date2,
          num: twitterperday.number2,
        },
        {
          item: twitterperday.date3,
          num: twitterperday.number3,
        },
        {
          item: twitterperday.date4,
          num: twitterperday.number4,
        },
        {
          item: twitterperday.date5,
          num: twitterperday.number5,
        },
      ],
      engagementColumn2: [
        {
          prop: "item",
          label: "Date",
        },
        {
          prop: "num",
          label: "Twitter regarding election in one day",
        },
      ],

    inflationRow1: [
        {
          item: "House Median Sale Price",
          year1: house[0],
          year2: house[1],
          year3: house[2],
          year4: house[3],
          year5: house[4],
          year6: house[5],
        },
      ],

      inflationColumn1: [
        {
          prop: "item",
          label: "Year",
        },
        {
          prop: "year1",
          label: "2014",
        },
        {
          prop: "year2",
          label: "2015",
        },
        {
          prop: "year3",
          label: "2016",
        },
        {
          prop: "year4",
          label: "2017",
        },
        {
          prop: "year5",
          label: "2018",
        },
        {
          prop: "year6",
          label: "2019",
        },
      ],

      inflationRow2: [
        {
          item: "Average petrol pump prices",
          year1: gas[0],
          year2: gas[1],
          year3: gas[2],
          year4: gas[3],
          year5: gas[4],
          year6: gas[5],
          year7: gas[6],
          year8: gas[7],
        },
      ],

      inflationColumn2: [
        {
          prop: "item",
          label: "Year",
        },
        {
          prop: "year1",
          label: "2014",
        },
        {
          prop: "year2",
          label: "2015",
        },
        {
          prop: "year3",
          label: "2016",
        },
        {
          prop: "year4",
          label: "2017",
        },
        {
          prop: "year5",
          label: "2018",
        },
         {
          prop: "year6",
          label: "2019",
        },
        {
          prop: "year7",
          label: "2020",
        }, 
        {
          prop: "year8",
          label: "2021",
        },
      ],


      piechart1: {
        title: "Twitter Comments",
        legend: { data: ["Positive", "Neutral", "Negative"] },
        data: [
          { value: covid.pos, name: "Positive" },
          { value: covid.neu, name: "Neutral" },
          { value: covid.neg, name: "Negative" },
        ],
      },

      barchart1: {
        title: "Twitter comments comparison",
        xLabel: { rotate: 0 },
        yAxis: {},
        xdata: ["Positive", "Neutral", "Negative"],
        ydata1: [covidMel.pos, covidMel.neu, covidMel.neg],
        ydata2: [covid.pos, covid.neu, covid.neg],
        legend: ["Melbourne", "Adelaide"],
      },

      barchart2: {
        title: "Medical facilities comparison",
        xdata: ["Melbourne", "Adelaide"],
        xLabel: { rotate: 0 },
        yAxis: {},
        ydata1: [covidMel.hos, covid.hos],
        ydata2: [covidMel.clinincs, covid.clinincs],
        legend: ["# of hospitals", "# of vaccination clinics"],
      },

      barchart3: {
        title: "Active cases and vaccination rate comparison",
        xLabel: { rotate: 0 },
        yAxis: [
          {
            name: "Cases",
            min: 0,
            max: 10000,
            splitNumber: 6,
          },
          {
            name: "%",
            min: 0,
            max: 100,
            splitNumber: 6,
          },
        ],
        xdata: ["Melbourne", "Adelaide"],
        ydata1: [covidMel.active, covid.active],
        ydata2: [covidMel.rate, covid.rate],
        yAxisIndex: 1,
        legend: ["Avtive cases", "Vaccination rate"],
      },

      barchart4: {
        title: "Twitter regarding policy",
        xdata: [
          twitterperday.date1,
          twitterperday.date2,
          twitterperday.date3,
          twitterperday.date4,
          twitterperday.date5,
        ],
        xLabel: { rotate: 0 },
        yAxis: {},
        ydata1: [
          twitterperday.number1,
          twitterperday.number2,
          twitterperday.number3,
          twitterperday.number4,
          twitterperday.number5,
        ],
        ydata2: [
          twitterperdayMel.number1,
          twitterperdayMel.number2,
          twitterperdayMel.number3,
          twitterperdayMel.number4,
          twitterperdayMel.number5,
        ],
        legend: ["Adelaide", "Melbourne"],
      },

      barchart5: {
        title: "Gender & Immigration rate",
        xdata: ["Male%", "Born overseas%"],
        xLabel: { rotate: 0 },
        yAxis: {},
        ydata1: [engagement.male, engagement.overper],
        ydata2: [engagementMel.male, engagementMel.overper],
        legend: ["Adelaide", "Melbourne"],
      },

      barchart6: {
        title: "Weekly persons earning",
        xdata: ["$1-499","$500-999","$1000-1999 ","$2000-2999","$3000 or more","nil income","negative income","not stated"],
        xLabel: { rotate: 30 },
        yAxis: {},
        ydata1: income,
        ydata2: incomeMel,
        legend: ["Adelaide", "Melbourne"],
      },

      barchart7: {
        title: "Highest degree",
        xdata: [
          "Bachelor or Higher",
          "Diploma",
          "Vocational",
          "No qualification",
          "Not stated",
        ],
        xLabel: { rotate: 0},
        yAxis: {},
        ydata1: degree,
        ydata2: degreeMel,
        legend: ["Adelaide", "Melbourne"],
      },

      linechart1: {
        title: "House Median Sale Price",
        legend: {
          data: ["Adelaide", "Melbourne","National"],
        },
        xtype: "category",
        xdata: ["2014","2015","2016","2017","2018","2019"],
        ydata: "($)",
        series: [
          {
            name: "Adelaide",
            type: "line",
            data: house,
          },
          {
            name: "Melbourne",
            type: "line",
            data: houseMel,
          },
          {
            name: "National",
            type: "line",
            data: houseNa,
          },
        ],
      },

       linechart2: {
        title: "Average petrol pump price",
        legend: {
          data: ["Adelaide", "Melbourne","National"],
        },
        xtype: "category",
        xdata: ["2014","2015","2016","2017","2018","2019","2020","2021"],
        ydata: "($)",
        series: [
          {
            name: "Adelaide",
            type: "line",
            data: gas,
          },
          {
            name: "Melbourne",
            type: "line",
            data: gasMel,
          },
          {
            name: "National",
            type: "line",
            data: gasNa,
          },
        ],
      },

      wordCloudChart: {
        title: "Word Cloud chart of inflation",
        legend: {},
        data: this.sendWordCloudData("adel"),
      },
    };
  },

  methods: {
    milliFormat(num) {
      return (
        num &&
        num.toString().replace(/\d+/, function (s) {
          return s.replace(/(\d)(?=(\d{3})+$)/g, "$1,");
        })
      );
    },
    sendWordCloudData(city) {
      var result;
      $.ajax({
        type:'GET',
        url:process.env.VUE_APP_BACKEND_URL+"/wordCloud_data",
        async:false,
        dataType:'json',
        success:function(data){
          result = data
        },
      });

      var json_data = result[city];
      var json_list = [];
      for (var i = 0; i < json_data.length; i++) {
        var json_dict = {
          name: json_data[i].name,
          value: json_data[i].value,
        };
        json_list.push(json_dict);
      }
        
      // console.log(json_list)
      return json_list
    },
  },
};
</script>

<style lang="scss" scoped>
// 新增开始
.white {
  color: #fff;
}
.background {
  background-color: rgba(0, 0, 0, 0.5) !important;
}
.dashboard-title{
  padding: 30px;
}
.dashboard-intro {
  margin-left: 0 !important;
  text-align: center;
  background: url(./Adelaide.jpeg);
  background-size: contain;
}
.dashboard-container[data-v-35bc3b10] {
    position: relative;
    margin: 0px !important;
    width: 100% !important;
}
.dashboard-topics{
  padding: 0 40px;
}
.dashboard-collapse{
  padding: 0 40px;
}
// 新增结束
.dashboard {
  &-container {
    position: relative;
    margin: 40px;
    width: 95%;
  }
  &-intro {
    margin-left: 15%;
    flex: 1;
    order: 2;
  }
  &-title {
    font-size: 40px;
    line-height: 46px;
    color: gray;
  }
  &-image {
    margin-left: 5%;
    line-height: 46px;
    color: gray;
    flex: 1;
    order: 1;
  }
  &-overview {
    font-size: 28px;
    line-height: 200%;
    color: black;
  }
  &-topics {
    margin: 100px 0;
    font-size: 20px;
    line-height: 24px;
    color: black;
  }

  // &-text4 {
  //   display: flex;
  //   font-size: 20px;
  //   line-height: 60px;
  //   height: 60px;
  //   color: black;
  //   justify-content: space-around;
  //   align-items: center;
  // }
  // &-text5 {
  //   margin: 0 auto;
  //   width: 90%;
  //   margin-left: 20%;
  // }
}
.dashboard-overview b {
  color: #2277d2;
}
h2 {
  color: #2277d2;
}
p {
  color: #a2a2a2;
}

// .chart-container {
//   position: relative;
//   width: 90%;
//   height: fit-content;
//   display: flex;
// }
</style>
