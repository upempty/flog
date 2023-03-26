<template>
  <div class="row">
    <div class="col-md-4">
      <div class="form-group">
        <input type="hidden" v-model="toedit" />
      </div>
      <div class="form-group">
        <el-input
          type="text"
          v-model="title"
          class="form-control"
          placeholder="title"
        />
      </div>
      <div class="form-group">
        <el-input
          type="textarea"
          class="form-control"
          v-model="description"
          :rows="2"
          placeholder="description"
        />
      </div>
      <div>
        <mavon-editor ref="md" v-model="content" @imgAdd="$imgAdd"> </mavon-editor>
      </div>
      <div>jjjend</div>
      <div class="form-group">
        <el-button class="btn btn-block btn-success" @click="saveBlog">
          Save
        </el-button>
        <el-button class="btn btn-block btn-success" @click="toArticles">
          Back To Article List 
        </el-button>
      </div>
    </div>
  </div>
</template>

<script>
import {mavonEditor} from "mavon-editor";
import marked from "marked";
import 'mavon-editor/dist/css/index.css';
import Qs from "qs";
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
  created() {
    this.getArticleEdit()
  },
  methods: {
    toArticles() {
      this.$router.push({name:'Articles'})
    },
    getArticleEdit() {
      alert('getArticleEdit')
      let t = this.$route.params.title
      if (t === '') {
        alert('new post')
        return
      }
      this.toedit = 'l'
      this.$axios({
        url: 'rest/article/',
        method: 'get',
        params: {
          title: this.$route.params.title
        }
      }).then(res => {
        let articles = res.data.data
        this.title = articles[0].title
        this.description = articles[0].description
        //this.article_html = marked(articles[0].content)
        this.content = articles[0].content
      })
    },
    $imgAdd(pos, file) {
        this.$axios({
          url: 'rest/article/',
          method: 'post',
          data: {
            //img: JSON.stringify({url: file['miniurl'], name: file['name'] })
            //img: {'url': file['miniurl'], 'name': file['name'] }
            img: {url: file['miniurl'], name: file['name'] }
          }
          }).then((res) => {
            alert(res.data.data)
            this.$refs.md.$img2Url(pos, res.data.data)
          })
    },
    saveBlog () {
      if (this.toedit === '') {
        this.$axios({
          url: 'rest/article/',
          method: 'post',
          data:{
            'title': this.title,
            'description': this.description,
            'content': this.content
          }
          })
          .then(() => {
            //this.getAll()
          })
      } else {
        this.$axios({
          url: 'rest/article/',
          method: 'put',
          data: {
            title: this.title,
            description: this.description,
            content: this.content,
          }})
          .then(() => {
            //this.getAll()
          })
      }
    },
    deleteBlog (blog) {
      this.$axios({
        url: 'rest/article/',
        method: 'delete',
        data: {
          title: blog.title,
          content: blog.content
        }}).then(() => {
        //this.getAll()
      })
    }
  },
  mounted () {
    //this.getAll()
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
