<template>
  <div>

  <br /><br />
  <hr />
  <h3>Provide comments</h3>
  <textarea
    v-model="message"
    :placeholder="placeholder"
    name="comment"
    id="comment-area"
    cols="60"
    rows="10"></textarea>
  <div>
    <el-button @click="submitComment" class="submitBtn">Submit</el-button>
  </div>
  </div>
</template>

<script>
export default {
  name: "Comments",
  props: ['articleId'], 
  watch: {
    articleIdValue() {
      this.articleId = articleId 
    }
  },
  data(){
    return {
      comments: [],
      message: 'msg',
      articleId: null, 
    }
  },

  create() {
  },

  methods:{
    submitComment() {
      alert(this.articleId)
      let comment = {message}
      this.comments.unshift(comment)
    },

    getArticleComments() {
      this.$axios({
        url: 'rest/article/comments',
        method: 'get',
        params: {
          //title: this.$route.query.title
          title: '1'
        }
      }).then(res => {
        let articles = res.data.data
        this.title = articles[0].title
        this.description = articles[0].description
        this.article_html = marked(articles[0].content)
        this.articleid = articles[0].id
        this.comments = [];
      })
    },

  }
}
</script>

<style scoped>

.comment-area {
  padding: 30px 10px;
}

</style>
