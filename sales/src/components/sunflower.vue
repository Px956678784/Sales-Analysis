<template>
    <div id="roseChart"></div>
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
            drawChart: function (date) {
                let dom_bar = document.getElementById("roseChart");
                let myChart_bar = this.$echarts.init(dom_bar);
                function drawflower(date) {
                    $.get('/sales/static/shopData.json', function (data) {
                        let sales = 0, individual = 0, visitGap = 0
                        for (let i = 0; i < data.length; i++) {

                            let simDate = data[i].date
                            simDate = Number(simDate.substr(simDate.length - 2, 2))
                            if (simDate == date) {
                                visitGap += (data[i].pv - data[i].uv)
                                sales = parseInt(data[i].uv * data[i].cro)
                                individual += data[i].uv - sales
                            }
                        }
                        let option = {
                            title: {
                                text: '比例分析',
                                left: 'center'
                            },
                            tooltip: {
                                trigger: 'item',
                                formatter: '{a} <br/>{b} : {c} ({d}%)'
                            },
                            legend: {
                                left: 'center',
                                top: 'bottom',
                                data: ['销量', '未转化销量', '重复访问']
                            },
                            toolbox: {
                                show: true,
                                feature: {
                                    mark: { show: true },
                                    dataView: { show: true, readOnly: false },
                                    magicType: {
                                        show: true,
                                        type: ['pie', 'funnel']
                                    },
                                    restore: { show: true },
                                    saveAsImage: { show: true }
                                }
                            },
                            series: [
                                {
                                    name: '半径模式',
                                    type: 'pie',
                                    radius: [20, 110],
                                    center: ['50%', '50%'],
                                    roseType: 'radius',
                                    label: {
                                        show: false
                                    },
                                    emphasis: {
                                        label: {
                                            show: true
                                        }
                                    },
                                    data: [
                                        { value: sales, name: '销量' },
                                        { value: individual, name: '未转化销量' },
                                        { value: visitGap, name: '重复访问' },
                                    ]
                                }
                            ]
                        };
                        if (option && typeof option === "object") {
                            myChart_bar.setOption(option, true);
                        }
                    })
                }
                drawflower(1)
                Bus.$on('select_time', (new_y, new_m, new_d) => {
                    drawflower(parseInt(new_d))
                })
            }
        }
    }
</script>
<style>
    #roseChart {
        flex: 1;
    }
</style>