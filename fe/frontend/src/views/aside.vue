<template>
<el-menu :default-active="activeIndex" router=true class="el-menu-demo"  background-color="#D3DCE6" mode="horizontal" @select="handleSelect">
  <el-menu-item index="/decoration">House Decoration</el-menu-item>
  <el-submenu index="sample">
    <template slot="title">My Blog</template>
    <el-menu-item index="/blog">Blog</el-menu-item>
    <el-menu-item index="/post">Post</el-menu-item>
  </el-submenu>
  <el-menu-item index="4">ContactMe</el-menu-item>
</el-menu>
</template>

<script>
export default {
  name: 'Aside'
}
</script>

<style>
</style>
