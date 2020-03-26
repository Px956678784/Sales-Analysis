<template>
    <div id="parallel"></div>
</template>
<script>
    import Bus from '@/util/bus.js'
    export default {
        data() {
            return {

            }
        },
        mounted() {
            this.drawChart()
        },
        methods: {
            drawChart: function () {
                var schema = [
                    { name: 'date', index: 0, text: '日期' },
                    { name: 'uv', index: 1, text: '独立访问量' },
                    { name: 'pv', index: 2, text: '访问量' },
                    { name: 'cro', index: 3, text: '消费比' },
                    { name: 'sales', index: 4, text: '销量' }
                ];

                var lineStyle = {
                    normal: {
                        width: 1,
                        opacity: 0.5
                    }
                };

                let dom_bar = document.getElementById("parallel");
                let myChart_bar = this.$echarts.init(dom_bar);
                $.get('/sales/static/shopData.json', function (data) {
                    const shopName = [], showData = []
                    for (let i = 0; i < 10; i++) {
                        shopName.push(data[i].shop)
                    }
                    for (let i = 0; i < shopName.length; i++) {
                        let shopDate = []
                        for (let j = 0; j < data.length; j++) {
                            if (data[j].shop == shopName[i]) {
                                let simDate = data[j].date
                                simDate = Number(simDate.substr(simDate.length - 2, 2))
                                shopDate.push([simDate, data[j].pv, data[j].uv, data[j].cro, parseInt(data[j].uv * data[j].cro)])
                            }
                        }
                        let shopInfo = { name: shopName[i], type: 'parallel', lineStyle: lineStyle, data: shopDate }
                        showData.push(shopInfo)
                    }
                    console.log(showData)
                    let option = {

                        legend: {
                            bottom: 30,
                            data: shopName,
                            itemGap: 20,
                            textStyle: {
                                color: '#fff',
                                fontSize: 14
                            }
                        },

                        // dataZoom: {
                        //     show: true,
                        //     orient: 'vertical',
                        //     parallelAxisIndex: [0]
                        // },
                        parallelAxis: [
                            { dim: 0, name: schema[0].text, inverse: true, max: 31, nameLocation: 'start' },
                            { dim: 1, name: schema[1].text },
                            { dim: 2, name: schema[2].text },
                            { dim: 3, name: schema[3].text },
                            { dim: 4, name: schema[4].text },
                        ],

                        parallel: {
                            left: '5%',
                            right: '10%',
                            bottom: 100,
                            parallelAxisDefault: {
                                type: 'value',
                                name: '销量',
                                nameLocation: 'end',
                                nameGap: 200,
                                nameTextStyle: {
                                    color: '#fff',
                                    fontSize: 12
                                },
                                axisLine: {
                                    lineStyle: {
                                        color: '#aaa'
                                    }
                                },
                                axisTick: {
                                    lineStyle: {
                                        color: '#777'
                                    }
                                },
                                splitLine: {
                                    show: false
                                },
                                axisLabel: {
                                    color: '#fff'
                                }
                            }
                        },
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
    #parallel {
        flex: 1;
        display: flex;
        justify-content: center;
    }
</style>