<template>
  <div id="article">
    <div class="article__title">
    <h2 v-text="title"></h2>
    </div>
    <el-divider></el-divider>
    <div class="desc">>>Descripton: {{description}}</div>
    <div class="article__text" v-highlight v-html="article_html"></div>
    <div> 
      <el-button class="btn btn-block btn-success" @click="toArticles">
        Back To Article List
      </el-button>
    </div>
  </div>
</template>

<script>
// import axios from "axios";
//ok import {marked} from 'marked';
//nok import marked from 'marked';
import {marked} from 'marked';
import 'mavon-editor/dist/css/index.css'
export default {
  name: "Article",
  data(){
    return {
      'title': this.$route.query.title, article_html:'xxx', 'description':'',
    }
  },
  created() {
    this.getArticleDetail()
  },
  mounted() {
  },
  watch: {
  },
  methods:{
    toArticles() {
      this.$router.push({name:'Articles'})
    },
    getArticleDetail() {
      this.$axios({
        url: 'rest/article/',
        method: 'get',
        params: {
          title: this.$route.query.title
        }
      }).then(res => {
        let articles = res.data.data
        this.title = articles[0].title
        this.description = articles[0].description
        this.article_html = marked(articles[0].content) 
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
.desc {
  margin: 5px;
  max-width: 400px;
  color: #000000;
  font-size:15px;
  line-height:1.5em;
}
.article__text {
  margin: 5px;
  max-width: 400px;
  color: #808000;
  line-height:1.5em;
}
#article{
  border: #C0C4CC .1rem solid;
  border-radius: .2rem;
  padding: .4rem;
  background-color: #C0C4CC40;
}
</style>
