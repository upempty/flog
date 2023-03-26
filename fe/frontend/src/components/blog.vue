<template>
    <div>
    <div>Not to be used for this page</div>
    <div>
      <mavon-editor ref="editor" v-model="doc"> </mavon-editor>
    </div>
    </div>
</template>
<script>
import {mavonEditor} from "mavon-editor";
//should use this{} !!! import {mavonEditor} from "mavon-editor";
//should use components :{}
import "mavon-editor/dist/css/index.css";
export default {
    name: "Create",
    components: {mavonEditor},
    data(){
      return {
        doc: '',
      }
    }
}
</script>
