<template>
  <div class="row">
    <div class="col-md-4">
      <div class="form-group">
        <input type="hidden" v-model="toedit" />
      </div>
      <div class="form-group">
        <input
          type="text"
          v-model="title"
          class="form-control"
          placeholder="title"
        />
      </div>
      <div class="form-group">
        <textarea
          class="form-control"
          v-model="description"
          placeholder="description"
        ></textarea>
      </div>
      <div>
        <mavon-editor ref="md" v-model="content"> </mavon-editor>
      </div>
      <div>jjjend</div>
      <div class="form-group">
        <button class="btn btn-block btn-success" @click="saveBlog">
          Save
        </button>
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
            <td>{{ blog.title }}</td>
            <td>{{ blog.description }}</td>
            <td>{{ blog.content }}</td>
            <td>
              <button class="btn btn-success" @click="editBlog(blog)">
              Edit
              </button>
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
  </div>
</template>

<script>
import {mavonEditor} from "mavon-editor";
import marked from "marked";
import 'mavon-editor/dist/css/index.css'
export default {
  name: 'Post',
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
    getAll () {
      this.$axios({
        url: 'post/article/',
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
    saveBlog () {
      if (this.toedit === '') {
        this.$axios({
          url: 'post/article/',
          method: 'post',
          data: {
            title: this.title,
            description: this.description,
            content: this.content
          }})
          .then(() => {
            this.getAll()
          })
      } else {
        this.$axios({
          url: 'post/article/',
          method: 'put',
          data: {
            title: this.title,
            description: this.description,
            content: this.content,
          }})
          .then(() => {
            this.getAll()
          })
      }
    },
    editBlog (blog) {
      this.toedit = '1'
      this.title = blog.title
      this.description = blog.description
      this.content = blog.content
    },
    deleteBlog (blog) {
      this.$axios({
        url: 'post/article/',
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
</style>
