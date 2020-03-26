<template>
    <el-container class="screen">
        <el-header>
            <div class="date" v-model="dateCount">店铺销售分析系统</div>
            <div class="title">Story</div>
            <Time></Time>


        </el-header>
        <el-container>
            <el-main>
                <div id="bar" class="content-box">
                    <Barchart></Barchart>
                </div>
            </el-main>
            <el-main class="left">
                <div id="pie" class="content-box">
                    <Sunflower></Sunflower>
                </div>
            </el-main>
        </el-container>
        <div class="down">
            <div id="line" class="content-box">
                <Linechart></Linechart>
            </div>
        </div>
    </el-container>
</template>
<script>
    import Bus from '@/util/bus.js'
    //引入标题和脚注
    import Sunflower from '../components/sunflower.vue'
    import Linechart from '../components/linechart.vue'
    import Barchart from '../components/barchart.vue'
    import Time from '../components/time.vue'
    export default {
        components: { Sunflower, Linechart, Barchart, Time },
        data() {
            return {
                dateCount: 10000
            }
        },
        methods: {

        }, mounted: function () {
            let Date2 = new Date()
            Date2.toLocaleDateString();
            let Date1 = "2019-01-11"
            let start = Date.parse(Date1);
            let seconds = Date2.getTime() - start
            let days = parseInt(seconds / (1000 * 60 * 60 * 24));
            this.dateCount = days
        }

    }

</script>
<style scoped>
    @import '../css/index.css';
</style>