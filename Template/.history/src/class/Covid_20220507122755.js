import $ from 'jquery'; 


function piechartData(){
    var result
    $.ajax({
      type:'GET',
      url:"http://127.0.0.1:2889/sentiData",
      async:false,
      dataType:'json',
      success:function(data){
        // console.log(data['data_line']);
        // console.log(data[city][senti])
        result = data
      },
      error:function(){
        alert("Cannot load the data")
      }
    });      

    return result
  }   

var result = piechartData()

class Covid {
    constructor (hos, active, clinincs, rate, city, senti){
        this.hos = hos;
        this.active = active;
        this.clinincs = clinincs;
        this.rate = rate;
        this.pos = result[city]['pos'];
        this.neg = result[city]['neg'];
        this.neu = result[city]['senti'];
    }
}

export default Covid