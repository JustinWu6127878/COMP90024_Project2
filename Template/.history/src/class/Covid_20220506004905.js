import $ from 'jquery'; 

class Covid {
    constructor (hos, active, clinincs, rate, pos, neg, neg){
        this.hos = hos;
        this.active = active;
        this.clinincs = clinincs;
        this.rate = rate;
        this.pos = pos;
        this.neg = neg;
        this.neu = neu;
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
    console.log(result)
    return result.pos
  }   

export default Covid