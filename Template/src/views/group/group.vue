<template>
  <div>
    <img src="./group1.jpeg" width="100%" />

    <div class="group-about">
      <h1>About</h1>
      <p>{{ about }}</p>
    </div>

    <img src="./cloud.jpeg" width="100%" />

    <div class="group-teamintro">
        <div>
            <h1> Group 35 </h1>
        </div>

<div class="group-team">
        <div class="group-member">
           <img src="./member1.jpeg" style="width:100px"/>
           <h1>Name1</h1> 
        </div>
        <div class="group-member">
           <img src="./member2.jpeg" style="width:100px"/>
           <h1>Name1</h1> 
        </div>
        <div class="group-member">
           <img src="./member3.jpeg" style="width:100px"/>
           <h1>Name1</h1> 
        </div>
        <div class="group-member">
           <img src="./member4.jpeg" style="width:100px"/>
           <h1>Name1</h1> 
        </div>
        <div class="group-member">
           <img src="./member5.jpeg" style="width:100px"/>
           <h1>Name1</h1> 
        </div>
</div>
    </div>

  </div>
</template>

<script>

export default {
data(){
    return{
    about : "This website shows the results of COMP90024 Assignment2"
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

</style>