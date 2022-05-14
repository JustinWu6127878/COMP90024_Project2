import $ from 'jquery'; 


function piechartData(){
    var result
    $.ajax({
      type:'GET',
      url:process.env.VUE_APP_BACKEND_URL+"/sentiData",
      async:false,
      dataType:'json',
      success:function(data){
        result = data
      },
      error:function(){
        alert("Cannot load the data")
      }
    });      
    // console.log(result['adel'])
    return result
}   
  
function round(value, precision) {
  var multiplier = Math.pow(10, precision || 0);
  return Math.round(value * multiplier) / multiplier;
}



var result = piechartData()
const sumValues = obj => Object.values(obj).reduce((a, b) => a + b);

class Covid {
    constructor (hos, active, clinincs, rate, city){
        this.hos = hos;
        this.active = active;
        this.clinincs = clinincs;
        this.rate = rate;
        this.pos = round(100 * ((result[city]['pos'] / sumValues(result[city]))), 2);
        this.neg = round(100 * ((result[city]['neg'] / sumValues(result[city]))), 2);
        this.neu = round(100 * ((result[city]['neu'] / sumValues(result[city]))), 2);
    }
}

export default Covid