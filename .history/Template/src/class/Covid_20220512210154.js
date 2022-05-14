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
  
function 

var result = piechartData()
const sumValues = obj => Object.values(obj).reduce((a, b) => a + b);

class Covid {
    constructor (hos, active, clinincs, rate, city){
        this.hos = hos;
        this.active = active;
        this.clinincs = clinincs;
        this.rate = rate;
        this.pos = 100 * ((result[city]['pos'] / sumValues(result[city])));
        this.neg = 100 * ((result[city]['neg'] / sumValues(result[city])));
        this.neu = 100 * ((result[city]['neu'] / sumValues(result[city])));
    }
}

export default Covid