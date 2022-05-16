<template>
  <div style="background-color: #f8f8f8;text-align: center;">
    <div style="padding: 20px 20px;background-color:#f8f8f8 ;">
      <div>
        <img src="./cloudtest.jpg" width="100%" style="border-radius:10px;">
        <h1 style="color: #2277D2; font-family: Sans;font-size: 40px;">ABOUT</h1>
        <p style="color: #a2a2a2;">{{ about }}</p>
      </div>

      <h1 style="color: #2277D2; font-family: Sans;font-size: 40px;">GROUP 35</h1>
    </div>
    <div>
      <div v-for="(item,index) in teamMembers" :key="index" class="Member">
        <img :src="item.img">
        <h2>{{ item.name }}</h2>
        <p style="color: #a2a2a2;">{{ try1 }}</p>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  data() {
    return {
      about: 'This website presents the analysis of Twitter data on Melbourne liveability from Group 35 in COMP90024. They comprehensively consider the inflation, medical level and election participation of the 4 cities. Line charts, pie charts, tables and word cloud graphs are used to present their cloud computing data results.',
      try1: ' ',
      teamMembers: [
        { name: 'KAICHENG WU',
          img: require('./member1.jpeg')
        },
        { name: 'JUNJIE WU',
          img: require('./member2.jpeg')
        },
        { name: 'ZIQIU HUANG',
          img: require('./member3.jpeg')
        },
        { name: 'JIAYI DAI',
          img: require('./member4.jpeg')
        },
        { name: 'YIFAN XIN',
          img: require('./member5.jpeg')
        }

      ]
    }
  }
}
</script>

<style scoped>




.group-about {
  font-size: 40px;
  margin: 0 auto;
  text-align: center;
  margin-top: 10%;
}

.group-teamintro{
  background-color:azure;
  margin: 0 auto;
  text-align: center;
  margin-top: 10%;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.group-team {
  height:400px;
  position: relative;
  display:flex;
  justify-content: space-around;
  align-items: center;
}
.group-member {
  background-color:bisque;
  margin: 0 auto;
  text-align: center;
  height: fit-content;
}
.Member{
  background-color: #ffffff;
  text-align: center;
  display: inline-block;
  width: 18%;
  margin: 10px 12px 30px 12px;
  border-radius:10px;
  box-shadow: 2px 1px 1px 0px rgba(200, 200, 200, 0.5)
}
.Member img{
  width:60%;
  padding: 15px 0 ;
  border-radius:50%
}
.Member h2{
 color: #2277D2;
 padding: 0 15px ;
}
.Member p{
 color: #a2a2a2;
 padding: 0 15px ;
}
</style>
