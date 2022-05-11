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
        :linechart6="linechart6"
        :linechart7="linechart7"
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

import Covid from "../../class/Covid.js";

import TableModel from "../../components/TableModel.vue";

import Collapse from "../../components/Collapse.vue";

import Piechart from "../../components/Charts/piechart.vue";

import Linechart from "@/components/Charts/linechart.vue";

import $ from 'jquery';

const enagement = new Enagement(49.52, 27.4507, 31.5, 29.85);
const enagementSyd = new Enagement(49.73, 28.3151, 34.2, 33.31);
const enagementBris = new Enagement(49.40, 22.9017, 32.3, 23.52);
const enagementAde = new Enagement(49.17, 21.2333, 28.0, 25.03);

const twitterperday = new TwitterPerDay('melb');
const twitterperdaySyd = new TwitterPerDay('syd');
const twitterperdayBris = new TwitterPerDay('bris');
const twitterperdayAde = new TwitterPerDay('adel');

const gas = [145.7, 126.3, 116.4, 128.7, 143.4, 141.1, 123.9, 147.6];

const gasNa = [148.8, 129.6, 117.8, 129.3, 144.3, 142, 123.4, 147.8];

const house = [547500,555000, 610500, 665000, 732000, 712000];

const houseNa = [460000, 480000, 500000, 525000, 553000, 545000];

const covid = new Covid(125, 20000, 1630, 95, 'melb');
const covidSyd = new Covid(132, 20000, 2045, 95, 'syd');
const covidBris = new Covid(51, 20000, 886, 95, 'bris');
const covidAde = new Covid(39, 20000, 448, 95, 'adel');

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
          num: enagement.overper + "%",
        },
        {
          item: "Person earning > $1000 per week: ",
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
        {
          item: twitterperday.date5,
          num: twitterperday.number5,
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
        title: "Persons earning per week",
        legend: {},
        data: [
          { value: enagement.income, name: "> $1000" },
          { value: 100 - enagement.income, name: "< $1000" },
        ],
      },

      linechart1: {
        title: "Positive comments vs Medical facilities",
        legend: {
          data: ["Hundreds of hospitals", "Thousands of Vaccination clinics"],
        },
        xtype: "value",
        xdata: [],
        ydata: "(Positive comments%)",
        series: [
          {
            name: "Hundreds of hospitals",
            type: "line",
            data: [
              [covid.hos/100, covid.pos],
              [covidSyd.hos/100 , covidSyd.pos],
              [covidBris.hos/100 , covidBris.pos],
              [covidAde.hos/100 , covidAde.pos],
            ],
            markPoint: {
              data: [
                {
                  name: "Hundreds of hospitals",
                  xAxis: covid.hos/100 ,
                  yAxis: covid.pos,
                  value: "Melbourne",
                },
              ],
            },
          },
          {
            name: "Thousands of Vaccination clinics",
            type: "line",
            data: [
              [covid.clinincs/1000 , covid.pos],
              [covidSyd.clinincs/1000 , covidSyd.pos],
              [covidBris.clinincs/1000 , covidBris.pos],
              [covidAde.clinincs/1000 , covidAde.pos],
            ],
            markPoint: {
              data: [
                {
                  name: "Thousands of Vaccination clinics",
                  xAxis: covid.clinincs/1000,
                  yAxis: covid.pos,
                  value: "Melbourne",
                },
              ],
            },
          },
        ],
      },

      linechart2: {
        title: "Active cases vs Vaccination rates",
        legend: {
          data: ["Vaccination rates"],
        },
        xtype: "value",
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
        xtype: "value",
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
          data: ["higher than bachelor", "Persons earning >$1000 per week"],
        },
        xdata: [],
        xtype: "value",
        ydata: "# of twitters of a day",
        series: [
          {
            name: "higher than bachelor",
            type: "line",
            data: [
              [enagement.edu, (twitterperday.number1+twitterperday.number2+twitterperday.number3+twitterperday.number4+twitterperday.number5)/5],
              [enagementSyd.edu, (twitterperdaySyd.number1+twitterperdaySyd.number2+twitterperdaySyd.number3+twitterperdaySyd.number4+twitterperdaySyd.number5)/5],
              [enagementBris.edu,(twitterperdayBris.number1+twitterperdayBris.number2+twitterperdayBris.number3+twitterperdayBris.number4+twitterperdayBris.number5)/5],
              [enagementAde.edu,(twitterperdayAde.number1+twitterperdayAde.number2+twitterperdayAde.number3+twitterperdayAde.number4+twitterperdayAde.number5)/5],
            ],
            markPoint: {
              data: [
                {
                  name: "higher than bachelor",
                  xAxis: enagement.edu,
                  yAxis: (twitterperday.number1+twitterperday.number2+twitterperday.number3+twitterperday.number4+twitterperday.number5)/5,
                  value: "Melbourne",
                },
              ],
            },
          },
          {
            name: "Persons earning >$1000 per week",
            type: "line",
            data: [
              [enagement.income, (twitterperday.number1+twitterperday.number2+twitterperday.number3+twitterperday.number4+twitterperday.number5)/5],
              [enagementSyd.income, (twitterperdaySyd.number1+twitterperdaySyd.number2+twitterperdaySyd.number3+twitterperdaySyd.number4+twitterperdaySyd.number5)/5],
              [enagementBris.income,(twitterperdayBris.number1+twitterperdayBris.number2+twitterperdayBris.number3+twitterperdayBris.number4+twitterperdayBris.number5)/5],
              [enagementAde.income,(twitterperdayAde.number1+twitterperdayAde.number2+twitterperdayAde.number3+twitterperdayAde.number4+twitterperdayAde.number5)/5],
            ],
            markPoint: {
              data: [
                {
                  name: "Persons earning >$1000 per week",
                  xAxis: enagement.income,
                  yAxis: (twitterperday.number1+twitterperday.number2+twitterperday.number3+twitterperday.number4+twitterperday.number5)/5,
                  value: "Melbourne",
                },
              ],
            },
          },
        ],
      },

      linechart5: {
        title: "Policy enagement vs gender & immigration",
        legend: {
          data: ["male percentage", "immigration percentage"],
        },
        xtype: "value",
        xdata: [],
        ydata: "(# of twitters of a day)",
        series: [
          {
            name: "male percentage",
            type: "line",
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
              [enagement.overper, twitterperday.number1],
              [enagementSyd.overper, twitterperday.number1],
              [enagementBris.overper, twitterperday.number1],
              [enagementAde.overper, twitterperday.number1],
            ],
            markPoint: {
              data: [
                {
                  name: "immigration percentage",
                  xAxis: enagement.overper,
                  yAxis: twitterperday.number1,
                  value: "Melbourne",
                },
              ],
            },
          },
        ],
      },

      linechart6: {
        title: "House Median Sale Price",
        legend: {
          data: ["Melbourne", "National"],
        },
        xtype: "category",
        xdata: ["2014","2015","2016","2017","2018","2019"],
        ydata: "($)",
        series: [
          {
            name: "Melbourne",
            type: "line",
            data: house,
          },
          {
            name: "National",
            type: "line",
            data: houseNa,
          },
        ],
      },

       linechart7: {
        title: "Average petrol pump price",
        legend: {
          data: ["Melbourne", "National"],
        },
        xtype: "category",
        xdata: ["2014","2015","2016","2017","2018","2019","2020","2021"],
        ydata: "($)",
        series: [
          {
            name: "Melbourne",
            type: "line",
            data: gas,
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
    },
    piechartData(city, senti){
      var result
      $.ajax({
        type:'GET',
        url:"http://127.0.0.1:2889/sentiData",
        async:false,
        dataType:'json',
        success:function(data){
          // console.log(data['data_line']);
          console.log(data[city][senti])
          result = data[city][senti]
        },
        error:function(){
          alert("Cannot load the data")
        }
      });      

      return result
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
