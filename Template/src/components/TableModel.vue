<template>
  <el-table
    :header-row-class-name="tableRowClass"
    :data="row"
    stripe>
    <el-table-column v-for= "(c, index) in column" :key= "index" align="center"
      :prop="c.prop"
      :label="c.label">
    </el-table-column>
  </el-table>
</template>

<script>
  export default {
    name: 'TableModel',
    props: ["row","column"],
    data() {
      return {
      }
    },
    methods:{
      tableRowClass({row, rowIndex}){
        if (rowIndex === 0){
          return 'HeaderRow'
        }
        else{
          return 'BodyRow'
        }
      }
      
    },
  }
</script>

<style scoped>
    .el-table>>> .HeaderRow th{
      font-size: 20px;
      margin:0 auto;
      color:cornflowerblue;
      background-color: burlywood !important;}
      .el-table>>> .BodyRow th{
      font-size: 20px;
      margin:0 auto;
      color:cornflowerblue;
      background-color: burlywood !important;}

</style>