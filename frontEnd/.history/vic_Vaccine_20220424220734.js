let today = new Date()
let today_iso = new Date(today .getTime() - (today.getTimezoneOffset() * 60000));

let yesterday = new Date();
let yesterday_iso = new Date(yesterday.getTime() - (yesterday.getTimezoneOffset() * 60000));
yesterday_iso.setDate(yesterday_iso.getDate() - 1);

let two_day_before = new Date();
let two_day_before_iso = new Date(two_day_before.getTime() - (two_day_before.getTimezoneOffset() * 60000));
two_day_before_iso.setDate(two_day_before_iso.getDate() - 2);

let url = 'https://vaccinedata.covid19nearme.com.au/data/'+ two_day_before_iso.toISOString().slice(0, 10)+'.json'
document.getElementById("yesterday_age").innerHTML = "VIC " + two_day_before_iso.toISOString().slice(0, 10) + " Vaccine Age Buckets";
document.getElementById("yesterday_states").innerHTML = "AUS " + two_day_before_iso.toISOString().slice(0, 10) + " Vaccine Dose Count";

if (today_iso.getHours() > 17){
  url = 'https://vaccinedata.covid19nearme.com.au/data/'+ yesterday_iso.toISOString().slice(0, 10)+'.json'
  document.getElementById("yesterday_age").innerHTML = "VIC " + yesterday_iso.toISOString().slice(0, 10) + " Vaccine Age Buckets";
  document.getElementById("yesterday_states").innerHTML = "AUS " + yesterday_iso.toISOString().slice(0, 10) + " Vaccine Dose Count";
}

console.log(url)

fetch(url)
  .then(response => response.json())
  .then(data => {
    let vic_age_buckets = data.pdfData.stateOfResidence.VIC.ageBucketsEstimatedPopulation

    let age_buckets = []
    let all_first_dose_per = [], all_second_dose_per = [], all_no_dose_per = []

    for (let i = 0; i < vic_age_buckets.length; i++){
      age_buckets.push(vic_age_buckets[i].ageLower)

      let cur_first_dose_per = vic_age_buckets[i].firstDosePct
      let cur_second_dose_per = vic_age_buckets[i].secondDosePct
      let only_first_dose_per = cur_first_dose_per - cur_second_dose_per
      let cur_no_dose_per = cur_first_dose_per - 100

      all_first_dose_per.push(round(only_first_dose_per, 2))
      all_second_dose_per.push(round(cur_second_dose_per, 2))
      all_no_dose_per.push(round(cur_no_dose_per, 2))
    }

    var chartDomb = document.getElementById('vic_vac');
    var myChartb = echarts.init(chartDomb);
    var optionb;

    optionb = {
      tooltip: {
        trigger: 'axis',
        axisPointer: {
          type: 'shadow'
        }
      },
      legend: {
        data: ['Only One Dose', 'Fully Vaccinated', 'Not Vacciated']
      },
      grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
      },
      xAxis: [
        {
          type: 'value',
          axisLabel: {
            formatter: "{value}%"
          },
        }
      ],
      yAxis: [
        {
          type: 'category',
          axisTick: {
            show: false
          },
          data: age_buckets
        }
      ],
      series: [
        {
          name: 'Only One Dose',
          type: 'bar',
          label: {
            show: true,
            position: 'inside'
          },
          emphasis: {
            focus: 'series'
          },
          data: all_first_dose_per,
          color: ["#27A4D0"]
        },
        {
          name: 'Fully Vaccinated',
          type: 'bar',
          stack: 'Total',
          label: {
            show: true
          },
          emphasis: {
            focus: 'series'
          },
          data: all_second_dose_per,
          color: ["#e8702c"]
        },
        {
          name: 'Not Vacciated',
          type: 'bar',
          stack: 'Total',
          label: {
            show: true,
            position: 'left'
          },
          emphasis: {
            focus: 'series'
          },
          data: all_no_dose_per,
          color: ["#9ba2af"]
        }
      ]
    };
    optionb && myChartb.setOption(optionb);
  });
