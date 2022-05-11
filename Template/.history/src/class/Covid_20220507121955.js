import $ from 'jquery'; 


function piechartData(city, senti){
    var result
    $.ajax({
      type:'GET',
      url:"http://127.0.0.1:2889/sentiData",
      async:false,
      dataType:'json',
      success:function(data){
        // console.log(data['data_line']);
        console.log(data[city][senti])
        result = data[city][senti]
      },
      error:function(){
        alert("Cannot load the data")
      }
    });      

    return result
  }   

var result = 33

class Covid {
    constructor (hos, active, clinincs, rate, pos, neg, neu){
        this.hos = hos;
        this.active = active;
        this.clinincs = clinincs;
        this.rate = rate;
        this.pos = result;
        this.neg = neg;
        this.neu = neu;
    }
}

export default Covid