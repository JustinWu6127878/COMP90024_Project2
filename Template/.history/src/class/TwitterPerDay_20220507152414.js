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
        var city_data = date_list[city];
        var len_data = city_data.length;
        this.date1 = Object.keys(city_data[len_data - 5]);
        this.number1 = Object.values(city_data[len_data - 5]);
        this.date2 = Object.keys(city_data[len_data - 1]);
        this.number2 = number2;
        this.date3 = Object.keys(city_data[len_data - 1]);
        this.number3 = number3;
        this.date4 = Object.keys(city_data[len_data - 1]);
        this.number4 = number4;
        this.date5 = Object.keys(city_data[len_data - 1]);
        this.number5 = number5;
    }
}

export default TwitterPerDay