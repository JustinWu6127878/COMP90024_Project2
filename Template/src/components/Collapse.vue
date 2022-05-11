<template>
  <el-collapse v-model="activeNames" @change="handleChange">
    <el-collapse-item name="1">
      <template slot="title">
        <h2 style="font-size: 32px; text-align: left">Covid-19</h2>
      </template>
      <div>
        <el-tabs v-model="activeName1" @tab-click="handleClick">
          <el-tab-pane style="font-size: 20px" label="Metrics" name="first">
            <div style="padding:40px 0px;text-align: center;">
              <el-row :gutter="20">
                <el-col :span="12"><TableModel :row="covidRow1" :column="covidColumn1" /></el-col>
                <el-col :span="12"> <TableModel :row="covidRow2" :column="covidColumn2" /></el-col>
              </el-row>
            </div>
          </el-tab-pane>
          <el-tab-pane style="font-size: 20px" label="Graphs" name="second">
            <div style="padding:40px 0px;text-align: center;">
              <el-row :gutter="20">
                <el-col :span="12"><Piechart :chartsource="piechart1" /></el-col>
                <el-col :span="12"> <Linechart :chartsource="linechart1" /></el-col>
              </el-row>
            </div>
            <div style="padding:40px 0px;">
              <el-row :gutter="20">
                <el-col :span="12"><Linechart :chartsource="linechart2" /></el-col>
                <el-col :span="12"> <Linechart :chartsource="linechart3" /></el-col>
              </el-row>
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
            <div style="padding:40px 0px;text-align: center;">
              <el-row :gutter="20">
                <el-col :span="12"><TableModel :row="enagementRow1" :column="enagementColumn1" /></el-col>
                <el-col :span="12">  <TableModel :row="enagementRow2" :column="enagementColumn2" /></el-col>
              </el-row>
            </div>
          </el-tab-pane>
          <el-tab-pane label="Graphs" name="second">
            <div style="padding:40px 0px;text-align: center;">
              <el-row :gutter="20">
                <el-col :span="12">              <Piechart :chartsource="piechart2" /></el-col>
                <el-col :span="12">  <Piechart :chartsource="piechart3" /></el-col>
              </el-row>
            </div>
            <div style="padding:40px 0px;text-align: center;">
              <el-row :gutter="20">
                <el-col :span="12">   <Linechart :chartsource="linechart4" /></el-col>
                <el-col :span="12">  <Linechart :chartsource="linechart5" /></el-col>
              </el-row>
            </div>
            <div style="padding:40px 0px;text-align: center;">
              <el-row :gutter="20">
                <el-col :span="12"> <Piechart :chartsource="piechart4" /></el-col>
                <el-col :span="12"> <Piechart :chartsource="piechart5" /></el-col>
              </el-row>
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
            <div style="padding:40px 0px;text-align: center;">
              <el-row :gutter="20">
                <el-col :span="24">              <TableModel :row="inflationRow1" :column="inflationColumn1" /></el-col>
                <el-col :span="24">              <TableModel :row="inflationRow2" :column="inflationColumn2" /></el-col>
              </el-row>
            </div>
          </el-tab-pane>
          <el-tab-pane label="Graphs" name="second">
            <div class="chart-container">
               <Linechart :chartsource="linechart6" />
               <Linechart :chartsource="linechart7" />            
            </div>
             <el-divider></el-divider>
            <div class="chart-container">
              <WordCloud :chartsource="wordCloudChart" />             
            </div>
          </el-tab-pane>
        </el-tabs>
      </div>
    </el-collapse-item>
  </el-collapse>
</template>

<script>
import TableModel from '@/components/TableModel.vue'

import Piechart from '@/components/Charts/piechart.vue'

// import Smallchart from "@/components/Charts/smallchart.vue";

import Linechart from '@/components/Charts/linechart.vue'

import Barchart from '@/components/Charts/barchart.vue'

import WordCloud from '@/components/Charts/wordCloud.vue'

export default {
  components: {
    TableModel,
    Piechart,
    // Smallchart,
    Linechart,
    Barchart,
    WordCloud
  },

  props: [
    'piechart1',
    'linechart1',
    'linechart2',
    'linechart3',

    'covidRow1',
    'covidColumn1',
    'covidRow2',
    'covidColumn2',

    'piechart2',
    'piechart3',
    'linechart4',
    'linechart5',
    'piechart4',
    'piechart5',

    'enagementRow1',
    'enagementColumn1',
    'enagementRow2',
    'enagementColumn2',

    'inflationRow1',
    'inflationColumn1',
    'wordCloudChart'

    "inflationRow1",
    "inflationColumn1",
    "inflationRow2",
    "inflationColumn2",

    "linechart6",
    "linechart7",
    "wordCloudChart"
  
  ],

  data() {
    return {
      activeNames: ['1', '2', '3'],
      activeName1: 'second',
      activeName2: 'second',
      activeName3: 'second'
      // isshow: false,
    }
  },

  methods: {
    handleChange(val) {
      console.log(val)
    },
    handleClick(tab, event) {
      console.log(tab, event)
      this.isshow = true
    }
  }
}
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
h2{
  color: #2277D2 ;
}
p{
 color: #a2a2a2 ;
}
</style>
