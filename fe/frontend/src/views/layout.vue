<template>
  <el-container>
    <el-header>
      <!--<Header> 小桥流水人家，倚坐门前屋檐下，仰望满天星星，化作一片片柳絮在空中飘荡。</Header>-->
      <el-row :gutter="20">
        <el-col :span="4"><div class="grid-content bg-purple">滴滴嗒嗒, 小步向前!</div></el-col>
        <el-col :span="16"><div class="grid-content bg-purple">小桥流水人家，倚坐门前屋檐下，仰望满天星星，化作一片片柳絮在空中飘荡。</div></el-col>
        <el-col :span="4"><div class="grid-content bg-purple"><el-button type="text" @click="add_route_login">Login</el-button></div></el-col>
      </el-row>
    </el-header>
    <el-container>
      <el-aside width="150px">
        <Aside />
.      </el-aside>
      <el-main>
        <router-view />
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
import Aside from '@/views/aside'
export default {
  name: 'Layout',
  components: {
    Aside
  },
  methods: {
    add_route_login() {
      this.$router.push('/login')
    }
  }
}
</script>

<style>
.el-header {
  background-color: #B3C0D1;
  color: #333;
  text-align: center;
  line-height: 60px;
  padding: 0;
  z-index: 1000;
}

.el-header .fr {
  float: right;
}
.el-header .el-menu {
  border-bottom: none;
}
.el-aside, el-main {
  padding-top: 60px;
}
.el-aside {
  background-color: #D3DCE6;
  color: #333;
  text-align: center;
  line-height: 200px;
}
.el-aside .el-menu {
  border-right: none;
}
.el-main {
  background-color: #E9EEF3;
  color: #333;
  text-align: left;
  padding-top: 60px;
  line-height: 50px;
}
.el-container {
  position: absolute;
  width: 100%;
  top: 0px;
  left: 0;
  bottom: 0;
}
</style>
