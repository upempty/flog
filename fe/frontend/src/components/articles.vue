<template>
  <div class="row">
    <div class="col-md-4">
      <div class="form-group">
        <input type="hidden" v-model="toedit" />
      </div>

     <div class="filter-container">
     Article List
     </div>
     <div>

      <el-form>
          <el-row>
           <el-col :span="4">
          <el-form-item>
            <el-input v-model="SearchKey"></el-input>
          </el-form-item>
          </el-col>

           <el-col :span="2">
          <el-form-item>
            <el-button type="primary" icon="el-icon-search" @click="onSearch">Search</el-button>
          </el-form-item>
          </el-col>

           <el-col :span="4">
          <el-form-item>
            <el-button type="primary" icon="el-icon-edit" @click="toPost">Post</el-button>
          </el-form-item>
          </el-col>

          </el-row>
       </el-form>

     </div>
    </div>

    <div class="col-md-8">
      <table class="table table-bordered table-hover">
        <thead>
          <th class="text-center">Title</th>
          <th class="text-center">Desc</th>
          <th class="text-center">Edit</th>
          <th class="text-center">Delete</th>
        </thead>
        <tbody>
          <tr v-for="blog in blogs" :key="blog.toedit">
            <td @click="getArticle(blog.title)">{{ blog.title }}</td>
            <td>{{ blog.description }}</td>
            <td>
              <el-button class="btn btn-success" @click="editBlog(blog)">
              Edit
              </el-button>
            </td>
            <td>
              <el-button class="btn btn-success" @click="deleteBlog(blog)">
              Del
              </el-button>
            </td>
            <td>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
 </div>
</template>

<script>
import {mavonEditor} from "mavon-editor";
import {marked} from "marked";
import 'mavon-editor/dist/css/index.css';
import Qs from "qs";
export default {
  name: 'Articles',
  props: {},
  components: {mavonEditor},
  data () {
    return {
      blogs: null,
      toedit: '',
      title: '',
      description: '',
      content: 'md content',
      article_value: 'I am fei',
      dooc: '',
      SearchKey: '',
    }
  },
  methods: {
    toPost() {
      this.$router.push({name: 'Post', params:{title: ''}})
    },
    getArticle(title) {
      this.$router.push({name:'Article', query:{title: title}})
    },
    getAll () {
      this.$axios({
        url: 'rest/article/',
        method: 'get',
        params: {}
      }).then(res => {
        this.blogs = res.data.data
        for (var x in this.blogs)
        {
            this.blogs[x].hh = marked(this.blogs[x].content)
        }
        this.title = ''
        this.description = ''
        this.content = ''
        this.toedit = ''
      })
        .catch(error => {
          console.log(error)
        })
    },
    onSearch () {
      alert('search')
      this.$axios({
        url: 'rest/article/',
        method: 'GET',
        params: {title: this.SearchKey, }, 
      }).then(res => {
        alert('sending response')
        this.blogs = res.data.data
        for (var x in this.blogs)
        {
            this.blogs[x].hh = marked(this.blogs[x].content)
        }
        this.title = ''
        this.description = ''
        this.content = ''
        this.toedit = ''
      }).catch(error => {
          console.log(error)
        })
      alert('tttjjwe')
    },

    editBlog (blog) {
      this.toedit = 'edit_mode'
      this.title = blog.title
      this.description = blog.description
      this.content = blog.content
      this.$router.push({name:'Post', params:{title: this.title}})
    },
    deleteBlog (blog) {
      this.$axios({
        url: 'rest/article/',
        method: 'delete',
        data: {
          title: blog.title,
          content: blog.content
        }}).then(() => {
        this.getAll()
      })
    }
  },
  mounted () {
    this.getAll()
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    .article-title {
        font-size: large;
        font-weight: bolder;
        color: black;
        text-decoration: none;
        padding: 5px 0 5px 0;
    }
</style>
