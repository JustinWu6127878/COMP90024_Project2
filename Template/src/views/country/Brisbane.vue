<template>
  <div>
    <div style="margin: 10px 30px;text-align: center;">
      <i style="float: left;" class="el-icon-arrow-left" @click="gotoCountry" />
      <h2>Brisbane</h2>
    </div>
    <div style="margin: 10px 30px;text-align: center;">
      <el-tabs v-model="activeName" @tab-click="handleClick">
        <el-tab-pane label="Enagement" name="a">topic1</el-tab-pane>
        <el-tab-pane label="inflationtopic2" name="b">topic2</el-tab-pane>
        <el-tab-pane label="COVID-19" name="c">topic3</el-tab-pane>
      </el-tabs>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      activeName: 'a'
    }
  },
  created() {
    console.log('参数:', this.$route.query, this.$route.query.index)
    if (this.$route.query.index) {
      this.activeName = this.$route.query.index
    }
  },
  methods: {
    handleClick(tab, event) {
      console.log(tab, event)
    },
    gotoCountry() {
      this.$router.push({
        path: '/home'
        // query: {
        // 	uid:'111915',
        // 	index:that.index
        // }
      })
    }
  }
}
</script>
