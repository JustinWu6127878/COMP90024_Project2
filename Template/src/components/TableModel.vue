<template>
  <el-table
    :header-row-class-name="tableRowClass"
    :data="row"
    stripe
  >
    <el-table-column
      v-for="(c, index) in column"
      :key="index"
      align="center"
      :prop="c.prop"
      :label="c.label"
    />
  </el-table>
</template>

<script>
export default {
  name: 'TableModel',
  props: ['row', 'column'],
  data() {
    return {
    }
  },
  methods: {
    tableRowClass({ row, rowIndex }) {
      if (rowIndex === 0) {
        return 'HeaderRow'
      } else {
        return 'BodyRow'
      }
    }

  }
}
</script>

<style scoped>
    .el-table>>> .HeaderRow th{
      font-size: 20px;
      margin:0 auto;
      color:#0A4182;
      background-color: #2277D2 !important;}
      .el-table>>> .BodyRow th{
      font-size: 20px;
      margin:0 auto;
      color:#0A4182;
      background-color: #2277D2 !important;}
      h2{
        color: #2277D2 ;
      }
      p{
       color: #a2a2a2 ;
      }

</style>
