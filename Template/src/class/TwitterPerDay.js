import $ from 'jquery';

function tweetPerDay() {
    var result
    $.ajax({
      type:'GET',
      url:process.env.VUE_APP_BACKEND_URL+"/tweetPerDay",
      async:false,
      dataType:'json',
      success:function(data){
          result = data
          // console.log(result)s
      },
      error:function(){
        alert("Cannot load the data")
      }
    });      
    return result
}   
  

var date_list = tweetPerDay()


class TwitterPerDay {
    constructor(city) {
        var city_data = date_list[city];
        var len_data = city_data.length;
        this.date1 = Object.keys(city_data[len_data - 6]);
        this.number1 = Object.values(city_data[len_data - 6])[0];
        this.date2 = Object.keys(city_data[len_data - 5]);
        this.number2 = Object.values(city_data[len_data - 5])[0];
        this.date3 = Object.keys(city_data[len_data - 4]);
        this.number3 = Object.values(city_data[len_data - 4])[0];
        this.date4 = Object.keys(city_data[len_data - 3]);
        this.number4 = Object.values(city_data[len_data - 3])[0];
        this.date5 = Object.keys(city_data[len_data - 2]);
        this.number5 = Object.values(city_data[len_data - 2])[0];
    }
}

export default TwitterPerDay