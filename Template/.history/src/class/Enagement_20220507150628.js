import $ from 'jquery';

function tweetPerDay() {
    var result
    $.ajax({
      type:'GET',
      url:"http://127.0.0.1:2889/tweetPerDay",
      async:false,
      dataType:'json',
      success:function(data){
        result = data
      },
      error:function(){
        alert("Cannot load the data")
      }
    });      
    console.log(result['adel'])
    return result
  }   

  

class Enagement {
    constructor (male, edu, income, overper){
        this.male = male;
        this.female = 100-male;
        this.edu = edu;
        this.income = income;
        this.overper = overper;
    }
}

export default Enagement