<template>
  <div class="row">
    <div class="col-md-4">
      <div class="form-group">
        <input type="hidden" v-model="toedit" />
      </div>
      <div>jjjend</div>
      <div class="form-group">
        <el-button class="btn btn-block btn-success" @click="toPost">
          Post 
        </el-button>
      </div>
    </div>
    <div class="col-md-8">
      <table class="table table-bordered table-hover">
        <thead>
          <th class="text-center">Title</th>
          <th class="text-center">Desc</th>
          <th class="text-center">Content</th>
          <th class="text-center">Edit</th>
          <th class="text-center">Delete</th>
        </thead>
        <tbody>
          <tr v-for="blog in blogs" :key="blog.toedit">
            <td @click="getArticle(blog.title)">{{ blog.title }}</td>
            <td>{{ blog.description }}</td>
            <td>{{ blog.content }}</td>
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
            <div class="markdown-body" v-html="blog.hh"></div>
            <link href="https://cdn.bootcss.com/github-markdown-css/2.10.0/github-markdown.min.css" rel="stylesheet" />
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  <div class="row">
   <div v-for="article in blogs">
    <router-link :to="{ name: 'Article', query: { title: article.title }}"
                  class="article-title">
      {{ article.title }}
    </router-link>
    </div>
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
    editBlog (blog) {
      this.toedit = '1'
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
