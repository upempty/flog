<template>
<el-menu :default-active="activeIndex" router=true class="el-menu-demo"  background-color="#D3DCE6" mode="horizontal" @select="handleSelect">
  <el-menu-item index="/decoration">House Decoration</el-menu-item>
  <el-submenu index="2">
    <template slot="title">My Family</template>
    <el-menu-item index="2-1">Ronia</el-menu-item>
    <el-menu-item index="2-2">Cindy</el-menu-item>
    <el-menu-item index="2-3">Nora</el-menu-item>
    <el-menu-item index="2-4">Fred</el-menu-item>
  </el-submenu>
  <el-menu-item index="3"><a href="https://www.ele.me" target="_blank">Management</a></el-menu-item>
  <el-menu-item index="4" disabled>ContactMe</el-menu-item>
</el-menu>
</template>

<script>
export default {
  name: 'Aside'
}
</script>

<style>
</style>
