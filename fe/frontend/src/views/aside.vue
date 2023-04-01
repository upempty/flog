<template>
<el-menu class="el-menu-vertical-demo" ref="menus" :default-openeds="['1']" @close="handleClose" :default-active="$route.path" router=true background-color="#D3DCE6" mode="horizontal">
  <el-submenu index="1">
      <template slot="title"><i class="el-icon-menu"></i>导航二</template>
        <el-menu-item-group>
          <template slot="title">分组一</template>
          <el-menu-item index="/decoration">House Decoration</el-menu-item>
          <el-menu-item index="/post">Post</el-menu-item>
          <el-menu-item index="/articles">Blog Posts</el-menu-item>
        </el-menu-item-group>
        <el-menu-item-group title="分组2">
          <el-menu-item index="dd">选项3</el-menu-item>
        </el-menu-item-group>
  </el-submenu>
</el-menu>
</template>

<script>
export default {
  name: 'Aside',
  methods: {
  handleClose(key, keyPath) 
  {
    this.$refs.menus.open(keyPath);
  }
  }
} 

</script>

<style>
</style>
