<template>
  <div style="background-color: #f8f8f8;text-align: center;">
    <div style="padding: 20px 20px;background-color:#f8f8f8 ;">
      <div>
        <img src="./testtest.jpeg" width="40%" height="270px" style="border-radius:10px;">
      </div>
      <div>
        <h1 style="color: #2277D2;">About</h1>
        <p style="color: #a2a2a2;">{{ about }}</p>
      </div>

      <img src="./cloud.jpeg" width="40%" height="270px" style="border-radius:10px;">
      <h1 style="color: #2277D2;">Group 35</h1>
    </div>
    <div>
      <div v-for="(item,index) in teamMembers" :key="index" class="Member">
        <img :src="item.img">
        <h2>{{ item.name }}</h2>
        <p style="color: #a2a2a2;">{{ about }}</p>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  data() {
    return {
      about: 'This website shows the results of COMP90024 Assignment2',
      teamMembers: [
        { name: 'Member1',
          img: require('./member1.jpeg')
        },
        { name: 'Member2',
          img: require('./member2.jpeg')
        },
        { name: 'Member3',
          img: require('./member3.jpeg')
        },
        { name: 'Member4',
          img: require('./member4.jpeg')
        },
        { name: 'Member5',
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
