<template>
  <div class="dashboard-container">
    <div style="display: flex">
      <div class="dashboard-intro">
        <div class="dashboard-title">
          <h1>{{ melbourne.name }}</h1>
          <p>State: {{ melbourne.state }}</p>
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
        <img src="./Melbourne.jpeg" height="700px" />
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
        :linechart1="linechart1"
        :linechart2="linechart2"
        :covidRow1="covidRow1"
        :covidColumn1="covidColumn1"
        :covidRow2="covidRow2"
        :covidColumn2="covidColumn2"
        :piechart2="piechart2"
        :linechart3="linechart3"
        :linechart4="linechart4"
        :enagementRow1="enagementRow1"
        :enagementColumn1="enagementColumn1"
        :enagementRow2="enagementRow2"
        :enagementColumn2="enagementColumn2"
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

const enagement = new Enagement(49.5, 30, 29.84, 25);
const twitterperday = new TwitterPerDay(
  ["29/04/2022", 12345],
  ["29/04/2022", 12345],
  ["29/04/2022", 12345],
  ["29/04/2022", 12345],
  ["29/04/2022", 12345],
  ["29/04/2022", 12345]
);
const covid = new Covid (5000,20000,300,95,33,33,33);

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
          num: covid.rate+"%",
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
          num: covid.pos +"%",
        },
        {
          item: "Negative comments rate: ",
          num: covid.neg +"%",
        },
        {
          item: "Neutral comments rate: ",
          num: covid.neu +"%",
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
        {
          item: "03/05/2022",
          num: "12345",
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

      piechart1: {
        title: "Twitter Comments",
        legend: { data: ["Positive", "Negative"] },
        data: [
          { value: covid.pos, name: "Positive" },
          { value: covid.neu, name: "Nutrual" },
          { value: covid.neu, name: "Negative" },
        ],
      },

      piechart2: {
        title: "Gender",
        legend: { data: ["Male", "Female"] },
        data: [
          { value: enagement.male, name: "Male" },
          { value: enagement.female, name: "Female" },
        ],
      },

      linechart1: {
        title: "Positive comments vs Hospital numbers",
        legend: {
          data: ["Hospital Numbers in the state"],
        },
        xdata: [],
        ydata: "(Positive %)",
        series: [
          {
            name: "Hospital Numbers in the state",
            type: "line",
            data: [
              [covid.hos, covid.pos],
              [4000,30],
              [5000,40],
              [3000,50],
            ],
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
        title: "Positive comments vs Vaccination clinics number",
        legend: {
          data: ["Vaccination clinics Numbers in the state"],
        },
        xdata: [],
        ydata: "(Positive %)",
        series: [
          {
            name: "Vaccination clinics Numbers in the state",
            type: "line",
            data: [
              [covid.clinincs, covid.pos],
              [400,30],
              [500,40],
              [300,50],
            ],
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
            data: [
              [covid.active, covid.pos],
              [10000,30],
              [12300,40],
              [31200,50],
            ],
          },
        ],
      },

      linechart4: {
        title: "Enagement",
        legend: {
          data: ["Gender", "Edu", "Immi", "Income"],
        },
        xdata: [10, 20, 30, 40, 50, 60, 70, 80, 90],
        ydata: "# of twitters of a day",
        series: [
          {
            name: "Gender",
            type: "line",
            data: [
              [49.5, 12234],
              [49.6, 12356],
              [48.5, 12453],
              [49.0, 14352],
            ],
          },
          {
            name: "Edu",
            type: "line",
            data: [
              [40, 12234],
              [30, 12356],
              [20, 12453],
              [25, 14352],
            ],
          },
          {
            name: "Immi",
            type: "line",
            data: [
              [33, 12234],
              [23, 12356],
              [45, 12453],
              [30, 14352],
            ],
          },
          {
            name: "Income",
            type: "line",
            data: [
              [30, 12234],
              [34, 12356],
              [25, 12453],
              [35, 14352],
            ],
          },
        ],
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
    flex: 1;
    order: 2;
  }
  &-title {
    font-size: 40px;
    line-height: 46px;
    color: gray;
  }
  &-image {
    line-height: 46px;
    color: gray;
    flex: 2;
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

  &-text4 {
    display: flex;
    font-size: 20px;
    line-height: 60px;
    height: 60px;
    color: black;
    justify-content: space-around;
    align-items: center;
  }
  &-text5 {
    margin: 0 auto;
    width: 90%;
    margin-left: 20%;
  }

}
// .chart-container {
//   position: relative;
//   width: 90%;
//   height: fit-content;
//   display: flex;
// }
</style>
