<template>
    <div id="chart"></div>
</template>
<script>
    export default {
        data() {
        },
        mounted() {
            this.drawChart()
        },
        methods: {
            drawChart: function () {
                let dom_bar = document.getElementById("chart");
                let myChart_bar = this.$echarts.init(dom_bar);
                $.get('/sales/static/shopData.json', function (data) {
                    const shopName = [], dateName = [], showData = []
                    for (let i = 0; i < 10; i++) {
                        shopName.push(data[i].shop)
                    }
                    for (let i = 0; i < data.length; i += 10) {
                        dateName.push(data[i].date)
                    }
                    for (let i = 0; i < shopName.length; i++) {
                        let shopDate = []
                        for (let j = 0; j < data.length; j++) {
                            if (data[j].shop == shopName[i]) {
                                shopDate.push(parseInt(data[j].uv * data[j].cro))
                            }
                        }
                        let shopInfo = { name: shopName[i], type: "line", stack: "总量", areaStyle: {}, data: shopDate }
                        showData.push(shopInfo)
                    }
                    let option = {
                        title: {
                            text: '销量趋势分析'
                        },
                        tooltip: {
                            trigger: 'axis',
                            axisPointer: {
                                type: 'cross',
                                label: {
                                    backgroundColor: '#6a7985'
                                }
                            }
                        },
                        legend: {
                            data: shopName
                        },
                        toolbox: {
                            feature: {
                                saveAsImage: {}
                            }
                        },
                        grid: {
                            left: '3%',
                            right: '4%',
                            bottom: '3%',
                            containLabel: true
                        },
                        xAxis: [
                            {
                                type: 'category',
                                boundaryGap: false,
                                data: dateName
                            }
                        ],
                        yAxis: [
                            {
                                type: 'value'
                            }
                        ],
                        series: showData
                    };

                    if (option && typeof option === "object") {
                        myChart_bar.setOption(option, true);
                    }
                })
            }
        }
    }
</script>
<style>
    #chart {
        flex: 1;
    }
</style>