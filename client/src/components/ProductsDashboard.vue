<template>
  <div class="container">
    <DataTable
      v-model:filters="filters"
      editMode="row"
      filterDisplay="row"
      dataKey="id"
      :value="products"
      tableStyle="min-width: 50rem"
    >
      <Column field="id" header="ID" sortable width="10%"></Column>
      <Column filterField="title" field="title" header="Title" sortable filter>
        <template #body="{ data }">
          {{ data.title }}
        </template>
        <template #filter="{ filterModel, filterCallback }">
          <InputText
            v-model="filterModel.value"
            type="text"
            @input="filterCallback()"
            class="p-column-filter"
            placeholder=""
          />
        </template>
      </Column>
      <Column
        filterField="price"
        field="price"
        header="Price"
        sortable
        filter
        width="10%"
      >
        <template #body="{ data }">
          {{ data.price }}
        </template>
        <template #filter="{ filterModel, filterCallback }">
          <InputText
            v-model="filterModel.value"
            type="text"
            @input="filterCallback()"
            class="p-column-filter"
            placeholder=""
          />
        </template>
      </Column>
      <Column
        filterField="searched"
        field="searched"
        header="Searched"
        sortable
        filter
        width="10%"
      >
        <template #body="{ data }"> {{ data.searched }}</template>
        <template #filter="{ filterModel, filterCallback }">
          <InputText
            v-model="filterModel.value"
            type="text"
            @input="filterCallback()"
            class="p-column-filter"
            placeholder=""
          />
        </template>
      </Column>
      <Column
        filterField="url"
        field="url"
        header="Url"
        sortable
        filter
        width="10%"
      >
        <template #body="{ data }">
          {{ data.url }}
        </template>
        <template #filter="{ filterModel, filterCallback }">
          <InputText
            v-model="filterModel.value"
            type="text"
            @input="filterCallback()"
            class="p-column-filter"
            placeholder=""
          />
        </template>
      </Column>
    </DataTable>
    <Button @click="getProducts" class="pi centered mt-2 mr-2"
      ><i class="pi" :class="'pi-refresh'"></i
    ></Button>
  </div>
</template>
    
    <script>
import axios from "axios";
import { FilterMatchMode } from "primevue/api";
export default {
  data() {
    return {
      products: [],

      filters: {
        title: { value: null, matchMode: FilterMatchMode.STARTS_WITH },
        price: { value: null, matchMode: FilterMatchMode.CONTAINS },
        searched: { value: null, matchMode: FilterMatchMode.STARTS_WITH },
        url: { value: null, matchMode: FilterMatchMode.CONTAINS },
      },
    };
  },
  components: {},
  created() {
    this.getProducts();
  },
  methods: {
    getProducts: async function () {
      const path = "/products";
      try {
        const res = await axios.get(path, {});
        this.products = res.data;
      } catch {
        this.$toast.add({
          severity: "info",
          summary: "Products Get Request Failed",
          detail: "See log for details",
          life: 3000,
        });
      }
    },
  },
};
</script>