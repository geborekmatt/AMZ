<template>
  <div>
    <div class="grid">
      <div class="col">
        <div class="text-center p-5 border-round-md bg-gray-50 font-bold">
          <h2 class="mr-2">Hopper Status</h2>
          <div class="field">
            <label class="mr-2">Input Files Count</label>
            {{ productsMetrics.unsearched }}
          </div>
          <div class="field">
            <label class="mr-2">Added Files Count</label>
            {{ productsMetrics.excluded }}
          </div>
          <div class="field">
            <label class="mr-2">Input Files Product Count</label>
            {{ productsMetrics.total }}
          </div>
          <div class="field">
            <label class="mr-2">Status</label> Stopped
            <Button> Start Hopper</Button>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="text-center p-5 border-round-md bg-gray-50 font-bold">
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
        <div class="text-center p-5 border-round-md bg-gray-50 font-bold">
          <h2 class="mr-2">Hopper Config</h2>
          <div class="field">
            <label class="mr-2">Ignore Disabled Brands</label>
            <InputSwitch
              v-model="hopperConfig.ignoreDisabledBrands"
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
        <div class="text-center p-5 border-round-md bg-gray-50 font-bold">
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
              width="10%"
            ></Column>
            <Column
              field="date_added"
              header="date_added"
              sortable
              width="10%"
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
      hopperResponse: "",
      hopperConfig: {
        ignoreDisabledBrands: true,
        ignorePIPBrands: true,
        ignoreGatedBrands: true,
        includeBrandAliases: true,
      },
      inputFiles: [
        {
          name: "Products1.xlsx",
          product_count: 167,
          date_added: "2024-01-12",
        },
        {
          name: "Products12.xlsx",
          product_count: 233,
          date_added: "2024-01-15",
        },
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
        console.log(res.data);
        this.testDataAPIBP = res.data;
      } catch {
        console.log("error: ");
      }
    },
    runHopper: async function () {
      const path = "/run_hopper";
      try {
        const res = await axios.post(path, {});
        console.log(res.data);
        this.hopperResponse = res.data;
      } catch {
        console.log("error: ");
      }
    },
  },
};
</script>
