Chart.defaults.global.defaultFontFamily='-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif',Chart.defaults.global.defaultFontColor="#292b2c";
ctx=document.getElementById("myBarChart"),myLineChart=new Chart(ctx,{type:"bar",data:{labels:["August, 2017", "September, 2017", "October, 2017", "November, 2017", "December, 2017", "January, 2018"],datasets:[{label:"Expense",backgroundColor:"rgba(2,117,216,1)",borderColor:"rgba(2,117,216,1)",data:[10372, 8567, 12070, 7841, 9821, 14984]}]},options:{scales:{xAxes:[{time:{unit:"month"},gridLines:{display:!1},ticks:{maxTicksLimit:6}}],yAxes:[{ticks:{min:0,max:15e3,maxTicksLimit:5},gridLines:{display:!0}}]},legend:{display:!1}}}) 