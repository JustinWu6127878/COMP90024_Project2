<template>
  <div class="dashboard-container">
    <div style="display: flex">
      <div class="dashboard-intro">
        <div class="dashboard-title">
          <h1>{{ melbourne.name }}</h1>
          <p>State: </p>
          <p> {{ melbourne.state }}</p>
        </div>

        <div class="dashboard-overview">
          <p>
            Total population:
            <b>{{ milliFormat(melbourne.pop) }} </b>
          </p>
          <p>
            Born overseas:
            <b>{{ milliFormat(melbourne.over) }}</b>
          </p>
          <p>
            Age 50+ percentage: <b>{{ melbourne.age50 + "%" }}</b>
          </p>
          <p>
            Age 60+ percentage: <b>{{ melbourne.age65 + "%" }}</b>
          </p>
          <p>
            Median annual income:
            <b>{{ "$" + milliFormat(melbourne.income) }}</b>
          </p>
        </div>
      </div>

      <div class="dashboard-image">
        <img src="./Melbourne.jpeg" height="700px" width="400px"/>
      </div>
    </div>

    <el-divider></el-divider>

    <div class="dashboard-topics">
      <h2>Topics</h2>
      <p>
        These are three topics for Melbourne, VIC. Explore the metrics and
        graphs behind the numbers.
      </p>
    </div>

    <div class="dashboard-collapse">
      <Collapse
        :piechart1="piechart1"
        :piechart2="piechart2"
        :piechart3="piechart3"
        :piechart4="piechart4"
        :piechart5="piechart5"
        :linechart1="linechart1"
        :linechart2="linechart2"
        :linechart3="linechart3"
        :linechart4="linechart4"
        :linechart5="linechart5"
        :covidRow1="covidRow1"
        :covidColumn1="covidColumn1"
        :covidRow2="covidRow2"
        :covidColumn2="covidColumn2"
        :enagementRow1="enagementRow1"
        :enagementColumn1="enagementColumn1"
        :enagementRow2="enagementRow2"
        :enagementColumn2="enagementColumn2"
        :inflationRow1="inflationRow1"
        :inflationColumn1="inflationColumn1"
        :inflationRow2="inflationRow2"
        :inflationColumn2="inflationColumn2"
        :wordCloudChart="wordCloudChart"
      />
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

import CityOverview from "../../class/Overview.js";

import Enagement from "../../class/Enagement.js";

import TwitterPerDay from "../../class/TwitterPerDay.js";

import Price from "../../class/Price.js";

import Covid from "../../class/Covid.js";

import TableModel from "../../components/TableModel.vue";

import Collapse from "../../components/Collapse.vue";

import Piechart from "../../components/Charts/piechart.vue";

import Linechart from "@/components/Charts/linechart.vue";

import $ from 'jquery';

const enagement = new Enagement(49.5, 30, 25);
const enagementSyd = new Enagement(49.5, 30, 25, 30);
const enagementBris = new Enagement(49.5, 30, 25,30);
const enagementAde = new Enagement(49.5, 30, 25,30);

const twitterperday = new TwitterPerDay(
  ["29/04/2022", 12345],
  ["29/04/2022", 12345],
  ["29/04/2022", 12345],
  ["29/04/2022", 12345],
  ["29/04/2022", 12345],
  ["29/04/2022", 12345]
);
const twitterperdaySyd = new TwitterPerDay(
  ["29/04/2022", 12345],
  ["29/04/2022", 12345],
  ["29/04/2022", 12345],
  ["29/04/2022", 12345],
  ["29/04/2022", 12345],
  ["29/04/2022", 12345]
);
const twitterperdayBris = new TwitterPerDay(
  ["29/04/2022", 12345],
  ["29/04/2022", 12345],
  ["29/04/2022", 12345],
  ["29/04/2022", 12345],
  ["29/04/2022", 12345],
  ["29/04/2022", 12345]
);
const twitterperdayAde = new TwitterPerDay(
  ["29/04/2022", 12345],
  ["29/04/2022", 12345],
  ["29/04/2022", 12345],
  ["29/04/2022", 12345],
  ["29/04/2022", 12345],
  ["29/04/2022", 12345]
);

const gas = new Price(
  ["2022", 12345],
  ["2021", 12345],
  ["2020", 12345],
  ["2019", 12345],
  ["2018", 12345],
  ["2017", 12345]
);

const house = new Price(
  ["2022", 12345],
  ["2021", 12345],
  ["2020", 12345],
  ["2019", 12345],
  ["2018", 12345],
  ["2017", 12345]
);

const covid = new Covid(5000, 20000, 300, 95, 33, 33, 33);
const covidSyd = new Covid(5000, 20000, 300, 95, 33, 33, 33);
const covidBris = new Covid(5000, 20000, 300, 95, 33, 33, 33);
const covidAde = new Covid(5000, 20000, 300, 95, 33, 33, 33);

const melbourne = new CityOverview(
  "Melbourne",
  "Victoria",
  5078193,
  1515597,
  30,
  13.8,
  49260
);


export default {
  name: "dashboard",
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
      melbourne: new CityOverview(
        "Melbourne",
        "Victoria",
        5078193,
        1515597,
        30,
        13.8,
        49260
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

      enagementRow1: [
        {
          item: "Male percentage: ",
          num: enagement.male + "%",
        },
        {
          item: "Female percentage: ",
          num: enagement.female + "%",
        },
        {
          item: "Graduate higher than bachelor degree:",
          num: enagement.edu + "%",
        },
        {
          item: "Born overseas percentage:",
          num: enagement.over + "%",
        },
        {
          item: "Annual income > $10,000 percentage: ",
          num: enagement.income + "%",
        },
      ],
      enagementColumn1: [
        {
          prop: "item",
          label: "Enagement data of the city",
        },
        {
          prop: "num",
          label: "",
        },
      ],

      enagementRow2: [
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
      ],
      enagementColumn2: [
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
          item: "Gas price",
          year1: gas.number1,
          year2: gas.number2,
          year3: gas.number3,
          year4: gas.number4,
          year5: gas.number5,
        },
        {
          item: "House price",
          year1: house.number1,
          year2: house.number2,
          year3: house.number3,
          year4: house.number4,
          year5: house.number5,
        },
      ],

      inflationColumn1: [
        {
          prop: "item",
          label: "Year",
        },
        {
          prop: "year1",
          label: gas.year1,
        },
        {
          prop: "year2",
          label: gas.year2,
        },
        {
          prop: "year3",
          label: gas.year3,
        },
        {
          prop: "year4",
          label: gas.year4,
        },
        {
          prop: "year5",
          label: gas.year5,
        },

      ],

      piechart1: {
        title: "Twitter Comments",
        legend: { data: ["Positive", "Neutral", "Negative"] },
        data: [
          { value: this.piechartData('melb', 'pos'), name: "Positive" },
          { value: this.piechartData('meln', 'pos'), name: "Neutral" },
          { value: this.piechartData('adel', 'pos'), name: "Negative" },
        ],
      },

      piechart2: {
        title: "Gender",
        legend: {},
        data: [
          { value: enagement.male, name: "Male" },
          { value: enagement.female, name: "Female" },
        ],
      },

      piechart3: {
        title: "Born overseas percentage",
        legend: {},
        data: [
          { value: melbourne.overper, name: "Overseas" },
          { value: 1 - melbourne.overper, name: "Local" },
        ],
      },

      piechart4: {
        title: "Highest degree",
        legend: {},
        data: [
          { value: enagement.edu, name: "Higher than bechalor" },
          { value: 100 - enagement.edu, name: "Lower than bechalor" },
        ],
      },
      piechart5: {
        title: "Annual income",
        legend: {},
        data: [
          { value: enagement.income, name: "> $100,000" },
          { value: 100 - enagement.income, name: "< $100,000" },
        ],
      },

      linechart1: {
        title: "Positive comments vs Medical facilities",
        legend: {
          data: ["Thousand hospitals", "Hundred Vaccination clinics"],
        },
        xdata: [],
        ydata: "(Positive comments%)",
        series: [
          {
            name: "Thousand hospitals",
            type: "line",
            // itemStyle:{
            //   normal:{
            //     color: "yellow",
            //   }
            // },

            // lineStyle:{
            //     color: "yellow",
            // },
            data: [
              [covid.hos / 1000, covid.pos],
              [covidSyd.hos / 1000, covidSyd.pos],
              [covidBris.hos / 1000, covidBris.pos],
              [covidAde.hos / 1000, covidAde.pos],
            ],
            markPoint: {
              data: [
                {
                  name: "Thousand hospitals",
                  xAxis: covid.hos / 1000,
                  yAxis: covid.pos,
                  value: "Melbourne",
                },
              ],
            },
          },
          {
            name: "Hundred Vaccination clinics",
            type: "line",
            data: [
              [covid.clinincs / 100, covid.pos],
              [covidSyd.clinincs / 100, covidSyd.pos],
              [covidBris.clinincs / 100, covidBris.pos],
              [covidAde.clinincs / 100, covidAde.pos],
            ],
            markPoint: {
              data: [
                {
                  name: "Hundred Vaccination clinics",
                  xAxis: covid.clinincs / 100,
                  yAxis: covid.pos,
                  value: "Melbourne",
                },
              ],
            },
          },
          // {
          //   name: "Vacci",
          //   type: "line",
          //   data: [
          //     [220, 40],
          //     [182, 30],
          //     [191, 20],
          //     [234, 30],
          //   ],
          // },
          // {
          //   name: "Active",
          //   type: "line",
          //   data: [
          //     [150, 33],
          //     [232, 11],
          //     [201, 45],
          //     [154, 50],
          //   ],
          // },
          // {
          //   name: "Rate",
          //   type: "line",
          //   data: [
          //     [320, 30],
          //     [332, 34],
          //     [301, 25],
          //     [334, 35],
          //   ],
          // },
        ],
      },

      linechart2: {
        title: "Active cases vs Vaccination rates",
        legend: {
          data: ["Vaccination rates"],
        },
        xdata: [],
        ydata: "Active cases",
        series: [
          {
            name: "Vaccination rates",
            type: "line",
            itemStyle: {
              normal: {
                color: "green",
              },
            },

            lineStyle: {
              color: "green",
            },
            data: [
              [covid.rate, covid.active],
              [covidSyd.rate, covidSyd.active],
              [covidBris.rate, covidBris.active],
              [covidAde.rate, covidAde.active],
            ],
            markPoint: {
              data: [
                {
                  name: "Vaccination rates",
                  xAxis: covid.rate,
                  yAxis: covid.active,
                  value: "Melbourne",
                },
              ],
            },
          },
        ],
      },

      linechart3: {
        title: "Positive comments vs Active cases",
        legend: {
          data: ["Active cases in the state"],
        },
        xdata: [],
        ydata: "(Positive %)",
        series: [
          {
            name: "Active cases in the state",
            type: "line",
            itemStyle: {
              normal: {
                color: "purple",
              },
            },

            lineStyle: {
              color: "purple",
            },
            data: [
              [covid.active, covid.pos],
              [covidSyd.active, covidSyd.pos],
              [covidBris.active, covidBris.pos],
              [covidAde.active, covidAde.pos],
            ],
            markPoint: {
              data: [
                {
                  name: "Active cases in the state",
                  xAxis: covid.active,
                  yAxis: covid.pos,
                  value: "Melbourne",
                },
              ],
            },
          },
        ],
      },

      linechart4: {
        title: "Policy enagement vs education level & income level",
        legend: {
          data: ["higher than bachelor", "annual income >$100,000"],
        },
        xdata: [],
        ydata: "# of twitters of a day",
        series: [
          {
            name: "higher than bachelor",
            type: "line",
            data: [
              [enagement.edu, twitterperday.number1],
              [enagementSyd.edu, twitterperdaySyd.number1],
              [enagementBris.edu, twitterperdayBris.number1],
              [enagementAde.edu, twitterperdayAde.number1],
            ],
            markPoint: {
              data: [
                {
                  name: "higher than bachelor",
                  xAxis: enagement.edu,
                  yAxis: twitterperday.number1,
                  value: "Melbourne",
                },
              ],
            },
          },
          {
            name: "annual income >$100,000",
            type: "line",
            data: [
              [enagement.income, twitterperday.number1],
              [enagementSyd.income, twitterperdaySyd.number1],
              [enagementBris.income, twitterperdayBris.number1],
              [enagementAde.income, twitterperdayAde.number1],
            ],
            markPoint: {
              data: [
                {
                  name: "annual income >$100,000",
                  xAxis: enagement.income,
                  yAxis: twitterperday.number1,
                  value: "Melbourne",
                },
              ],
            },
          },
          // {
          //   name: "Immi",
          //   type: "line",
          //   data: [
          //     [33, 12234],
          //     [23, 12356],
          //     [45, 12453],
          //     [30, 14352],
          //   ],
          // },
          // {
          //   name: "Income",
          //   type: "line",
          //   data: [
          //     [30, 12234],
          //     [34, 12356],
          //     [25, 12453],
          //     [35, 14352],
          //   ],
          // },
        ],
      },

      linechart5: {
        title: "Policy enagement vs gender & immigration",
        legend: {
          data: ["male percentage", "immigration percentage"],
        },
        xdata: [],
        ydata: "(# of twitters of a day)",
        series: [
          {
            name: "male percentage",
            type: "line",
            // itemStyle:{
            //   normal:{
            //     color: "yellow",
            //   }
            // },

            // lineStyle:{
            //     color: "yellow",
            // },
            data: [
              [enagement.male, twitterperday.number1],
              [enagementSyd.male, twitterperdaySyd.number1],
              [enagementBris.male, twitterperdayBris.number1],
              [enagementAde.male, twitterperdayAde.number1],
            ],
            markPoint: {
              data: [
                {
                  name: "male percentage",
                  xAxis: enagement.male,
                  yAxis: twitterperday.number1,
                  value: "Melbourne",
                },
              ],
            },
          },
          {
            name: "immigration percentage",
            type: "line",
            data: [
              [melbourne.overper, twitterperday.number1],
              [enagementSyd.overper, twitterperday.number1],
              [enagementBris.overper, twitterperday.number1],
              [enagementAde.overper, twitterperday.number1],
            ],
            markPoint: {
              data: [
                {
                  name: "immigration percentage",
                  xAxis: melbourne.overper,
                  yAxis: twitterperday.number1,
                  value: "Melbourne",
                },
              ],
            },
          },
        ],
      },

      wordCloudChart: {
        title: "Word Cloud chart of inflation",
        legend: {},
        data: this.sendWordCloudData('melb'),
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
    sendWordCloudData(city){
      var result
      $.ajax({
        type:'GET',
        url:"http://127.0.0.1:2889/wordCloud_data",
        async:false,
        dataType:'json',
        success:function(data){
          // console.log(data['data_line']);
          console.log(data)
          result = data
        },
        error:function(){
          alert("Cannot load the data")
        }
      });

      var json_data = result[city]
      var json_list = []
      for (var i=0; i < json_data.length; i++){
        var json_dict = {
          name: json_data[i].name,
          value: json_data[i].value,
        }
        json_list.push(json_dict)
      }
        
      console.log(json_list)
      return json_list
    }
  },

  
};
</script>


<style lang="scss" scoped>
.dashboard {
  &-container {
    position: relative;
    margin: 40px;
    width: 85%;
  }
  &-intro {
    margin-left:15%;
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
// .chart-container {
//   position: relative;
//   width: 90%;
//   height: fit-content;
//   display: flex;
// }
</style>
