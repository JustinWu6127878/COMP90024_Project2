<template>
  <el-collapse v-model="activeNames" @change="handleChange">
    <el-collapse-item name="1">
      <template slot="title">
        <h2 style="font-size: 32px; text-align: left">Covid-19</h2>
      </template>
      <div>
        <el-tabs v-model="activeName1" @tab-click="handleClick">
          <el-tab-pane style="font-size: 20px" label="Metrics" name="first">
            <div class="dashboard-text5">
              <TableModel :row="covidRow1" :column="covidColumn1" />
            </div>

            <el-divider></el-divider>

            <div class="dashboard-text5">
              <TableModel :row="covidRow2" :column="covidColumn2" />
            </div>
          </el-tab-pane>
          <el-tab-pane style="font-size: 20px" label="Graphs" name="second">
            <div class="chart-container">
              <Piechart :chartsource="piechart1" />
              <Linechart :chartsource="linechart1" />
            </div>
            <div class="chart-container">
              <Linechart :chartsource="linechart2" />
              <Linechart :chartsource="linechart3" />
            </div>
          </el-tab-pane>
        </el-tabs>
      </div>
    </el-collapse-item>
    <el-collapse-item name="2">
      <template slot="title">
        <h2 style="font-size: 32px; text-align: left">Enagement</h2>
      </template>
      <div>
        <el-tabs v-model="activeName2" @tab-click="handleClick">
          <el-tab-pane label="Metrics" name="first">
            <div class="dashboard-text5">
              <TableModel :row="enagementRow1" :column="enagementColumn1" />
            </div>

            <el-divider></el-divider>

            <div class="dashboard-text5">
              <TableModel :row="enagementRow2" :column="enagementColumn2" />
            </div>
          </el-tab-pane>
          <el-tab-pane label="Graphs" name="second">
            <div class="chart-container">
              <!-- <Smallchart :chartsource="piechart2" /> -->
              <Piechart :chartsource="piechart2" />
              <Piechart :chartsource="piechart3" />
            </div>
            <div class="chart-container">
              <Linechart :chartsource="linechart4" />
              <Linechart :chartsource="linechart5" />
            </div>
            <div class="chart-container">
              <!-- <Smallchart :chartsource="piechart2" /> -->
              <Piechart :chartsource="piechart4" />
              <Piechart :chartsource="piechart5" />
            </div>
            

          </el-tab-pane>
        </el-tabs>
      </div>
    </el-collapse-item>
    <el-collapse-item name="3">
      <template slot="title">
        <h2 style="font-size: 32px; text-align: left">Inflation</h2>
        <!-- <span style="flex: 1; color: red; font-weight: 900"> metrics </span>
      <span style="flex: 1; color: red; font-weight: 900"> graphs </span> -->
      </template>
      <div>
        <el-tabs v-model="activeName3" @tab-click="handleClick">
          <el-tab-pane label="Metrics" name="first">
            <div class="dashboard-text5">
              <TableModel :row="inflationRow1" :column="inflationColumn1" />
            </div>

          </el-tab-pane>
          <el-tab-pane label="Graphs" name="second">Inflation Grpahs</el-tab-pane>
            <div class="chart-container">

              
        </el-tabs>
      </div>
    </el-collapse-item>
  </el-collapse>
</template>


<script>
import TableModel from "@/components/TableModel.vue";

import Piechart from "@/components/Charts/piechart.vue";

// import Smallchart from "@/components/Charts/smallchart.vue";

import Linechart from "@/components/Charts/linechart.vue";

import Barchart from "@/components/Charts/barchart.vue";

// import 

export default {
  components: {
    TableModel,
    Piechart,
    // Smallchart,
    Linechart,
    Barchart,
  },

  data() {
    return {
      activeNames: ["1", "2", "3"],
      activeName1: "second",
      activeName2: "second",
      activeName3: "second",
      // isshow: false,
    };
  },

  props: [
    "piechart1",
    "linechart1",
    "linechart2",
    "linechart3",
    
    "covidRow1",
    "covidColumn1",
    "covidRow2",
    "covidColumn2",
    
    "piechart2",
    "piechart3",
    "linechart4",
    "linechart5",
    "piechart4",
    "piechart5",

    "enagementRow1",
    "enagementColumn1",
    "enagementRow2",
    "enagementColumn2",

    "inflationRow1",
    "inflationColumn1",
  
  ],

  methods: {
    handleChange(val) {
      console.log(val);
    },
    handleClick(tab, event) {
      console.log(tab, event);
      this.isshow = true;
    },
  },
};
</script>

<style scoped>
.chart-container {
  position: relative;
  margin-left:5%;
  height: fit-content;
  display: flex;
}
.dashboard-text5 {
  margin: 0 auto;
  width: 70%;
}
</style>