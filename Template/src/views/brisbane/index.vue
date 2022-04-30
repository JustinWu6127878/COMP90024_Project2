<template>
  <div class="dashboard-container" >
    <div style="display:flex">
      <div class="dashboard-text1" > <h1>{{brisbane.name}}</h1><p>State: {{brisbane.state}}</p>
      
      </div>

      <div class="dashboard-text2" > <p>Total population:</p>
          <p><b>{{milliFormat(brisbane.pop)}} </b></p>
          <p>Born overseas: </p>
          <p><b>{{milliFormat(brisbane.over)}}</b> </p>
          <p>Age 50+ percentage: <i>{{brisbane.age50 + "%"}}</i> </p>
          <p>Age 60+ percentage: <i>{{brisbane.age65 + "%"}}</i> </p>
          <p>Median annual income: <i>{{"$"+milliFormat(brisbane.income)}}</i></p>
      </div>
    </div>

    <el-divider></el-divider>

    <div class="dashboard-text3" > <h2>Topics</h2> 
      <p> These are three topics for brisbane, VIC.
       Explore the metrics and graphs behind the numbers. </p>
    </div>

    <div class="dashboard-text4"> <h3 style="flex:2; text-align:center">Covid-19</h3> 
    <span style="flex:1; color:red; font-weight:900"> metrics </span> <span style="flex:1; color:red; font-weight:900"> graphs </span>
    </div>

    <div class="dashboard-text5">
    <TableModel
    :row = "covidRow1"
    :column="covidColumn1"
    /> 
    </div>

    <el-divider></el-divider>
    
    <div class="dashboard-text5">
    <TableModel
    :row = "covidRow2"
    :column="covidColumn2"
    /> 
    </div>

    <div class="dashboard-text4"> <h3 style="flex:2; text-align:center">Enagement</h3> 
    <span style="flex:1; color:red; font-weight:900"> metrics </span> <span style="flex:1; color:red; font-weight:900"> graphs </span>
    </div>

    <div class="dashboard-text5">
    <TableModel
    :row = "enagementRow1"
    :column="enagementColumn1"
    /> 
    </div>
    
    <el-divider></el-divider>

    <div class="dashboard-text5">
    <TableModel
    :row = "enagementRow2"
    :column="enagementColumn2"
    /> 
    </div>

  </div>
</template>

<script>
import { mapGetters } from 'vuex'

//import brisbanemap from './brisbanemap.jpg'

import CityOverview from '../../class/Overview.js'

//import Enagement from '../../class/Enagement.js'

import TableModel from '../../components/TableModel.vue'

export default {
  name: 'dashboard',
  computed: {
    ...mapGetters([
      'name'
    ])
  },
  components:{
    TableModel, 
  },
  data () {
    return {
  
  covidRow1 : [{
          item: 'Number of hospitals ',
          num: '123456',
          
        }, {
          item: 'Covid-19 active cases',
          num: '123456',
          
        }, {
          item: 'Number of vaccination clinics',
          num: '123456',
          
        }, {
          item: 'Vaccination rate',
          num: '50%', 
  
        }],
  covidColumn1 : [{
    prop : "item",
    label:"COVID-19 data of the city",
  },{
    prop : "num",
    label:"",
  }],

  covidRow2 : [{
          item: 'Positive comments rate: ',
          num: '33%%',
          
        }, {
          item: 'Negative comments rate: ',
          num: '33%',
          
        }, {
          item: 'Neutral',
          num: '33%',
          
        }],
  covidColumn2 : [{
    prop : "item",
    label:"Twitter comments in the state",
  },{
    prop : "num",
    label:"",
  }],

  enagementRow1 : [{
          item: 'Male percentage: ',
          num: '49.4%',
          
        }, {
          item: 'Female percentage: ',
          num: '50.6%%',
          
        }, {
          item: 'Graduate higher than bachelor degree:',
          num: '50%',
          
        }, {
          item: 'Born overseas percentage:',
          num: '50%', 
  
        },
        {
          item: 'Annual income > $10,000 percentage: ',
          num: '50%', 
  
        }],
  enagementColumn1 : [{
    prop : "item",
    label:"Enagement data of the city",
  },{
    prop : "num",
    label:"",
  }],

  enagementRow2 : [{
          item: '29/04/2022',
          num: '12345',
          
        }, {
          item: '30/04/2022',
          num: '12345',
          
        }, {
          item: '01/05/2022',
          num: '12345',
          
        }, {
          item: '02/05/2022',
          num: '12345', 
  
        },
        {
          item: '03/05/2022',
          num: '12345', 
  
        }],
  enagementColumn2 : [{
    prop : "item",
    label:"Date",
  },{
    prop : "num",
    label:"Twitter regarding election in one day",
  }],
  
  brisbane : new CityOverview("Brisbane", "Queensland", 2514184, 591344, 30.3, 13.7, 50011),
    
  //enagement : new Enagement ( 49.5, 50.5, 50, 50, 50, 50, 50), 
    }
  },
  

  
  


  methods :{
  milliFormat(num) {
    return num && num.toString()
        .replace(/\d+/, function(s){
             return s.replace(/(\d)(?=(\d{3})+$)/g, '$1,')
         })
}

  }
  

}
</script>


<style lang="scss" scoped>
.dashboard {
  &-container {
    position: relative;
    margin: 40px;
    width: 100%;
  }
  &-text1 {
    line-height: 46px;
    color: gray;
    flex:2;
  }
  &-text2 {
    font-size: 20px;
    line-height: 46px;
    color: black;
    flex:1;
  }
  &-text3 {
    font-size: 20px;
    line-height: 24px;
    color: black;
  }
  &-text4 {
    display:flex;
    font-size: 20px;
    line-height: 60px;
    height: 60px;
    color: black;
    justify-content: space-around;
    align-items: center;
    
    
  }
  &-text5 {
  margin: 0 auto;  
  width: fit-content 
  }
}
</style>
