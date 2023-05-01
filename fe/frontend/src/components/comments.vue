<template>
  <div>

  <br /><br />
  <hr />
  <h3>Provide comments</h3>
  <textarea
    v-model="comment.message"
    :placeholder="placeholder"
    name="commentname"
    id="comment-area"
    cols="60"
    rows="10"></textarea>
  <div>
    <el-button @click="submitComment" class="submitBtn">Submit</el-button>
  </div>


    <hr>
    <div v-for="commentt in comments" :key="commentt.id">
        <div class="comments">
            <div>
               comment: 
            </div>
            <div class="content">
                {{ commentt.message }}
            </div>
        </div>
     </div>
     <hr>


  </div>
</template>

<script>
export default {
  name: "Comments",
  props: ['articleId',], 
  watch: {
    articleIdUpdate() {
      this.articleId2 = articleId
    }
  },
  data(){
    return {
      comments: [],
      message: 'msg',
      comment: {},
      articleId: this.articleId, 
    }
  },

  create() {
    //no here this.getArticleComments()
    //this.getArticleComments()
  },

  mounted() {
    //'this prefix is must'
    this.getArticleComments()
  },

  methods:{
    submitComment() {
      this.comment.article_id = this.articleId
      let comm = {article_id: this.articleId, message:this.comment.message}
      this.comments.unshift(comm)
      alert(this.comment.message)
      this.$axios({
        url: 'rest/comment/',
        method: 'post',
        data: {
          article_id: this.articleId,
          message: this.comment.message,
        }
      }).then(res => {
        let article_comments = res.data.data
        let mss = article_comments[0].message
        let idd = article_comments[0].article_id
        //this.comments = article_comments;
        alert('responsed')

      })


    },

    getArticleComments() {
      let a = this.articleId
      alert(a)
      this.$axios({
        url: 'rest/comment/',
        method: 'get',
        params: {
          article_id: a,
        }
      }).then(res => {
        alert('get responsed comments')
        this.comments = res.data.data
        //let article_comments = res.data.data
        alert('get responsed comments')
        //this.comments = article_comments
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
