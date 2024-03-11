<template>
  <div class="container">
    <DataTable
      v-model:filters="filters"
      v-model:editingRows="editingRows"
      editMode="row"
      filterDisplay="row"
      dataKey="id"
      :value="brands"
      tableStyle="min-width: 50rem"
      @row-edit-save="onRowEditSave"
    >
      <Column field="id" header="ID" sortable width="10%"></Column>
      <Column filterField="name" field="name" header="Name" sortable filter>
        <template #body="{ data }">
          {{ data.name }}
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
        <template #editor="{ data, field }">
          <InputText v-model="data[field]" />
        </template>
      </Column>
      <Column
        filterField="gated"
        field="gated"
        header="Gated"
        sortable
        filter
        width="10%"
      >
        <template #body="{ data }">
          {{ data.gated }}
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
        <template #editor="{ data, field }">
          <div class="pi centered">
            <InputSwitch v-model="data[field]"></InputSwitch
            >{{ data[field] == false ? " No" : " Yes" }}
          </div>
        </template>
      </Column>
      <Column
        filterField="possible_ip"
        field="possible_ip"
        header="Possible IP"
        sortable
        filter
        width="10%"
      >
        <template #body="{ data }"> {{ data.possible_ip }}</template>
        <template #filter="{ filterModel, filterCallback }">
          <InputText
            v-model="filterModel.value"
            type="text"
            @input="filterCallback()"
            class="p-column-filter"
            placeholder=""
          />
        </template>
        <template #editor="{ data, field }">
          <InputSwitch v-model="data[field]"></InputSwitch
          >{{ data[field] == false ? " No" : " Yes" }}
        </template>
      </Column>
      <Column
        filterField="disabled"
        field="disabled"
        header="Disabled"
        sortable
        filter
        width="10%"
      >
        <template #body="{ data }">
          {{ data.disabled }}
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
        <template #editor="{ data, field }">
          <InputSwitch v-model="data[field]"></InputSwitch
          >{{ data[field] == false ? " No" : " Yes" }}
        </template>
      </Column>
      <Column
        filterField="aliases"
        field="aliases"
        header="Aliases"
        sortable
        filter
      >
        <template #body="{ data }">
          {{ data.aliases }}
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
        <template #editor="{ data, field }">
          <InputText v-model="data[field]" />
        </template>
      </Column>
      <Column header="Actions">
        <template #body="{ data }">
          <Button
            @click="deleteBrand(data.id)"
            class="pi centered"
            severity="danger"
          >
            <i class="pi" :class="'pi-trash'"></i>
          </Button>
        </template>
      </Column>
      <Column
        :rowEditor="true"
        style="width: 10%; min-width: 8rem"
        bodyStyle="text-align:center"
      >
      </Column>
    </DataTable>
    <Button @click="getBrands" class="pi centered mt-2 mr-2"
      ><i class="pi" :class="'pi-refresh'"></i
    ></Button>
    <Button @click="isAddBrandActive = true" class="pi centered mt-2"
      ><i class="pi" :class="'pi-plus'"></i
    ></Button>
    <Dialog
      v-model:visible="isAddBrandActive"
      :style="{ width: '450px' }"
      header="Add New Brand"
      :modal="true"
      class="p-fluid"
    >
      <div class="field">
        <label for="name">Name</label>
        <InputText
          id="name"
          v-model="newBrand.name"
          required="true"
          autofocus
        />
      </div>
      <div class="field">
        <p for="gated" class="pi mr-1">Gated</p>
        <InputSwitch v-model="newBrand.gated"></InputSwitch
        >{{ newBrand.gated == false ? " No" : " Yes" }}
      </div>
      <div class="field">
        <p for="possible_ip" class="pi mr-1">Possible IP Complaint</p>
        <InputSwitch v-model="newBrand.possible_ip"></InputSwitch
        >{{ newBrand.possible_ip == false ? " No" : " Yes" }}
      </div>
      <div class="">
        <p for="disabled" class="pi mr-1">Disabled</p>
        <InputSwitch v-model="newBrand.disabled"></InputSwitch
        >{{ newBrand.disabled == false ? " No" : " Yes" }}
      </div>
      <div class="field">
        <label for="aliases">Aliases</label>
        <InputText
          id="aliases"
          v-model="newBrand.aliases"
          required="false"
          autofocus
        />
      </div>
      <Button @click="addBrand"> Save </Button>
    </Dialog>
  </div>
</template>
  
  <script>
import axios from "axios";
import { FilterMatchMode } from "primevue/api";
export default {
  data() {
    return {
      brands: [],
      editBrandActive: false,
      editingRows: [],
      isAddBrandActive: false,
      newBrand: {
        name: "",
        gated: false,
        possible_ip: false,
        disabled: false,
        aliases: "",
      },
      filters: {
        name: { value: null, matchMode: FilterMatchMode.STARTS_WITH },
        gated: { value: null, matchMode: FilterMatchMode.STARTS_WITH },
        possible_ip: { value: null, matchMode: FilterMatchMode.STARTS_WITH },
        disabled: { value: null, matchMode: FilterMatchMode.STARTS_WITH },
        aliases: { value: null, matchMode: FilterMatchMode.CONTAINS },
      },
    };
  },
  components: {},
  created() {
    this.getBrands();
  },
  methods: {
    getBrands: async function () {
      const path = "/brands";
      try {
        const res = await axios.get(path, {});
        this.brands = res.data;
      } catch {
        this.$toast.add({ severity: 'info', summary: 'Brands Get Request Failed', detail: `See log for details`, life: 3000 });
      }
    },
    addBrand: async function () {
      const path = "/brands/add";
      try {
        const res = await axios.post(path, { newData: this.newBrand });
        this.isAddBrandActive = !this.isAddBrandActive
        this.newBrand =
          {
            name: "",
            gated: false,
            possible_ip: false,
            disabled: false,
            aliases: "",
          };
          this.$toast.add({ severity: 'success', summary: 'Brand Added', detail: '', life: 1000 });
        this.getBrands();
      } catch(err) {
        this.$toast.add({ severity: 'info', summary: 'Brand Add Request Failed', detail: 'See log for details', life: 3000 });
      }
    },
    onRowEditSave: async function (event) {
      const path = "/brands/edit";
      try {
        let { newData, index } = event;
        const res = await axios.post(path, { newData });
        this.getBrands();
        this.$toast.add({ severity: 'success', summary: 'Brand Edited', detail: '', life: 1000 });
      } catch {
        this.$toast.add({ severity: 'info', summary: 'Brand Edit Request Failed', detail: 'See log for details', life: 3000 });
      }
    },
    deleteBrand: async function (id) {
      const path = "/brands/delete";
      try {
        const res = await axios.post(path, { id: id });
        this.getBrands();
        this.$toast.add({ severity: 'success', summary: 'Brand Deleted', detail: '', life: 1000 });
      } catch {
        this.$toast.add({ severity: 'info', summary: 'Brand Delete Request Failed', detail: 'See log for details', life: 3000 });
      }
    },
  },
};
</script>