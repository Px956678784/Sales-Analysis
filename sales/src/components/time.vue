<template>
    <div class="time">
        <el-date-picker v-model="value1" type="date" placeholder="选择日期" @change="chooseDate">
        </el-date-picker>
    </div>
</template>
<script>
    import Bus from '@/util/bus.js'
    export default {
        data() {
            return {
                value1: ''
            };
        }, methods: {
            chooseDate(date) {
                let newDate = new Date(+date + 8 * 3600 * 1000)
                let realDate = newDate.toISOString().slice(0, 10)
                Bus.$emit('select_time', realDate.substr(0, 4), realDate.substr(5, 2), realDate.substr(8, 2))
            }
        }
    }
</script>