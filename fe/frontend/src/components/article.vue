<template>
  <div id="article">
    <div class="article__title">
    <h2 v-text="title"></h2>
    </div>
    <el-divider></el-divider>
    <div>Descripton: {{description}}</div>
    <div class="article__text" v-html="article_html"></div>
  </div>
</template>

<script>
// import axios from "axios";
import marked from "marked";
import 'mavon-editor/dist/css/index.css'
export default {
  name: "Article",
  data(){
    return {
      'title': this.$route.query.title,
      'article_html':'',
      'description':'',
    }
  },
  created() {
    this.getArticle()
  },
  mounted() {
  },
  watch: {
  },
  methods:{
    getArticle() {
      this.$axios({
        url: 'post/article/',
        method: 'get',
        params: {
          title: this.$route.query.title
        }
      }).then(res => {
        let articles = res.data.data
        this.article_html = marked(articles[0].content)
        this.description = articles[0].description
      })
    },
  }
}
</script>

<style scoped>
.article__title {
  width: -moz-available;
  margin: 5px;
  max-width: 400px;
  color: #E6A23C;
  height: 20px;
}
#article{
  border: #C0C4CC .1rem solid;
  border-radius: .2rem;
  padding: .4rem;
  background-color: #C0C4CC40;
}
</style>
