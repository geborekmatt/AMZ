
<template>
  <div class="container">
    <button @click="testBPAPIBP">Test Route BP</button>
    <p>BE:{{ testDataAPIBP }}</p>
    <button @click="runHopper">Run Hopper</button>
    <p>BE:{{ hopperResponse }}</p>
    <Button @click="runHopper" label="Start Hopper" icon="pi pi-file-import"></Button>

  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      testDataAPIBP: "",
      testDataAPI: "",
      hopperResponse: "",
    };
  },
  components: {},
  methods: {
    testBPAPIBP: async function () {
      const path = "/test_api_bp";
      try {
        const res = await axios.post(path, {});
        this.testDataAPIBP = res.data;
      } catch {
        console.log("error");
      }
    },
    runHopper: async function () {
      const path = "/run_hopper";
      try {
        const res = await axios.post(path, {});
        this.hopperResponse = res.data;
      } catch {
        console.log("error");
      }
    },
  },
};
</script>
