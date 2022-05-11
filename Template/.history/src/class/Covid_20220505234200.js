class Covid {
    constructor (hos, active, clinincs, rate, pos, neg, neu){
        this.hos = hos;
        this.active = active;
        this.clinincs = clinincs;
        this.rate = rate;
        this.pos = pos;
        this.neg = neg;
        this.neu = neu;
    }
}

piechartData(city, senti){
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

export default Covid