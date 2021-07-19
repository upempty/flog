<template>
  <div class="row">
    <div class="col-md-4">
      <div class="form-group">
        <input type="hidden" v-model="url" />
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
          v-model="content"
          placeholder="content"
        ></textarea>
      </div>
      <div class="form-group">
        <button class="btn btn-block btn-success" @click="saveBlog()">
          Save
        </button>
      </div>
    </div>
    <div class="col-md-8">
      <table class="table table-bordered table-hover">
        <thead>
          <th class="text-center">Title</th>
          <th class="text-center">Content</th>
          <th class="text-center">Edit</th>
          <th class="text-center">Delete</th>
        </thead>
        <tbody>
          <tr v-for="blog in blogs" :key="blog.url">
            <td>{{ blog.title }}</td>
            <td>{{ blog.content }}</td>
            <td>
              <button class="btn btn-success" @click="editBlog(blog)">
                <i class="fa fa-edit"></i>
              </button>
            </td>
            <td>
              <button class="btn btn-success" @click="deleteBlog(blog)">
                <i class="fa fa-trash"></i>
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>

export default {
  name: 'Post',
  props: {},
  data () {
    return {
      baseUrl: 'http://127.0.0.1:8000/api/blog/',
      blogs: null,
      url: '',
      title: '',
      content: ''
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
        this.title = ''
        this.content = ''
      })
        .catch(error => {
          console.log(error)
        })
    },
    saveBlog () {
      if (this.url === '') {
        this.$axios({
          url: 'post/article/',
          method: 'post',
          data: {
            title: this.title,
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
            content: this.content
          }})
          .then(() => {
            this.getAll()
          })
      }
    },
    editBlog (blog) {
      this.url = blog.url
      this.title = blog.title
      this.content = blog.content
    },
    deleteBlog (blog) {
      this.$axios({
        url: 'post/article/',
        method: 'delete',
        data: {
          title: this.title,
          content: this.content
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
<style scoped></style>
