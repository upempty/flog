<template>
  <div id='deco'>
     <div class='ShowLevel'>
       <el-breadcrumb seperator="/" class="padding-b">
          <el-breadcrumb-item :to="{path: '/'}">Home</el-breadcrumb-item>
          <el-breadcrumb-item>Decoration</el-breadcrumb-item>
       </el-breadcrumb>
     </div>
     <div class='ToSearch' font-size:0>
       <table class="tables">
       <td><el-col><el-input placeholder="项目名" v-model="SearchData.name" style="display:inline"></el-input></el-col></td>
       <td><el-col><el-button type="button" plain @click="on_search">搜索</el-button></el-col></td>
       </table>
     </div>
     <div class="ToInput">
       <table class="tables">
         <tr>
           <td><el-col width="15%"><el-input placeholder="编号" v-model="InData.payid"></el-input></el-col></td>
           <td><el-col width="15%"><el-input placeholder="项目名" v-model="InData.name"></el-input></el-col></td>
           <td><el-col width="15%"><el-input placeholder="费用" v-model="InData.fee"></el-input></el-col><td>
           <td><el-date-picker v-model="InData.paydate" type="datetime" placeholder="chosse time" value-format="yyyy-MM-dd HH:mm:ss"></el-date-picker></td>
           <td><el-col width="15%"><el-button type="button" plain @click="on_add">添加</el-button></el-col></td>
           <td><el-col width="15%"><el-button type="button" plain @click="on_query">查询刷新</el-button></el-col></td>
           <td><el-col width="10%"><el-button type="button" plain @click="on_update">更新</el-button></el-col></td>
           <td><el-col width="10%"><el-button type="button" plain @click="on_delete">删除</el-button></el-col></td>
         </tr>
       </table>
     </div>
    <div class='Listing'>
       <el-table :data="ItemsFee.slice((currentPage-1)*pagesize, currentPage*pagesize)" ref="multipleTable" border :header-cell-style="tableHeaderColor">
         <el-table-column type="selection" width="55"></el-table-column>
         <el-table-column prop="payid" label="编号" width="80">
           <template slot-scope="{row, $index}">
              <input class="edit-cell" v-show="showEdit[$index]" v-model="row.payid">
              <span v-show="!showEdit[$index]">{{row.payid}}</span>
           </template>
         </el-table-column>
         <el-table-column prop="name" label="项目" width="140"></el-table-column>
         <el-table-column prop="fee" label="费用" width="120"></el-table-column>
         <el-table-column prop="paydate" label="付款时间" width="200"></el-table-column>
         <el-table-column label="操作" width="200">
           <template slot-scope="scope">
           <el-button size="small" type="danger" @click="handle_edit(scope.$index, scope.row)" v-if="!showBtn[scope.$index]">编辑</el-button>
           <el-button size="small" type="danger" @click="handle_save(scope.$index, scope.row)" v-if="showBtn[scope.$index]">save</el-button>
           <el-button size="mini" type="info" @click="handle_delete(scope.$index, scope.row)">删除</el-button>
           </template>
         </el-table-column>
       </el-table>
     </div>
     <div style="text-align: left;margin-top: 5px;">
       <el-pagination
          background
          layout="prev, pager, next"
          :page-size="pagesize" :total="totalSize"
          @size-change="handleSizeChange"
          @current-change="current_change">
      </el-pagination>
    </div>
   </div>
</template>

<script>
export default {
  name: 'ItemsFee',
  data () {
    return { ItemsFee: [],
      InData: {},
      SearchData: {},
      showEdit: [],
      showBtn: [],
      currentPage: 1,
      pagesize: 6,
      totalSize: 0
    }
  },
  mounted: function () {
    this.$axios({
      url: 'decoration/cart/',
      method: 'get',
      params: {}
    }).then(res => {
      res = res.data
      this.ItemsFee = res.data
      this.totalSize = this.ItemsFee.length
      console.log('testend-mount')
      alert(this.ItemsFee[0].name)
      alert(res.status)
    })
  },
  methods: {
    tableRowStyle ({ row, rowIndex }) {
      return 'background-color: #F7F6Fd'
    },
    tableHeaderColor ({row, column, rowIndex, columnIndex}) {
      if (rowIndex === 0) {
        return 'background-color: lightblue;color: #fff;font-weight: 500;'
      }
    },
    on_add () {
      console.log('test')
      console.log(this.InData.name, this.InData.fee)
      this.$axios({
        url: 'decoration/cart/',
        method: 'post',
        data: {
          payid: this.InData.payid,
          name: this.InData.name,
          fee: this.InData.fee,
          paydate: this.InData.paydate
        }
      }).then(res => {
        res = res.data
        alert(res.msg)
      })
      console.log('testend')
    },
    on_query () {
      console.log('test query')
      console.log(this.InData.name, this.InData.fee)
      this.$axios({
        url: 'decoration/cart/',
        method: 'get',
        params: {
        }
      }).then(res => {
        res = res.data
        this.ItemsFee = res.data
        this.totalSize = this.ItemsFee.length
        alert(res.msg)
      })
      console.log('testend')
    },
    on_search () {
      this.$axios({
        url: 'decoration/cart/',
        method: 'get',
        params: {
          name: this.SearchData.name
        }
      }).then(res => {
        res = res.data
        this.ItemsFee = res.data
        this.totalSize = this.ItemsFee.length
        this.currentPage = 1
        alert(this.totalSize)
        alert(this.currentPage)
      })
    },
    on_update () {
      console.log('test update')
      alert('updating')
      console.log(this.InData.name, this.InData.fee)
      this.$axios({
        url: 'decoration/cart/',
        method: 'put',
        data: {
          payid: this.InData.payid,
          name: this.InData.name,
          fee: this.InData.fee,
          paydate: this.InData.paydate
        }
      }).then(res => {
        res = res.data
        this.ItemsFee = res.data
        alert(res.msg)
      })
      console.log('testend')
    },
    on_delete () {
      alert('deleting')
      console.log(this.InData.name, this.InData.fee)
      this.$axios({
        url: 'decoration/cart/',
        method: 'delete',
        data: {
          payid: this.InData.payid,
          name: this.InData.name,
          fee: this.InData.fee,
          paydate: this.InData.paydate
        }
      }).then(res => {
        res = res.data
        alert(res.msg)
      })
      console.log('testend')
    },
    handle_delete (index, row) {
      alert('handling deleting')
      this.ItemsFee.splice(index, 1)
      alert('handling deleted')
    },
    handle_edit (index, row) {
      alert('handling editing')
      this.showEdit[index] = true
      this.showBtn[index] = true
      this.$set(this.showEdit, row, true)
      this.$set(this.showBtn, row, true)
      alert(row.payid)
    },
    handle_save (index, row) {
      alert('handling saving')
      this.showEdit[index] = false
      this.showBtn[index] = false
      this.$set(this.showEdit, row, false)
      this.$set(this.showBtn, row, false)
      this.$nextTick(() => {
        alert('tik')
      })
      alert(row.payid)
    },
    current_change (currentPage) {
      this.currentPage = currentPage
    },
    handleSizeChange (newSize) {
      this.pagesize = newSize
    }
  }
}
</script>

<style>
.el-breadcrumb {
  display: inline-block;
}

.el-table__header tr,
  .el-table__header th {
      padding: 0;
      height: 30px;
      line-height: 30px;
  }
.el-table__body tr,
  .el-table__body td {
      padding: 0;
      height: 20px;
      line-height: 20px;
  }
#sum1 {
      padding: 0;
      height: 20px;
      line-height: 20px;
  }
#tofill {
      padding: 0;
      height: 20px;
      line-height: 20px;
  }
</style>
