<template>
  <div class="container">
        <button @click="testBPAPI" > Test Route</button>
    <p> BE:{{testDataAPI}} </p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
        testData: "",
        testDataAPI:""
    };
  },
  components: {
  },
  methods: {
        testBPAPI : async function(){
      const path = '/testMattAPI';
        try{
          const res = await axios.post(path,{})
          console.log(res.data)
          this.testDataAPI = res.data
        }catch{
          console.log("error: ")
        }
    }
  }
};
</script>
