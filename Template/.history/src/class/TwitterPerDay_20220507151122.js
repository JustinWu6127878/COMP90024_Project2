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
  

var date_list = tweetPerDay()


class TwitterPerDay {
    constructor (city){
        this.dateList = date1;

    }
}

export default TwitterPerDay