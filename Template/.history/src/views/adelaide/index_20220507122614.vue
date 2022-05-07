<template>
  <div class="dashboard-container">
    <div style="display: flex">
      <div class="dashboard-intro">
        <div class="dashboard-title">
          <h1>{{ adelaide.name }}</h1>
          <p>State:</p>
          <p>{{ adelaide.state }}</p>
        </div>

        <div class="dashboard-overview">
          <p>
            Total population:
            <b>{{ milliFormat(adelaide.pop) }} </b>
          </p>
          <p>
            Born overseas:
            <b>{{ milliFormat(adelaide.over) }}</b>
          </p>
          <p>
            Age 50+ percentage: <b>{{ adelaide.age50 + "%" }}</b>
          </p>
          <p>
            Age 60+ percentage: <b>{{ adelaide.age65 + "%" }}</b>
          </p>
          <p>
            Median annual income:
            <b>{{ "$" + milliFormat(adelaide.income) }}</b>
          </p>
        </div>
      </div>

      <div class="dashboard-image">
        <img src="./Adelaide.jpeg" height="700px" width="400px" />
      </div>
    </div>

    <el-divider></el-divider>

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

import Collapse from "../../components/CollapseCom.vue";

import Piechart from "../../components/Charts/piechart.vue";

import Linechart from "@/components/Charts/linechart.vue";

import $ from 'jquery';


const enagement = new Enagement(49.5, 30, 25);
const enagementMel = new Enagement(49.5, 30, 25, 30);

const twitterperday = new TwitterPerDay(
  ["29/04", 12345],
  ["29/04", 12345],
  ["29/04", 12345],
  ["29/04", 12345],
  ["29/04", 12345],
  ["29/04", 12345]
);

const twitterperdayMel = new TwitterPerDay(
  ["29/04/2022", 12345],
  ["29/04/2022", 12345],
  ["29/04/2022", 12345],
  ["29/04/2022", 12345],
  ["29/04/2022", 12345],
  ["29/04/2022", 12345]
);

const income = ["23.8","23.6","24.4","28.2"]
const incomeMel = [24.4,24.8,25.4,25.5];

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

const covid = new Covid(5000, 20000, 300, 95, 'adel', 'pos');
const covidMel = new Covid(5000, 20000, 300, 95, 'melb');

const adelaide = new CityOverview(
  "Adelaide",
  "South Australia",
  5312163,
  1769610,
  30.4,
  14.0,
  51191
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
      adelaide: new CityOverview(
        "Adelaide",
        "South Australia",
        5312163,
        1769610,
        30.4,
        14.0,
        51191
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
          { value: covid.pos, name: "Positive" },
          { value: covid.neu, name: "Neutral" },
          { value: covid.neg, name: "Negative" },
        ],
      },

      barchart1: {
        title: "Twitter comments comparison",
        xLabel: {rotate:0},
        yAxis: {},
        xdata: ["Positive", "Neutral", "Negative"],
        ydata1: [this.piechartData('melb', 'pos'), this.piechartData('melb', 'neu'), this.piechartData('melb', 'neg')],
        ydata2: [this.piechartData('adel', 'pos'), this.piechartData('adel', 'neu'), this.piechartData('adel', 'neg')],
        legend: ["Melbourne", "Adelaide"],
      },

      barchart2: {
        title: "Medical facilities comparison",
        xdata: ["Melbourne", "Adelaide"],
        xLabel: {rotate:0},
        yAxis: {},
        ydata1: [covidMel.hos / 1000, covid.hos / 1000],
        ydata2: [covidMel.clinincs / 100, covid.clinincs / 100],
        legend: ["Thousand of hospitals", "Hundred of vaccination clinics"],
      },

      barchart3: {
        title: "Active cases and vaccination rate comparison",
        xLabel: {rotate:0},
        yAxis: [
          {
            name: "Cases",
            min: 0,
            max: 80000,
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
        ydata1: [covidMel.active, covidMel.active],
        ydata2: [covid.rate, covid.rate],
        yAxisIndex: 1,
        legend: ["Avtive cases", "Vaccination rate"],
      },

      barchart4: {
        title: "Twitter regarding policy",
        xdata: [twitterperday.date1,twitterperday.date2,twitterperday.date3,twitterperday.date4,twitterperday.date5],
        xLabel: {rotate:0},
        yAxis: {},
        ydata1: [twitterperday.number1, twitterperday.number2,twitterperday.number3,twitterperday.number4,twitterperday.number5],
        ydata2: [twitterperdayMel.number1, twitterperdayMel.number2,twitterperdayMel.number3,twitterperdayMel.number4,twitterperdayMel.number5],
        legend: ["Adelaide", "Melbourne"],
      },
    
     barchart5: {
        title: "Gender & Immigration rate",
        xdata: ["Male%","Born overseas%"],
        xLabel: {rotate:0},
        yAxis: {},
        ydata1: [enagement.male,adelaide.overper*100],
        ydata2: [enagementMel.male,enagementMel.overper],
        legend: ["Adelaide", "Melbourne"],
      },

      barchart6: {
        title: "Total income quartile",
        xdata: ["Lowest","Second","Third","Highest"],
        xLabel: {rotate:0},
        yAxis: {},
        ydata1: [income],
        ydata2: [incomeMel],
        legend: ["Adelaide", "Melbourne"],
      },

      barchart7: {
        title: "Highest degree",
        xdata: ["Postgraduate","Diploma","Bachelor","Certificate","Non-school"],
        xLabel: {rotate:40},
        yAxis: {},
        ydata1: [income],
        ydata2: [incomeMel],
        legend: ["Adelaide", "Melbourne"],
      },

      wordCloudChart: {
        title: "Word Cloud chart of inflation",
        legend: {},
        data: this.sendWordCloudData('adel'),
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
// .chart-container {
//   position: relative;
//   width: 90%;
//   height: fit-content;
//   display: flex;
// }
</style>
