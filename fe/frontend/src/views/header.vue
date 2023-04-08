<template>
      <!--<Header> 小桥流水人家，倚坐门前屋檐下，仰望满天星星，化作一片片柳絮在空中飘荡。</Header>-->
      <el-row :gutter="20">
        <el-col :span="4"><div class="grid-content bg-purple">滴滴嗒嗒, 小步向前! {{user}}</div></el-col>
        <el-col :span="16"><div class="grid-content bg-purple">小桥流水人家，倚坐门前屋檐下，仰望满天星星，化作一片片柳絮在空中飘荡。</div></el-col>
        <el-col :span="4">
          <div class="grid-content bg-purple">
            <el-button type="text" @click="add_route_login">Login</el-button>
            <el-button type="text" @click="add_route_register">Register</el-button>
          </div>
        </el-col>
      </el-row>
</template>

<script>
export default {
  name: 'Header',
  data() {
    return {
      user33notupdate: this.$store.state.user,
    }
  }
}
</script>

<style>
</style>
