import $ from 'jquery'; 

class Covid {
    constructor (hos, active, clinincs, rate, city){
        this.hos = hos;
        this.active = active;
        this.clinincs = clinincs;
        this.rate = rate;
        this.pos = piechartData(city, 'pos');
        this.neg = piechartData(city, 'neu');
        this.neu = piechartData(city, 'neg');
    }
}

function piechartData(city, senti){
    var result
    $.ajax({
      type:'GET',
      url:"http://127.0.0.1:2889/sentiData",
      async:false,
      dataType:'json',
      success:function(data){
        // console.log
        // console.log(data[city][senti])
        result = data[city]
        // console.log(result)
        // console.log('end')
      },
      error:function(){
        alert("Cannot load the data")
      }
    });   
    console.log('result')
    console.log(result[senti])
    return result
  }   

export default Covid