var colors = ['blue','red','green','yellow','purple','orange','pink','brown','cyan','snow','plum','olive','moccasin','maroon', 'lime','khaki','indigo']

var ctx = 'syntidonitsi';
var myChart = new Chart(ctx, {
    type: 'doughnut',
    data: {
        labels: synnit_nimi,
        datasets: [{
            backgroundColor: colors.slice(0, synnit_maara.length), 
            data: synnit_maara  
       }]
    },
    options: {
        title: {
            display: true,
            text: synnintekija+' tunnusti syntiä '+laatu+' '+kpl+' kpl'
        }
    }
});
