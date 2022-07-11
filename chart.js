Highcharts.chart('container', {
    chart: {
        type: 'column'
    },
    title: {
        text: 'Tanzania Premium Collected'
    },
    subtitle: {
        text: 'Source: IMIS'
    },
    xAxis: {
        categories: [
            'Jan',
            'Feb',
            'Mar',
            'Apr',
            'May',
            'Jun',
            'Jul',
            'Aug',
            'Sep',
            'Oct',
            'Nov',
            'Dec'
        ],
        crosshair: true
    },
    yAxis: {
        min: 0,
        title: {
            text: 'TZS'
        }
    },
    tooltip: {
        headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
        pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
            '<td style="padding:0"><b>{point.y:.1f} TZS</b></td></tr>',
        footerFormat: '</table>',
        shared: true,
        useHTML: true
    },
    plotOptions: {
        column: {
            pointPadding: 0.2,
            borderWidth: 0
        }
    },
    series: [{
        name: 'Bank',
        data: [41530000.0, 26200000.0, 28240000.0, 15230000.0, 37471000.0, 115160006.0, 60816000.0, 82586000.0, 167440000.0, 235309674.0, 270296000.0, 134510000.0]

    }, {
        name: 'Cash',
        data: [715053580.0, 605060981.3, 682143908.0, 406348003.0, 359010632.0, 370404637.0, 485334001.0, 575951963.0, 736336846.2, 819090204.3, 602660000.0, 402476000.0]

    }, {
        name: 'Mobile',
        data: [28034132.0, 24304784.0, 31833806.0, 26895762.0, 24805110.0, 27397132.0, 27003806.0, 23306740.0, 29126414.0, 42241960.0, 29396414.0, 22089112.0]

    }]
});