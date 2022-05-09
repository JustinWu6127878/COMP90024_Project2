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
  

var date_list = tweetPerDay


class TwitterPerDay {

    constructor(city) {
        var city_data = date_list[city
        this.date1 = date_list[city][date_list[city].length];
        this.number1 = number1;
        this.date2 = date2;
        this.number2 = number2;
        this.date3 = date3;
        this.number3 = number3;
        this.date4 = date4;
        this.number4 = number4;
        this.date5 = date5;
        this.number5 = number5;
    }
}

export default TwitterPerDay