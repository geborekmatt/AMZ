<template>
  <div>
    <div class="grid">
      <div class="col">
        <div class="text-center p-5 border-round-md font-bold">
          <h2 class="mr-2">Hopper Status</h2>
          <div class="field">
            <label class="mr-2">Input Files Count</label>
            {{ hopperStatus.input_file_count }}
          </div>
          <div class="field">
            <label class="mr-2">Added Files Count</label>
            {{ hopperStatus.added_file_count }}
          </div>
          <div class="field">
            <label class="mr-2">Input Files Product Count</label>
            {{ hopperStatus.input_file_product_count }}
          </div>
          <div class="field">
            <Button @click="runHopper"> Start Hopper</Button>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="text-center p-5 border-round-md font-bold">
          <h2 class="mr-2">Products Metrics</h2>
          <div class="field">
            <label class="mr-2">Total</label> {{ productsMetrics.total }}
          </div>
          <div class="field">
            <label class="mr-2">Unsearched</label>
            {{ productsMetrics.unsearched }}
          </div>
          <div class="field">
            <label class="mr-2">Excluded</label> {{ productsMetrics.excluded }}
          </div>
          <div class="field">
            <label class="mr-2">Already Searched</label>
            {{ productsMetrics.searched }}
          </div>
        </div>
      </div>
    </div>
    <div class="grid">
      <div class="col">
        <div class="text-center p-5 border-round-md font-bold">
          <h2 class="mr-2">Hopper Config</h2>
          <div class="field">
            <label class="mr-2">Ignore Unapproved Brands</label>
            <InputSwitch
              v-model="hopperConfig.ignoreUnapprovedBrands"
            ></InputSwitch>
          </div>
          <div class="field">
            <label class="mr-2">Ignore PIP Brands</label>
            <InputSwitch v-model="hopperConfig.ignorePIPBrands"></InputSwitch>
          </div>
          <div class="field">
            <label class="mr-2">Ignore Gated Brands</label>
            <InputSwitch v-model="hopperConfig.ignoreGatedBrands"></InputSwitch>
          </div>
          <div class="field">
            <label class="mr-2">Include Brand Aliases</label>
            <InputSwitch
              v-model="hopperConfig.includeBrandAliases"
            ></InputSwitch>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="text-center p-5 border-round-md font-bold">
          <h2 class="mr-2">Input Files</h2>
          <DataTable
            tableStyle="min-width: 50rem"
            dataKey="name"
            :value="inputFiles"
          >
            <Column
              field="name"
              header="File Name"
              sortable
              width="80%"
            ></Column>
            <Column
              field="product_count"
              header="Product Count"
              sortable
              width="20%"
            ></Column>
          </DataTable>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      testDataAPIBP: "",
      testDataAPI: "",
      hopperStatus: {input_file_count: -1, added_file_count: -1, input_file_product_count: -1},
      hopperConfig: {
        ignoreUnapprovedBrands: true,
        ignorePIPBrands: true,
        ignoreGatedBrands: true,
        includeBrandAliases: true,
      },
      inputFiles: [

      ],
      productsMetrics: {
        total: 1000,
        unsearched: 492,
        excluded: 200,
        searched: 308,
      },
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
        console.log("error: ");
      }
    },
    runHopper: async function () {
      const path = "/run_hopper";
      try {
        const res = await axios.post(path, {});
        this.hopperResponse = res.data;
      } catch {
        console.log("error: ");
      }
      await this.getInputFiles()
      await this.getHopperStatus()
    },
    getInputFiles: async function () {
      const path = "/input_files";
      try {
        const res = await axios.get(path, {});
        this.inputFiles = res.data;
      } catch {
        console.log("error: ");
      }
    },
    getHopperStatus: async function () {
      const path = "/hopper_status";
      try {
        const res = await axios.get(path, {});
        this.hopperStatus = res.data;
      } catch {
        console.log("error: ");
      }
    },
  },
  created :async function(){
    await this.getInputFiles()
    await this.getHopperStatus()
  }
};
</script>
